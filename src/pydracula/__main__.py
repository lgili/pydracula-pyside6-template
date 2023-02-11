
from pathlib import Path
import sys
path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))

import pydracula
from pydracula.controllers.SingleApplication import SingleApplication
from pydracula.controllers.main_window import MainWindow
from PySide6.QtGui import QFont, QFontDatabase
import gettext
from pydracula.controllers.splash_screen import SplashScreen
from os import environ, getenv




def main():

    # When running outside Flatpak
    #if not pydracula.isFlatpak:
    #    # Session Type
    #    XDG_SESSION_TYPE = getenv('XDG_SESSION_TYPE')
    #    if XDG_SESSION_TYPE == 'wayland':
    #        environ['QT_QPA_PLATFORM'] = 'wayland'
    #    elif XDG_SESSION_TYPE is 'te_y':
    #        environ['QT_QPA_PLATFORM'] = 'windows'    
    #    elif XDG_SESSION_TYPE is None:
    #        environ['QT_QPA_PLATFORM'] = 'xcb'



   
    # Define application attributes
    app = SingleApplication(pydracula.__appid__, sys.argv)
    app.setApplicationName(pydracula.__appname__)
    app.setApplicationVersion(pydracula.__version__)
    app.setDesktopFileName(pydracula.__desktopid__)
    app.setOrganizationDomain(pydracula.__domain__)

    # Create main window
    # window = MainWindow(app)
    window = SplashScreen(app)
    app.setWindow(window)
    app.setActivationWindow(window)

    # Checks the hidden start
    isStart_system = window.settings.value(
        "system/start_system", False, bool)
    if isStart_system and '--hideStart' in sys.argv:
        window.hide()
    else:
        window.show()

     # Create Database
   
    
      
    # Start app
    sys.exit(app.exec())

if __name__ == "__main__":
   main()
