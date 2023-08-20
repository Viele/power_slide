import bpy
from .. import errors as _cb_errors


def create(callback_prop):
    callback_prop["text"] = ""
    callback_prop["text_object"] = None


def draw(callback_prop, context: bpy.types.Context, layout: bpy.types.UILayout):
    layout.prop_search(callback_prop, '["text_object"]', bpy.data, "curves", text="Text Object")
    layout.prop(callback_prop, '["text"]', text="Text")


def execute(callback_prop, context: bpy.types.Context):
    text = callback_prop["text"]
    text_object = callback_prop["text_object"]
    if not text_object or not hasattr(text_object, "body"):
        raise _cb_errors.CallbackError(f"Cannot set text on {text_object}")
    text_object.body = text


def get_list_name(callback_prop) -> str:
    text = callback_prop["text"]
    shortened_text = (text[:32] + "...") if len(text) > 35 else text
    return f"Set Text - {shortened_text}"


def pre_start_setup(callback_prop):
    pass
