import bpy


_TEMPLATE_COLLECTION = "power_slide_templates"


def get_slide_template_collection(context: bpy.types.Context) -> bpy.types.LayerCollection:
    view_layer = context.view_layer
    if _TEMPLATE_COLLECTION in view_layer.layer_collection.children:
        return view_layer.layer_collection.children[_TEMPLATE_COLLECTION]
    
    if _TEMPLATE_COLLECTION in bpy.data.collections:
        template_collection = bpy.data.collections[_TEMPLATE_COLLECTION]
    else:
        template_collection = bpy.data.collections.new(_TEMPLATE_COLLECTION)

    view_layer.layer_collection.collection.children.link(template_collection)
    return view_layer.layer_collection.children[_TEMPLATE_COLLECTION]
