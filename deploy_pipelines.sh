#!/usr/bin/env bash
#
#
nato_letters=(alpha bravo charlie delta echo foxtrot golf hotel india juliet kilo lima mike november oscar papa quebec romeo sierra tango uniform victor whiskey xray)
fly_target=
directory=generated_pipelines

for nato_letter in "${nato_letters[@]}"; do
  echo "Flying pipeline $nato_letter"

  fly --target ${fly_target} set-pipeline \
    --pipeline "${nato_letter}" \
    --config "${directory}/pipeline_${nato_letter}.yaml" \
    --non-interactive \
    --load-vars-from values.yaml

  fly -t ${fly_target} unpause-pipeline \
    --pipeline "${nato_letter}"
done

