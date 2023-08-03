import sys
import os
import datetime
import pandas as pd
import socket
import threading
import mysql.connector
import matplotlib.pyplot as plt
from PySide6.QtCore import QTimer, Qt,QObject, Signal, QDateTime
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QApplication, QTableWidget,QStyle,QDialog,QDockWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules import *
from widgets import *
from login import Ui_Form
from Problem import Problem
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%
# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui
        self.menu_shown = False
        # TOGGLE MENU
        UIFunctions.toggleMenu(self, True)
        self.ui.leftMenuBg.setMinimumWidth(Settings.MENU_WIDTH)
        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)
        # CHỨC NĂNG ///////////////////////////////////////////////////////////////
        self.sensor_receiver = SensorDataReceiver(socket.gethostname(),8234)
        # Start listening for connections
        self.sensor_receiver.start_listening()
        self.canvas = MatplotlibCanvasNhietdo()
        self.canvasdoam = MatplotlibCanvasDoam()
        self.sensor_receiver.dataReceived.connect(self.canvas.update_figureNhietdo)
        self.sensor_receiver.dataReceived.connect(self.canvasdoam.update_figureDoam)
        self.ui.screen_nhietdo.addWidget(self.canvas)
        self.ui.screen_doam.addWidget(self.canvasdoam)
        self.sensor_receiver.dataReceived.connect(self.update_label)

        

        # ////// thời gian thực hiển thị
        self.menu_layout = QVBoxLayout()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_label_datetime)
        self.timer.start(1000) 
        # LEFT MENUS
        widgets.btn_lu139.clicked.connect(self.buttonClick)
        widgets.btn_lu205.clicked.connect(self.buttonClick)
        widgets.btn_lu132.clicked.connect(self.buttonClick)
        widgets.btn_lu596.clicked.connect(self.buttonClick)
        # widgets.btn_lu205.clicked.connect( lambda: self.show_error_dock)
        # EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)
        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)
        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)
        self.show()
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()
        # SHOW WIDGETS PAGE
        if btnName == "btn_lu139":
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            self.show_drop_down_menu(btn)
        if btnName == "btn_lu205":
            self.show_drop_down_menu(btn)
        

    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)
    def update_label_datetime(self):
        current_datetime = QDateTime.currentDateTime()
        formatted_datetime = current_datetime.toString("dd/MM/yyyy, hh:mm:ss")
        self.ui.label_2.setText(formatted_datetime)
        self.ui.thoigian_nhietdo.setText(formatted_datetime)
        self.ui.label_thoigian_doam.setText(formatted_datetime)
    def update_label(self,temperature, humidity, light, voltage_dc, voltage_ac ):
        self.ui.label_nhietdo.setText(f" Nhiệt độ hiện tại : {temperature}°C")
        self.ui.label_nhietdo_2.setText(f" Nhiệt độ hiện tại : {temperature}°C")
        self.ui.label_nhietdo_3.setText(f" Nhiệt độ hiện tại : {temperature}°C")
        self.ui.label_nhietdo_4.setText(f" Nhiệt độ hiện tại : {temperature}°C")
        self.ui.label_nhietdo_5.setText(f" Nhiệt độ hiện tại : {temperature}°C")
        self.ui.label_nhietdo_6.setText(f" Nhiệt độ hiện tại : {temperature}°C")
        self.ui.label_doam_2.setText(f" Độ ẩm hiện tại : {humidity} %")
        self.ui.label_doam_3.setText(f" Độ ẩm hiện tại : {humidity} %")
        self.ui.label_doam_4.setText(f" Độ ẩm hiện tại : {humidity} %")
        self.ui.label_doam_5.setText(f" Độ ẩm hiện tại : {humidity} %")
        self.ui.label_doam_6.setText(f" Độ ẩm hiện tại : {humidity} %")
        self.ui.label_doam_7.setText(f" Độ ẩm hiện tại : {humidity} %")
        
        if voltage_ac == 0:
            self.ui.pushButton_ac1.setStyleSheet("background-color:rgb(255, 0, 0);")
            self.ui.pushButton_ac1_2.setStyleSheet("background-color:rgb(255, 0, 0);")
            self.ui.pushButton_ac1_3.setStyleSheet("background-color:rgb(255, 0, 0);")
            self.ui.pushButton_ac1_4.setStyleSheet("background-color:rgb(255, 0, 0);")
            self.ui.pushButton_ac1_5.setStyleSheet("background-color:rgb(255, 0, 0);") 
            self.ui.pushButton_ac1_6.setStyleSheet("background-color:rgb(255, 0, 0);")
        elif voltage_ac == 220:
            self.ui.pushButton_ac1.setStyleSheet("background-color: rgb(0, 170, 0);")
            self.ui.pushButton_ac1_2.setStyleSheet("background-color: rgb(0, 170, 0);")
            self.ui.pushButton_ac1_3.setStyleSheet("background-color: rgb(0, 170, 0);")
            self.ui.pushButton_ac1_4.setStyleSheet("background-color: rgb(0, 170, 0);")
            self.ui.pushButton_ac1_5.setStyleSheet("background-color: rgb(0, 170, 0);") 
            self.ui.pushButton_ac1_6.setStyleSheet("background-color: rgb(0, 170, 0);")
        
        
         # Update the color of the QPushButton based on temperature
        if 20 <= temperature <= 25:
            colorTem = "background-color: rgb(0, 170, 0);"
        elif 25 < temperature <= 30:
            colorTem = "background-color: rgb(255, 255, 0);"
        else:
            colorTem = "background-color: rgb(255, 0, 0);"
        buttons = [self.ui.pushButton_nhietdo, self.ui.pushButton_nhietdo_2, self.ui.pushButton_nhietdo_3, self.ui.pushButton_nhietdo_4,self.ui.pushButton_nhietdo_5, self.ui.pushButton_nhietdo_6]
        for button in buttons:
            button.setStyleSheet(colorTem)
        
        if 50 <= humidity <= 60:
            colorHum = "background-color: rgb(0, 170, 0);"
        elif 60 < humidity <= 70:
            colorHum = "background-color: rgb(255, 255, 0);"
        else:
            colorHum = "background-color: rgb(255, 0, 0);"
        buttons = [self.ui.pushButton_doam, self.ui.pushButton_doam_2, self.ui.pushButton_doam_3, self.ui.pushButton_doam_4, self.ui.pushButton_doam_5, self.ui.pushButton_doam_6]
        for button in buttons:
            button.setStyleSheet(colorHum)

        if 10 <= voltage_dc <= 12:
            colorDC = "background-color: rgb(0, 170, 0);"
        elif 1 < voltage_dc <= 10:
            colorDC = "background-color: rgb(255, 255, 0);"
        else:
            colorDC = "background-color: rgb(255, 0, 0);"
        buttons = [self.ui.pushButton_dc1, self.ui.pushButton_dc1_2, self.ui.pushButton_dc1_3, self.ui.pushButton_dc1_4, self.ui.pushButton_dc1_5, self.ui.pushButton_dc1_6]
        for button in buttons:
            button.setStyleSheet(colorDC)
    def show_drop_down_menu(self, button):
        menu = QMenu(self)
        menu.setFixedSize(270, 110)
        action1 = menu.addAction("Trạm A01")
        action2 = menu.addAction("Trạm A70")
        action3 = menu.addAction("Trạm A45")
        action4 = menu.addAction("Trạm A48")
        action5 = menu.addAction("Trạm A171")
        action6 = menu.addAction("Trạm A78")
        # Connect each action to a function that handles the selected option
        action1.triggered.connect(lambda: self.show_sub_menu("Trạm A01"))
        action2.triggered.connect(lambda: self.show_sub_menu("Trạm A70"))
        action3.triggered.connect(lambda: self.show_sub_menu("Trạm A45"))
        action4.triggered.connect(lambda: self.show_sub_menu("Trạm A48"))
        action5.triggered.connect(lambda: self.show_sub_menu("Trạm A171"))
        action6.triggered.connect(lambda: self.show_sub_menu("Trạm A78"))

        position = button.mapToGlobal(button.rect().bottomLeft())
        menu.exec(position)
    
    def show_sub_menu(self, main_option):
        sub_menu = QMenu(self)
        sub_menu.setFixedSize(240, 110)
        sub_action1 = sub_menu.addAction("Nhiệt Độ")
        sub_action2 = sub_menu.addAction("Độ Ẩm")
        sub_action3 = sub_menu.addAction("Điện Áp DC")
        sub_action4 = sub_menu.addAction("Điện Áp AC")
        sub_action5 = sub_menu.addAction("Sự Cố")

        # Kết nối các hành động của menu phụ
        sub_action1.triggered.connect(lambda: self.handle_option("Nhiệt Độ"))
        sub_action2.triggered.connect(lambda: self.handle_option("Độ Ẩm"))
        sub_action3.triggered.connect(lambda: self.handle_option("Điện Áp DC"))
        sub_action4.triggered.connect(lambda: self.handle_option("Điện Áp AC"))
        sub_action5.triggered.connect(lambda: self.handle_option("Sự Cố"))
        position = self.sender().mapToGlobal(self.sender().rect().bottomLeft())
        sub_menu.exec(position)
    def handle_option(self, option_name):
        if option_name == "Nhiệt Độ":
            widgets.stackedWidget.setCurrentWidget(widgets.Nhietdo)
        elif option_name == "Độ Ẩm" :
            widgets.stackedWidget.setCurrentWidget(widgets.Doam)
        elif option_name == "Sự Cố" :
            self.show_error_dock()
    def show_error_dock(self):
        # Tạo cửa sổ QDockWidget
        dock = QDockWidget("Sự Cố")
        # Thêm widget bên trong cửa sổ
        label = QLabel("Đây là cửa sổ sự cố!")
        layout = QVBoxLayout()
        layout.addWidget(label)
        widget = QWidget()
        widget.setLayout(layout)
        dock.setWidget(widget)
        # Đặt vị trí của DockWidget ở trung tâm MainWindow
        self.addDockWidget(Qt.RightDockWidgetArea, dock)
        dock.setFloating(True)  # Cho DockWidget nổi trên cửa sổ chính
        dock.setGeometry(self.width()/4, self.height()/4, self.width()/2, self.height()/2)  # Đặt kích thước DockWidget
        dock.show()
    
class LoginWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.login_attempt)

    def login_attempt(self):
        # Perform the login validation here
        # For example, check the username and password entered by the user
        username = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()

        if username == "admin" and password == "123456":
            # If the login is successful, accept the dialog
            self.accept()
        else:
            # If the login is not successful, display an error message
            QMessageBox.warning(self, "Login Failed", "Invalid username or password")
            # And reject the dialog
            self.reject()            
class MatplotlibCanvasNhietdo(FigureCanvas):
    dataReceived = Signal(float, float,float,float,float,float)
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        super().__init__(self.fig)
        self.temperature = []
        self.time = []
        self.ax.set_xlim(0, 23)
        self.ax.set_xlabel('Thời gian')
        self.ax.set_ylabel('Nhiệt độ')
        self.ax.set_ylim(0, 50)
        
        self.data_count = 0
    def update_figureNhietdo(self, temperature):
        current_time = datetime.datetime.now().strftime('%H:%M')
        self.temperature.append(temperature)
        self.time.append(current_time)
        self.data_count += 1
        
        if self.data_count > 24:
            self.temperature.pop(0)
            self.time.pop(0)
        self.ax.clear()  
        if len(self.temperature) < 24:
            self.ax.plot(range(len(self.temperature)), self.temperature, '-o', label='Nhiệt độ')
            self.ax.set_xticks(range(len(self.temperature)))
            self.threshold = 30  # Giá trị ngưỡng nhiệt độ
            self.ax.axhline(self.threshold, color='r', linestyle='--', label='Ngưỡng quá nhiệt độ')
            self.ax.set_xlim(0, 23)
            self.ax.set_xticklabels(self.time)
        else:
            self.ax.plot(range(24), self.temperature[-24:], '-o', label='Nhiệt độ')
            self.ax.set_xticks(range(24))
            self.ax.set_xlim(0, 23) 
            self.threshold = 30  # Giá trị ngưỡng nhiệt độ
            self.ax.axhline(self.threshold, color='r', linestyle='--', label='Ngưỡng quá nhiệt độ')
            self.ax.set_xticklabels(self.time[-24:])
        
        self.ax.set_xlabel('Thời gian')
        self.ax.set_ylabel('Nhiệt độ')
        self.ax.set_ylim(0, 50)
        self.ax.legend()
        self.draw()
    def get_latest_humidity_from_mysql(self):
        # Kết nối msql
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="duong0378920430",
                database="datamodul"
                )
            mycusor = mydb.cursor()
            query ="SELECT * FROM datamodul.data; "
            mycusor.execute(query)
            result = mycusor.fetchone()

        # Close the database connection
            mycusor.close()
            mydb.close()
