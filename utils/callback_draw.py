import bpy
from . import constants as _constants
from ..typings import callback as _callback_types


def _draw_run_script_callback(
        callback_prop: _callback_types.PSL_Callback, context: bpy.types.Context, layout: bpy.types.UILayout):
    layout.label(text=callback_prop.type)
    layout.prop_search(callback_prop, '["text"]', bpy.data, "texts")


def draw_callback_props(callback_prop: _callback_types.PSL_Callback, context, layout):
    draw_function_map = {
        _constants.CALLBACK_RUN_SCRIPT: _draw_run_script_callback,
    }
    draw_fn = draw_function_map.get(callback_prop.type)
    if draw_fn:
        draw_fn(callback_prop, context, layout)
