import bpy
from ..utils import (
    slide as _slide_utils, 
    callbacks as _callback_utils
)

from ..callbacks import main as _cb_main


def _draw_callback_gui(context: bpy.types.Context, layout: bpy.types.UILayout, callback_list: str):
    active_slide = _slide_utils.get_current_slide(context)
    layout.label(text=f"Callbacks for slide: '{active_slide.name}'")
    layout.template_list(
        "PSL_UL_callbacks", "", 
        getattr(active_slide.collection, callback_list), "callbacks", 
        getattr(active_slide.collection, callback_list), "active_index")
    row = layout.row()
    op = row.operator("psl.create_callback")
    op.callback_list = callback_list
    op = row.operator("psl.delete_callback")
    op.callback_list = callback_list

    callbacks = _callback_utils.get_callbacks(context, callback_list)
    for cb in callbacks:
        box = layout.box()
        box.label(text=_cb_main.get_list_name(cb))
        _cb_main.draw(cb, context, box)


class PSL_PT_Callbacks(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "Callbacks - On Enter"
    bl_category = "Power Slide"

    def draw(self, context: bpy.types.Context):
        layout = self.layout
        _draw_callback_gui(context, layout, "on_enter")
