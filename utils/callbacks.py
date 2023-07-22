import bpy
from . import constants as _constants
from ..typings import callback as _callback_types


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
        _constants.CALLBACK_SET_TEXT: (
            ("text", ""),
            ("text_object", None),
        )
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
