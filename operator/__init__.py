import bpy

from . import slide, presentation, callbacks, slide_template

_CLASSES = (
    slide.PSL_OT_Create_Slide,
    slide.PSL_OT_Delete_Slide,
    slide.PSL_OT_Duplicate_Slide,
    slide.PSL_OT_Reorder_Slide,
    slide.PSL_OT_Add_Object_To_Slide,
    slide.PSL_OT_Remove_Object_From_Slide,
    presentation.PSL_OT_Start_Presentation,
    presentation.PSL_OT_Stop_Presentation,
    presentation.PSL_OT_Next_Slide,
    presentation.PSL_OT_Previous_Slide,
    callbacks.PSL_OT_Create_Callback,
    callbacks.PSL_OT_Delete_Callback,
    slide_template.PSL_OT_Create_Slide_Template,
    slide_template.PSL_OT_Delete_Slide_Template,
    slide_template.PSL_OT_Add_Template_To_Slide,
    slide_template.PSL_OT_Remove_Template_from_Slide,
)


def register_operators():
    for c in _CLASSES:
        bpy.utils.register_class(c)

def unregister_operators():
    for c in reversed(_CLASSES):
        bpy.utils.unregister_class(c)
