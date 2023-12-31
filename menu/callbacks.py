import bpy
from ..utils import (
    slide as _slide_utils, 
    callbacks as _callback_utils
)

from ..callbacks import main as _cb_main


class PSL_UL_callbacks(bpy.types.UIList):
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        item_text = _cb_main.get_list_name(item)
        layout.label(text=item_text)


def _draw_callback_gui(context: bpy.types.Context, layout: bpy.types.UILayout):
    active_slide = _slide_utils.get_current_slide(context)
    if not active_slide:
        layout.label(text="No active slide")
        return
    layout.label(text=f"Callbacks for slide: '{active_slide.name}'")
    row = layout.row()
    row.template_list(
        "PSL_UL_callbacks", "", 
        active_slide.collection.slide_callbacks, "callbacks", 
        active_slide.collection.slide_callbacks, "active_index")
    col = row.column()
    col.operator("psl.create_callback", icon='ADD', text="")
    col.operator("psl.delete_callback", icon='REMOVE', text="")

    callbacks = _callback_utils.get_callbacks_from_active_slide(context)
    for cb in callbacks:
        box = layout.box()
        box.label(text=_cb_main.get_list_name(cb))
        _cb_main.draw(cb, context, box)


class PSL_PT_Callbacks(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "Callbacks"
    bl_category = "Power Slide"
    bl_parent_id = "PSL_PT_Slides"

    def draw(self, context: bpy.types.Context):
        layout = self.layout
        _draw_callback_gui(context, layout)
