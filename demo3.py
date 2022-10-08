# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'number2.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(240, 320)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../media/ursia/16EC8BACEC8B84A9/Users/ursia/Pictures/IM_20/LOGO DEMARCHE/43704.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QtCore.QSize(18, 18))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(60, 50, 160, 16))
        self.horizontalSlider.setMinimum(10)
        self.horizontalSlider.setMaximum(80)
        self.horizontalSlider.setProperty("value", 20)
        self.horizontalSlider.valueChanged.connect(valueChange)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.verticalSlider = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider.setEnabled(True)
        self.verticalSlider.setGeometry(QtCore.QRect(20, 80, 16, 160))
        self.verticalSlider.setMinimum(1)
        self.verticalSlider.setMaximum(30)
        self.verticalSlider.setProperty("value", 3)
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setInvertedAppearance(True)
        self.verticalSlider.setInvertedControls(False)
        self.verticalSlider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.verticalSlider.setTickInterval(5)
        self.verticalSlider.setObjectName("verticalSlider")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 20, 67, 17))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextEditable)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setEnabled(True)
        self.menubar.setGeometry(QtCore.QRect(34, 2, 240, 22))
        self.menubar.setDefaultUp(True)
        self.menubar.setNativeMenuBar(False)
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.label.setBuddy(self.horizontalSlider)

        self.retranslateUi(MainWindow)
        self.toolBar.actionTriggered['QAction*'].connect(self.label.show) # type: ignore

        font = QtGui.QFont()
        sice = self.horizontalSlider.value()
        fonps = '0'
        if sice >= 21:
            fonps = font.setPointSize(sice)
        else:
            print("value inferior")
        font.setFamily("Tlwg Typewriter")    
        self.label.setFont(fonps)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "menu"))
        self.label.setText(_translate("MainWindow", "home"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))


def valueChange(horizontalSlider):
    sice1 = horizontalSlider
    print(sice1)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())