bl_info = {
    "name": "Power Slide",
    "description": "Slide Presentation but with Blender",
    "author": "Christoph Lendenfeld",
    "version": (1, 0),
    "blender": (3, 6, 0),
    "category": "Animation",
}

import bpy
from . import operator, menu, typings
from .utils import slide as _slide_utils

_MODULES = [
    typings,
    operator,
    menu,
]


def _active_slide_changed(self, context):
    _slide_utils.active_slide_changed(context)


def register():
    bpy.types.Scene.active_slide = bpy.props.IntProperty(
        update=_active_slide_changed
    )

    for m in _MODULES:
        m.register_operators()


def unregister():
    del bpy.types.Scene.active_slide

    for m in reversed(_MODULES):
        m.unregister_operators()
