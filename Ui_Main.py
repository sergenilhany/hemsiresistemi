from PyQt5 import QtCore, QtGui, QtWidgets
from Ui_hemşire import Ui_Form
from Ui_Başhemşire import Ui_Bashemsire
from pymongo import MongoClient
from PyQt5.QtGui import QPixmap

class Ui_MainWindow(object):
    def __init__(self):
       self.client = MongoClient("mongodb://localhost:27017")
       self.db = self.client["Hemşireler"]
       self.collection = self.db["hemsireler"]
       self.seconf_window = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 640, 480))
        self.widget.setObjectName("widget")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(242, 340, 151, 28))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(172, 130, 281, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(172, 200, 281, 22))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton.clicked.connect(self.ikincisayfaac)
        self.pushButton.clicked.connect(self.checkLogin)
        
        self.second_window = None
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.client = MongoClient("mongodb://localhost:27017")
        self.db = self.client["Hemşireler"]
        self.collection = self.db["hemsireler"]

        self.MainWindow = MainWindow

        self.second_window = None
       
    def checkLogin(self):
     hemsire_id = self.lineEdit.text()
     password = self.lineEdit_2.text()

     if hemsire_id == "123456" and password == "sergen":
        QtWidgets.QMessageBox.information(self.MainWindow, "Başarılı", "Doğru giriş, Başhemşire sayfası açılıyor.")
        self.openBashemsirePage()
        return

     query = {"nurse_id": hemsire_id, "password": password}
     result = self.collection.find_one(query)

     if result:
        QtWidgets.QMessageBox.information(self.MainWindow, "Başarılı", "Doğru giriş, ikinci pencere açılıyor.")
        if not self.second_window:
            self.Form2 = QtWidgets.QWidget()
            ui = Ui_Form(data=result)
            ui.setupUi(self.Form2)
        self.Form2.show()
        self.MainWindow.hide()
     else:
        QtWidgets.QMessageBox.warning(self.MainWindow, "Hata", "Giriş bilgileri hatalı. Lütfen tekrar deneyin.")
        self.Form2.close()
        self.MainWindow.show()
    
    def openBashemsirePage(self):
        self.bashemsire_window = QtWidgets.QWidget()
        ui = Ui_Bashemsire()
        ui.setupUi(self.bashemsire_window)
        ui.displayData() 
        self.bashemsire_window.show()
        self.MainWindow.hide()

    def ikincisayfaac(self):
       self.Form2 = QtWidgets.QWidget()
       self.Form2.ui = Ui_Form()
       self.Form2.ui.setupUi(self.Form2)
       self.Form2.show()
       self.MainWindow.hide()



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Hemşire ID"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

  


