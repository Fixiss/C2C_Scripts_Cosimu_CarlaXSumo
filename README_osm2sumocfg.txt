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

dossiers :

Sumo/...
Carla/...
scripts/map_xodr/...
        map_osm/...
        map_net_xml/...
        map_rou_xml/...
        map_sumocfg/...
        Osm2Sumocfg.sh
        osm2xodr.py

Une fois le sh termminé :
python3 ..\Carla\Co-Simulation\Sumo\run_synchronization.py .\map_sumocfg\map.sumocfg --sumo-gui --sync-vehicle-lights