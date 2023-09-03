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
    # needed because the slide update callback needs to cleanup the previous slide
    bpy.types.Scene.previous_slide = bpy.props.IntProperty()
    bpy.types.Scene.active_slide = bpy.props.IntProperty(
        update=_active_slide_changed
    )
    bpy.types.Scene.active_slide_template = bpy.props.IntProperty()

    for m in _MODULES:
        m.register_operators()


def unregister():
    del bpy.types.Scene.active_slide_template
    del bpy.types.Scene.active_slide
    del bpy.types.Scene.previous_slide

    for m in reversed(_MODULES):
        m.unregister_operators()
