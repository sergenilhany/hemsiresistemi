
import collections
from PyQt5 import QtCore, QtGui, QtWidgets
from pymongo import MongoClient




class Ui_Bashemsire(object):
    def setupUi(self, Bashemsire):
        self.MainWindow = QtWidgets.QMainWindow()  # Add this line to create MainWindow
        self.bashemsire_window = Bashemsire
        Bashemsire.setObjectName("Bashemsire")
        Bashemsire.resize(640, 480)
        self.widget = QtWidgets.QWidget(Bashemsire)
        self.widget.setGeometry(QtCore.QRect(0, 0, 640, 480))
        self.widget.setObjectName("widget")
        self.tableWidget = QtWidgets.QTableWidget(self.widget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 640, 480))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.back_button = QtWidgets.QPushButton(self.widget)
        self.back_button.setText("Geri Dön")
        self.back_button.setGeometry(QtCore.QRect(400, 440, 100, 30))
        self.back_button.clicked.connect(lambda: self.back_to_main_window(self.MainWindow))
        # Add these lines in the setupUi method, after creating the back_button
        self.search_input = QtWidgets.QLineEdit(self.widget)
        self.search_input.setGeometry(QtCore.QRect(10, 440, 200, 30))

        self.search_input = QtWidgets.QLineEdit(self.widget)
        self.search_input.setGeometry(QtCore.QRect(10, 440, 200, 30))

        self.search_button = QtWidgets.QPushButton(self.widget)
        self.search_button.setText("Ara")
        self.search_button.setGeometry(QtCore.QRect(220, 440, 75, 30))
        self.search_button.clicked.connect(self.search_data)

        self.retranslateUi(Bashemsire)
        QtCore.QMetaObject.connectSlotsByName(Bashemsire)


        self.retranslateUi(Bashemsire)
        QtCore.QMetaObject.connectSlotsByName(Bashemsire)
    
    def back_to_main_window(self, MainWindow):
        Bashemsire.hide()
        self.MainWindow = QtWidgets.QWidget()
        self.MainWindow.ui = MainWindow
        self.MainWindow.ui.setupUi(self.MainWindow)
        self.MainWindow.show()

    def retranslateUi(self, Bashemsire):
        _translate = QtCore.QCoreApplication.translate
        Bashemsire.setWindowTitle(_translate("Bashemsire", "Form"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Bashemsire", "Hasta Adı"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Bashemsire", "Uygulanan Tedavi veya ilaç"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Bashemsire", "Uygulama saati"))

    def displayData(self):
     
        client = MongoClient("mongodb://localhost:27017")
        db = client["Hemşireler"]
        collection = db["hastabilgileri"]
        self.tableWidget.setRowCount(0)
       
        for row, data in enumerate(collection.find()):
            self.tableWidget.insertRow(row)
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(data.get("hasta_adi", "")))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(data.get("tedavi_adi", "")))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(data.get("uygulama_saati", "")))


    def search_data(self):
        client = MongoClient("mongodb://localhost:27017")
        db = client["Hemşireler"]
        self.collection = db["hastabilgileri"]  # collection özelliğini burada tanımlayın

        hasta_adi = self.search_input.text()
        veriler = self.collection.find({"hasta_adi": hasta_adi})

        self.tableWidget.setRowCount(0)

        for row, data in enumerate(veriler):  # Fix the loop to use 'veriler' instead of 'collections'
            self.tableWidget.insertRow(row)
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(data.get("hasta_adi", "")))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(data.get("tedavi_adi", "")))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(data.get("uygulama_saati", "")))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    Bashemsire = QtWidgets.QWidget()
    ui = Ui_Bashemsire()
    ui.setupUi(Bashemsire)
    ui.displayData()  
    Bashemsire.show()
    sys.exit(app.exec_())
    