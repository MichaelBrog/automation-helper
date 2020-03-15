#  Python Automation Helper
[**About**](#About)<br>
[**Usage**](#Usage)<br>
[**Installation**](#Installing)<br>
[**Create an Executable file**](#Creating-an-Executable-file)<br>
# About

Tool to help automate certain tasks that require simular keyboard or mouse inputs by providing a GUI that allows a user to create and delete text files that you can then record your inputs into. This file can be later played back simulating the inputs in real time. 

![GUI](https://i.imgur.com/uTELZu2.jpg)

# Usage 

To Start the application launch the GUI using:
```shell
py .\gui.py or python3 ./gui.py
```
The actions will be recorded in a folder in the directory called 'events', if none exists it will be created. 

#### Creating a file
In order to record your actions a file must be selected, to create one put a name in the lower textbox and click the 'Add file' button, upon which a file name will appear in the upper text area.

#### Record a file

To record, select one of the files in the text area and press record, all the clicking, scrolling, and keyboard key pressing actions will be recorded in the selected text file. Once you are ready to stop recording, press the F8 key and the recording will stop. 

### Playing back a file
To play back a file, select the file you wish to play back in the file text area and press 'Play Selected', the playback will begin, because timestamps are taken along with the recording the clicks take place in real time, as they were recorded. 

## Recording format
Currently the recording is being put into .txt files with each action taking one row, each action is recorded with a timestamp as well what type of input it was from (mouse or keyboard currently), and what type of action was used with the input device. 

### The layout is for a keyboard would be:
```
Timestamp#keyboard#type#
ex. 2020-03-15 16:35:28.360227#keyboard#click#keyclicked
```
### The layout is for a mouse would be:
```
Timestamp#mouse#type#coordinate
2020-03-15 16:35:31.959277#mouse#clickleft#(-805, 972)
```

# Installing
It is recommended for this project to create a virtual env:
https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/

## Installing pip
**Windows**
```shell 
py -m pip install --upgrade pip
```
**MacOS**
```shell
python3 -m pip install --user --upgrade pip
```

## Installing virtual env

### Installing on windows

Install virtual env
```shell
py -m pip install --user virtualenv
```
Create the virtual environment in project directory.
```shell
py -m venv env
```
Activating the virtual environment
```shell
.\env\Scripts\activate
```
Installing the dependencies from requirements.txt
```shell
pip install -r requirements.txt
```
### Installing on MacOS/Linux

Install virtual env
```shell
python3 -m pip install --user virtualenv
```
Create the virtual environment in project directory.

```shell
python3 -m venv env
```
Activating the virtual environment

```shell
source env/bin/activate
```
Installing the dependencies from requirements.txt
```shell
pip install -r requirements.txt
```

# Creating an Executable file
An EXE file can be created by using pyinstaller.

Pyinstaller can be installed using pip, if you don't have pip see steps [**above**](##Installing-pip).

```shell
pyinstaller --onefile --windowed gui.py
```
If it is correctly installed, the exe will appear in:
```shell
...\automation-helper\dist\gui.exe
```