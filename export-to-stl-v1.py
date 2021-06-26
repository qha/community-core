#
# Community Core - STL Export Script
#
# Exports objects in "Community Core" collection into STL files in subdirectory "stl-export"
#
# For description of Blender scripting, see
# https://docs.blender.org/manual/en/latest/editors/text_editor.html

import bpy
import os

# https://blender.stackexchange.com/a/142317/3413
def console_log(*data):
    for window in bpy.context.window_manager.windows:
        screen = window.screen
        for area in screen.areas:
            if area.type == 'CONSOLE':
                override = {'window': window, 'screen': screen, 'area': area}
                bpy.ops.console.scrollback_append(override, text=str(" ".join([str(x) for x in data])), type="OUTPUT")       

# get the current path and make a new folder for the exported meshes
path = bpy.path.abspath('//stl-export/')

if not os.path.exists(path):
    os.makedirs(path)

for name in bpy.data.collections:
    console_log("Collection: ", name)

# Automatically select correct objects:
bpy.ops.object.select_all(action='DESELECT')
for obj in bpy.data.collections['Community core'].all_objects:
    obj.select_set(True)

for object in bpy.context.selected_objects:


    # deselect all meshes
    bpy.ops.object.select_all(action='DESELECT')

    # select the object
    #bpy.context.scene.objects.active = object
    object.select_set(True)

    console_log("Exporting \"" + object.name + ".stl\" ...")


    # export object with its name as file name
    fPath = str((path + object.name + '.stl'))

    # https://docs.blender.org/api/current/bpy.ops.export_mesh.html
    #bpy.context.active_object = object
    bpy.ops.export_mesh.stl(filepath=fPath, use_selection=True, use_mesh_modifiers=True) # maybe add scale= some number, use_scene_unit=true?, use_mesh_modifiers=true

