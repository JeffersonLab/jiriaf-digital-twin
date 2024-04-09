#!/bin/bash


# run ros2
cd ~/digitaltwin_ws
. install/setup.bash
ros2 launch digitaltwin digitaltwin_launch.py > /workspaces/UAV-Digital-Twin/log.txt 2>&1