import typing
import bpy
from bpy.types import Context
from ..utils import slide as _slide_utils, callbacks as _callback_utils
from ..callbacks import main as _cb_main

def _pre_start_setup(context: bpy.types.Context):
    slides = _slide_utils.get_slides(context)
    for slide in slides:
        callbacks = _callback_utils.get_callbacks(slide, "on_enter")
        for cb in callbacks:
            _cb_main.pre_start_setup(cb)


class PSL_OT_Start_Presentation(bpy.types.Operator):
    bl_idname = "psl.start_presentation"
    bl_label = "Start Presentation"

    def execute(self, context: bpy.types.Context):
        context.scene.frame_current = 1
        context.scene.frame_end = 7200 * context.scene.render.fps  # 2hrs should be enough for any presentation
        _pre_start_setup(context)
        bpy.ops.screen.animation_play(sync=True)
        _slide_utils.set_slide_index(context, 0)
        return {'FINISHED'}


class PSL_OT_Stop_Presentation(bpy.types.Operator):
    bl_idname = "psl.stop_presentation"
    bl_label = "Stop Presentation"

    def execute(self, context: Context):
        bpy.ops.screen.animation_cancel()
        return {'FINISHED'}
    

class PSL_OT_Next_Slide(bpy.types.Operator):
    bl_idname = "psl.next_slide"
    bl_label = "Next Slide"

    def execute(self, context: Context):
        _slide_utils.next_slide(context)
        return {'FINISHED'}
    

class PSL_OT_Previous_Slide(bpy.types.Operator):
    bl_idname = "psl.previous_slide"
    bl_label = "Previous Slide"

    def execute(self, context: Context):
        _slide_utils.previous_slide(context)
        return {'FINISHED'}
