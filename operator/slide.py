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
        collection_names = []
        for name in collection_names:
            collection = bpy.data.collections.get(name)
            bpy.data.collections.remove(collection)
        return {"FINISHED"}


class PSL_OT_Reorder_Slide(bpy.types.Operator):
    bl_idname = "psl.reorder_slide"
    bl_label = "Reorder Slide"


class PSL_OT_Add_Object_To_Slide(bpy.types.Operator):
    bl_idname = "psl.add_object_to_slide"
    bl_label = "Add Object to Slide"


class PSL_OT_Remove_Object_From_Slide(bpy.types.Operator):
    bl_idname = "psl.remove_object_from_slide"
    bl_label = "Remove Object from Slide"
