import bpy
from ..utils import slide as _slide_utils


class PSL_UL_slides(bpy.types.UIList):
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        # split = layout.split(factor=0.2)
        # split.label(text="Slide: {index}".format(index=index))
        layout.prop(item, "name")


class PSL_PT_Slides(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "Slides"
    bl_category = "Power Slide"


    def draw(self, context: bpy.types.Context):
        layout = self.layout
        # layout.operator_context = "INVOKE_DEFAULT"
        slide_collection = _slide_utils.get_slide_collection(context)
        row = layout.row()
        row.template_list(
            "PSL_UL_slides", "", 
            slide_collection.collection, "children", 
            context.scene, "active_slide"
        )
        col = row.column()
        col.operator("psl.create_slide", icon='ADD', text="")
        col.operator("psl.delete_slide", icon='REMOVE', text="")

        col.separator()
        col.operator("psl.reorder_slide", icon='TRIA_UP', text="").direction = 'UP'
        col.operator("psl.reorder_slide", icon='TRIA_DOWN', text="").direction = 'DOWN'

        layout.separator()

        row = layout.row()
        row.operator("psl.start_presentation")
        row.operator("psl.stop_presentation")
        
        row = layout.row()
        row.operator("psl.previous_slide")
        row.operator("psl.next_slide")
