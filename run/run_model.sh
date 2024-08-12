#!/bin/bash


# run ros2
cd ~/digitaltwin_ws
. install/setup.bash
ros2 launch digitaltwin digitaltwin_launch_gui_logger.py > /workspaces/jiriaf-digital-twin/log.txt 2>&1

# ros2 launch digitaltwin digitaltwin_launch_gui_logger.py

#digitaltwin_launch_gui_logger.py