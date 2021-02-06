from editor import editor
from PyQt5.QtWidgets import (
    QMainWindow,
    QAction,
    qApp,
    QApplication,
    QWidget,
    QHBoxLayout,
    QPushButton,
    QCheckBox,
    QStyle,
    QLabel,
)
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt
import sys


class Menu(QMainWindow):
    def __init__(self, parent=None):
        super(Menu, self).__init__(parent)

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Hello World")
        # self.resize(250, 300)
        self.setWindowIcon(QIcon("/static/logo.ico"))

        self.setGeometry(0, 0, 500, 500)

        self.label = QLabel("The toggle state is ")
        self.label.setAlignment(Qt.AlignCenter)

        self.label.setFont(QFont("Times", 12, QFont.Bold))

        self.setCentralWidget(self.label)

        toggleAction = QAction("&Toggle Label", self, checkable=True)
        toggleAction.setStatusTip("Toggle the label")
        toggleAction.triggered.connect(self.toggleLabel)

        exitAction = QAction(
            self.style().standardIcon(QStyle.SP_DialogCancelButton), "&Exit", self
        )
        exitAction.setShortcut("Ctrl+Q")
        exitAction.setStatusTip("Exit application")
        exitAction.triggered.connect(qApp.quit)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu("&File")
        fileMenu.addAction(toggleAction)
        fileMenu.addAction(exitAction)

        preferencesMenu = menubar.addMenu("&Preferences")

        self.show()

    def toggleLabel(self, state):
        self.label.setText("The toggle state is {}".format(state))

if __name__ == "__main__":
    root = QApplication(sys.argv)
    app = Menu()
    sys.exit(root.exec_())
