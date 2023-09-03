import bpy
from ..typings import callback as _cb_types
from . import slide as _slide_utils


def get_active_callback(context: bpy.types.Context) -> _cb_types.PSL_Callback:
    current_slide = _slide_utils.get_current_slide(context)
    
    callback_list = current_slide.collection.slide_callbacks
    if len(callback_list.callbacks) == 0:
        return
    return callback_list.callbacks[callback_list.active_index]


def get_callbacks_from_active_slide(context: bpy.types.Context):
    current_slide = _slide_utils.get_current_slide(context)
    callback_list = current_slide.collection.slide_callbacks
    return callback_list.callbacks


def get_callbacks(slide: bpy.types.LayerCollection):
    callback_list = slide.collection.slide_callbacks
    return callback_list.callbacks
