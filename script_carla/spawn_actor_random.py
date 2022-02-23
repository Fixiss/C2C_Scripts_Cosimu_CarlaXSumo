import random
import time
import carla

def main():
    vehicleList = []
    try:
        client = carla.Client('localhost', 2000)
        client.set_timeout(10.0)
        tm = client.get_trafficmanager(8000)
        tm.set_synchronous_mode(True)
        tm.set_hybrid_physics_mode(True)
        tm_port = tm.get_port()
        world = client.get_world()
        map = world.get_map()
        spawn_points = map.get_spawn_points()
        blueprint_library = world.get_blueprint_library()
        for k in range(10): 
            vehicle_bp = random.choice(blueprint_library.filter('cybertruck'))
            spawn = random.choice(spawn_points)
            vehicle = world.try_spawn_actor(vehicle_bp, spawn)
            if(vehicle != None):
                vehicleList.append(vehicle)
        for v in vehicleList:
            v.set_autopilot(True, tm_port)
        spectator = world.get_spectator()
        i=0
        while(True):
            transform = vehicleList[i].get_transform()
            spectator.set_transform(carla.Transform(transform.location + carla.Location(z=50), carla.Rotation(pitch=-90)))
            i = (i+1) % len(vehicleList)
            time.sleep(1.0)
            
    except KeyboardInterrupt:
        pass
    finally:
        client.apply_batch([carla.command.DestroyActor(x) for x in vehicleList])
        

if __name__ == '__main__' :
    main()
        