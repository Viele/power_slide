import bpy

from . import main_menu


_CLASSES = (
    main_menu.PSL_PT_Main_Menu,
    main_menu.Foo,
    main_menu.PSL_UL_list_test
)


def register_operators():
    for c in _CLASSES:
        bpy.utils.register_class(c)

    bpy.types.Scene.slide_list = bpy.props.CollectionProperty(type=main_menu.Foo)
    bpy.types.Scene.slide_list_index = bpy.props.IntProperty()


def unregister_operators():
    for c in reversed(_CLASSES):
        bpy.utils.unregister_class(c)
    
    del bpy.types.Scene.slide_list
    del bpy.types.Scene.slide_list_index