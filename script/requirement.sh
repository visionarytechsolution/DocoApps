#!/bin/bash
sudo systemctl stop django
python3 -m pip install --upgrade pip
pip3 install -r /home/ubuntu/requirements/python/prod.txt