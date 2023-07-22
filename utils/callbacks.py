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


def _execute_run_script_callback(callback_prop: _callback_types.PSL_Callback):
    text_object = callback_prop["text"]
    if not text_object:
        raise RuntimeError("No text defined, cannot run callback")
    exec(text_object.as_string())


def execute(callback_prop: _callback_types.PSL_Callback):
    execute_function_map = {
        _constants.CALLBACK_RUN_SCRIPT: _execute_run_script_callback,
    }
    execute_function = execute_function_map.get(callback_prop.type)
    if not execute_function:
        raise RuntimeError(f"No execution function defined for {callback_prop.type}")
    execute_function(callback_prop)


def get_active_callback(context: bpy.types.Context, list_name: str) -> _callback_types.PSL_Callback:
    from . import slide as _slide_utils
    current_slide = _slide_utils.get_current_slide(context)
    
    callback_list = getattr(current_slide.collection, list_name)
    if len(callback_list.callbacks) == 0:
        return
    return callback_list.callbacks[callback_list.active_index]


def construct_type_props(callback_prop: _callback_types.PSL_Callback):
    """ Dynamically create properties needed for this type of callback"""
    # assumes type is already set on callback_object
    properties_map = {
        _constants.CALLBACK_RUN_SCRIPT: (
            ("text", None),
        ),
    }
    callback_properties = properties_map.get(callback_prop.type, {})
    for name, prop_value in callback_properties:
        callback_prop[name] = prop_value


def get_callback_list(slide: bpy.types.LayerCollection, list_name: str) -> _callback_types.PSL_CallbackGroup:
    if list_name in slide.children:
        return slide.children[list_name]
    
    callback_list = bpy.data.collections.new(list_name)
    slide.collection.children.link(callback_list)

    return slide.children[list_name]
