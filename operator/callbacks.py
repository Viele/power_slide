import bpy
from bpy.types import Context, Event
from ..utils import slide as _slide_utils
from ..callbacks import constants as _cb_constants, main as _cb_main


class PSL_OT_Create_Callback(bpy.types.Operator):
    bl_idname = "psl.create_callback"
    bl_label = "Create Callback"
    bl_property = "callback_type"

    callback_type : bpy.props.EnumProperty(
        items=_cb_constants.CALLBACK_TYPES
    )

    def execute(self, context: bpy.types.Context):   
        current_slide = _slide_utils.get_current_slide(context)
        item = current_slide.collection.slide_callbacks.callbacks.add()
        item.type = self.callback_type
        _cb_main.create(item)
        for region in context.area.regions:
            region.tag_redraw()
        return {'FINISHED'}
    
    def invoke(self, context: Context, event: Event):
        wm = context.window_manager
        wm.invoke_search_popup(self)
        return {'FINISHED'}
    

class PSL_OT_Delete_Callback(bpy.types.Operator):
    bl_idname = "psl.delete_callback"
    bl_label = "Delete Callback"

    def execute(self, context: bpy.types.Context):
        current_slide = _slide_utils.get_current_slide(context)
        callback_list = current_slide.collection.slide_callbacks
        callback_list.callbacks.remove(callback_list.active_index)
        if callback_list.active_index > 0 and callback_list.active_index >= len(callback_list.callbacks):
            callback_list.active_index -= 1
        return {'FINISHED'}