class MatplotlibCanvasDoam(FigureCanvas):
    dataReceived = Signal(float,float,float,float,float,float)
    def __init__(self):
        self.figdoam, self.axdoam = plt.subplots()
        super().__init__(self.figdoam)
        self.humidity = []
        self.time = []
        self.axdoam.set_xlim(0, 23)
        self.axdoam.set_xlabel('Thời gian')
        self.axdoam.set_ylabel('Độ Ẩm')
        self.axdoam.set_ylim(0, 100)
        
        self.data_count = 0
    def update_figureDoam(self,temperature,humidity,light,voltage_dc,voltage_ac,current_time):
        current_time = datetime.datetime.now().strftime('%H:%M')
        self.humidity.append(humidity)
        self.time.append(current_time)
        self.data_count += 1
        if self.data_count > 24:
            self.humidity.pop(0)
            self.time.pop(0)
        self.axdoam.clear()  
        if len(self.humidity) < 24:
            self.axdoam.plot(range(len(self.humidity)), self.humidity, '-o', label='Độ ẩm')
            self.axdoam.set_xticks(range(len(self.humidity)))
            self.threshold = 70  # Giá trị ngưỡng nhiệt độ
            self.axdoam.axhline(self.threshold, color='r', linestyle='--', label='Ngưỡng quá Độ ẩm')
            self.axdoam.set_xlim(0, 23)
            self.axdoam.set_xticklabels(self.time)
        else:
            self.axdoam.plot(range(24), self.humidity[-24:], '-o', label='Độ ẩm')
            self.axdoam.set_xticks(range(24))
            self.axdoam.set_xlim(0, 23) 
            self.threshold = 70  # Giá trị ngưỡng nhiệt độ
            self.axdoam.axhline(self.threshold, color='r', linestyle='--', label='Ngưỡng quá Độ ẩm')
            self.axdoam.set_xticklabels(self.time[-24:])
        
        self.axdoam.set_xlabel('Thời gian')
        self.axdoam.set_ylabel('Độ Ẩm')
        self.axdoam.set_ylim(0, 100)
        self.axdoam.legend()
        self.draw()
    def get_latest_humidity_from_mysql(self):
        # Kết nối msql
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="duong0378920430",
                database="datamodul"
                )
            mycusor = mydb.cursor()
            query ="SELECT * FROM datamodul.data; "
            mycusor.execute(query)
            result = mycusor.fetchone()

        # Close the database connection
            mycusor.close()
            mydb.close()
