#!/bin/bash

# docker run -it -d -v /home/jeng-yuantsai/JIRIAF/UAV-Digital-Twin/src:/digitaltwin/src tiryoh/ros2:eloquent
docker run -it -v /home/jeng-yuantsai/JIRIAF/UAV-Digital-Twin/src:/digitaltwin/src -v /home/jeng-yuantsai/JIRIAF/UAV-Digital-Twin/docker:/docker tiryoh/ros2:eloquent

