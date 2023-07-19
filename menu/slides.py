import bpy
from bpy.types import Context
from ..utils import slide as _slide_utils


class PSL_PT_Slides(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "Slides"
    bl_category = "Power Slide"


    def draw(self, context: Context):
        layout = self.layout
        # layout.operator_context = "INVOKE_DEFAULT"
        slide_collection = _slide_utils.get_slide_collection(context)
        layout.template_list("PSL_UL_slides", "", slide_collection.collection, "children", context.scene, "active_slide")
        row = layout.row()
        row.operator("psl.create_slide")
        row.operator("psl.delete_slide")

        row = layout.row()
        row.operator("psl.start_presentation")
        row.operator("psl.stop_presentation")
        
        layout.operator("psl.next_slide")
