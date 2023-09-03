""" Not an actual callback, just the functions and their parameters. """
import bpy


def create(callback_prop):
    """Create the required properties for the callback. """
    pass


def draw(callback_prop, context: bpy.types.Context, layout: bpy.types.UILayout):
    """ Draw the properties of the callback so the user can set them. """
    pass


def execute(callback_prop, context: bpy.types.Context):
    """ Run the callback. """
    pass


def cleanup(callback_prop, context: bpy.types.Context):
    """ Called just before the slide of the callback is left. """
    pass


def get_list_name(callback_prop) -> str:
    """ Return a nice name that is used in lists. """
    pass


def pre_start_setup(callback_prop):
    """ Setup anything that needs to be done before the presentation is started. """
    pass