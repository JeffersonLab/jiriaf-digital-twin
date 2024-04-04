FROM tiryoh/ros2:eloquent

# Add any additional setup commands you need here

# RUN mkdir -p ~/digitaltwin_ws/src && \
#     cp -r /digitaltwin/src/* ~/digitaltwin_ws/src && \
#     cd ~/digitaltwin_ws && \
#     colcon build


RUN apt-get update && \
    apt-get install -y python3-dev graphviz libgraphviz-dev pkg-config python3-pip python3-scipy python3-tk cython3 x11-apps && \
    pip3 install networkx==2.5 pomegranate==0.13.0 pygraphviz==1.6