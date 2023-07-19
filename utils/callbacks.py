import abc
import bpy
from . import constants as _constants


def _draw_execute_script_callback(callback_prop, context: bpy.types.Context, layout: bpy.types.UILayout):
    layout.label(text=callback_prop.type)
    # layout.prop(callback_prop, "callback_data")
    if not callback_prop.callback_object:
        return
    print(callback_prop.callback_object)
    # layout.prop(callback_prop.callback_object, '["text"]')
    layout.prop_search(callback_prop.callback_object, "['text']", bpy.data, "texts")


def execute(callbacks):
    pass


def get_active_callback(context: bpy.types.Context, list_name: str):
    from . import slide as _slide_utils
    current_slide = _slide_utils.get_current_slide(context)
    if len(current_slide.children) == 0:
        return
    
    callback_list = getattr(current_slide.collection, list_name)
    if len(callback_list.callbacks) == 0:
        return
    return callback_list.callbacks[callback_list.active_index]


_CALLBACK_PROPERTIES = {
    _constants.CALLBACK_RUN_SCRIPT: (
        ("text", bpy.props.PointerProperty, {"type":bpy.types.Text}),
    ),
}


_CALLBACK_DRAW_FUNCTIONS = {
    _constants.CALLBACK_RUN_SCRIPT: _draw_execute_script_callback,
}


def construct_type_props(callback_object: bpy.types.Object):
    """ Dynamically create properties needed for this type of callback"""
    # assumes type is already set on callback_object
    callback_properties = _CALLBACK_PROPERTIES.get(callback_object.type, {})
    print(callback_object)
    for name, prop_type, prop_kwargs in callback_properties:
        print(name)
        callback_object[name] = prop_type(**prop_kwargs)
        # setattr(callback_object, name, )


def draw_callback_props(callback_prop, context, layout):
    draw_fn = _CALLBACK_DRAW_FUNCTIONS.get(callback_prop.type)
    if draw_fn:
        draw_fn(callback_prop, context, layout)


def get_callback_list(slide: bpy.types.LayerCollection, list_name: str):
    if list_name in slide.children:
        return slide.children[list_name]
    
    callback_list = bpy.data.collections.new(list_name)
    slide.collection.children.link(callback_list)

    return slide.children[list_name]


















class AbstractCallback(abc.ABC):
    name = "Abstract Callback"

    def execute(self):
        pass

    def draw(self, context, layout):
        pass


class SetText(AbstractCallback):
    name = "Set Text"


class PlayVideo(AbstractCallback):
    name = "Play Video"


class PauseVideo(AbstractCallback):
    name = "Pause Video"


class RunScript(AbstractCallback):
    name = "Execute Script"

    def draw(self, context, layout):
        layout.label(text="test")
