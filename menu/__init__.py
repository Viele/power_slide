import bpy

from . import callbacks, lists, slides


_CLASSES = (
    slides.PSL_PT_Slides,
    lists.PSL_UL_slides,
    lists.PSL_UL_callbacks,
    callbacks.PSL_PT_Callbacks_On_Enter,
)


def register_operators():
    for c in _CLASSES:
        bpy.utils.register_class(c)


def unregister_operators():
    for c in reversed(_CLASSES):
        bpy.utils.unregister_class(c)
    