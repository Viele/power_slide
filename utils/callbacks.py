import bpy
from ..typings import callback as _cb_types


def get_active_callback(context: bpy.types.Context, list_name: str) -> _cb_types.PSL_Callback:
    from . import slide as _slide_utils
    current_slide = _slide_utils.get_current_slide(context)
    
    callback_list = getattr(current_slide.collection, list_name)
    if len(callback_list.callbacks) == 0:
        return
    return callback_list.callbacks[callback_list.active_index]
