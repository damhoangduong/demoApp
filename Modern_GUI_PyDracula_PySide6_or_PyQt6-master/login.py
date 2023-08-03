
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys
from PySide6.QtWidgets import QApplication, QWidget
import resources

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(600, 360)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMinimumSize(QSize(160, 0))
        self.label.setPixmap(QPixmap(u":/images/images/images/logo-binh-chung-thong-tin-lien-lac (1).png"))
        self.label.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label)

        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy2)
        self.verticalLayout_2 = QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget_3)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setStyleSheet(u"font: 20pt \"Segoe UI\";\n"
"font: 18pt \"Segoe UI\";\n"
"font: 700  \"Segoe UI\";\n"
"color: rgb(85, 170, 255);")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.widget_3)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setStyleSheet(u"\n"
"font: 16pt \"Segoe UI\";\n"
"font: 700  \"Segoe UI\";\n"
"color: rgb(255, 0, 0);")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_3)


        self.horizontalLayout.addWidget(self.widget_3)


        self.verticalLayout_3.addWidget(self.widget_2)

        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_5 = QWidget(self.widget_4)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_4 = QVBoxLayout(self.widget_5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_5 = QLabel(self.widget_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"font: 11pt \"Segoe UI\";")
        self.label_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_5.setMargin(0)

        self.verticalLayout_4.addWidget(self.label_5)

        self.label_6 = QLabel(self.widget_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"\n"
"font: 700 11pt \"Segoe UI\";")

        self.verticalLayout_4.addWidget(self.label_6)

        self.label_7 = QLabel(self.widget_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"\n"
"font:  11pt \"Segoe UI\";")

        self.verticalLayout_4.addWidget(self.label_7)

        self.label_8 = QLabel(self.widget_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"\n"
"font:  11pt \"Segoe UI\";")

        self.verticalLayout_4.addWidget(self.label_8)

        self.label_9 = QLabel(self.widget_5)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"\n"
"font:  11pt \"Segoe UI\";")

        self.verticalLayout_4.addWidget(self.label_9)


        self.horizontalLayout_2.addWidget(self.widget_5)

        self.widget_6 = QWidget(self.widget_4)
        self.widget_6.setObjectName(u"widget_6")
        self.label_4 = QLabel(self.widget_6)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, -1, 291, 41))
        self.label_4.setStyleSheet(u"font: 11pt \"Segoe UI\";")
        self.lineEdit = QLineEdit(self.widget_6)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 40, 271, 41))
        self.lineEdit.setStyleSheet(u"font: 11pt \"Segoe UI\";")
        self.lineEdit_2 = QLineEdit(self.widget_6)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(10, 90, 271, 41))
        self.lineEdit_2.setStyleSheet(u"font: 11pt \"Segoe UI\";")
        self.checkBox = QCheckBox(self.widget_6)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(20, 159, 161, 21))
        self.pushButton = QPushButton(self.widget_6)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(60, 210, 161, 41))
        self.pushButton.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")

        self.horizontalLayout_2.addWidget(self.widget_6)


        self.verticalLayout_3.addWidget(self.widget_4)


        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi
        

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"BINH CH\u1ee6NG TH\u00d4NG TIN LI\u00caN L\u1ea0C", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"C\u1ed4NG TH\u00d4NG TIN \u0110I\u1ec6N T\u1eec", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"    H\u1ed7 tr\u1ee3 k\u1ef9 thu\u1eadt", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"    Ban c\u00f4ng ngh\u1ec7 th\u00f4ng tin - BTM ", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"    S\u1ed1 \u0111i\u1ec7n tho\u1ea1i : 588.657 - 935.178", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"    Th\u01b0 \u0111i\u1ec7n t\u1eed : bancntt@bctt.bqp", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"    T\u1ea3i t\u00e0i li\u1ec7u h\u01b0\u1edbng d\u1eabn s\u1eed d\u1ee5ng", None))
        self.label_4.setText(QCoreApplication.translate("Form", u" \u0110\u1ed3ng ch\u00ed nh\u1eadp th\u00f4ng tin", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Username", None))
        self.lineEdit_2.setText(QCoreApplication.translate("Form", u"Password", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Form", u"Password", None))
        self.checkBox.setText(QCoreApplication.translate("Form", u"Nh\u1edb th\u00f4ng tin \u0111\u0103ng nh\u1eadp", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u0110\u0103ng nh\u1eadp", None))
    # retranslateUi


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = QWidget()
    ui = Ui_Form()
    ui.setupUi(form)
    form.show()
    sys.exit(app.exec())