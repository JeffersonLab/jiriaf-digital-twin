#!/bin/bash

mkdir -p ~/digitaltwin_ws/src
cd ~/digitaltwin_ws/src

cp -r /workspaces/jiriaf-digital-twin/src/* .

cd ~/digitaltwin_ws/src
cd ../
colcon build
