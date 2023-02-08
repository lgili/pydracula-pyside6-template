
import sys
import pydracula
from pydracula.controllers.SingleApplication import SingleApplication
from pydracula.controllers.main_window import MainWindow
from PySide6.QtGui import QFont, QFontDatabase
import gettext
from pydracula.controllers.splash_screen import SplashScreen
from os import environ, getenv

from pydracula.model.repository.database import SQLiteRepository
from pydracula.model.notes import Note
import asyncio
_ACTIVE_NOTES = {}


async def main():

    # When running outside Flatpak
    if not pydracula.isFlatpak:
        # Session Type
        XDG_SESSION_TYPE = getenv('XDG_SESSION_TYPE')
        if XDG_SESSION_TYPE == 'wayland':
            environ['QT_QPA_PLATFORM'] = 'wayland'
        elif XDG_SESSION_TYPE is None:
            environ['QT_QPA_PLATFORM'] = 'xcb'

    # Local Debug (python -m pydracula --appDebug)
    if '--appDebug' in sys.argv:
        # Settings for Debug
        import os
        os.environ['XCURSOR_SIZE'] = '24'
        os.environ['XCURSOR_THEME'] = 'Fluent-cursor'
        os.environ['QT_QPA_PLATFORM'] = 'xcb'
        os.environ['QTWEBENGINE_REMOTE_DEBUGGING'] = '12345'

    # Create Database
    sqlite = SQLiteRepository(Note)
    sqlite.engine_factory()
    sqlite.create(text="Documentos", x="mac", y="moc")
    existing_notes = sqlite.list()
    print(str(existing_notes))

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

    # Start app
    sys.exit(app.exec())

if __name__ == "__main__":
    asyncio.run(main())
