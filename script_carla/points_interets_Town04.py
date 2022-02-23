# général : Transform(Location(x=-46.499439, y=47.091656, z=834.813660), Rotation(pitch=-87.808296, yaw=-91.897728, roll=-0.000670))
# ville : Transform(Location(x=219.444626, y=-57.057800, z=372.209442), Rotation(pitch=-76.228661, yaw=-87.416748, roll=-0.001069))
# le pont : Transform(Location(x=42.242859, y=9.309633, z=107.283073), Rotation(pitch=-68.665077, yaw=170.743332, roll=-0.000885))
# feux autoroutes : Transform(Location(x=-328.744965, y=14.240213, z=51.059624), Rotation(pitch=-48.154842, yaw=-178.522141, roll=-0.000885))
# stop autoroutes : Transform(Location(x=378.543030, y=-1.073679, z=78.516823), Rotation(pitch=-83.857254, yaw=14.944255, roll=-0.000981))
# sortie nord : Transform(Location(x=58.836407, y=-336.930145, z=27.107143), Rotation(pitch=-32.555294, yaw=142.710449, roll=-0.000915))
# intersection : Transform(Location(x=247.115997, y=-156.910461, z=46.706787), Rotation(pitch=-69.582947, yaw=-63.765865, roll=-0.001008))

import carla
import keyboard

def main():
    try:
        client = carla.Client('localhost', 2000)
        client.set_timeout(10.0)
        world = client.get_world()
        spectator = world.get_spectator()
        while(True):
            if keyboard.is_pressed("1"):
                spectator.set_transform(carla.Transform(carla.Location(x=-46.499439, y=47.091656, z=834.813660), carla.Rotation(pitch=-87.808296, yaw=-91.897728, roll=-0.000670)))
                print("Vue generale")
            if keyboard.is_pressed("2"):
                spectator.set_transform(carla.Transform(carla.Location(x=219.444626, y=-57.057800, z=372.209442), carla.Rotation(pitch=-76.228661, yaw=-87.416748, roll=-0.001069)))
                print("Ville")
            if keyboard.is_pressed("3"):
                spectator.set_transform(carla.Transform(carla.Location(x=42.242859, y=9.309633, z=107.283073), carla.Rotation(pitch=-68.665077, yaw=170.743332, roll=-0.000885)))
                print("Le pont")
            if keyboard.is_pressed("4"):
                spectator.set_transform(carla.Transform(carla.Location(x=-328.744965, y=14.240213, z=51.059624), carla.Rotation(pitch=-48.154842, yaw=-178.522141, roll=-0.000885)))
                print("Feux autoroute")
            if keyboard.is_pressed("5"):
                spectator.set_transform(carla.Transform(carla.Location(x=378.543030, y=-1.073679, z=78.516823), carla.Rotation(pitch=-83.857254, yaw=14.944255, roll=-0.000981)))
                print("Stop autoroute")
            if keyboard.is_pressed("6"):
                spectator.set_transform(carla.Transform(carla.Location(x=58.836407, y=-336.930145, z=27.107143), carla.Rotation(pitch=-32.555294, yaw=142.710449, roll=-0.000915)))
                print("Sortie Nord")
            if keyboard.is_pressed("7"):
                spectator.set_transform(carla.Transform(carla.Location(x=247.115997, y=-156.910461, z=46.706787), carla.Rotation(pitch=-69.582947, yaw=-63.765865, roll=-0.001008)))
                print("Intersection")
            if keyboard.is_pressed("x"):
                spectator.set_transform(carla.Transform(carla.Location(x=2512.497559, y=-1271.629639, z=72.877922), carla.Rotation(pitch=-18.669556, yaw=-29.571350, roll=0.000011)))
                print("Intersection")
        
    except KeyboardInterrupt:
        pass
        

if __name__ == '__main__' :
    main()