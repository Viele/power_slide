import bpy
from ..utils import slide_template as _template_utils

    

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
        current_index = context.scene.active_slide_template
        template_collection = _template_utils.get_slide_template_collection(context)
        if not template_collection.collection.children:
            return
        current_template = template_collection.collection.children[current_index]
        template_collection.collection.children.unlink(current_template)
        bpy.data.collections.remove(current_template)
        # not removing the objects that are within the collection. 
        # If they have no users, they will be cleaned on save/reload
        if current_index > 0 and current_index >= len(template_collection.collection.children):
            context.scene.active_slide_template -= 1
        return {"FINISHED"}