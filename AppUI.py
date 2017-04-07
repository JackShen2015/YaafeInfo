import sys
from PyQt4 import QtCore, QtGui


class Window(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.resize(450, 500)
        self.setWindowTitle("mianWindows")

        textEdit = QtGui.QTextEdit()
        self.setCentralWidget(textEdit)

        exit = QtGui.QAction('Exit', self)
        exit.setShortcut('Ctrl+Q')
        exit.setStatusTip('Exit application')
        self.connect(exit, QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))

        self.statusBar()

        menubar = self.menuBar()
        file = menubar.addMenu('&File')
        file.addAction(exit)

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exit)

        # label = QtGui.QLabel("label")
        # abel.setAlignment(QtCore.Qt.AlignCenter)
        # self.setCentralWidget(label)


app = QtGui.QApplication(sys.argv)
demo = Window()
demo.show()
sys.exit(app.exec_())
