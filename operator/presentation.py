import bpy
from bpy.types import Context
from ..utils import slide as _slide_utils


class PSL_OT_Start_Presentation(bpy.types.Operator):
    bl_idname = "psl.start_presentation"
    bl_label = "Start Presentation"

    def execute(self, context: bpy.types.Context):
        context.scene.frame_current = 1
        context.scene.frame_end = 7200 * context.scene.render.fps  # 2hrs should be enough for any presentation
        bpy.ops.screen.animation_play(sync=True)
        _slide_utils.activate_first_slide(context)
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
