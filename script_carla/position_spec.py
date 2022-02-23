import carla
import keyboard

def main():
    try:
        client = carla.Client('localhost', 2000)
        client.set_timeout(10.0)
        world = client.get_world()
        spectator = world.get_spectator()
        while(True):
            if keyboard.is_pressed("k"):
                print(spectator.get_transform())
        
    except KeyboardInterrupt:
        pass
        

if __name__ == '__main__' :
    main()