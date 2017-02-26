# typing_speed.py

"""
Typing Speed Test
Author: Morgan Allison
Created: 2/17
Edited: 2/17
Windows 7 64 bit
Anaconda 4.2.0 (Python 3.5.2)
"""

from PyQt4 import QtGui, QtCore
import sys

class Window(QtGui.QMainWindow):
	def __init__(self):
		super(Window, self).__init__()
		self.setGeometry(50, 50, 1000, 800)
		self.setWindowTitle('Typing Speed Tester')

		quit = QtGui.QAction('&Quit', self)
		quit.setShortcut('Alt+F4')
		quit.triggered.connect(sys.exit)

		self.statusBar = self.statusBar()
		mainMenu = self.menuBar()
		fileMenu = mainMenu.addMenu('&File')
		fileMenu.addAction(quit)

		self.home()

	def home(self):
		self.trialTextBox = QtGui.QLabel(self)
		self.trialTextBox.resize(500, 800)
		self.trialTextBox.setText('Yar')

		self.show()

def main():
	with open('C:\\users\\mallison\\documents\\github\\playground\\typing_speed\\fuckyou.txt') as f:
		x = f.read()
		print(x)
	app = QtGui.QApplication([])
	GUI = Window()

	app.exec_()

if __name__ == '__main__':
	main()
