import bpy
from . import callbacks as _callback_utils

_SLIDE_COLLECTION = "power_slide_slides"


def _disable_all_slides(context: bpy.types.Context):
    slide_collection = get_slide_collection(context)
    for child in slide_collection.children:
        child.exclude = True


def get_slide_collection(context: bpy.types.Context) -> bpy.types.LayerCollection:
    view_layer = context.view_layer
    if _SLIDE_COLLECTION in view_layer.layer_collection.children:
        return view_layer.layer_collection.children[_SLIDE_COLLECTION]
    
    slide_collection = bpy.data.collections.new(_SLIDE_COLLECTION)
    view_layer.layer_collection.children.link(slide_collection)

    return view_layer.layer_collection.children[_SLIDE_COLLECTION]


def get_slide(context: bpy.types.Context, name: str) -> bpy.types.LayerCollection:
    slide_collection = get_slide_collection(context)

    if name not in slide_collection.children:
        raise ValueError(f"Slide '{name}' does not exist")
    
    return slide_collection.children[name]


def get_current_slide(context: bpy.types.Context) -> bpy.types.LayerCollection:
    current_index = context.scene.active_slide
    slide_collection = get_slide_collection(context)
    return slide_collection.children[current_index]


def activate_slide(context: bpy.types.Context, slide: bpy.types.LayerCollection):
    slide_collection = get_slide_collection(context)
    # not supported until I find a pre property changed callback
    # current_slide = slide_collection.children[context.scene.active_slide]
    # _callbacks.execute(current_slide.collection.on_exit)

    _disable_all_slides(context)

    context.scene.active_slide = slide_collection.children.find(slide.name)
    set_slide_visibility(slide)


def set_slide_visibility(slide: bpy.types.LayerCollection):
    slide.exclude = False
    slide.hide_viewport = False

    for child_collection in slide.children:
        child_collection.exclude = False
        child_collection.hide_viewport = False

    for callback in slide.collection.on_enter.callbacks:
        _callback_utils.execute(callback)


def active_slide_changed(context: bpy.types.Context):
    # callback to set things when the prop changed
    slide_collection = get_slide_collection(context)
    set_slide_visibility(slide_collection.children[context.scene.active_slide])


def next_slide(context: bpy.types.Context):
    current_index = context.scene.active_slide
    slide_collection = get_slide_collection(context)
    if current_index+1 >= len(slide_collection.children):
        # hit last slide
        return
    
    activate_slide(context, slide_collection.children[current_index+1])


def set_slide_index(context: bpy.types.Context, index: int):
    context.scene.active_slide = index
