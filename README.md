# Stress Out Your Concourse

## Overview
This project automates the generation and deployment of multiple Concourse CI pipelines to perform varying levels of system stress tests. Each pipeline is named after a NATO phonetic alphabet letter and configured to progressively increase the stress applied to system resources. This approach allows for detailed observation of how systems perform under different loads, aiding in identifying potential performance bottlenecks or failure points. Under the hood, I'm using stress-ng in an alpine container. 

## Purpose
The purpose of these pipelines is to provide a scalable and systematic method to test system robustness across a range of controlled stress scenarios. This ensures that each component of the system can handle expected and peak loads without degradation of service or system failure. The use of varying intervals and stress levels allows for a comprehensive assessment of system performance and resilience.

## Pipeline Generation
Pipelines are defined using templates and generated through a Python script that utilizes Jinja2 for template rendering. Each generated pipeline configuration corresponds to a specific level of system stress, outlined by a unique set of parameters such as CPU, disk, and network load.

Feel free to make changes to the `generate_pipelines.py` script. I've included the generated pipelines for simplicity's sake.

Ensure you have a values.yaml file to replace the two variables, `((registry_token))` and `((registry_username))`:

```yaml
registry_token: whatever_token
registry_username: 4n3w
```

**OR** edit the `pipeline-template.j2` to your liking.

# Deployment Script
The deployment of these pipelines is managed through a simple Bash script, deploy_pipelines.sh. This script iterates over each generated pipeline configuration and uses the fly CLI tool to set and unpause pipelines on a specified Concourse target. Here’s how you use the script:

1. Set Fly Target: Define your Concourse target in the fly_target variable.
1. Specify Directory: Ensure that the directory variable points to where your generated pipeline configurations are stored.
1. Run the Script:

```bash
./deploy_pipelines.sh
```

This script automates the process of flying your pipelines, making it easy to deploy multiple pipelines quickly and efficiently, ensuring consistent and error-free deployment across all stress test scenarios.