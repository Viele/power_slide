import bpy
from . import constants as _cb_constants, errors as _cb_errors
from ..typings import callback as _cb_types
from . import (
    _run_script, 
    _set_text,
)


# files in here are expected to have the following functions: create, draw, execute
_CALLBACK_TYPE_MAP = {
    _cb_constants.CALLBACK_RUN_SCRIPT: _run_script,
    _cb_constants.CALLBACK_SET_TEXT: _set_text,
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