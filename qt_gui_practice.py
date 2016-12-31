# qt_gui_practice
# Anaconda 4.2.0 (64 bit Python 3.5.2)
# PyQtGraph 0.9.10 (pyqt 4.8.7, qt 4.11.4)

import sys
from PyQt4 import QtGui, QtCore
import pyqtgraph as pg
import numpy as np

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
		self.setGeometry(50, 50, 1000, 600)
		self.setWindowTitle('PyQT Tutorial')
		self.setWindowIcon(QtGui.QIcon('pyLogo.png'))
		
		# Create an action
		# Set a keyboard shortcut for the action		
		# Again the connect method lets you choose what happens when a button or menu is clicked
		quit = QtGui.QAction('&Quit', self)
		quit.setShortcut('esc')
		quit.setStatusTip('Leave the app')
		quit.triggered.connect(sys.exit)

		# Calls the status bar into being
		self.statusBar()	# we don't need to make any changes to the status bar, so we can just create it
		mainMenu = self.menuBar()	# we need to do things with mainMenu, so we assign it to a variable
		fileMenu = mainMenu.addMenu('&File')
		fileMenu.addAction(quit)

		# self.show()
		self.home()

	def home(self):
		self.p = pg.PlotWidget(self, title='Continuous Spectrum')
		self.p.move(50,50)
		self.p.resize(900, 500)
		self.flag = -1
		self.f = 10
		self.x = np.linspace(0,4*np.pi,1000)
		self.y = np.cos(self.f*self.x)
		self.pData = self.p.plot(self.x, self.y)
		
		self.timer = QtCore.QTimer()
		self.timer.timeout.connect(self.update)
		self.timer.start()


		self.show()

	def update(self):		
		if self.flag == -1:
			self.f = self.f/1.005
		else:
			self.f = self.f*1.005
		
		if self.f < 0.5:
			self.flag = 1
		if self.f > 11:
			self.flag = -1
		
		self.y = np.cos(self.f*self.x)
		self.pData.setData(self.x, self.y)


def main():
	app = QtGui.QApplication([])
	GUI = Window()
	
	# timer = QtCore.QTimer()
	# timer.timeout.connect(GUI.update)
	# timer.start()

	app.exec_()

if __name__ == '__main__':
	main()