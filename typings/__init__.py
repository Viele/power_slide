import bpy

from . import callback, slide_template
from ..callbacks import constants as _cb_constants


_CLASSES = (
    callback.PSL_Callback,
    callback.PSL_CallbackGroup,
    slide_template.PSL_Template,
    slide_template.PSL_TemplateGroup,
)


def register_operators():
    for c in _CLASSES:
        bpy.utils.register_class(c)

    bpy.types.Collection.template_data = bpy.props.PointerProperty(type=slide_template.PSL_TemplateGroup)
    bpy.types.Collection.slide_callbacks = bpy.props.PointerProperty(type=callback.PSL_CallbackGroup)


def unregister_operators():
    del bpy.types.Collection.slide_callbacks
    del bpy.types.Collection.template_data

    for c in reversed(_CLASSES):
        bpy.utils.unregister_class(c)
    
    