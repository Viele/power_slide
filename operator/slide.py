import bpy
from ..utils import slide as _slide_utils

    

class PSL_OT_Create_Slide(bpy.types.Operator):
    bl_idname = "psl.create_slide"
    bl_label = "Create Slide"

    def execute(self, context: bpy.types.Context):
        slide = bpy.data.collections.new("Slide")
        slide_collection = _slide_utils.get_slide_collection(context)
        slide_collection.collection.children.link(slide)
        
        return {"FINISHED"}


class PSL_OT_Duplicate_Slide(bpy.types.Operator):
    bl_idname = "psl.duplicate_slide"
    bl_label = "Duplicate Slide"

    def execute(self, context: bpy.types.Context):
        pass


class PSL_OT_Delete_Slide(bpy.types.Operator):
    bl_idname = "psl.delete_slide"
    bl_label = "Delete Slide"

    def execute(self, context: bpy.types.Context):
        current_index = context.scene.active_slide
        slide_collection = _slide_utils.get_slide_collection(context)
        current_slide = slide_collection.collection.children[current_index]
        slide_collection.collection.children.unlink(current_slide)
        bpy.data.collections.remove(current_slide)
        # not removing the objects that are within the collection. 
        # If they have no users, they will be cleaned on save/reload
        if current_index > 0 and current_index >= len(slide_collection.collection.children):
            context.scene.active_slide -= 1
        return {"FINISHED"}


class PSL_OT_Reorder_Slide(bpy.types.Operator):
    bl_idname = "psl.reorder_slide"
    bl_label = "Reorder Slide"

    direction: bpy.props.EnumProperty(items=(
        ('UP', "Up", "Move slide up in the list"),
        ('DOWN', "Down", "Move slide down in the list"),
    ))

    def execute(self, context: bpy.types.Context):
        current_index = context.scene.active_slide
        target_index = current_index - 1 if self.direction == 'UP' else current_index + 1

        slide_collection = _slide_utils.get_slide_collection(context)
        if target_index < 0 or target_index > len(slide_collection.children):
            return {'CANCELLED'}
        slides = slide_collection.collection.children[:]
        slides[current_index], slides[target_index] = slides[target_index], slides[current_index]
        for slide in slides:
            slide_collection.collection.children.unlink(slide)
            slide_collection.collection.children.link(slide)

        context.scene.active_slide = target_index
        return {'FINISHED'}


class PSL_OT_Add_Object_To_Slide(bpy.types.Operator):
    bl_idname = "psl.add_object_to_slide"
    bl_label = "Add Object to Slide"


class PSL_OT_Remove_Object_From_Slide(bpy.types.Operator):
    bl_idname = "psl.remove_object_from_slide"
    bl_label = "Remove Object from Slide"
