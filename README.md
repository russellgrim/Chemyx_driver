# Chemyx_driver

## Quick Start Guide
* Download code from git 
* Dowload python3.7
* Open CMD
* Navigate to folder
* pip install virtualenv
* python -m venv env
* env\Scripts\activate.bat
* pip install -r requirements.txt
* Connect syringe pump 
* identify com port with device manger
* identify buad rate from the display on device
* update script at the bottom with com and buad
* python script.py





Use python 3.7
## Git
Useful commands for using git. 
TODO: find a tutorial to describe how to do this
* Create a new branch
    * git checkout -b feature#xx
    * git push --set-upstream origin feature#xx
* Workflow
    * git pull
    * git add *
    * git commit -m "some commit message"
    * git push 

## Python
If python interface is introduced, usefull commands here:
* Virtual environments 
    * pip install virtualenv
    * python -m venv env
    * env\Scripts\activate.bat
    * deactivate
* Requirements
    * pip install -r requirements.txt
    * pip list
* Delinting
    * Navigate to the folder
    * pylint
* Testing
    * Navigate to the folder
    * pytest
    * pytest test_mytest.py
    * pytest test_mytest.py::test_sometest
* Documentation
    * Deoxigen
* Logging
    * TBC
