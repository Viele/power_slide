import bpy

class PSL_Template(bpy.types.PropertyGroup):
    # keeping track of the templates added manually so as not to confuse with other collection children
    template: bpy.props.PointerProperty(type=bpy.types.Collection)


class PSL_TemplateGroup(bpy.types.PropertyGroup):
    templates: bpy.props.CollectionProperty(type=PSL_Template)
    active_index: bpy.props.IntProperty()
