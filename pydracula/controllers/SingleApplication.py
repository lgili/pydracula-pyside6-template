from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Signal, Qt, QTextStream, Slot
from PySide6.QtNetwork import QLocalServer, QLocalSocket
import sys


class SingleApplication(QApplication):
    messageReceived = Signal(str)

    def __init__(self, appid, *argv):
        super(SingleApplication, self).__init__(*argv)
        self._appid = appid
        self._activationWindow = None
        self._activateOnMessage = False
        self._outSocket = QLocalSocket()
        self._outSocket.connectToServer(self._appid)
        self._isRunning = self._outSocket.waitForConnected()
        self._outStream = None
        self._inSocket = None
        self._inStream = None
        self._server = None
        self.window = None       

    def close(self):
        if self._inSocket:
            self._inSocket.disconnectFromServer()
        if self._outSocket:
            self._outSocket.disconnectFromServer()
        if self._server:
            self._server.close()

    def isRunning(self):
        return self._isRunning

    def appid(self):
        return self._appid

    def activationWindow(self):
        return self._activationWindow

    def setActivationWindow(self, activationWindow, activateOnMessage=True):
        self._activationWindow = activationWindow
        self._activateOnMessage = activateOnMessage

    def activateWindow(self):
        if not self._activationWindow:
            return
        self._activationWindow.setWindowState(
            self._activationWindow.windowState() & ~Qt.WindowState.WindowMinimized)
        self._activationWindow.show()
        self._activationWindow.raise_()
        self._activationWindow.activateWindow()
    
    def setWindow(self, window):
        self.window = window

    def getWindow(self):
        return self.window
