#!/bin/bash
rm -rf __pycache__
rm -rf configuration/__pycache__
rm -rf controller/__pycache__
rm -rf Database/__pycache__
rm -rf recorders/__pycache__
rm -rf view/__pycache__
rm -rf view/components/__pycache__
rm -rf view/configuration_tab/__pycache__
rm -rf view/home_tab/__pycache__
rm -rf view/sync_tab/__pycache__
rm -rf view/assets/__pycache__
rm -rf .idea

sudo apt update
sudo apt install -y auditd wmctrl
python3 -m pip install pyautogui
sudo apt-get install scrot
sudo apt-get install python3-tk
sudo apt-get install python3-dev


if [ ! -d "venv/" ]
then
    python3 -m venv venv
fi

source "venv/bin/activate"
pip install -r requirements.txt
systemctl start mongod
clear
python3 main.py
