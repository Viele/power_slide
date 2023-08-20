import bpy
from . import constants as _cb_constants, errors as _cb_errors
from ..typings import callback as _cb_types
from ._callback_modules import (
    play_video,
    run_script,
    set_text,
    set_camera,
    play_animation,
    play_grease_pencil,
)


# files in here are expected to have the following functions: create, draw, execute
_CALLBACK_TYPE_MAP = {
    _cb_constants.CALLBACK_RUN_SCRIPT: run_script,
    _cb_constants.CALLBACK_SET_TEXT: set_text,
    _cb_constants.CALLBACK_PLAY_VIDEO: play_video,
    _cb_constants.CALLBACK_SET_CAMERA: set_camera,
    _cb_constants.CALLBACK_PLAY_ANIMATION: play_animation,
    _cb_constants.CALLBACK_PLAY_GREASE_PENCIL: play_grease_pencil,
}


def _get_callback_module(type: str):
    callback_module = _CALLBACK_TYPE_MAP.get(type)
    if not callback_module:
        raise _cb_errors.CallbackError(f"No callback functions defined for {type}")
    return callback_module


def create(callback_prop: _cb_types.PSL_Callback):
    """ 
    Dynamically create properties needed for this type of callback. 
    Assumes type is already set on callback_object.
    """
    callback_module = _get_callback_module(callback_prop.type)
    callback_module.create(callback_prop)


def execute(callback_prop: _cb_types.PSL_Callback, context: bpy.types.Context):
    callback_module = _get_callback_module(callback_prop.type)
    callback_module.execute(callback_prop, context)


def draw(callback_prop: _cb_types.PSL_Callback, context: bpy.types.Context, layout):
    callback_module = _get_callback_module(callback_prop.type)
    callback_module.draw(callback_prop, context, layout)


def get_list_name(callback_prop: _cb_types.PSL_Callback) -> str:
    callback_module = _get_callback_module(callback_prop.type)
    return callback_module.get_list_name(callback_prop)


def pre_start_setup(callback_prop: _cb_types.PSL_Callback):
    """ Called before the presentation is run. """
    callback_module = _get_callback_module(callback_prop.type)
    callback_module.pre_start_setup(callback_prop)
