import bpy

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
    current_index = context.scene.slide_list_index
    slide_collection = get_slide_collection(context)
    return slide_collection.children[current_index]


def activate_slide(context: bpy.types.Context, slide: bpy.types.LayerCollection):
    _disable_all_slides(context)
    slide_collection = get_slide_collection(context)
    context.scene.slide_list_index = slide_collection.children.find(slide.name)
    slide.exclude = False


def next_slide(context: bpy.types.Context):
    current_index = context.scene.slide_list_index
    slide_collection = get_slide_collection(context)
    if current_index+1 >= len(slide_collection.children):
        # hit last slide
        return
    
    activate_slide(context, slide_collection.children[current_index+1])


def activate_first_slide(context: bpy.types.Context):
    first_slide = get_slide_collection(context).children[0]
    activate_slide(context, first_slide)
