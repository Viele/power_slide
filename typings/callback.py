import bpy
from ..utils import constants as _constants


class CallbackError(Exception):
    pass


class PSL_Callback(bpy.types.PropertyGroup):
    type: bpy.props.EnumProperty(
        items=_constants.CALLBACK_TYPES
    )
    # keyword "callback" will be added that holds the callback class


class PSL_CallbackGroup(bpy.types.PropertyGroup):
    callbacks: bpy.props.CollectionProperty(type=PSL_Callback)
    active_index : bpy.props.IntProperty()
