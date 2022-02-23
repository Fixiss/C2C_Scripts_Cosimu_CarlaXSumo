import carla
import sys
args = sys.argv[1:]
if(len(args)>=1):
    client = carla.Client('localhost', 2000)
    client.set_timeout(100.0)
    world = client.load_world(args[0])
else:
    print("1 argument is required : arg -> map")