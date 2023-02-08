

<!-- To build on windows -->
<!-- https://hub.docker.com/r/cdrx/pyinstaller-windows -->
<!-- To build on Linux -->
<!-- pyinstaller --onefile --windowed --icon=icon.ico main.py   -->

# PyDracula - Modern GUI PySide6 / PyQt6
# 
This project was based on [Pydracula](https://github.com/Wanderson-Magalhaes/Modern_GUI_PyDracula_PySide6_or_PyQt6).
## Features
* Compatible with Python **3.8+**
* PySide6
* PyDracula Theming (Dark/Light)
* Splash Screen
* Resources compiled ahead of time:
  * Final build only consists of Python files
* Packaging for Windows, Linux and Flatpak
* Database repository with sqlalchemy (SQLite, Postgres, MySQL)

# Development Setup

## First Steps

1. Set up the development environment for your OS (please look [here](docs/) for a guide)
2. Run `python run.py` to start the app
3. Run `python build.py -h` to see all system supported to package
4. Run `python build.py -s linux` to generate package for linux

## Read Further

* Qt6: https://doc.qt.io/
* Python: https://www.python.org/
* PySide6: https://doc.qt.io/qtforpython/contents.html
* Scripting: https://doc.qt.io/qt-6/topics-scripting.html

# Dependencies

* PySide6 https://pypi.org/project/PySide6/
* PyTest https://pypi.org/project/pytest/
  
#
> ## :gift: **//// DONATE ////**
> ## 🔗 Donate (Gumroad): https://gum.co/mHsRC
> This interface is free for any use, but if you are going to use it commercially, consider helping to maintain this project and others with a donation by Gumroado at the link above. This helps to keep this and other projects active.

> **Warning**: this project was created using PySide6 and Python 3.9, using previous versions can cause compatibility problems.

# YouTube - Presentation And Tutorial
Presentation and tutorial video with the main functions of the user interface.
> 🔗 https://youtu.be/9DnaHg4M_AM


# Multiple Themes
![PyDracula_Default_Dark](https://user-images.githubusercontent.com/60605512/112993874-0b647700-9140-11eb-8670-61322d70dbe3.png)
![PyDracula_Light](https://user-images.githubusercontent.com/60605512/112993918-18816600-9140-11eb-837c-e7a7c3d2b05e.png)

# High DPI
> Qt Widgets is an old technology and does not have a good support for high DPI settings, making these images look distorted when your system has DPI applied above 100%.
You can minimize this problem using a workaround by applying this code below in "main.py" just below the import of the Qt modules.
```python
# ADJUST QT FONT DPI FOR HIGHT SCALE
# ///////////////////////////////////////////////////////////////
os.environ["QT_FONT_DPI"] = "96"
```

# Running
> Inside your preferred terminal run the commands below depending on your system, remembering before installing Python 3.9> and PySide6 "pip install PySide6".
> ## **Windows**:
```console
python run.py
```
> ## **MacOS and Linux**:
```console
python3 run.py
```
# Compiling
> ## **Windows**:
```console
python setup.py -s windows
```

> ## **linux**:
```console
python setup.py -s linux
```

> ## **Flatpak**:
```console
python setup.py -s flatpak
```

# Project Files And Folders
> **__main__.py**: application initialization file.

> **main.ui**: Qt Designer project.

> **resouces.qrc**: Qt Designer resoucers, add here your resources using Qt Designer. Use version 6 >

> **setup.py**: cx-Freeze setup to compile your application (configured for Windows and Linux).

> **themes/**: add here your themes (.qss).

> **controllers/app_funtions.py**: add your application's functions here.
Up
> **controllers/app_settings.py**: global variables to configure user interface.

> **view/resources_rc.py**: "resource.qrc" file compiled for python using the command: ```pyside6-rcc resources.qrc -o resources_rc.py```.

> **controllers/ui_functions.py**: add here only functions related to the user interface / GUI.

> **view/ui_main.py**: file related to the user interface exported by Qt Designer. You can compile it manually using the command: ```pyside6-uic main.ui> ui_main.py ```.
After expoting in .py and change the line "import resources_rc" to "from . resources_rc import *" to use as a module.

> **assets/**: put all your images and icons here before converting to Python (resources_re.py) ```pyside6-rcc resources.qrc -o resources_rc.py```.

