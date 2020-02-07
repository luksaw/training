# Test automation

This repository contains test framework based on Python, Robot Framework and Selenium

SKIP README IF YOU ARE ONLY INTERESTED IN ROBOT FRAMEWORK TESTS

## Tools used

- PyCharm 2019.3
- Python 3.7
- robotframework	3.1.2
- robotframework-seleniumlibrary	4.2.0
- selenium	3.141.0
- IntelliBot plugin for PyCharm (can be installed from Settings/Plugins

# Steps how to run test
Follow below instructions to setup virtual environment and run test.

## First time setup of virtualenv

for Mac/Linux
~~~~
 $ sudo apt-get install python-virtualenv
~~~~
for Windows
~~~~
 pip3 install virtualenv
~~~~

## Setting up the environment

After cloning this repo to a host machine, navigate to project directory and create new virtual environment by calling

For Mac/Linux
~~~~
 $ virtualenv .venv
 or if you want to specify python3 as your project interpreter
 $ virtualenv .venv -p /usr/bin/python3
 then 
 $ source .venv/bin/activate
~~~~

For Windows
~~~~
 cd .venv/Scripts
 activate.bat
 ~~~~

Then install required packageds (robot framework and selenium)

~~~~
 (.venv) $ pip install --upgrade pip # many distributions ship criminal old pip
 (.venv) $ pip install -r requirements.txt
~~~~

## Leaving the virtual environment

Leaving the virtual environment can be done from the terminal by the following call

For Mac/Linux
~~~~
 (.venv) $ deactivate
~~~~

For Windows
~~~~
deactivate.bat
~~~~

## PATH & PYTHONPATH

- Path to project should be added to PYTHONPATH.
- Path to browser drivers (chromedriver, geckodriver) should be added to PATH in environment variables settings. Or just copy browser drivers to project directory

## Executing Login test for Robot Framework 

In command line/terminal navigate to project directory and execute below command to run test:
~~~~
 robot -d Login/results Login/tests_login.robot 
~~~~

## Browsing test execution results

Test results are stored in `results` folder within project

## Executing Numbers code in python

In command line/terminal navigate to project directory and execute below command to run test:
~~~~
 python Numbers/Numbers.py
~~~~

## Executin Numbers unit tests

In command line/terminal navigate to project directory and execute below command to run test:
~~~~
 python -m unittest Numbers/test.py
~~~~
