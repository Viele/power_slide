import bpy
from ..callbacks import constants as _cb_constants


class PSL_Callback(bpy.types.PropertyGroup):
    type: bpy.props.EnumProperty(
        items=_cb_constants.CALLBACK_TYPES
    )
    # keyword "callback" will be added that holds the callback class


class PSL_CallbackGroup(bpy.types.PropertyGroup):
    callbacks: bpy.props.CollectionProperty(type=PSL_Callback)
    active_index : bpy.props.IntProperty()
