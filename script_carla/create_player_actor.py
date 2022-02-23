import random
import carla
import keyboard

def set_2_auto(v, s):
    print("automatique on")
    v.set_autopilot(True)
    while(True):
            transform = v.get_transform()
            s.set_transform(carla.Transform(transform.location + carla.Location(z=50), carla.Rotation(pitch=-90)))
            if keyboard.is_pressed("m"):
                set_2_manuel(v,s)
                
    
def set_2_manuel(v, s):
    print("automatique off")
    v.set_autopilot(False)
    while(True):
            transform = v.get_transform()
            s.set_transform(carla.Transform(transform.location + carla.Location(z=50), carla.Rotation(pitch=-90)))
            if keyboard.is_pressed("o"):
                set_2_auto(v,s)

def main():
    vehicule = None
    try:
        client = carla.Client('localhost', 2000)
        client.set_timeout(10.0)
        world = client.get_world()
        map = world.get_map()
        tm = client.get_trafficmanager(8000)
        tm.set_synchronous_mode(True)
        tm.set_hybrid_physics_mode(True)
        spawn_points = map.get_spawn_points()
        blueprint_library = world.get_blueprint_library()
        vehicle_bp = random.choice(blueprint_library.filter('cybertruck'))
        spawn = random.choice(spawn_points)
        vehicle = world.try_spawn_actor(vehicle_bp, spawn)
        spectator = world.get_spectator()
        set_2_manuel(vehicle,spectator)
        
    except KeyboardInterrupt:
        pass
    finally:
        print(vehicle.destroy())
        

if __name__ == '__main__' :
    main()
        