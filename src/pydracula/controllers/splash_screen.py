from PySide6.QtWidgets import QMainWindow, QGraphicsDropShadowEffect
from PySide6.QtCore import QSettings, QByteArray, QTimer, Qt
from PySide6.QtGui import QColor
## ==> SPLASH SCREEN
import pydracula
from pydracula.view.ui_splash_screen import Ui_SplashScreen
from pydracula.controllers.main_window import MainWindow
from pydracula.model.repository.database import SQLiteRepository
from pydracula.model.notes import Note

## ==> GLOBALS
counter = 0

# SPLASH SCREEN
class SplashScreen(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)
        self.app = parent

        self.settings = QSettings(pydracula.__appname__, pydracula.__appname__)

        ## UI ==> INTERFACE CODES
        ########################################################################

        ## REMOVE TITLE BAR
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)


        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        ## QTIMER ==> START
        self.timer = QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(35)

        # CHANGE DESCRIPTION

        # Initial Text
        self.ui.label_description.setText("<strong>WELCOME</strong> TO MY APPLICATION")

        # Change Texts
        QTimer.singleShot(1500, lambda: self.ui.label_description.setText("<strong>LOADING</strong> DATABASE"))
        self.startDatabase()
        QTimer.singleShot(3000, lambda: self.ui.label_description.setText("<strong>LOADING</strong> USER INTERFACE"))


        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    ## ==> APP FUNCTIONS
    ########################################################################
    def progress(self):

        global counter

        # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(counter)

        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            self.main = MainWindow(self.app)
            self.main.show()

            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        counter += 1


    def startDatabase(self):
       sqlite = SQLiteRepository(Note)
       try:
           sqlite.create(text="Documentos", x="mac", y="moc")
           existing_notes = sqlite.list()
           print(str(existing_notes))
        
       except:
          print('An exception occurred')