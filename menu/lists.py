import bpy
from ..callbacks import main as _cb_main


class PSL_UL_slides(bpy.types.UIList):
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        # split = layout.split(factor=0.2)
        # split.label(text="Slide: {index}".format(index=index))
        layout.prop(item, "name")

    
class PSL_UL_callbacks(bpy.types.UIList):
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        item_text = _cb_main.get_list_name(item)
        layout.label(text=item_text)
