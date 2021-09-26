## AVERT UI 

### Installation
Before running the software we have to install all the python packages for PyQt5:
```
pip install -r requirements.txt
```

### How it Works
Simply run the `main.py` file and the UI will pop up with all of the needed behavior:
```
py main.py
```
There is going to be additonal methods and/or general code affecting the UI such as button press
triggers and creation of custom widgets. 

When editing the ui within QT, simply save, and run:
```
pyuic5 AvertUI.ui -o avert.py
```

This converts the `AvertUI.ui` file to a **python executable** and from there run the main and address 
the result or errors that are brought up. 

### Configuration View, Accordion (HomePage), and Tag Tab in Detailed View

This repo holds the `AvertUI.ui` file produced using QT Designer as well as the 
Python executable, `avert.py` which has no additional code to it. This means that the code
included within William's branch which I merged was removed due to it being overwritten 
everytime the avert.ui file was modified and saved. All additonal code was added into the main.py 
executable which houses the needed items to run the UI. 