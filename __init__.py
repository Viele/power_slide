import bpy

bl_info = {
    "name": "Power Slide",
    "description": "Slide Presentation but with Blender",
    "author": "Christoph Lendenfeld",
    "version": (1, 0),
    "blender": (3, 6, 0),
    "category": "Animation",
}

_CLASSES = []


def register():
    for c in _CLASSES:
        bpy.utils.register_class(c)


def unregister():
    for c in _CLASSES:
        bpy.utils.unregister_class(c)
