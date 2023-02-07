import os
from PySide6.QtCore import QStandardPaths
__version__ = '0.1'
__appname__ = 'PyDracula'
__comment__ = 'PyDracula theme for Qt'
__domain__ = 'com.lgili'
__desktopid__ = 'com.lgili.pydracula'
__appid__ = 'pydracula-application'

__author__ = ' Wanderson Magalhaes'
__website__ = 'https://github.com/Wanderson-Magalhaes/Modern_GUI_PyDracula_PySide6_or_PyQt6'
__bugreport__ = 'https://github.com/Wanderson-Magalhaes/Modern_GUI_PyDracula_PySide6_or_PyQt6/issues'
__releases__ = 'https://github.com/Wanderson-Magalhaes/Modern_GUI_PyDracula_PySide6_or_PyQt6/releases'
__licence__ = 'MIT License'

# iniciando os paths
from PySide6.QtCore import QFileInfo
abs_path = QFileInfo(__file__).absolutePath()


# Path translations
po_path = os.path.join(abs_path, 'po')

# Is Flatpak?
isFlatpak = abs_path.startswith('/app/')

# Path DataBase
DATABASE_DIR = os.path.join(
    QStandardPaths.writableLocation(
        QStandardPaths.StandardLocation.AppLocalDataLocation), __appname__, 'db'
)

if not os.path.exists(DATABASE_DIR):
    os.makedirs(DATABASE_DIR)

DATABASE_FILE = os.path.join(DATABASE_DIR, 'zapzap.db')

# Path
path_storage = os.path.join(
    QStandardPaths.writableLocation(
        QStandardPaths.StandardLocation.AppLocalDataLocation), __appname__, "QtWebEngine"
)
