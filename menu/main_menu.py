import bpy
from ..operator import slide as _op_slide


class PSL_UL_list_test(bpy.types.UIList):
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        split = layout.split(factor=0.2)
        split.label(text="Slide: {index}".format(index=index))
        split.prop(item, "name")


class Foo(bpy.types.PropertyGroup):
    collection_ptr: bpy.props.PointerProperty(
        name="Collection",
        type=bpy.types.Collection
    )


class PSL_PT_Main_Menu(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    # bl_idname = "PSL_PT_main_menu"
    bl_label = "Power Slide"
    bl_category = "Power Slide"


    def draw(self, context):
        layout = self.layout
        # layout.operator_context = "INVOKE_DEFAULT"
        slide_collection = _op_slide.get_slide_collection(context.scene)
        layout.template_list("PSL_UL_list_test", "test", slide_collection, "children", context.scene, "slide_list_index")
        layout.operator("psl.create_slide")
        layout.operator("psl.delete_slide")

