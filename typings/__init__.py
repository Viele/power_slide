import bpy

from . import callback
from ..callbacks import constants as _cb_constants


_CLASSES = (
    callback.PSL_Callback,
    callback.PSL_CallbackGroup,
)


def register_operators():
    for c in _CLASSES:
        bpy.utils.register_class(c)

    for enum_item in _cb_constants.CALLBACK_LISTS:
        setattr(bpy.types.Collection, enum_item[0], bpy.props.PointerProperty(type=callback.PSL_CallbackGroup))


def unregister_operators():
    for enum_item in reversed(_cb_constants.CALLBACK_LISTS):
        delattr(bpy.types.Collection, enum_item[0])

    for c in reversed(_CLASSES):
        bpy.utils.unregister_class(c)
    
    