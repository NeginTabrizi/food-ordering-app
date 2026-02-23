from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(432, 474)
        Form.setStyleSheet("QWidget {\n"
"    background-color: #1e1e2f;\n"
"    color: white;\n"
"    font-size: 12pt;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #ff9800;\n"
"    color: black;\n"
"    border-radius: 8px;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #ffc107;\n"
"}\n"
"\n"
"QListWidget, QComboBox, QSpinBox {\n"
"    background-color: #2e2e3e;\n"
"    border-radius: 6px;\n"
"    padding: 4px;\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setFrameShape(QtWidgets.QFrame.Panel)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.restaurantBox = QtWidgets.QComboBox(Form)
        self.restaurantBox.setObjectName("restaurantBox")
        self.verticalLayout.addWidget(self.restaurantBox)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.menuList = QtWidgets.QListWidget(Form)
        self.menuList.setObjectName("menuList")
        self.verticalLayout.addWidget(self.menuList)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.quantitySpin = QtWidgets.QSpinBox(Form)
        self.quantitySpin.setMinimum(1)
        self.quantitySpin.setMaximum(20)
        self.quantitySpin.setObjectName("quantitySpin")
        self.verticalLayout.addWidget(self.quantitySpin)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.orderList = QtWidgets.QListWidget(Form)
        self.orderList.setObjectName("orderList")
        self.verticalLayout.addWidget(self.orderList)
        self.totalLabel = QtWidgets.QLabel(Form)
        self.totalLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.totalLabel.setObjectName("totalLabel")
        self.verticalLayout.addWidget(self.totalLabel)
        self.addButton = QtWidgets.QPushButton(Form)
        self.addButton.setObjectName("addButton")
        self.verticalLayout.addWidget(self.addButton)
        self.removeButton = QtWidgets.QPushButton(Form)
        self.removeButton.setObjectName("removeButton")
        self.verticalLayout.addWidget(self.removeButton)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "🍔 Food Ordering App"))
        self.label_5.setText(_translate("Form", "انتخاب رستوران"))
        self.label_2.setText(_translate("Form", "منوی غذا"))
        self.label_3.setText(_translate("Form", "تعداد"))
        self.label_4.setText(_translate("Form", "سفارش شما"))
        self.totalLabel.setText(_translate("Form", "مبلغ کل: 0 تومان"))
        self.addButton.setText(_translate("Form", "➕ افزودن"))
        self.removeButton.setText(_translate("Form", "❌ حذف"))
