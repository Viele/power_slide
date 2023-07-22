import bpy
from . import errors as _cb_errors


def create(callback_prop):
    callback_prop["text"] = None


def draw(callback_prop, context: bpy.types.Context, layout: bpy.types.UILayout):
    layout.prop_search(callback_prop, '["text"]', bpy.data, "texts")


def execute(callback_prop, context: bpy.types.Context):
    text_object = callback_prop["text"]
    if not text_object:
        raise _cb_errors.CallbackError("No text defined, cannot run callback")
    exec(text_object.as_string())
