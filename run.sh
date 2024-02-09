#!/bin/bash
echo "Starting mlp pipeline for AIAP-14 Task 2"

# Change directory and run file
cd src/
pip install -r requirements.txt
python mlp_pipeline.py

# Pause
echo "Program completed, thank you."
/bin/bash
read 