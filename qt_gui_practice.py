# qt_gui_practice

import sys
from PyQt4 import QtGui, QtCore

# Tutorial 1
# app = QtGui.QApplication([])
# window = QtGui.QWidget()
# window.setGeometry(50,50,1000,600)
# window.setWindowTitle('PyQT Practice')

# window.show()

class Window(QtGui.QMainWindow):
	def __init__(self):
		# getting parent object
		super(Window, self).__init__()
		self.setGeometry(50, 50, 500, 300)
		self.setWindowTitle('PyQT Tutorial')
		self.setWindowIcon(QtGui.QIcon('pyLogo.png'))
		
		# Create an action
		# Set a keyboard shortcut for the action		
		# Again the connect method lets you choose what happens when a button or menu is clicked
		extractAction = QtGui.QAction('&GET TO THE CHOPPA!!', self)
		extractAction.setShortcut('esc')
		extractAction.setStatusTip('Leave the app')
		extractAction.triggered.connect(sys.exit)

		randAction = QtGui.QAction('&yar', self)
		randAction.setShortcut('e')
		randAction.setStatusTip('yar')
		randAction.triggered.connect(sys.exit)

		# Calls the status bar into being
		self.statusBar()	# we don't need to make any changes to the status bar, so we can just create it
		mainMenu = self.menuBar()	# we need to do things with mainMenu, so we assign it to a variable
		fileMenu = mainMenu.addMenu('&File')
		fileMenu.addAction(extractAction)
		fileMenu.addAction(randAction)

		# self.show()
		self.home()

	def home(self):
		btn = QtGui.QPushButton('Quit', self)
		# generally when something happens, use connect and pass a function
		# the function passed just quits the instance of your application
		btn.clicked.connect(sys.exit)
		
		# QT has some cool button sizing functions
		btn.resize(btn.sizeHint())
		# btn.resize(btn.minimumSizeHint())
		# btn.resize(100,50)
		btn.move(100,100)

		extractAction = QtGui.QAction(QtGui.QIcon('todachoppa.png'), 'Flee the scene', self)
		extractAction.triggered.connect(sys.exit)

		self.toolBar = self.addToolBar('Extraction')
		self.toolBar.addAction(extractAction)

		self.show()


def main():
	app = QtGui.QApplication([])
	GUI = Window()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()