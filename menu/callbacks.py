import bpy
from bpy.types import Context
from ..utils import slide as _slide_utils


class PSL_PT_Callbacks(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "Callbacks"
    bl_category = "Power Slide"

    def draw(self, context: Context):
        layout = self.layout
        active_slide = _slide_utils.get_current_slide(context)
        layout.label(text=f"Callbacks for slide: '{active_slide.name}'")
        layout.template_list("PSL_UL_callbacks", "", active_slide.collection.on_enter, "callbacks", active_slide.collection.on_enter, "active_index")
        row = layout.row()
        row.operator("psl.create_callback")
        row.operator("psl.delete_callback")
