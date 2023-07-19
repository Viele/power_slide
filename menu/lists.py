import bpy


class PSL_UL_slides(bpy.types.UIList):
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        split = layout.split(factor=0.2)
        split.label(text="Slide: {index}".format(index=index))
        split.prop(item, "name")

    
class PSL_UL_callbacks(bpy.types.UIList):
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        layout.prop(item, "type", text="Type")
