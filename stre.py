import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class window(QWidget):
	def __init__(self, parent = None):
		super(window, self).__init__(parent)
		grid = QGridLayout()
		self.setLayout(grid)
		self.setWindowTitle("PyQt Grid Layout")
		self.setGeometry(100,100,200,100)
		self.grid.clicked.connect(flunc)

	def flunc(grid):
		for i in range(1,5):
			for i in range(1,5):
				grid.addWidget(QPushButton("B"+str(i)+str(j)))

def main():
	app = QApplication(sys.argv)

    ex = window()
    ex.show()
    
    sys.exit(app.exec_())

if __name__ == '__main__':
	main()
