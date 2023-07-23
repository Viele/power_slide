import bpy
from ..utils import slide_template as _template_utils


class PSL_UL_slide_templates(bpy.types.UIList):
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        layout.prop(item, "name")


class PSL_PT_Slide_Templates(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "Slide Templates"
    bl_category = "Power Slide"

    def draw(self, context: bpy.types.Context):
        layout = self.layout
        template_collection = _template_utils.get_slide_template_collection(context)

        row = layout.row()
        row.template_list("PSL_UL_slide_templates", "", 
                          template_collection.collection, "children",
                          context.scene, "active_slide_template"
        )
        col = row.column()
        col.operator("psl.create_slide_template", icon='ADD', text="")
        col.operator("psl.delete_slide_template", icon='REMOVE', text="")