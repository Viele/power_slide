import bpy
from . import constants as _constants
from ..typings import callback as _callback_types


def _draw_run_script_callback(
        callback_prop: _callback_types.PSL_Callback, context: bpy.types.Context, layout: bpy.types.UILayout):
    layout.prop_search(callback_prop, '["text"]', bpy.data, "texts")


def _draw_set_text(
        callback_prop: _callback_types.PSL_Callback, context: bpy.types.Context, layout: bpy.types.UILayout):
    layout.prop(callback_prop, '["text"]')
    layout.prop_search(callback_prop, '["text_object"]', bpy.data, "curves")


def draw_callback_props(callback_prop: _callback_types.PSL_Callback, context, layout):
    draw_function_map = {
        _constants.CALLBACK_RUN_SCRIPT: _draw_run_script_callback,
        _constants.CALLBACK_SET_TEXT: _draw_set_text,
    }
    draw_fn = draw_function_map.get(callback_prop.type)
    if draw_fn is None:
        raise _callback_types.CallbackError(f"No draw function defined for {callback_prop.type}")
    draw_fn(callback_prop, context, layout)
