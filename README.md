## AVERT UI 
#### Configuration View, Accordion (HomePage), and Tag Tab in Detailed View

This repo holds AVERTS ui file produced using QT Designer as well as the 
Python executalble, avert.py which has not additional code to it. This means that the code
included within William's branch which I merged was removed due to it being overwritten 
everytime the avert.ui file was modified and saved. All additonal code was added into the main.py 
executable which houses the needed items to run the UI. 

### How it Works
Simply run the main.py file and the UI will pop up with all of the needed behavior, so far, included
if there is going to be any additonal methods and/or general code affecting the UI such as button press
triggers and creation of custom widgets. 
When editing the ui within QT, simply save, and run "_pyuic5 AvertUI.ui -o avert.py_". 
This converts the ui file to the python executable and from there run the main and address 
the result or errors that are brought up. 
