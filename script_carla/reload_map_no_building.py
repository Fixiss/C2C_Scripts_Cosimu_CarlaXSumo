import carla

def main():
    try:
        client = carla.Client('localhost', 2000)
        client.set_timeout(10.0)
        world = client.get_world()
        map = world.get_map()
        map_name = map.name.split('/')
        map_opt = map_name[-1].split('_')
        if(map_opt[-1] == "Opt"):
            world = client.load_world(map_name[-1]
                                , carla.MapLayer.Particles 
                                    | carla.MapLayer.Buildings 
                                    | carla.MapLayer.ParkedVehicles 
                                    | carla.MapLayer.Props 
                                    | carla.MapLayer.Foliage 
                                    | carla.MapLayer.Walls
                                    | carla.MapLayer.Ground)
            world.unload_map_layer(carla.MapLayer.Buildings)
            world.unload_map_layer(carla.MapLayer.Props)
            world.unload_map_layer(carla.MapLayer.Foliage)
            world.unload_map_layer(carla.MapLayer.ParkedVehicles)
            world.unload_map_layer(carla.MapLayer.Walls)
            world.unload_map_layer(carla.MapLayer.Particles)
            #world.unload_map_layer(carla.MapLayer.Ground)
        else:
            world = client.load_world((map_name[-1]+"_Opt")
                                , carla.MapLayer.Particles 
                                    | carla.MapLayer.Buildings 
                                    | carla.MapLayer.ParkedVehicles 
                                    | carla.MapLayer.Props 
                                    | carla.MapLayer.Foliage 
                                    | carla.MapLayer.Walls
                                    | carla.MapLayer.Ground)
            world.unload_map_layer(carla.MapLayer.Buildings)
            world.unload_map_layer(carla.MapLayer.Props)
            world.unload_map_layer(carla.MapLayer.Foliage)
            world.unload_map_layer(carla.MapLayer.ParkedVehicles)
            world.unload_map_layer(carla.MapLayer.Walls)
            world.unload_map_layer(carla.MapLayer.Particles)
            #world.unload_map_layer(carla.MapLayer.Ground)
    finally:
        print("Done.")
    

if __name__ == '__main__' :
    main()