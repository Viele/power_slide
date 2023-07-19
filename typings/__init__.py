import bpy

from . import callback


_CLASSES = (
    callback.PSL_Callback,
    callback.PSL_CallbackGroup,
)


def register_operators():
    for c in _CLASSES:
        bpy.utils.register_class(c)

    bpy.types.Collection.on_enter = bpy.props.PointerProperty(type=callback.PSL_CallbackGroup)
    bpy.types.Collection.on_exit = bpy.props.PointerProperty(type=callback.PSL_CallbackGroup)


def unregister_operators():
    del bpy.types.Collection.on_enter
    del bpy.types.Collection.on_exit

    for c in reversed(_CLASSES):
        bpy.utils.unregister_class(c)
    
    