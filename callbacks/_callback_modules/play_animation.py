import bpy
from .. import errors as _cb_errors


def _get_nla_track(ob: bpy.types.Object) -> bpy.types.NlaTrack:
    if not ob.animation_data:
        ob.animation_data_create()
    if "power_slider_track" in ob.animation_data.nla_tracks:
        return ob.animation_data.nla_tracks["power_slider_track"]
    track = ob.animation_data.nla_tracks.new()
    track.name = "power_slider_track"
    return track


def _get_action_range(action: bpy.types.Action):
    range = [0, 1]
    for fcu in action.fcurves:
        range[0] = max(range[0], fcu.keyframe_points[0].co[0])
        range[1] = max(range[1], fcu.keyframe_points[-1].co[0])
    return range


def create(callback_prop):
    callback_prop["object"] = None
    callback_prop["action"] = None
    callback_prop["use_action_range"] = False
    callback_prop["action_range"] = (1, 100)
    callback_prop["loop"] = False


def draw(callback_prop, context: bpy.types.Context, layout: bpy.types.UILayout):
    layout.prop_search(callback_prop, '["object"]', bpy.data, "objects", text="Object")
    layout.prop_search(callback_prop, '["action"]', bpy.data, "actions", text="Action")
    layout.prop(callback_prop, '["loop"]', text="Loop")

    layout.prop(callback_prop, '["use_action_range"]', text="Action Range")
    row = layout.row()
    row.enabled = callback_prop["use_action_range"]
    row.prop(callback_prop, '["action_range"]', text="")


def execute(callback_prop, context: bpy.types.Context):
    ob = callback_prop["object"]
    action  = callback_prop["action"]
    if not ob or not action:
        raise _cb_errors.CallbackError("Object or Action not defined. Cannot apply animation.")
    
    if ob.animation_data:
        # need to disable the action so the track can play
        ob.animation_data.action = None

    nla_track = _get_nla_track(ob)
    nla_track.mute = False
    if "power_slide_strip" in nla_track.strips:
        strip = nla_track.strips["power_slide_strip"]
        strip.action = action
        strip.frame_start = context.scene.frame_current
    else:
        strip = nla_track.strips.new("power_slide_strip", context.scene.frame_current, action)
        # the name in new() doesn't stick
        strip.name = "power_slide_strip"

    if callback_prop["use_action_range"]:
        strip.action_frame_start = callback_prop["action_range"][0]
        strip.action_frame_end = callback_prop["action_range"][1]
    else:
        action_range = _get_action_range(action)
        strip.action_frame_start = 1  # hardcoding to 1 to allow for a non moving start
        strip.action_frame_end = action_range[1]

    # 1000 seems to be the max value
    strip.repeat = 1000 if callback_prop["loop"] else 1


def cleanup(callback_prop, context: bpy.types.Context):
    pass


def get_list_name(callback_prop) -> str:
    action = callback_prop["action"]
    text = action.name if action else "None"
    return f"Play Animation - {text}"


def pre_start_setup(callback_prop):
    ob = callback_prop["object"]
    action = callback_prop["action"]
    if not action or not ob:
        return
    
    nla_track = _get_nla_track(ob)
    nla_track.mute = True