class SensorDataReceiver(QObject):
    dataReceived = Signal(float,float,float,float,float,datetime.datetime)
    def __init__(self, host, port):
        super().__init__()
        self.host = host
        self.port = port
        self.socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_server.bind((self.host, self.port))
        self.socket_server.listen(5)
        print(f"Server listening on {self.host}:{self.port}")

    def start_listening(self):
        threading.Thread(target=self.accept_connections).start()

    def accept_connections(self):
        while True:
            client_socket, client_address = self.socket_server.accept()
            print(f"Accepted connection from {client_address[0]}:{client_address[1]}")
            threading.Thread(target=self.receive_data, args=(client_socket,)).start()

    def receive_data(self, client_socket):
        try:
            while True:
            # Nhận độ ẩm nhiệt độ gửi lên dưới dạng chuỗi
                data = client_socket.recv(1024).decode()
                if not data:
                    break
                #tách nhiệt độ độ ẩm từ chuỗi với ngăn cách dấu phẩy
                temperature, humidity, light, voltage_dc, voltage_ac = data.split(",")
                # chuyển thành float để hiển thị chính xác hơn
                temperature = float(temperature) 
                humidity = float(humidity)
                light = float(light)
                voltage_dc = float(voltage_dc)
                voltage_ac = float(voltage_ac)
                current_time = datetime.datetime.now()
                self.dataReceived.emit(temperature, humidity, light, voltage_dc, voltage_ac,current_time)
                print(f"Received data: {temperature}, {humidity}, {light}, {voltage_dc}, {voltage_ac},{current_time}")
                self.send_data_to_mysql(temperature,humidity,light,voltage_dc,voltage_ac,current_time)
        except socket.error:
            print("Error receiving data from the sensor.")

    def send_data_to_mysql(self, temperature,humidity,light,voltage_dc,voltage_ac,current_time):
      try:  
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="duong0378920430",
            database="datamodul"
            )
        mycursor = mydb.cursor()
        query = "INSERT INTO data (temperature, humidity, light, voltage_dc, voltage_ac,time) VALUES (%s,%s,%s,%s,%s,%s);"
        values = (str(temperature), str(humidity), str(light), str(voltage_dc), str(voltage_ac),current_time)
        mycursor.execute(query, values)
        mydb.commit()
        print("Data sent to MySQL successfully.")
      except mysql.connector.Error as error:
        print("Error inserting data into MySQL:", error)
