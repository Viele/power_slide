import bpy
from ..utils import callbacks as _callbacks
    

class PSL_Callback(bpy.types.PropertyGroup):
    callback: _callbacks.AbstractCallback
