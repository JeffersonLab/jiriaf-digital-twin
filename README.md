# Digital Twin Queue System Analysis

## Overview

This repository contains a comprehensive analysis of a digital twin model designed for a queue system. The model utilizes a Dynamic Bayesian Network (DBN) to capture dependencies among system variables and provide a probabilistic framework for analyzing these dependencies over time.

## Experimental Setup

The experimental setup includes:
- A stream sender and receiver with a queue system.
- Event sending rates adjusted to measure the processing rate and queue length under different compute capabilities (16 and 32 threads).

## Key Features

- **Real-time Data Assimilation**: The DBN model effectively assimilates real-time data.
- **Accurate State Estimation**: Provides accurate state estimation of the queue system.
- **Adaptive Control Optimization**: Offers adaptive control recommendations to manage system pressure.
- **Performance**: Demonstrates strong performance in aligning with observed data, despite minor delays in state tracking during decreasing queue lengths.

## Results

The results underscore the potential of DBN-based digital twins in enhancing real-time monitoring and decision-making in complex systems. The model successfully managed system pressure through adaptive control recommendations, providing valuable insights for future developments in digital twin technology.

## Usage Instructions

To build and run the source code in a development container with Visual Studio Code, follow these steps:

### Prerequisites

Set up the environment using the `.devcontainer/Dockerfile` or directly use the devcontainer feature in the Visual Studio Code IDE.

### Steps

1. Run `/run/build.sh` to compile the source code.
2. Run `/run/run_model.sh` to run the model.

### Essential Inputs

The essential inputs for this modeling are stored in the file: `src/digitaltwin/inputfiles/UAVconfig.json`.

## Citation

This repository is based on the following work and repository. If you use this work in an academic context, please cite the following publication(s):

Kapteyn, Michael G., Jacob V.R. Pretorius, and Karen E. Willcox. **A Probabilistic Graphical Model Foundation for Enabling Predictive Digital Twins at Scale.** arXiv preprint arXiv:2012.05841 (2020). [https://arxiv.org/abs/2012.05841](https://arxiv.org/abs/2012.05841)