# class CustomDockWidget(QDockWidget):
#     def __init__(self, title):
#         super().__init__(title)

#         self.init_ui()

#     def init_ui(self):
#         widget = QWidget()
#         layout = QVBoxLayout()

#         # Tạo các QLabel và QDateTimeEdit
#         label1 = QLabel("Ngày bắt đầu:")
#         self.date_edit1 = QDateTimeEdit()
#         label2 = QLabel("Ngày kết thúc:")
#         self.date_edit2 = QDateTimeEdit()

#         # Đặt chế độ chỉnh sửa thời gian cho QDateTimeEdit
#         self.date_edit1.setDisplayFormat("dd/MM/yyyy, hh:mm:ss")
#         self.date_edit2.setDisplayFormat("dd/MM/yyyy, hh:mm:ss")

#         # Tạo QPushButton
#         button = QPushButton("Xem sự cố")
#         button.clicked.connect(self.on_button_clicked)

#         # Thêm các thành phần vào layout
#         layout.addWidget(label1)
#         layout.addWidget(self.date_edit1)
#         layout.addWidget(label2)
#         layout.addWidget(self.date_edit2)
#         layout.addWidget(button)

#         # Đặt layout cho widget
#         widget.setLayout(layout)

#         # Đặt widget làm nội dung cho QDockWidget
#         self.setWidget(widget)

#     def on_button_clicked(self):
#         # Xử lý sự kiện khi nhấn vào nút "Xem sự cố"
#         # Ở đây chúng ta chỉ in ra ngày được chọn từ QDateTimeEdit
#         start_date = self.date_edit1.dateTime().toString("dd/MM/yyyy, hh:mm:ss")
#         end_date = self.date_edit2.dateTime().toString("dd/MM/yyyy, hh:mm:ss")
#         print(f"Ngày bắt đầu: {start_date}")
#         print(f"Ngày kết thúc: {end_date}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icons.ico"))
    # Create and show the login window
    login_window = LoginWindow()
    
    login_window = LoginWindow()
   
    if login_window.exec() == QDialog.Accepted:
        print("Login successful")
        # If the login is successful, create and show the MainWindow:
        window = MainWindow()
        window.show()
        sys.exit(app.exec())
    else:
        print("Login canceled")
