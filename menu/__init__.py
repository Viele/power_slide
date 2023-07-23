import bpy

from . import callbacks, slides, slide_templates


_CLASSES = (
    slides.PSL_UL_slides,
    slides.PSL_PT_Slides,
    slide_templates.PSL_UL_slide_templates,
    slide_templates.PSL_UL_assigned_templates,
    slide_templates.PSL_PT_Slide_Templates,
    slide_templates.PSL_PT_Slide_Assigned_Templates,
    callbacks.PSL_UL_callbacks,
    callbacks.PSL_PT_Callbacks_On_Enter,
)


def register_operators():
    for c in _CLASSES:
        bpy.utils.register_class(c)


def unregister_operators():
    for c in reversed(_CLASSES):
        bpy.utils.unregister_class(c)
    