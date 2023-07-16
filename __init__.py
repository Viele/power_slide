bl_info = {
    "name": "Power Slide",
    "description": "Slide Presentation but with Blender",
    "author": "Christoph Lendenfeld",
    "version": (1, 0),
    "blender": (3, 6, 0),
    "category": "Animation",
}


def register():
    from . import operator, menu
    modules = [
        operator,
        menu
    ]
    for m in modules:
        m.register_operators()


def unregister():
    from . import operator, menu
    modules = [
        operator,
        menu
    ]
    for m in modules:
        m.unregister_operators()
