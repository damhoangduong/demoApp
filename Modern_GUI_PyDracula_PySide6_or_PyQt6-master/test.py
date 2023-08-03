from PySide6.QtWidgets import QApplication, QMainWindow, QMenu,QPushButton
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Main Window")
        self.setGeometry(100, 100, 800, 600)

        # Tạo QPushButton
        button = QPushButton("Open Menu")
        button.clicked.connect(self.show_main_menu)

        self.setCentralWidget(button)

        self.show()

    def show_main_menu(self):
        main_menu = QMenu(self)
        action1 = main_menu.addAction("Trạm A01")
        action2 = main_menu.addAction("Trạm A70")
        action3 = main_menu.addAction("Trạm A45")
        action4 = main_menu.addAction("Trạm A48")
        action5 = main_menu.addAction("Trạm A171")
        action6 = main_menu.addAction("Trạm A78")

        # Kết nối các hành động với các menu phụ
        action1.triggered.connect(lambda: self.show_sub_menu(action1.text()))
        action2.triggered.connect(lambda: self.show_sub_menu(action2.text()))
        action3.triggered.connect(lambda: self.show_sub_menu(action3.text()))
        action4.triggered.connect(lambda: self.show_sub_menu(action4.text()))
        action5.triggered.connect(lambda: self.show_sub_menu(action5.text()))
        action6.triggered.connect(lambda: self.show_sub_menu(action6.text()))

        position = self.sender().mapToGlobal(self.sender().rect().bottomLeft())
        main_menu.exec(position)

    def show_sub_menu(self, main_option):
        sub_menu = QMenu(self)
        action1 = sub_menu.addAction("Menu Phụ 1")
        action2 = sub_menu.addAction("Menu Phụ 2")

        # Kết nối các hành động của menu phụ
        action1.triggered.connect(lambda: self.handle_option(main_option, action1.text()))
        action2.triggered.connect(lambda: self.handle_option(main_option, action2.text()))

        position = self.sender().mapToGlobal(self.sender().rect().bottomRight())
        sub_menu.exec(position)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())