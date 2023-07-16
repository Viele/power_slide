import bpy

from . import main_menu


_CLASSES = (
    main_menu.PSL_PT_Slides,
    main_menu.PSL_UL_collection_list,
    main_menu.PSL_PT_Callbacks,
)


def register_operators():
    for c in _CLASSES:
        bpy.utils.register_class(c)


def unregister_operators():
    for c in reversed(_CLASSES):
        bpy.utils.unregister_class(c)
    