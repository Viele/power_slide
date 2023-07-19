import bpy


class PSL_OT_Create_Callback(bpy.types.Operator):
    bl_idname = "psl.create_callback"
    bl_label = "Create Callback"

    def execute(self, context: bpy.types.Context):
        
        return {'FINISHED'}
    

class PSL_OT_Delete_Callback(bpy.types.Operator):
    bl_idname = "psl.delete_callback"
    bl_label = "Delete Callback"

    def execute(self, context: bpy.types.Context):
        
        return {'FINISHED'}