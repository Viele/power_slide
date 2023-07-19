import bpy
from ..utils import slide as _slide_utils, constants as _constants


class PSL_OT_Create_Callback(bpy.types.Operator):
    bl_idname = "psl.create_callback"
    bl_label = "Create Callback"
    callback_list : bpy.props.EnumProperty(
        items=(
            ("on_enter", "On Enter", "foo"),
            ("on_exit", "On Exit", "foo"),
        )
    )
    callback_type : bpy.props.EnumProperty(
        items=_constants.CALLBACK_TYPES
    )

    def execute(self, context: bpy.types.Context):
        current_slide = _slide_utils.get_current_slide(context)
        item = getattr(current_slide.collection, self.callback_list).callbacks.add()
        item.type = self.callback_type
        return {'FINISHED'}
    

class PSL_OT_Delete_Callback(bpy.types.Operator):
    bl_idname = "psl.delete_callback"
    bl_label = "Delete Callback"

    def execute(self, context: bpy.types.Context):
        
        return {'FINISHED'}