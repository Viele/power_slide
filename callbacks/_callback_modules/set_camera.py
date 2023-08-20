import bpy
from .. import errors as _cb_errors


def create(callback_prop):
    callback_prop["camera"] = None


def draw(callback_prop, context: bpy.types.Context, layout: bpy.types.UILayout):
    layout.prop_search(callback_prop, '["camera"]', bpy.data, "objects", text="Camera")


def execute(callback_prop, context: bpy.types.Context):
    camera = callback_prop["camera"]
    if not camera:
        raise _cb_errors.CallbackError("No camera defined, cannot run callback")
    context.scene.camera = camera


def get_list_name(callback_prop) -> str:
    camera_object = callback_prop["camera"]
    text = camera_object.name if camera_object else "None"
    return f"Set Camera - {text}"


def pre_start_setup(callback_prop):
    pass
