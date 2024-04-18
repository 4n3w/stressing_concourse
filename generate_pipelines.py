#!/usr/bin/env python3
import jinja2
import os

# Define stress levels and parameters
stress_levels = {
    'alpha': {'trigger_interval': 15, 'jobs': {'cpu': {'duration': 900, 'params': '--cpu 1'}}},
    'bravo': {'trigger_interval': 30, 'jobs': {'cpu': {'duration': 900, 'params': '--cpu 2'}}},
    'charlie': {'trigger_interval': 45, 'jobs': {'cpu': {'duration': 900, 'params': '--cpu 3'}}},
    'delta': {'trigger_interval': 60, 'jobs': {'cpu': {'duration': 900, 'params': '--cpu 4'}, 'disk': {'duration': 900, 'params': '--hdd 1 --hdd-bytes 512M'}}},
    'echo': {'trigger_interval': 75, 'jobs': {'cpu': {'duration': 900, 'params': '--cpu 5'}, 'disk': {'duration': 900, 'params': '--hdd 2 --hdd-bytes 1G'}, 'network': {'duration': 900, 'params': '--netdev 1'}}},
    'foxtrot': {'trigger_interval': 90, 'jobs': {'cpu': {'duration': 900, 'params': '--cpu 6'}, 'disk': {'duration': 900, 'params': '--hdd 2 --hdd-bytes 1G'}, 'network': {'duration': 900, 'params': '--netdev 2'}}},
    'golf': {'trigger_interval': 105, 'jobs': {'cpu': {'duration': 900, 'params': '--cpu 7'}, 'disk': {'duration': 900, 'params': '--hdd 2 --hdd-bytes 1.5G'}, 'network': {'duration': 900, 'params': '--netdev 2'}}},
    'hotel': {'trigger_interval': 120, 'jobs': {'cpu': {'duration': 900, 'params': '--cpu 8'}, 'disk': {'duration': 900, 'params': '--hdd 3 --hdd-bytes 1.5G'}, 'network': {'duration': 900, 'params': '--netdev 2'}}},
    'india': {'trigger_interval': 135, 'jobs': {'cpu': {'duration': 900, 'params': '--cpu 8'}, 'disk': {'duration': 900, 'params': '--hdd 3 --hdd-bytes 2G'}, 'network': {'duration': 900, 'params': '--netdev 3'}}},
    'juliet': {'trigger_interval': 150, 'jobs': {'cpu': {'duration': 900, 'params': '--cpu 8'}, 'disk': {'duration': 900, 'params': '--hdd 4 --hdd-bytes 2G'}, 'network': {'duration': 900, 'params': '--netdev 3'}}},
    'kilo': {'trigger_interval': 165, 'jobs': {'cpu': {'duration': 900, 'params': '--cpu 8'}, 'disk': {'duration': 900, 'params': '--hdd 4 --hdd-bytes 2.5G'}, 'network': {'duration': 900, 'params': '--netdev 3'}}},
    'lima': {'trigger_interval': 180, 'jobs': {'cpu': {'duration': 900, 'params': '--cpu 8'}, 'disk': {'duration': 900, 'params': '--hdd 5 --hdd-bytes 2.5G'}, 'network': {'duration': 900, 'params': '--netdev 4'}}},
    'mike': {'trigger_interval': 195, 'jobs': {'cpu': {'duration': 900, 'params': '--cpu 8'}, 'disk': {'duration': 900, 'params': '--hdd 5 --hdd-bytes 3G'}, 'network': {'duration': 900, 'params': '--netdev 4'}}},
    'november': {'trigger_interval': 210, 'jobs': {'cpu': {'duration': 900, 'params': '--cpu 8'}, 'disk': {'duration': 900, 'params': '--hdd 6 --hdd-bytes 3G'}, 'network': {'duration': 900, 'params': '--netdev 4'}}},
    'oscar': {'trigger_interval': 225, 'jobs': {'cpu': {'duration': 900, 'params': '--cpu 8'}, 'disk': {'duration': 900, 'params': '--hdd 6 --hdd-bytes 3.5G'}, 'network': {'duration': 900, 'params': '--netdev 5'}}},
    'papa': {'trigger_interval': 240, 'jobs': {'cpu': {'duration': 900, 'params': '--cpu 8'}, 'disk': {'duration': 900, 'params': '--hdd 7 --hdd-bytes 3.5G'}, 'network': {'duration': 900, 'params': '--netdev 5'}}},
    'quebec': {'trigger_interval': 255, 'jobs': {'cpu': {'duration': 900, 'params': '--cpu 8'}, 'disk': {'duration': 900, 'params': '--hdd 7 --hdd-bytes 4G'}, 'network': {'duration': 900, 'params': '--netdev 5'}}},
    'romeo': {'trigger_interval': 270, 'jobs': {'cpu': {'duration': 900, 'params': '--cpu 8'}, 'disk': {'duration': 900, 'params': '--hdd 8 --hdd-bytes 4G'}, 'network': {'duration': 900, 'params': '--netdev 5'}}},
    'sierra': {'trigger_interval': 285, 'jobs': {'cpu': {'duration': 900, 'params': '--cpu 8'}, 'disk': {'duration': 900, 'params': '--hdd 8 --hdd-bytes 4.5G'}, 'network': {'duration': 900, 'params': '--netdev 6'}}},
    'tango': {'trigger_interval': 300, 'jobs': {'cpu': {'duration': 900, 'params': '--cpu 8'}, 'disk': {'duration': 900, 'params': '--hdd 9 --hdd-bytes 4.5G'}, 'network': {'duration': 900, 'params': '--netdev 6'}}},
    'uniform': {'trigger_interval': 315, 'jobs': {'cpu': {'duration': 900, 'params': '--cpu 8'}, 'disk': {'duration': 900, 'params': '--hdd 9 --hdd-bytes 5G'}, 'network': {'duration': 900, 'params': '--netdev 6'}}},
    'victor': {'trigger_interval': 330, 'jobs': {'cpu': {'duration': 900, 'params': '--cpu 8'}, 'disk': {'duration': 900, 'params': '--hdd 10 --hdd-bytes 5G'}, 'network': {'duration': 900, 'params': '--netdev 6'}}},
    'whiskey': {'trigger_interval': 345, 'jobs': {'cpu': {'duration': 900, 'params': '--cpu 8'}, 'disk': {'duration': 900, 'params': '--hdd 10 --hdd-bytes 5.5G'}, 'network': {'duration': 900, 'params': '--netdev 7'}}},
    'xray': {'trigger_interval': 400, 'jobs': {'cpu': {'duration': 900, 'params': '--cpu 8'}, 'disk': {'duration': 900, 'params': '--hdd 11 --hdd-bytes 6G'}, 'network': {'duration': 900, 'params': '--netdev 8'}}},
}

# Load Jinja2 environment
env = jinja2.Environment(loader=jinja2.FileSystemLoader('.'))
template = env.get_template('pipeline-template.j2')

# Specify the directory name
directory = "generated_pipelines"

# Check if the directory exists
if not os.path.exists(directory):
    os.makedirs(directory)
    print(f"Directory '{directory}' was created.")
else:
    print(f"Directory '{directory}' already exists.")

# Generate pipeline files
for level, config in stress_levels.items():
    with open(f'{directory}/pipeline_{level}.yaml', 'w') as file:
        file.write(template.render(trigger_interval=config['trigger_interval'], jobs=config['jobs']))

print("Generated pipeline files for all stress levels.")
