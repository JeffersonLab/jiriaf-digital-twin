#!/bin/bash

mkdir -p ~/digitaltwin_ws/src
cd ~/digitaltwin_ws/src

cp -r /digitaltwin/src/* .

cd ~/digitaltwin_ws/src
cd ../
colcon build



# install python packages
echo 'ubuntu' | sudo -S apt-get update
echo 'ubuntu' | sudo -S apt-get install python3-dev graphviz libgraphviz-dev pkg-config -y
echo 'ubuntu' | sudo -S apt-get install python3-pip -y

# install python3-tk
echo 'ubuntu' | sudo -S apt-get install python3-scipy -y
echo 'ubuntu' | sudo -S apt-get install python3-tk -y

echo 'ubuntu' | sudo -S pip3 install networkx==2.5

# install pomegranate
echo 'ubuntu' | sudo -S apt-get install cython3 -y
echo 'ubuntu' | sudo -S pip3 install pomegranate==0.13.0

# install pygraphviz
echo 'ubuntu' | sudo -S pip3 install pygraphviz==1.6


# run ros2
cd ~/digitaltwin_ws
. install/setup.bash
ros2 launch digitaltwin digitaltwin_launch_gui.py