import bpy
from ..callbacks import main as _cb_main
from ..utils import callbacks as _cb_utils

_SLIDE_COLLECTION = "power_slide_slides"


def _disable_all_slides(context: bpy.types.Context):
    slide_collection = get_slide_collection(context)
    for child in slide_collection.children:
        child.exclude = True


def _set_slide_visibility(slide: bpy.types.LayerCollection):
    slide.exclude = False
    slide.hide_viewport = False

    for child_collection in slide.children:
        child_collection.exclude = False
        child_collection.hide_viewport = False


def _execute_slide_callbacks(slide: bpy.types.LayerCollection, context: bpy.types.Context):
    callbacks = _cb_utils.get_callbacks(slide)
    for callback in callbacks:
        _cb_main.execute(callback, context)


def _cleanup_slide_callbacks(context: bpy.types.Context, slide: bpy.types.LayerCollection):
    callbacks = _cb_utils.get_callbacks(slide)
    for callback in callbacks:
        _cb_main.cleanup(callback, context)


def get_slide_collection(context: bpy.types.Context) -> bpy.types.LayerCollection:
    view_layer = context.view_layer
    if _SLIDE_COLLECTION in view_layer.layer_collection.children:
        return view_layer.layer_collection.children[_SLIDE_COLLECTION]
    
    if _SLIDE_COLLECTION in bpy.data.collections:
        slide_collection = bpy.data.collections[_SLIDE_COLLECTION]
    else:
        slide_collection = bpy.data.collections.new(_SLIDE_COLLECTION)
        
    view_layer.layer_collection.collection.children.link(slide_collection)

    return view_layer.layer_collection.children[_SLIDE_COLLECTION]


def get_slide(context: bpy.types.Context, name: str) -> bpy.types.LayerCollection:
    slide_collection = get_slide_collection(context)

    if name not in slide_collection.children:
        raise ValueError(f"Slide '{name}' does not exist")
    
    return slide_collection.children[name]


def get_slides(context: bpy.types.Context):
    slide_collection = get_slide_collection(context)
    return slide_collection.children


def get_current_slide(context: bpy.types.Context) -> bpy.types.LayerCollection:
    current_index = context.scene.active_slide
    slide_collection = get_slide_collection(context)
    if not slide_collection.children:
        return
    return slide_collection.children[current_index]


def active_slide_changed(context: bpy.types.Context):
    # callback to set things when the prop changed
    slide_collection = get_slide_collection(context)
    if not slide_collection.children:
        return
    current_index = context.scene.active_slide
    if current_index < 0 or current_index >= len(slide_collection.children):
        return
    
    previous_index = context.scene.slide_index_buffer
    _cleanup_slide_callbacks(context, slide_collection.children[previous_index])

    slide = slide_collection.children[current_index]
    _disable_all_slides(context)
    _set_slide_visibility(slide)
    context.view_layer.active_layer_collection = slide
    _execute_slide_callbacks(slide, context)

    context.scene.slide_index_buffer = current_index


def next_slide(context: bpy.types.Context):
    current_index = context.scene.active_slide
    
    slide_collection = get_slide_collection(context)
    if current_index+1 >= len(slide_collection.children):
        # hit last slide
        return
    
    set_slide_index(context, current_index+1)


def previous_slide(context: bpy.types.Context):
    current_index = context.scene.active_slide
    if current_index - 1 < 0:
        # hit first slide
        return
    
    set_slide_index(context, current_index-1)


def set_slide_index(context: bpy.types.Context, index: int):
    # The visibility will be set by the callback on the prop
    context.scene.active_slide = index
