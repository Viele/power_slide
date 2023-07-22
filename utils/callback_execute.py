import bpy
from . import constants as _constants
from ..typings import callback as _callback_types


def _execute_run_script_callback(callback_prop: _callback_types.PSL_Callback):
    text_object = callback_prop["text"]
    if not text_object:
        raise RuntimeError("No text defined, cannot run callback")
    exec(text_object.as_string())


def execute(callback_prop: _callback_types.PSL_Callback):
    execute_function_map = {
        _constants.CALLBACK_RUN_SCRIPT: _execute_run_script_callback,
    }
    execute_function = execute_function_map.get(callback_prop.type)
    if not execute_function:
        raise RuntimeError(f"No execution function defined for {callback_prop.type}")
    execute_function(callback_prop)
