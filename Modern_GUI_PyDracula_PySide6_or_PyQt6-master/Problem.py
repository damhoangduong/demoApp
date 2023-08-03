
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDateEdit, QDockWidget, QGridLayout,
    QLabel, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys

class Problem(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(355, 160)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.dockWidget = QDockWidget(Form)
        self.dockWidget.setObjectName(u"dockWidget")
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.gridLayout = QGridLayout(self.dockWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.dockWidgetContents)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.dockWidgetContents)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

        self.dateEdit = QDateEdit(self.dockWidgetContents)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setAlignment(Qt.AlignCenter)
        self.dateEdit.setDate(QDate(2023, 1, 1))

        self.gridLayout.addWidget(self.dateEdit, 1, 0, 1, 1)

        self.dateEdit_2 = QDateEdit(self.dockWidgetContents)
        self.dateEdit_2.setObjectName(u"dateEdit_2")
        self.dateEdit_2.setAlignment(Qt.AlignCenter)
        self.dateEdit_2.setDate(QDate(2023, 1, 1))

        self.gridLayout.addWidget(self.dateEdit_2, 1, 1, 1, 1)

        self.pushButton = QPushButton(self.dockWidgetContents)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 2)

        self.dockWidget.setWidget(self.dockWidgetContents)

        self.verticalLayout.addWidget(self.dockWidget)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Th\u1eddi gian b\u1eaft \u0111\u1ea7u", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Th\u1eddi gian k\u1ebft th\u00fac", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Xem s\u1ef1 c\u1ed1", None))
    # retranslateUi
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     form = QWidget()
#     ui = Problem()
#     ui.setupUi(form)
#     form.show()
#     sys.exit(app.exec())
