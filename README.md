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
_pyuic5 AvertUI.ui -o entername.py
```

This converts the `AvertUI.ui` file to a **python executable** which you can copy and paste towards avert.py. You need 
to copy and paste these changes because if you run 
```
_pyuic5 AvertUI.ui -o avert.py
```
It will overwrite all the work that has been added manually by code. Code was added manually by different members of the 
team and thus any changes to the UI must be copy and pasted. Once you copy and paste your UI changes in to avert.py. Make 
any behavioral coding within **main.py**. 
 