import bpy
from .. import errors as _cb_errors


def create(callback_prop):
    callback_prop["text"] = None


def draw(callback_prop, context: bpy.types.Context, layout: bpy.types.UILayout):
    layout.prop_search(callback_prop, '["text"]', bpy.data, "texts", text="Script")


def execute(callback_prop, context: bpy.types.Context):
    text_object = callback_prop["text"]
    if not text_object:
        raise _cb_errors.CallbackError("No text defined, cannot run callback")
    exec(text_object.as_string())


def cleanup(callback_prop, context: bpy.types.Context):
    pass


def get_list_name(callback_prop) -> str:
    text_object = callback_prop["text"]
    text = text_object.name if text_object else "None"
    return f"Run Script - {text}"


def pre_start_setup(callback_prop):
    pass
