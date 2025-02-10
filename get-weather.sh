#!/usr/bin/sh
source /home/joel/miniforge3/etc/profile.d/conda.sh
eval "$(conda shell.bash hook)"
conda activate joel
python /home/joel/CityWeather/main.py
