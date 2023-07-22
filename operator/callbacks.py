import typing
import bpy
from bpy.types import Context, Event
from ..utils import slide as _slide_utils, constants as _constants, callbacks as _callback_utils


_CALLBACK_LISTS = (
    ("on_enter", "On Enter", "Executed before the slide is shown"),
)


class PSL_OT_Create_Callback(bpy.types.Operator):
    bl_idname = "psl.create_callback"
    bl_label = "Create Callback"

    callback_list : bpy.props.EnumProperty(
        items=_CALLBACK_LISTS
    )
    callback_type : bpy.props.EnumProperty(
        items=_constants.CALLBACK_TYPES
    )

    def execute(self, context: bpy.types.Context):   
        current_slide = _slide_utils.get_current_slide(context)
        item = getattr(current_slide.collection, self.callback_list).callbacks.add()
        item.type = self.callback_type
        _callback_utils.construct_type_props(item)

        return {'FINISHED'}
    
    def invoke(self, context: Context, event: Event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)
    

class PSL_OT_Delete_Callback(bpy.types.Operator):
    bl_idname = "psl.delete_callback"
    bl_label = "Delete Callback"

    callback_list : bpy.props.EnumProperty(
        items=_CALLBACK_LISTS
    )

    def execute(self, context: bpy.types.Context):
        current_slide = _slide_utils.get_current_slide(context)
        callback_list = getattr(current_slide.collection, self.callback_list)
        callback_list.callbacks.remove(callback_list.active_index)
        return {'FINISHED'}
