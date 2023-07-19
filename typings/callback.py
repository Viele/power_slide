import bpy
from ..utils import constants as _constants


class PSL_Callback(bpy.types.PropertyGroup):
    type: bpy.props.EnumProperty(
        items=_constants.CALLBACK_TYPES
    )
    val: bpy.props.IntProperty()


class PSL_CallbackGroup(bpy.types.PropertyGroup):
    callbacks: bpy.props.CollectionProperty(type=PSL_Callback)
    active_index : bpy.props.IntProperty()
