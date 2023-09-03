import bpy
from .. import errors as _cb_errors


def _get_gp_modifier(ob):
    modifier_name = "psl_gp_play"
    if modifier_name not in ob.grease_pencil_modifiers:
        ob.grease_pencil_modifiers.new(modifier_name, "GP_TIME")
    return ob.grease_pencil_modifiers[modifier_name]


def create(callback_prop):
    callback_prop["object"] = None
    callback_prop["use_range"] = False
    callback_prop["range"] = (1, 100)
    callback_prop["loop"] = False


def draw(callback_prop, context: bpy.types.Context, layout: bpy.types.UILayout):
    layout.prop_search(callback_prop, '["object"]', bpy.data, "objects", text="Object")
    layout.prop(callback_prop, '["loop"]', text="Loop")

    layout.prop(callback_prop, '["use_range"]', text="Range")
    row = layout.row()
    row.enabled = callback_prop["use_range"]
    row.prop(callback_prop, '["range"]', text="")


def execute(callback_prop, context: bpy.types.Context):
    ob = callback_prop["object"]
    if not ob:
        raise _cb_errors.CallbackError("Object not defined. Cannot play grease pencil animation")
    modifier = _get_gp_modifier(ob)
    modifier.show_viewport = True
    modifier.offset = context.scene.frame_current
    modifier.use_keep_loop = callback_prop["loop"]
    modifier.use_custom_frame_range = callback_prop["use_range"]
    modifier.frame_start = callback_prop["range"][0]
    modifier.frame_end = callback_prop["range"][1]


def cleanup(callback_prop, context: bpy.types.Context):
    pass


def get_list_name(callback_prop) -> str:
    ob = callback_prop["object"]
    text = ob.name if ob else "None"
    return f"Play Grease Pencil - {text}"


def pre_start_setup(callback_prop):
    ob = callback_prop["object"]
    if not ob:
        return
    
    modifier = _get_gp_modifier(ob)
    modifier.show_viewport = False