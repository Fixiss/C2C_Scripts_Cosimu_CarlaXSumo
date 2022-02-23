import random
import carla
import keyboard
import time

def main():
    try :
        client = carla.Client('localhost', 2000)
        client.set_timeout(10.0)
        world = client.get_world()
        i = 0
        time.sleep(5)
        while(True) :
            acteurs = world.get_actors()
            if(acteurs[i].type_id != 'spectator'):
                print(acteurs[i].type_id)
                acteurs[i].show_debug_telemetry(True)
            if keyboard.read_key("m"):
                i=(i+1)%10
                print(i)
            
    except KeyboardInterrupt:
        print("done")
        
if __name__ == '__main__' :
    main()