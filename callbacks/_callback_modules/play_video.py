import bpy
from .. import errors as _cb_errors


def create(callback_prop):
    callback_prop["video"] = None


def draw(callback_prop, context: bpy.types.Context, layout: bpy.types.UILayout):
    # needs to be objects because "image_user", for which the frame_start can be set, is on the object
    layout.prop_search(callback_prop, '["video"]', bpy.data, "objects", text="Video")


def execute(callback_prop, context: bpy.types.Context):
    video_object = callback_prop["video"]
    if not video_object or not hasattr(video_object, "image_user"):
        raise _cb_errors.CallbackError("No Video defined, cannot run callback")
    video_object.image_user.frame_start = context.scene.frame_current


def cleanup(callback_prop, context: bpy.types.Context):
    pass


def get_list_name(callback_prop) -> str:
    video = callback_prop["video"]
    text = video.name if video else "None"
    return f"Play Video - {text}"


def pre_start_setup(callback_prop):
    pass
