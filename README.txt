Prérequis :
- installer Carla : https://hackmd.io/QVzi08gOQyeO57Aovv1WyA?view#Tuto-installer-Carla-avec-python-37

- installer Sumo : https://www.eclipse.org/sumo/

+

sudo apt-get install python3.7
sudo apt-get install python3-pip
sudo apt-get install libjpeg-turbo8
sudo apt-get install libtiff-dev
sudo apt-get install sumo sumo-tools sumo-doc
pip install --user pygame numpy && pip3 install --user pygame numpy
pip3 install carla

+

- récupérer le script "osm2xodr.py" : https://hackmd.io/V2mprt3YSayoztrsrW3b-A#:~:text=Convertir%20le%20fichier%20.osm%20en%20un%20fichier%20.xodr

+

Dossiers :

Sumo/...
Carla/...
scripts/map_xodr/...    --> dossier contenant les maps ouvrables sur Carla pourra afficher le côté réaliste de la simulation
        map_osm/...     --> dossier contenant les maps télécharger depuis OpenStreetMap (OSM)
        map_net_xml/... --> dossier contenant les maps Sumo
        map_rou_xml/... --> dossier contenant les routes Sumo pour la simulation
        map_sumocfg/... --> dossier contenant les configuration Sumo à utiliser pour la co-simulation
        script_carla/...--> dossier contenant plusieurs scripts python utilitaires pour Carla
        Osm2Sumocfg.sh  --> fichier bash transformant une map OSM en une configuration Sumo
        osm2xodr.py     --> fichier python transformant une map OSM et map xodr pour Carla

Lancement du fichier Osm2Sumocfg.sh :
        ./Osm2Sumocfg.sh map.osm [-t titre=type_map] [-n nbVehicles=50]

titre des configurations à respecter : 

TypeDeLaSimulation_TitreDeLaSimulation_NbVehicules

TypeDeLaSimulation = Route|Intersection|Regroupement
TitreDeLaSimulation = un maximum explicite : aire2 < aire_autoroute_vers_Bordeaux < aire_NomDeLAire
nbVehicles = automatiquement rajouté lors de l'execution du fichier Osm2Sumocfg.sh

Une fois le sh termminé :
python3 ..\Carla\Co-Simulation\Sumo\run_synchronization.py .\map_sumocfg\map.sumocfg --sumo-gui --sync-vehicle-lights