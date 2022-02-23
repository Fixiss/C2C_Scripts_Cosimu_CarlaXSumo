import carla
import io
import sys

args = sys.argv[1:]
if(len(args)>=1):
    # Read the .osm data
    f = io.open(args[0], mode="r")
    xodr_data = f.read()
    f.close()
    client = carla.Client('localhost', 2000)
    vertex_distance = 2.0  # in meters
    max_road_length = 500.0 # in meters
    wall_height = 0.0      # in meters
    extra_width = 0.6      # in meters
    world = client.generate_opendrive_world(xodr_data, carla.OpendriveGenerationParameters(
        vertex_distance=vertex_distance,
        max_road_length=max_road_length,
        wall_height=wall_height,
        additional_width=extra_width,
        smooth_junctions=True,
        enable_mesh_visibility=True))
else:
    print("1 argument is required : arg->fichier.xodr")