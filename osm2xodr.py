import carla
import io
import sys

args = sys.argv[1:]
if(len(args)>=2):
    # Read the .osm data
    f = io.open(args[0], mode="r", encoding="utf-8")
    osm_data = f.read()
    f.close()

    # Define the desired settings. In this case, default values.
    settings = carla.Osm2OdrSettings()
    settings.generate_traffic_lights = True
    # Set OSM road types to export to OpenDRIVE
    settings.set_osm_way_types(["motorway", "motorway_link", "trunk", "trunk_link", "primary", "primary_link", "secondary", "secondary_link", "tertiary", "tertiary_link", "unclassified", "residential"])
    # Convert to .xodr
    xodr_data = carla.Osm2Odr.convert(osm_data, settings)

    # save opendrive file
    f = open(args[1], 'w')
    f.write(xodr_data)
    f.close()
else:
    print("2 arguments is required : arg1->fichier.osm (origine) arg2->fichier.xodr (destination)")