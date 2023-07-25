import bpy
from ..utils import slide_template as _template_utils, slide as _slide_utils

    

class PSL_OT_Create_Slide_Template(bpy.types.Operator):
    bl_idname = "psl.create_slide_template"
    bl_label = "Create Slide Template"

    def execute(self, context: bpy.types.Context):
        slide_template = bpy.data.collections.new("Slide Template")
        template_collection = _template_utils.get_slide_template_collection(context)
        template_collection.collection.children.link(slide_template)
        
        return {"FINISHED"}


class PSL_OT_Delete_Slide_Template(bpy.types.Operator):
    bl_idname = "psl.delete_slide_template"
    bl_label = "Delete Slide Template"

    def execute(self, context: bpy.types.Context):
        # TODO deleting a template needs to remove it from all slides as well but raise a warning before
        """current_index = context.scene.active_slide_template
        template_collection = _template_utils.get_slide_template_collection(context)
        if not template_collection.collection.children:
            return
        current_template = template_collection.collection.children[current_index]
        template_collection.collection.children.unlink(current_template)
        bpy.data.collections.remove(current_template)
        # not removing the objects that are within the collection. 
        # If they have no users, they will be cleaned on save/reload
        if current_index > 0 and current_index >= len(template_collection.collection.children):
            context.scene.active_slide_template -= 1"""
        return {"FINISHED"}


class PSL_OT_Add_Template_To_Slide(bpy.types.Operator):
    bl_idname = "psl.add_template_to_slide"
    bl_label = "Add Template to Slide"

    template: bpy.props.EnumProperty(
        name="Templates", 
        items=_template_utils.get_template_enum
    )

    def execute(self, context: bpy.types.Context):
        active_slide = _slide_utils.get_current_slide(context)
        # going for bpy.data because we only get the name from the enum
        template = bpy.data.collections[self.template]

        if template.name in active_slide.collection.children:
            message = f"Template '{template.name}' already assigned to '{active_slide.name}'"
            self.report({'ERROR'}, message)
            return {'CANCELLED'}
        
        _template_utils.add_template_to_slide(active_slide, template)
        return {'FINISHED'}
    

    def invoke(self, context: bpy.types.Context, event: bpy.types.Event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)
    

class PSL_OT_Remove_Template_from_Slide(bpy.types.Operator):
    bl_idname = "psl.remove_template_from_slide"
    bl_label = "Remove Template from Slide"

    def execute(self, context: bpy.types.Context):
        active_slide = _slide_utils.get_current_slide(context)
        if not active_slide:
            return {'CANCELLED'}
        
        if not active_slide.collection.children:
            self.report({'ERROR'}, "No template to remove")
            return {'CANCELLED'}

        template_data = active_slide.collection.template_data
        slide_template_index = template_data.active_index
        template = template_data.templates[slide_template_index].template

        if template.name not in active_slide.collection.children:
            self.report({'ERROR'}, "Template not used on slide")
            return {'CANCELLED'}
        
        _template_utils.remove_template_from_slide(active_slide, template)
        return {'FINISHED'}
