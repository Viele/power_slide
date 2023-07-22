import bpy
from . import constants as _constants
from ..typings import callback as _callback_types


def _execute_run_script_callback(callback_prop: _callback_types.PSL_Callback, context: bpy.types.Context):
    text_object = callback_prop["text"]
    if not text_object:
        raise _callback_types.CallbackError("No text defined, cannot run callback")
    exec(text_object.as_string())


def _execute_set_text_callback(callback_prop: _callback_types.PSL_Callback, context: bpy.types.Context):
    text = callback_prop["text"]
    text_object = callback_prop["text_object"]
    text_object.body = text


def execute(callback_prop: _callback_types.PSL_Callback, context: bpy.types.Context):
    execute_function_map = {
        _constants.CALLBACK_RUN_SCRIPT: _execute_run_script_callback,
        _constants.CALLBACK_SET_TEXT: _execute_set_text_callback,
    }
    execute_function = execute_function_map.get(callback_prop.type)
    if not execute_function:
        raise _callback_types.CallbackError(f"No execution function defined for {callback_prop.type}")
    execute_function(callback_prop, context)
