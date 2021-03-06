# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NECMainP.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import time

# import eye_detection_03
# import win32api


threadPool = QtCore.QThreadPool()


class MainWindow():

    def __init__(self, qMainWindow):
        self.qMainWindow = qMainWindow
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.qMainWindow)

        self.ui.ViewHisButton_2.clicked.connect(self.countdown)

        # self.ui.ViewHisButton_2.clicked.connect(self.countup)
        self.ui.ViewHisButton_3.clicked.connect(self.stoptime)
        self.count_up = None

    # timefuction
    def countdown(self):
        self.countdown_args = {
            'is_start': True
        }
        countWorker = CountdownWorker(self.ui.Countdowner, 5, self.countdown_args)
        threadPool.start(countWorker)
        if (self.count_up == None) :
            self.count_up = CountUpWorker(self.ui.TimerCock, 1)
            threadPool.start(self.count_up)

    # def countup(self):
    #     count_up = CountUpWorker(self.ui.TimerCock, 1)
    #     threadPool.start(count_up)

    def stoptime(self):
        self.countdown_args['is_start'] = False


class Ui_MainWindow(object):

    def __init__(self):
        self.gs = 30 * 60

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(536, 398)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 501, 141))
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 30, 483, 83))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.TimerCock = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.TimerCock.setFont(font)
        self.TimerCock.setObjectName("TimerCock")
        self.verticalLayout.addWidget(self.TimerCock)
        self.Countdowner = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Countdowner.setFont(font)
        self.Countdowner.setObjectName("Countdowner")
        self.verticalLayout.addWidget(self.Countdowner)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 160, 501, 182))
        self.widget.setObjectName("widget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_8 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)
        self.FacePosi = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.FacePosi.setFont(font)
        self.FacePosi.setObjectName("FacePosi")
        self.horizontalLayout_3.addWidget(self.FacePosi)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ViewHisButton_2 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.ViewHisButton_2.setFont(font)
        self.ViewHisButton_2.setCheckable(False)
        self.ViewHisButton_2.setObjectName("ViewHisButton_2")
        self.horizontalLayout_2.addWidget(self.ViewHisButton_2)
        self.ViewHisButton_3 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.ViewHisButton_3.setFont(font)
        self.ViewHisButton_3.setCheckable(False)
        self.ViewHisButton_3.setObjectName("ViewHisButton_3")
        self.horizontalLayout_2.addWidget(self.ViewHisButton_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.ViewHisButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.ViewHisButton.setFont(font)
        self.ViewHisButton.setCheckable(False)
        self.ViewHisButton.setObjectName("ViewHisButton")
        self.verticalLayout_4.addWidget(self.ViewHisButton)
        self.ExitButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.ExitButton.setFont(font)
        self.ExitButton.setCheckable(False)
        self.ExitButton.setObjectName("ExitButton")
        self.verticalLayout_4.addWidget(self.ExitButton)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 536, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Timer"))
        self.label_4.setText(_translate("MainWindow", "เวลาในการมองทั้งหมด:"))
        self.label_3.setText(_translate("MainWindow", "ควรพักภายในอีก:"))
        self.TimerCock.setText(_translate("MainWindow", "00:00:00"))
        self.Countdowner.setText(_translate("MainWindow", "00:30:00"))
        self.label_5.setText(_translate("MainWindow", "นาที"))
        self.label_6.setText(_translate("MainWindow", "นาที"))
        self.label_8.setText(_translate("MainWindow", "Face Position:"))
        self.FacePosi.setText(_translate("MainWindow", "OFFLINE"))
        self.ViewHisButton_2.setText(_translate("MainWindow", "เริ่ม"))
        self.ViewHisButton_3.setText(_translate("MainWindow", "หยุด"))
        self.ViewHisButton.setText(_translate("MainWindow", "ดูสถิติ"))
        self.ExitButton.setText(_translate("MainWindow", "ออกจากระบบ"))


class CountdownWorker(QtCore.QRunnable):

    def __init__(self, CountDowner, countdown_time, countdown_args, *args, **kwargs):
        super(CountdownWorker, self).__init__()

        self.Countdowner = CountDowner
        self.countdown_time = countdown_time
        self.countdown_args = countdown_args

    def run(self) -> None:
        while self.countdown_time and self.countdown_args['is_start']:
            mins, secs = divmod(self.countdown_time, 60)
            hour, mins = divmod(mins, 60)
            timer = '{:02d}:{:02d}:{:02d}'.format(hour, mins, secs)
            self.Countdowner.setText(timer)
            time.sleep(1)
            self.countdown_time -= 1
            print(self.countdown_time)

        print("HELL", self.countdown_time)
        mins, secs = divmod(self.countdown_time, 60)
        timer = '{:02d}:{:02d}:{:02d}'.format(hour, mins, secs)
        self.Countdowner.setText(timer)
        # win32api.MessageBox(None, 'hello', 'title')


class CountUpWorker(QtCore.QRunnable):

    def __init__(self, Timer_Cock, countup_time, *args, **kwargs):
        super(CountUpWorker, self).__init__()

        self.TimerCock = Timer_Cock
        self.countup_time = countup_time

    def run(self) -> None:
        while self.countup_time:
            minss, secss = divmod(self.countup_time, 60)
            hours, minss = divmod(minss, 60)
            timerup = '{:02d}:{:02d}:{:02d}'.format(hours, minss, secss)
            self.TimerCock.setText(timerup)
            time.sleep(1)
            self.countup_time += 1

        self.TimerCock.setText(timerup)
        print("EELLO")


class BreakTime(QtCore.QRunnable):
    print("BELLO")
    # def stop_time(self):
    #     self.timer.stop()
    #
    #     print("LELLO")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    qMainWindow = QtWidgets.QMainWindow()

    mainWindow = MainWindow(qMainWindow)

    qMainWindow.show()
    sys.exit(app.exec_())
