import bpy
    

class PSL_Callback(bpy.types.PropertyGroup):
    type: bpy.props.EnumProperty(
        items=(
            ('A', "test", "foo"),
        )
    )
    val: bpy.props.IntProperty()


class PSL_CallbackGroup(bpy.types.PropertyGroup):
    callbacks: bpy.props.CollectionProperty(type=PSL_Callback)
    active_index : bpy.props.IntProperty()
