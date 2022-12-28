import sys
sys.path.append('./')
import bpy

from options import Options
from load_bvh import load_bvh
from scene import make_scene, add_material_for_character, add_rendering_parameters

if __name__ == '__main__':
    args = Options(sys.argv).parse()

    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()

    character = load_bvh(args.bvh_path)
    scene = make_scene(floor_size=1000, camera_position=(40, 0, -2), camera_rotation=(1.57, 0.0109881, 1.57))
    add_material_for_character(character)
    bpy.ops.object.select_all(action='DESELECT')

    add_rendering_parameters(bpy.context.scene, args, scene[0])

    if args.render:
        bpy.ops.render.render(animation=True, use_viewport=True)
