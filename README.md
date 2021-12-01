## AVERT UI 

### Installation (Not Required)
Before running the software please install all required modules and tools. You can do this with the following 
command.
We recommend to install the following within a virtual enviorment on your system. This can be done with the 
following set of commands

```
python3 -m venv venv
sudo su (AVERT requires root privaledges)
source ./venv/bin/activate
pip install -r requirements.txt
python3 main.py (main file for AVERT)
```

### How it Works and Other Installation
Simply run the `main.py` file using root priviladges and a virtual enviorment in the shell (as listed above) or use 
`run.sh` with the command `./run.sh` on the command line. AVERT will automatically install all needed modules and prompt for
authentication as AVERT must run with root priviladges. This is due to certain recorders needing the priviladges to attain the data required. 
All modules and tools used can be found within the requirements.txt file and are listed below. 

#### Tools and modules
PyQt5==5.15.4
PyQt5-Qt5==5.15.2
PyQt5-sip==12.9.0
PyQtChart==5.15.4
PyQtChart-Qt5==5.15.2
pymongo==3.12.0
pynput==1.7.3
six==1.16.0
psutil==5.8.0
numpy==1.21.2
Pillow==8.4.0
PyAutoGUI==0.9.53
imageio==2.10.1
imageio-ffmpeg==0.4.5
mplayer.py==0.7.2
