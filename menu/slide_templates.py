import bpy
from ..utils import slide_template as _template_utils, slide as _slide_utils


class PSL_UL_slide_templates(bpy.types.UIList):
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        layout.prop(item, "name")


class PSL_UL_assigned_templates(bpy.types.UIList):
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


class PSL_PT_Slide_Assigned_Templates(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "Assigned Templates"
    bl_category = "Power Slide"
    bl_parent_id = "PSL_PT_Slides"

    def draw(self, context: bpy.types.Context):
        layout = self.layout
        active_slide = _slide_utils.get_current_slide(context)
        if not active_slide:
            return []
        row = layout.row()
        row.template_list(
            "PSL_UL_assigned_templates", "foo", 
            active_slide.collection, "children",
            active_slide.collection, '["active_template"]'
        )
        col = row.column()
        col.operator("psl.add_template_to_slide", icon='ADD', text="")