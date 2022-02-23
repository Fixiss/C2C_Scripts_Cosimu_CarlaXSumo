#!/bin/bash

echo "Nombre d'arguments : "$#
if test $# -eq 0 
then 
    echo "./Osm2Sumocfg.sh map.osm [-t titre=map] [-n nbVehicle=50]"
    kill
fi
#on initialise l'argument obligatoire
osm=$1
shift

#on initialise par défault les autres arguments
titre=map
nbVehicles=50

#on vérifie les options et on associe les nouvelles valeurs si besoin
while getopts 't:n:' OPTION; do
        case $OPTION in 
            t) titre=$OPTARG;;
            n) nbVehicles=$OPTARG;;
        esac
done

#on commence de traitement
#affichage des valeurs
echo "Le fichier osm : "$osm
echo "Le titre du sumocfg : "$titre
echo "Le nombre de véhicules dans la simulation : "$nbVehicles
#création du fichier xodr
echo > map_xodr/$titre.xodr
#traduction du osm en xodr
echo $(python3 osm2xodr.py $osm map_xodr/$titre.xodr)
#transformation du xodr en network Sumo
echo $(../Sumo/bin/netconvert.exe --opendrive-files ./map_xodr/$titre.xodr -o ./map_net_xml/$titre.net.xml) > /dev/null
#création des routes pour le network Sumo
echo $(python3 ../Sumo/tools/randomTrips.py -n ./map_net_xml/$titre.net.xml -r ./map_rou_xml/$titre.rou.xml -e $nbVehicles -l) > /dev/null
#rédaction du fichier sumocfg
echo "<configuration>
<input>
    <net-file value=\"../map_net_xml/$titre.net.xml\"/>
    <route-files value=\"../map_rou_xml/$titre.rou.xml\"/>
</input>
<time>
    <begin value=\"0\"/>
    <end value=\"2000\"/>
</time>
</configuration>" > map_sumocfg/$titre_$nbVehicles.sumocfg