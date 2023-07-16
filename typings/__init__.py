import bpy

from . import groups


_CLASSES = (
    groups.PSL_Callback,
)


def register_operators():
    for c in _CLASSES:
        bpy.utils.register_class(c)

    bpy.types.Collection.on_enter = bpy.props.CollectionProperty(type=groups.PSL_Callback)
    bpy.types.Collection.on_exit = bpy.props.CollectionProperty(type=groups.PSL_Callback)


def unregister_operators():
    del bpy.types.Collection.on_enter
    del bpy.types.Collection.on_exit

    for c in reversed(_CLASSES):
        bpy.utils.unregister_class(c)
    
    