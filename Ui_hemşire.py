from typing import Collection
from PyQt5 import QtCore, QtGui, QtWidgets
from pymongo import MongoClient

class Ui_Form(object):
    def __init__(self,data=None):
        print("0")
        self.data=data
        self.collection = None
        self.parentWidget = None

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(640, 480)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(92, 90, 331, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 160, 331, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(90, 230, 331, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 310, 151, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        
        print("connect")
        self.pushButton_2.clicked.connect(self.saveData)  
        print("signal")
       
        if self.data:
            self.lineEdit.setText(self.data.get("hasta_adi", ""))
            self.lineEdit_2.setText(self.data.get("tedavi_adi", ""))
            self.lineEdit_3.setText(self.data.get("uygulama_saati", ""))

        self.parentWidget = Form

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    
    def print_method(self):
        print("push button clicked")
    
    def saveData(self, Form):
        print("Button clicked")
        hasta_adi = self.lineEdit.text()
        tedavi_adi = self.lineEdit_2.text()
        uygulama_saati = self.lineEdit_3.text()
        print(f"Hasta Adı: {hasta_adi}, Tedavi Adı: {tedavi_adi}, Uygulama Saati: {uygulama_saati}")

        client = MongoClient("mongodb://localhost:27017")
        db = client["Hemşireler"]
        self.collection = db["hastabilgileri"] 
  
        data = {
             "hasta_adi": hasta_adi,
             "tedavi_adi": tedavi_adi,
             "uygulama_saati": uygulama_saati,
    }
        print(data)

        try:
            print("1")
            result = self.collection.insert_one(data)
            print(result)
            if result.inserted_id:
                print("Veri başarıyla kaydedildi.")
            else:
                print("Veri kaydetme başarısız.")

        except Exception as e:
            print(f"Hata oluştu: {e}")



    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Hasta Adı"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Tedavi Veya ilaç Adı"))
        self.lineEdit_3.setPlaceholderText(_translate("Form", "Uygulama saati"))
        self.pushButton_2.setText(_translate("Form", "PushButton"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())