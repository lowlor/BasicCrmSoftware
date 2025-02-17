import mysql.connector
import PyQt5.QtWidgets as qtw
from docxtpl import DocxTemplate
from docx2pdf import convert
from datetime import datetime
from PyQt5.QtCore import Qt, QDateTime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate
import os
import subprocess
import loginPhoto_rc

loginStatus = 0
currentUser = ''
currentQueueID = ''
currentBillID = ''
currentInvoiceID = ''
currentReceiptID = ''
currentQuotationID = ''
currentDeliveryID = ''
currentUserPos = ''
goMainPage = 0

mydb = mysql.connector.connect(
  host="",
  user="",
  password="",
  database=''
)
cursor = mydb.cursor()

class login(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 800)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.headLabel = QtWidgets.QLabel(self.centralwidget)
        self.headLabel.setGeometry(QtCore.QRect(920, 240, 100, 36))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.headLabel.setFont(font)
        self.headLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.headLabel.setStyleSheet("QLabel {\n"
"    color: RED;              /* White text */\n"
"}")
        self.headLabel.setObjectName("headLabel")
        self.confirmButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.loginButton())
        self.confirmButton.setGeometry(QtCore.QRect(870, 470, 181, 23))
        self.confirmButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.confirmButton.setAutoFillBackground(False)
        self.confirmButton.setStyleSheet("QPushButton {\n"
"                background-color: #156d9c; \n"
"                color: white; \n"
"                padding: 15px;\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #2891ca;  /* Lighter green on hover */\n"
"            }")
        self.confirmButton.setObjectName("confirmButton")
        self.username_Label = QtWidgets.QLabel(self.centralwidget)
        self.username_Label.setGeometry(QtCore.QRect(750, 310, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.username_Label.setFont(font)
        self.username_Label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.username_Label.setObjectName("username_Label")
        self.usernameTextField = QtWidgets.QLineEdit(self.centralwidget)
        self.usernameTextField.setGeometry(QtCore.QRect(890, 320, 251, 20))
        self.usernameTextField.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.usernameTextField.setText("")
        self.usernameTextField.setObjectName("usernameTextField")
        self.passwordTextField = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordTextField.setGeometry(QtCore.QRect(890, 390, 251, 20))
        self.passwordTextField.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.passwordTextField.setText("")
        self.passwordTextField.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordTextField.setObjectName("passwordTextField")
        self.password_Label = QtWidgets.QLabel(self.centralwidget)
        self.password_Label.setGeometry(QtCore.QRect(750, 380, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.password_Label.setFont(font)
        self.password_Label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.password_Label.setObjectName("password_Label")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-30, -100, 721, 991))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 21))
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
        self.headLabel.setText(_translate("MainWindow", "LOGIN"))
        self.confirmButton.setText(_translate("MainWindow", "Confirm"))
        self.username_Label.setText(_translate("MainWindow", "username:"))
        self.password_Label.setText(_translate("MainWindow", "password:"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/photo/loginImg.jpg\"/></p></body></html>"))

    def loginButton(self):
            print('ok')
            sql = "SELECT Employee_ID id FROM employee WHERE Employee_Username = %s AND Employee_Password = %s"
            val = (self.usernameTextField.text(),self.passwordTextField.text())
            cursor.execute(sql,val)

            result =cursor.fetchone()
            print(result)

            if result:
                global currentUser, goMainPage
                result = list(result)
                currentUser = result[0]
                print(currentUser, "dekdoekdoed")
                goMainPage = 1
                print('goMainpage',goMainPage)
                print('complete')
                mainPagePage.fetchData() 
                widget.setCurrentWidget(mainPagePage)
            else:
                information = qtw.QMessageBox()
                information.setWindowTitle("Information")
                information.setText("Incorrect password or username")
                information.setIcon(qtw.QMessageBox.Information)
                information.setStandardButtons(qtw.QMessageBox.Ok)
                information.setDefaultButton(qtw.QMessageBox.Ok)
                response = information.exec_()
                print("try again")
        
class mainPage(QtWidgets.QMainWindow):
    def __init__(self):
        global goMainPage

        super().__init__()
        
        self.setupUi(self)
        print('gomainnpage', goMainPage)

        
        print('gomainnpage', goMainPage)
    def fetchData(self):
        global currentUser, currentUserPos

        self.createQuotationButton.setVisible(True)
        self.createBillButton.setVisible(True)
        self.createDeliveryOrderButton.setVisible(True)
        self.createReceiptButton.setVisible(True)
        self.stockButton.setVisible(True)
        self.createOrderButton.setVisible(True)
        self.deliveryButton.setVisible(True)

        print('sdfsfsdfsdfsd')
        self.queueListGet = []

        self.orderTableWidget.cellClicked.connect(self.clickedQueueTable)

        sq = "SELECT Employee_Name,  Employee_Nickname, Employee_Position FROM Employee WHERE Employee_ID = %s"
        val = (str(currentUser),)
        print(val)
        print(val,sq)
        cursor.execute(sq,val)
        employeeToList = []
        self.employeeGet = list(cursor.fetchone())
        for i in self.employeeGet :
            employeeToList.append(i)
        print('helllo', employeeToList, currentUser)
        self.userLabel.setText(employeeToList[0])
        self.roleLabel.setText(employeeToList[2])
        
         
        currentUserPos = employeeToList[2]

        if employeeToList[2] == 'Sales':
            self.createBillButton.setVisible(False)
            self.createDeliveryOrderButton.setVisible(False)
            self.createReceiptButton.setVisible(False)
            self.stockButton.setVisible(False)
            self.createOrderButton.setVisible(False)
            self.deliveryButton.setVisible(False)
        elif employeeToList[2] == 'Staff':
            self.createQuotationButton.setVisible(False)
        self.userList = cursor.fetchall()

        sq = "SELECT Queue_ID, Queue_Status FROM queue_order WHERE Queue_Status != 'Finished' AND Queue_Status != 'Decline Order'"        
        cursor.execute(sq)

        self.queueList = cursor.fetchall()
        self.updateQueueTable()
        print()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1201, 81))
        self.label.setStyleSheet("background-color: #1d97b5;\n"
"color: #ffffff;\n"
"font: 20pt \"Arial\";")
        self.label.setObjectName("label")
        self.orderTableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.orderTableWidget.setGeometry(QtCore.QRect(0, 80, 921, 601))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.orderTableWidget.setFont(font)
        self.orderTableWidget.setObjectName("orderTableWidget")
        self.orderTableWidget.setColumnCount(2)
        self.orderTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.orderTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.orderTableWidget.setHorizontalHeaderItem(1, item)
        self.createBillButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.goToCreateBill())
        self.createBillButton.setGeometry(QtCore.QRect(970, 360, 191, 41))
        self.createBillButton.setObjectName("createBillButton")
        self.orderHistoryButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.goToFinishedOrder())
        self.orderHistoryButton.setGeometry(QtCore.QRect(970, 110, 91, 41))
        self.orderHistoryButton.setObjectName("finishedOrderButton")
        self.declineOrderButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.goToDeclineOrder())
        self.declineOrderButton.setGeometry(QtCore.QRect(1070, 110, 91, 41))
        self.declineOrderButton.setObjectName("finishedOrderButton")
        self.logoutButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda:self.logout())
        self.logoutButton.setGeometry(QtCore.QRect(1110, 610, 75, 31))
        self.logoutButton.setObjectName("logoutButton")
        self.createDeliveryOrderButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.goToDeliveryNote())
        self.createDeliveryOrderButton.setGeometry(QtCore.QRect(970, 300, 191, 41))
        self.createDeliveryOrderButton.setObjectName("delivery")
        self.createOrderButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.goToCreateOrder())
        self.createOrderButton.setGeometry(QtCore.QRect(970, 240, 191, 41))
        self.createOrderButton.setObjectName("createOrderButton")
        self.createQuotationButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda:self.goToQuotationCreate())
        self.createQuotationButton.setGeometry(QtCore.QRect(970, 170, 191, 41))
        self.createQuotationButton.setObjectName("createQuotationButton")
        self.createReceiptButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.goToCreateReceipt())
        self.createReceiptButton.setGeometry(QtCore.QRect(970, 420, 191, 41))
        self.createReceiptButton.setObjectName("createReceiptButton")
        self.stockButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.goToStock())
        self.stockButton.setGeometry(QtCore.QRect(970, 480, 191, 41))
        self.stockButton.setObjectName("stockButton")
        self.profileiconLabel = QtWidgets.QLabel(self.centralwidget)
        self.profileiconLabel.setGeometry(QtCore.QRect(950, 10, 51, 51))
        self.profileiconLabel.setText("")
        self.profileiconLabel.setPixmap(QtGui.QPixmap("../Users/ASUS/Downloads/profileimages.png"))
        self.profileiconLabel.setScaledContents(True)
        self.profileiconLabel.setObjectName("profileiconLabel")
        self.userLabel = QtWidgets.QLabel(self.centralwidget)
        self.userLabel.setGeometry(QtCore.QRect(1010, 10, 181, 31))
        self.userLabel.setStyleSheet("color: #ffffff;")
        self.userLabel.setScaledContents(False)
        self.userLabel.setObjectName("userLabel")
        self.roleLabel = QtWidgets.QLabel(self.centralwidget)
        self.roleLabel.setGeometry(QtCore.QRect(1010, 40, 131, 31))
        self.roleLabel.setStyleSheet("color: #febb4c;")
        self.roleLabel.setScaledContents(False)
        self.roleLabel.setObjectName("roleLabel")
        self.goButton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda:self.goToQueueDetail())
        self.goButton.setGeometry(QtCore.QRect(940, 620, 75, 23))
        self.goButton.setObjectName("goButton")
        self.searchDocButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda:self.goToSearchDoc())
        self.searchDocButton.setGeometry(QtCore.QRect(970, 540, 191, 41))
        self.searchDocButton.setObjectName("searchDocButton")
        self.deliveryButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda:self.goToDelivery())
        self.deliveryButton.setGeometry(QtCore.QRect(1030, 620, 75, 23))
        self.deliveryButton.setObjectName("deliveryButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 21))
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
        self.label.setText(_translate("MainWindow", "Order queue"))
        item = self.orderTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Queue_ID"))
        item = self.orderTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Status"))
        self.createBillButton.setText(_translate("MainWindow", "Create Bill"))
        self.orderHistoryButton.setText(_translate("MainWindow", "Finished Order"))
        self.declineOrderButton.setText(_translate("MainWindow", "Declined Order"))
        self.createDeliveryOrderButton.setText(_translate("MainWindow", "Create Delivery Note/Tax Invoice"))
        self.createOrderButton.setText(_translate("MainWindow", "Create Order"))
        self.createQuotationButton.setText(_translate("MainWindow", "Create Quotation"))
        self.createReceiptButton.setText(_translate("MainWindow", "Create receipt"))
        self.stockButton.setText(_translate("MainWindow", "Stock"))
        self.userLabel.setText(_translate("MainWindow", "Achira Wisatechaiyakorn"))
        self.roleLabel.setText(_translate("MainWindow", "Manager"))
        self.goButton.setText(_translate("MainWindow", "Go"))
        self.searchDocButton.setText(_translate("MainWindow", "Search Document"))
        self.deliveryButton.setText(_translate("MainWindow", "Delivery"))
        self.logoutButton.setText(_translate("MainWindow", "Logout"))

    def updateQueueTable(self):
        self.orderTableWidget.setRowCount(len(self.queueList))
        for row, item in enumerate(self.queueList):
            table_item = qtw.QTableWidgetItem(item[0])
            table_item.setFlags(table_item.flags() & ~Qt.ItemIsEditable) 
            self.orderTableWidget.setItem(row, 0, table_item)

            table_item = qtw.QTableWidgetItem(item[1])
            table_item.setFlags(table_item.flags() & ~Qt.ItemIsEditable) 
            self.orderTableWidget.setItem(row, 1, table_item)

    def clickedQueueTable(self,row,col):
        row_data = []
        for col in range(self.orderTableWidget.columnCount()):
            item = self.orderTableWidget.item(row, col)
            if item:
                row_data.append(item.text())
        
        self.queueListGet = row_data
        print(f'Row {row} data: {row_data}')

    def goToQueueDetail(self):
        if self.queueListGet:
            global currentQueueID
            print(self.queueListGet)
            currentQueueID = self.queueListGet[0]
            orderDetailPage.fetchData()
            widget.setCurrentWidget(orderDetailPage)
        
    def goToCreateOrder(self):
        createOrderPage.fetchData()
        widget.setCurrentWidget(createOrderPage)

    def goToSearchDoc(self):
        documentSearchPage.fetchData()
        widget.setCurrentWidget(documentSearchPage)

    def goToQuotationCreate(self):
        print('ok')
        createQuotationPage.fetchData()
        widget.setCurrentWidget(createQuotationPage)
    def goToDelivery(self):
        deliverPagePage.fetchData()
        widget.setCurrentWidget(deliverPagePage)
    def goToStock(self):
        stockPagePage.fetchData()
        widget.setCurrentWidget(stockPagePage)
    def goToFinishedOrder(self):
        finishOrderPage.fetchData()
        widget.setCurrentWidget(finishOrderPage)
    def goToDeclineOrder(self):
        declineOrderPage.fetchData()
        widget.setCurrentWidget(declineOrderPage)
    def goToCreateBill(self):
        createBillPage.fetchData()
        widget.setCurrentWidget(createBillPage)
        print('hello')
    def goToCreateReceipt(self):
        createReceiptPage.fetchData()
        widget.setCurrentWidget(createReceiptPage)
        print('hello')
    def goToDeliveryNote(self):
        createTaxInvoicePage.fetchData()
        widget.setCurrentWidget(createTaxInvoicePage)
    def logout(self):
        global currentUser, loginStatus
        currentUser = 0
        loginStatus = 0
        widget.setCurrentWidget(loginPage)


class createQuotation(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        print("createquooooo")
        
    def fetchData(self):
        self.ErrorLabelNotfound.setText("")
        thailand_provinces = [
        "Amnat Charoen", "Ang Thong", "Bangkok", "Bueng Kan", "Buriram", "Chachoengsao", 
        "Chai Nat", "Chaiyaphum", "Chanthaburi", "Chiang Mai", "Chiang Rai", "Chonburi", 
        "Chumphon", "Kalasin", "Kamphaeng Phet", "Kanchanaburi", "Khon Kaen", "Krabi", 
        "Lampang", "Lamphun", "Loei", "Lopburi", "Mae Hong Son", "Maha Sarakham", 
        "Mukdahan", "Nakhon Nayok", "Nakhon Pathom", "Nakhon Phanom", "Nakhon Ratchasima", 
        "Nakhon Sawan", "Nakhon Si Thammarat", "Nan", "Narathiwat", "Nong Bua Lam Phu", 
        "Nong Khai", "Nonthaburi", "Pathum Thani", "Pattani", "Phang Nga", "Phatthalung", 
        "Phayao", "Phetchabun", "Phetchaburi", "Phichit", "Phitsanulok", "Phra Nakhon Si Ayutthaya", 
        "Phrae", "Phuket", "Prachinburi", "Prachuap Khiri Khan", "Ranong", "Ratchaburi", 
        "Rayong", "Roi Et", "Sa Kaeo", "Sakon Nakhon", "Samut Prakan", "Samut Sakhon", 
        "Samut Songkhram", "Saraburi", "Satun", "Sing Buri", "Si Sa Ket", "Songkhla", 
        "Sukhothai", "Suphan Buri", "Surat Thani", "Surin", "Tak", "Trang", 
        "Trat", "Ubon Ratchathani", "Udon Thani", "Uthai Thani", "Uttaradit", "Yala", 
        "Yasothon"
        ]
        
        self.CompanyProvinceLineEdit.addItems(thailand_provinces)
        self.flagField = [0,0]
        self.NameLabel.setVisible(False)
        self.NameLineEdit.setVisible(False)
        self.AddressLabel.setVisible(False)
        self.AddressLineEdit.setVisible(False)
        self.PhoneNumberLabel.setVisible(False)
        self.PhoneNumberLineEdit.setVisible(False)
        self.FaxLabel.setVisible(False)
        self.FaxLineEdit.setVisible(False)
        self.TaxIDNumberLabel.setVisible(False)
        self.TaxIdNumberLineEdit.setVisible(False)
        self.CompanyNameLabel.setVisible(False)
        self.CompanyNameLineEdit.setVisible(False)
        self.CompanyProvinceLabel.setVisible(False)
        self.CompanyProvinceLineEdit.setVisible(False)
        self.CompanyBranchLabel.setVisible(False)
        self.CompanyBranchLineEdit.setVisible(False)
        self.TableCustomerName.cellClicked.connect(self.clickedCustomerTable)

        self.flag = 3
        self.producrListRemoved = []
        self.productList = []
        self.customerList = []
        self.productListGet = []
        self.customerListGet = []
        sq = "SELECT Employee_id, Employee_Name FROM Employee WHERE Employee_Position = 'Sales'"
        cursor.execute(sq)
        self.EmployeeName = cursor.fetchall()
        print(self.EmployeeName)

        sq = "SELECT Product_ID, Product_Name, Product_Price, Product_Quantity FROM product"
        cursor.execute(sq)

        self.productList = cursor.fetchall()
        print('--> ',self.EmployeeName)
        for employee in self.EmployeeName:
                self.SalesCombobox.addItem(employee[1], employee[0])
        self.updateProductBox()
    def updateProductBox(self):
        for id, name, price, quantity in self.productList:
                self.productComboBox.addItem(name,(name, id, quantity, price))

        
    def setupUi(self,MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1192, 691)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.CreateAUotationHead = QtWidgets.QLabel(self.centralwidget)
        self.CreateAUotationHead.setGeometry(QtCore.QRect(20, 10, 101, 16))
        self.CreateAUotationHead.setObjectName("CreateAUotationHead")
        self.CustomernameLabel = QtWidgets.QLabel(self.centralwidget)
        self.CustomernameLabel.setGeometry(QtCore.QRect(10, 60, 101, 16))
        self.CustomernameLabel.setObjectName("CustomernameLabel")
        self.CustomernameEditSearch = QtWidgets.QLineEdit(self.centralwidget)
        self.CustomernameEditSearch.setGeometry(QtCore.QRect(110, 60, 131, 22))
        self.CustomernameEditSearch.setObjectName("CustomernameEditSearch")
        self.ButtonSearchCustomer = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.checkCustomerButton())
        self.ButtonSearchCustomer.setGeometry(QtCore.QRect(250, 60, 93, 21))
        self.ButtonSearchCustomer.setStyleSheet("QPushButton {\n"
"                background-color: #156d9c; \n"
"                color: white; \n"
"                padding: 15px;\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #2891ca;  /* Lighter green on hover */\n"
"            }")
        self.ButtonSearchCustomer.setObjectName("ButtonSearchCustomer")
        self.Searchresult = QtWidgets.QLabel(self.centralwidget)
        self.Searchresult.setGeometry(QtCore.QRect(120, 100, 81, 16))
        self.Searchresult.setObjectName("Searchresult")
        self.TableCustomerName = QtWidgets.QTableWidget(self.centralwidget)
        self.TableCustomerName.setGeometry(QtCore.QRect(20, 130, 401, 141))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.TableCustomerName.setFont(font)
        self.TableCustomerName.setObjectName("TableCustomerName")
        self.TableCustomerName.setColumnCount(2)
        self.TableCustomerName.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.TableCustomerName.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableCustomerName.setHorizontalHeaderItem(1, item)
        self.SalesLabel = QtWidgets.QLabel(self.centralwidget)
        self.SalesLabel.setGeometry(QtCore.QRect(30, 290, 31, 16))
        self.SalesLabel.setObjectName("SalesLabel")
        self.ProductLabel = QtWidgets.QLabel(self.centralwidget)
        self.ProductLabel.setGeometry(QtCore.QRect(30, 320, 51, 16))
        self.ProductLabel.setObjectName("ProductLabel")
        self.ProductQuantityLabel = QtWidgets.QLabel(self.centralwidget)
        self.ProductQuantityLabel.setGeometry(QtCore.QRect(30, 350, 55, 16))
        self.ProductQuantityLabel.setObjectName("ProductQuantityLabel")
        self.QuantitytochooseBox = QtWidgets.QSpinBox(self.centralwidget)
        self.QuantitytochooseBox.setGeometry(QtCore.QRect(90, 350, 44, 22))
        self.QuantitytochooseBox.setObjectName("QuantitytochooseBox")
        self.ChooseProductforCustomerTaBle = QtWidgets.QTableWidget(self.centralwidget)
        self.ChooseProductforCustomerTaBle.setGeometry(QtCore.QRect(30, 380, 391, 231))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.ChooseProductforCustomerTaBle.setFont(font)
        self.ChooseProductforCustomerTaBle.setObjectName("ChooseProductforCustomerTaBle")
        self.ChooseProductforCustomerTaBle.setColumnCount(3)
        self.ChooseProductforCustomerTaBle.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.ChooseProductforCustomerTaBle.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.ChooseProductforCustomerTaBle.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.ChooseProductforCustomerTaBle.setHorizontalHeaderItem(2, item)
        self.AddOrderButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.addItem())
        self.AddOrderButton.setGeometry(QtCore.QRect(320, 290, 91, 21))
        self.AddOrderButton.setStyleSheet("QPushButton {\n"
"                background-color: #156d9c; \n"
"                color: white; \n"
"                padding: 15px;\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #2891ca;  /* Lighter green on hover */\n"
"            }")
        self.AddOrderButton.setObjectName("AddOrderButton")
        self.DeletOrderButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.removeItem())
        self.DeletOrderButton.setGeometry(QtCore.QRect(320, 320, 111, 21))
        self.DeletOrderButton.setStyleSheet("QPushButton {\n"
"                background-color: #156d9c; \n"
"                color: white; \n"
"                padding: 15px;\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #2891ca;  /* Lighter green on hover */\n"
"            }")
        self.DeletOrderButton.setObjectName("DeletOrderButton")
        self.CompanyProvinceLabel = QtWidgets.QLabel(self.centralwidget)
        self.CompanyProvinceLabel.setGeometry(QtCore.QRect(740, 360, 201, 31))
        self.CompanyProvinceLabel.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.CompanyProvinceLabel.setObjectName("CompanyProvinceLabel")
        self.MustIncludeLAbel = QtWidgets.QLabel(self.centralwidget)
        self.MustIncludeLAbel.setGeometry(QtCore.QRect(990, 10, 171, 21))
        self.MustIncludeLAbel.setStyleSheet("QLabel {\n"
"    font: 14pt \"Arial\";\n"
"    font: 12pt \"MS Shell Dlg 2\";\n"
"    color: RED;              /* White text */\n"
"}")
        self.MustIncludeLAbel.setObjectName("MustIncludeLAbel")
        self.ErrorLabelNotfound = QtWidgets.QLabel(self.centralwidget)
        self.ErrorLabelNotfound.setGeometry(QtCore.QRect(260, 100, 181, 16))
        self.ErrorLabelNotfound.setStyleSheet("QLabel {\n"
"    color: RED;              /* White text */\n"
"}")
        self.ErrorLabelNotfound.setObjectName("ErrorLabelNotfound")
        self.CompanyProvinceLineEdit = QtWidgets.QComboBox(self.centralwidget)
        self.CompanyProvinceLineEdit.setGeometry(QtCore.QRect(740, 410, 171, 31))
        self.CompanyProvinceLineEdit.setObjectName("CompanyProvinceLineEdit")
        self.ApplyQuotationButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.checkAgain())
        self.ApplyQuotationButton.setGeometry(QtCore.QRect(950, 500, 171, 101))
        self.ApplyQuotationButton.setStyleSheet("QPushButton {\n"
"    font: 22pt \"Arial\";\n"
"                background-color: #156d9c; \n"
"                color: white; \n"
"                padding: 15px;\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #2891ca;  /* Lighter green on hover */\n"
"            }")
        self.ApplyQuotationButton.setObjectName("ApplyQuotationButton")
        self.CompanyNameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.CompanyNameLineEdit.setGeometry(QtCore.QRect(500, 410, 191, 31))
        self.CompanyNameLineEdit.setObjectName("CompanyNameLineEdit")
        self.CompanyNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.CompanyNameLabel.setGeometry(QtCore.QRect(500, 360, 201, 31))
        self.CompanyNameLabel.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.CompanyNameLabel.setObjectName("CompanyNameLabel")
        self.CompanyBranchLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.CompanyBranchLineEdit.setGeometry(QtCore.QRect(980, 410, 191, 31))
        self.CompanyBranchLineEdit.setObjectName("CompanyBranchLineEdit")
        self.CompanyBranchLabel = QtWidgets.QLabel(self.centralwidget)
        self.CompanyBranchLabel.setGeometry(QtCore.QRect(990, 360, 201, 31))
        self.CompanyBranchLabel.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.CompanyBranchLabel.setObjectName("CompanyBranchLabel")
        self.FaxLabel = QtWidgets.QLabel(self.centralwidget)
        self.FaxLabel.setGeometry(QtCore.QRect(810, 210, 41, 31))
        self.FaxLabel.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.FaxLabel.setObjectName("FaxLabel")
        self.FaxLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.FaxLineEdit.setGeometry(QtCore.QRect(740, 260, 191, 31))
        self.FaxLineEdit.setObjectName("FaxLineEdit")
        self.PhoneNumberLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.PhoneNumberLineEdit.setGeometry(QtCore.QRect(500, 260, 191, 31))
        self.PhoneNumberLineEdit.setObjectName("PhoneNumberLineEdit")
        self.TaxIdNumberLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.TaxIdNumberLineEdit.setGeometry(QtCore.QRect(980, 260, 191, 31))
        self.TaxIdNumberLineEdit.setObjectName("TaxIdNumberLineEdit")
        self.TaxIDNumberLabel = QtWidgets.QLabel(self.centralwidget)
        self.TaxIDNumberLabel.setGeometry(QtCore.QRect(1000, 210, 161, 31))
        self.TaxIDNumberLabel.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.TaxIDNumberLabel.setObjectName("TaxIDNumberLabel")
        self.PhoneNumberLabel = QtWidgets.QLabel(self.centralwidget)
        self.PhoneNumberLabel.setGeometry(QtCore.QRect(510, 210, 201, 31))
        self.PhoneNumberLabel.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.PhoneNumberLabel.setObjectName("PhoneNumberLabel")
        self.AddressLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.AddressLineEdit.setGeometry(QtCore.QRect(860, 140, 191, 31))
        self.AddressLineEdit.setObjectName("AddressLineEdit")
        self.NameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.NameLineEdit.setGeometry(QtCore.QRect(590, 140, 191, 31))
        self.NameLineEdit.setObjectName("NameLineEdit")
        self.NameLabel = QtWidgets.QLabel(self.centralwidget)
        self.NameLabel.setGeometry(QtCore.QRect(660, 100, 71, 31))
        self.NameLabel.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.NameLabel.setObjectName("NameLabel")
        self.AddressLabel = QtWidgets.QLabel(self.centralwidget)
        self.AddressLabel.setGeometry(QtCore.QRect(910, 100, 91, 31))
        self.AddressLabel.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.AddressLabel.setObjectName("AddressLabel")
        self.SalesCombobox = QtWidgets.QComboBox(self.centralwidget)
        self.SalesCombobox.setGeometry(QtCore.QRect(80, 290, 221, 22))
        self.SalesCombobox.setObjectName("SalesCombobox")
        self.productComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.productComboBox.setGeometry(QtCore.QRect(80, 320, 221, 22))
        self.productComboBox.setObjectName("productComboBox")
        self.backButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.goToHome())
        self.backButton.setGeometry(QtCore.QRect(700, 540, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.backButton.setFont(font)
        self.backButton.setObjectName("backButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1192, 31))
        self.menubar.setObjectName("menubar")
        self.menuCreate_Quotation = QtWidgets.QMenu(self.menubar)
        self.menuCreate_Quotation.setObjectName("menuCreate_Quotation")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuCreate_Quotation.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        

    def retranslateUi(self,MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.CreateAUotationHead.setText(_translate("MainWindow", "Create Quotation"))
        self.CustomernameLabel.setText(_translate("MainWindow", "Customer Name"))
        self.ButtonSearchCustomer.setText(_translate("MainWindow", "Search"))
        self.Searchresult.setText(_translate("MainWindow", "Search Result"))
        item = self.TableCustomerName.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Customer ID"))
        item = self.TableCustomerName.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Customer Name"))
        self.SalesLabel.setText(_translate("MainWindow", "Sales"))
        self.ProductLabel.setText(_translate("MainWindow", "Product"))
        self.ProductQuantityLabel.setText(_translate("MainWindow", "Quantity"))
        item = self.ChooseProductforCustomerTaBle.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Product"))
        item = self.ChooseProductforCustomerTaBle.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Quantity"))
        item = self.ChooseProductforCustomerTaBle.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Price"))
        self.AddOrderButton.setText(_translate("MainWindow", "Add Order"))
        self.DeletOrderButton.setText(_translate("MainWindow", "Delete Order"))
        self.CompanyProvinceLabel.setText(_translate("MainWindow", "Company Province*"))
        self.MustIncludeLAbel.setText(_translate("MainWindow", "* Must Include"))
        self.ErrorLabelNotfound.setText(_translate("MainWindow", "Not found Please Create New"))
        self.ApplyQuotationButton.setText(_translate("MainWindow", "Apply"))
        self.CompanyNameLabel.setText(_translate("MainWindow", "Company Name*"))
        self.CompanyBranchLabel.setText(_translate("MainWindow", "Company Branch"))
        self.FaxLabel.setText(_translate("MainWindow", "Fax"))
        self.TaxIDNumberLabel.setText(_translate("MainWindow", "Tax ID Number"))
        self.PhoneNumberLabel.setText(_translate("MainWindow", "Phone Number*"))
        self.NameLabel.setText(_translate("MainWindow", "Name*"))
        self.AddressLabel.setText(_translate("MainWindow", "Address*"))
        self.backButton.setText(_translate("MainWindow", "Back"))
        self.menuCreate_Quotation.setTitle(_translate("MainWindow", "Create Quotation"))
    def checkCustomerButton(self):
        self.ChooseProductforCustomerTaBle.setRowCount(0)
        customerNameToSearch = self.CustomernameEditSearch.text()
        if self.CustomernameEditSearch.text() != '':
            sql = 'SELECT Customer_ID, Customer_Name FROM customer WHERE Customer_Name LIKE %s'
            val = ('%' + customerNameToSearch + '%',)
            cursor.execute(sql,val)
            self.customerList = list(cursor.fetchall())
            print(self.customerList)
            if self.customerList:
                self.ChooseProductforCustomerTaBle.setRowCount(0)
                self.NameLabel.setVisible(False)
                self.NameLineEdit.setVisible(False)
                self.AddressLabel.setVisible(False)
                self.AddressLineEdit.setVisible(False)
                self.PhoneNumberLabel.setVisible(False)
                self.PhoneNumberLineEdit.setVisible(False)
                self.FaxLabel.setVisible(False)
                self.FaxLineEdit.setVisible(False)
                self.TaxIDNumberLabel.setVisible(False)
                self.TaxIdNumberLineEdit.setVisible(False)
                self.CompanyNameLabel.setVisible(False)
                self.CompanyNameLineEdit.setVisible(False)
                self.CompanyProvinceLabel.setVisible(False)
                self.CompanyProvinceLineEdit.setVisible(False)
                self.CompanyBranchLabel.setVisible(False)
                self.CompanyBranchLineEdit.setVisible(False)
                self.ErrorLabelNotfound.setText('found it')
                self.flag = 0
                self.updateCustomerTable()
            else: 
                self.customerList = []
                print("thisthis")
                self.TableCustomerName.setRowCount(0)
                self.ErrorLabelNotfound.setText('not found create new')
                self.NameLabel.setVisible(True)
                self.NameLineEdit.setVisible(True)
                self.AddressLabel.setVisible(True)
                self.AddressLineEdit.setVisible(True)
                self.PhoneNumberLabel.setVisible(True)
                self.PhoneNumberLineEdit.setVisible(True)
                self.FaxLabel.setVisible(True)
                self.FaxLineEdit.setVisible(True)
                self.TaxIDNumberLabel.setVisible(True)
                self.TaxIdNumberLineEdit.setVisible(True)
                self.CompanyNameLabel.setVisible(True)
                self.CompanyNameLineEdit.setVisible(True)
                self.CompanyProvinceLabel.setVisible(True)
                self.CompanyProvinceLineEdit.setVisible(True)
                self.CompanyBranchLabel.setVisible(True)
                self.CompanyBranchLineEdit.setVisible(True)
                self.flag = 1
        else:
            self.ErrorLabelNotfound.setText('not found create new')
            self.NameLabel.setVisible(True)
            self.NameLineEdit.setVisible(True)
            self.AddressLabel.setVisible(True)
            self.AddressLineEdit.setVisible(True)
            self.PhoneNumberLabel.setVisible(True)
            self.PhoneNumberLineEdit.setVisible(True)
            self.FaxLabel.setVisible(True)
            self.FaxLineEdit.setVisible(True)
            self.TaxIDNumberLabel.setVisible(True)
            self.TaxIdNumberLineEdit.setVisible(True)
            self.CompanyNameLabel.setVisible(True)
            self.CompanyNameLineEdit.setVisible(True)
            self.CompanyProvinceLabel.setVisible(True)
            self.CompanyProvinceLineEdit.setVisible(True)
            self.CompanyBranchLabel.setVisible(True)
            self.CompanyBranchLineEdit.setVisible(True)
            self.flag = 1


    def updateCustomerTable(self):

        self.TableCustomerName.setRowCount(len(self.customerList))
        for row, item in enumerate(self.customerList):
                table_item = qtw.QTableWidgetItem(item[0])
                table_item.setFlags(table_item.flags() & ~Qt.ItemIsEditable)  
                self.TableCustomerName.setItem(row, 0, table_item)

                table_item = qtw.QTableWidgetItem(item[1])
                table_item.setFlags(table_item.flags() & ~Qt.ItemIsEditable)  
                self.TableCustomerName.setItem(row, 1, table_item)

    def clickedCustomerTable(self,row, col): 
        row_data = []
        for col in range(self.TableCustomerName.columnCount()):
                item = self.TableCustomerName.item(row, col)
                if item:
                    row_data.append(item.text())
        
        self.customerListGet = row_data
        print(f'Row {row} data: {row_data}')
        self.flagField[0] = 1
    def updateProductTable(self):
        self.ChooseProductforCustomerTaBle.setRowCount(len(self.productListGet))
        print(self.productListGet)
        for row, item in enumerate(self.productListGet):
                print(item[0])
                table_item = qtw.QTableWidgetItem(item[0])
                table_item.setFlags(table_item.flags() & ~Qt.ItemIsEditable)  
                self.ChooseProductforCustomerTaBle.setItem(row, 0, table_item)
                print(item[2])

                table_item = qtw.QTableWidgetItem(str(item[2]))
                table_item.setFlags(table_item.flags() & ~Qt.ItemIsEditable)  
                self.ChooseProductforCustomerTaBle.setItem(row, 1, table_item)
                print(item[3])

                table_item = qtw.QTableWidgetItem(str(item[3]))
                table_item.setFlags(table_item.flags() & ~Qt.ItemIsEditable)  
                self.ChooseProductforCustomerTaBle.setItem(row, 2, table_item)
    
    def addItem(self):
        selectedData = self.productComboBox.currentData()
        self.quantityRefer = 0
        print(selectedData,'okokok')
        if selectedData:
            selectedData = list(selectedData)  
            if self.QuantitytochooseBox.value() > 0:
                self.quantityRefer = selectedData[2]
                selectedData[2] = self.QuantitytochooseBox.value() 
                print(selectedData)
                self.productListGet.append(selectedData)  
            
                index = self.productComboBox.currentIndex()
                self.productComboBox.removeItem(index) 
    
            self.updateProductTable()
    def removeItem(self):
        if self.productListGet:
            removedItem = self.productListGet.pop()

            print(removedItem)
            removedItem[2] = self.quantityRefer
            print(self.productListGet)
            print(tuple(removedItem))
        
            self.productComboBox.addItem(removedItem[0], tuple(removedItem))  

            self.updateProductTable()

    def checkAgain(self):
        applyPopUp = qtw.QMessageBox()
        applyPopUp.setWindowTitle("Apply")
        applyPopUp.setText("Are you really want to add?")
        applyPopUp.setIcon(qtw.QMessageBox.Question)
        applyPopUp.setStandardButtons(qtw.QMessageBox.Ok|qtw.QMessageBox.Cancel)
        applyPopUp.setDefaultButton(qtw.QMessageBox.Cancel)

        response = applyPopUp.exec_()

        if response == qtw.QMessageBox.Ok:
            print("Ok clicked")
            self.applyButton()

    def applyButton(self):
        if self.ChooseProductforCustomerTaBle.rowCount() and self.AddressLineEdit.text() and self.CompanyProvinceLineEdit.currentText() and self.CompanyNameLineEdit.text() and self.PhoneNumberLineEdit.text() and self.NameLineEdit.text() and self.CompanyBranchLineEdit.text() and self.flag :
            sq = 'SELECT COUNT(*) FROM quotation'
            cursor.execute(sq)
            final_result = [i[0] for i in cursor.fetchall()]
            self.idToInsert = "Q"+str(final_result[0]+1)
            print(self.idToInsert)
            self.sumPrice = 0
            for i in self.productListGet:
                    self.sumPrice += i[2]*i[3]
            self.sumPriceVat = float(self.sumPrice)*0.07
            self.sumPriceWithVat = float(self.sumPrice)+ float(self.sumPriceVat)

            self.current_dateTime = datetime.today().strftime('%Y-%m-%d')

            if self.flag == 1:
                  sq = "SELECT COUNT(*) FROM customer"
                  cursor.execute(sq)

                  final_result = [i[0] for i in cursor.fetchall()]
                  CusID = 'CUS'+str(final_result[0] +1)
                  print(CusID)
                  print(self.idToInsert, self.AddressLineEdit.text(),self.CompanyProvinceLineEdit.currentText(),self.CompanyNameLineEdit.text() ,self.PhoneNumberLineEdit.text(),self.FaxLineEdit.text(),self.TaxIdNumberLineEdit.text(),self.NameLineEdit.text(),self.CompanyBranchLineEdit.text())
                  sq = "INSERT INTO customer (Customer_ID, Customer_Address, Customer_Company_Province, Customer_Company_Name, Customer_Phone_Number, Customer_Fax, Customer_Tax_ID_Number, Customer_Name, Customer_Company_Branch) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                  val = (CusID, self.AddressLineEdit.text(),self.CompanyProvinceLineEdit.currentText(),self.CompanyNameLineEdit.text() ,self.PhoneNumberLineEdit.text(),self.FaxLineEdit.text(),self.TaxIdNumberLineEdit.text(),self.NameLineEdit.text(),self.CompanyBranchLineEdit.text())

                  cursor.execute(sq,val)
            else:
                  CusID = self.customerListGet[0]

            employeeIdGet = list(self.SalesCombobox.currentData())
            print("print -->",employeeIdGet[0])
            print(self.idToInsert, CusID, employeeIdGet[0],self.current_dateTime, self.SalesCombobox.currentText(), self.sumPrice, self.sumPriceWithVat, self.sumPriceVat)
            sq = "INSERT INTO quotation (Quotation_ID, Customer_ID, Employee_ID, Quotation_Date, Quotation_Sale_Person, Quotation_Total_Price, Quotation_Total_Price_And_VAT, Quotation_VAT) VALUES (%s, %s , %s ,%s , %s , %s , %s , %s )"
            val = (str(self.idToInsert), str(CusID), str(employeeIdGet[0]),self.current_dateTime, self.SalesCombobox.currentText(), self.sumPrice, self.sumPriceWithVat, self.sumPriceVat) 
            cursor.execute(sq,val)

            count =1
            for i in self.productListGet:
                    print(i)
                    sq = "INSERT INTO quotation_detail (Quotation_ID, Quotation_Detail_ID, Product_ID, Quotation_Detail_Product_Quantity, Quotation_Detail_Price_per_product,Product_Name) VALUES (%s,%s,%s,%s,%s,%s)"
                    val = (str(self.idToInsert), str(self.idToInsert)+'QD'+str(count), str(i[1]), int(i[2]), float(i[3]), str(i[0]))
                    cursor.execute(sq,val)
                    count +=1
            mydb.commit()


            information = qtw.QMessageBox()
            information.setWindowTitle("Information")
            information.setText("Added")
            information.setIcon(qtw.QMessageBox.Information)
            information.setStandardButtons(qtw.QMessageBox.Ok)
            information.setDefaultButton(qtw.QMessageBox.Ok)

            response = information.exec_()

            if response == qtw.QMessageBox.Ok:
                self.TableCustomerName.setRowCount(0)

                self.goToHome()
        elif self.flagField[0] and self.ChooseProductforCustomerTaBle.rowCount() and self.flag == 0:
            print('drdrdrdfvfbdgfbdfgrd')
            sq = 'SELECT COUNT(*) FROM quotation'
            cursor.execute(sq)
            final_result = [i[0] for i in cursor.fetchall()]
            self.idToInsert = 'Q'+str(final_result[0]+1)
            print(self.idToInsert)
            self.sumPrice = 0
            for i in self.productListGet:
                    self.sumPrice += i[2]*i[3]
            self.sumPriceVat = float(self.sumPrice)*0.07
            self.sumPriceWithVat = float(self.sumPrice) + float(self.sumPriceVat)

            self.current_dateTime = datetime.today().strftime('%Y-%m-%d')

            if self.flag == 1:
                  sq = "SELECT COUNT(*) FROM customer"
                  cursor.execute(sq)

                  final_result = [i[0] for i in cursor.fetchall()]
                  CusID = 'CUS'+str(final_result[0] +1)
                  print(CusID)
                  print(self.idToInsert, self.AddressLineEdit.text(),self.CompanyProvinceLineEdit.currentText(),self.CompanyNameLineEdit.text() ,self.PhoneNumberLineEdit.text(),self.FaxLineEdit.text(),self.TaxIdNumberLineEdit.text(),self.NameLineEdit.text(),self.CompanyBranchLineEdit.text())
                  sq = "INSERT INTO customer (Customer_ID, Customer_Address, Customer_Company_Province, Customer_Company_Name, Customer_Phone_Number, Customer_Fax, Customer_Tax_ID_Number, Customer_Name, Customer_Company_Branch) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                  val = (CusID, self.AddressLineEdit.text(),self.CompanyProvinceLineEdit.currentText(),self.CompanyNameLineEdit.text() ,self.PhoneNumberLineEdit.text(),self.FaxLineEdit.text(),self.TaxIdNumberLineEdit.text(),self.NameLineEdit.text(),self.CompanyBranchLineEdit.text())

                  cursor.execute(sq,val)
            else:
                  CusID = self.customerListGet[0]

            employeeIdGet = list(self.SalesCombobox.currentData())
            print("print -->",employeeIdGet[0])
            print(self.idToInsert, CusID, employeeIdGet[0],self.current_dateTime, self.SalesCombobox.currentText(), self.sumPrice, self.sumPriceWithVat, self.sumPriceVat)
            sq = "INSERT INTO quotation (Quotation_ID, Customer_ID, Employee_ID, Quotation_Date, Quotation_Sale_Person, Quotation_Total_Price, Quotation_Total_Price_And_VAT, Quotation_VAT) VALUES (%s, %s , %s ,%s , %s , %s , %s , %s )"
            val = (str(self.idToInsert), str(CusID), str(employeeIdGet[0]),self.current_dateTime, self.SalesCombobox.currentText(), self.sumPrice, self.sumPriceWithVat, self.sumPriceVat) 
            cursor.execute(sq,val)

            count =1
            for i in self.productListGet:
                    print(i)
                    sq = "INSERT INTO quotation_detail (Quotation_ID, Quotation_Detail_ID, Product_ID, Quotation_Detail_Product_Quantity, Quotation_Detail_Price_per_product, Product_Name) VALUES (%s,%s,%s,%s,%s,%s)"
                    val = (str(self.idToInsert), str(self.idToInsert)+'QD'+str(count), str(i[1]), int(i[2]), float(i[3]), str(i[0]))
                    cursor.execute(sq,val)
                    count +=1
            mydb.commit()


            information = qtw.QMessageBox()
            information.setWindowTitle("Information")
            information.setText("Added")
            information.setIcon(qtw.QMessageBox.Information)
            information.setStandardButtons(qtw.QMessageBox.Ok)
            information.setDefaultButton(qtw.QMessageBox.Ok)

            response = information.exec_()

            if response == qtw.QMessageBox.Ok:
                self.TableCustomerName.setRowCount(0)

                self.goToHome()
        else:
            print('drdrdrdrd')
            information = qtw.QMessageBox()
            information.setWindowTitle("Information")
            information.setText("Please fill all field")
            information.setIcon(qtw.QMessageBox.Information)
            information.setStandardButtons(qtw.QMessageBox.Ok)
            information.setDefaultButton(qtw.QMessageBox.Ok)

            response = information.exec_()
    def goToHome(self):
        self.ChooseProductforCustomerTaBle.setRowCount(0)
        self.TableCustomerName.setRowCount(0)
        self.ErrorLabelNotfound.setText("")
        self.CompanyProvinceLineEdit.clear()
        self.SalesCombobox.clear()
        self.productComboBox.clear()
        widget.setCurrentWidget(mainPagePage)
class orderDetail(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    def fetchData(self):
        global currentQueueID, currentUserPos
        sq = "SELECT Queue_ID, PO_Document_Id, Queue_Status FROM queue_order WHERE Queue_ID = %s"
        val = (currentQueueID,)
        cursor.execute(sq,val)

        self.queueList = list(cursor.fetchone())

        self.changeStatusButton_2.setVisible(False)
        self.changeStatusButton_3.setVisible(False)

        
        if(currentUserPos == 'Manager'):
            sq = "SELECT Queue_ID, PO_Document_Id, Queue_Status FROM queue_order WHERE Queue_ID = %s AND Queue_Status = 'Waiting For Accept Order'"
            val = (currentQueueID,)
            cursor.execute(sq,val)

            if(cursor.fetchone()):
                self.changeStatusButton_3.setVisible(True)
                self.changeStatusButton_2.setVisible(True)
        self.qIDLabel.setText(self.queueList[0])
        self.poIDLabel.setText(self.queueList[1])
        self.statusLabel.setText(self.queueList[2])

        self.statusLineEdit.addItems(["During Producing",
        'producing finished', 'Send to Customer', 'Customer come to recieve',
        'Rent, Customer send','Rent, Receive from Customer Place',
         'Rent, Update to Storage', 'Finished'])


        self.statusLineEdit.setVisible(True)
        self.changeStatusButton.setVisible(True)
        
        sq = "SELECT Queue_ID, PO_Document_Id, Queue_Status FROM queue_order WHERE Queue_ID = %s AND (Queue_Status = 'Waiting For Accept Order' OR Queue_Status = 'Decline Order')"
        val = (currentQueueID,)
        cursor.execute(sq,val)
        
        if(cursor.fetchone()):
            print('dkdkdkdkdkdkdkddkdkddkdk')
            self.statusLineEdit.setVisible(False)
            self.changeStatusButton.setVisible(False)


        sq = "SELECT PO_Total_Price, PO_Vat, PO_Total_Price_VAT, Quotation_ID, PO_Discount FROM purchase_order WHERE PO_Document_ID = %s"
        val = (self.queueList[1],)
        cursor.execute(sq,val)

        self.poList = list(cursor.fetchone())
        print(self.poList)

        print(self.queueList[1],'fiifheifhiehiehifheifhiefhiheihihi')
        sq = "SELECT PO_Detail_Product_ID, PO_Detail_Product, PO_Detail_Detail_Product_Quantity, PO_Detail_Price_per_product FROM purchase_order_detail WHERE PO_Document_ID = %s"
        val = (self.queueList[1],)
        cursor.execute(sq,val)

        rows = cursor.fetchall()

        self.productList = [list(row) for row in rows]

        sq = "SELECT Customer_ID FROM quotation WHERE Quotation_ID = %s"
        val = (self.poList[3],)
        cursor.execute(sq,val)

        cusID = list(cursor.fetchone())

        print(cusID)
        self.customerIDLabel.setText(cusID[0])

        


        self.priceLabel.setText(str(self.poList[0]))
        self.vatLabe.setText(str(self.poList[1]))
        self.priceWithVat.setText(str(self.poList[2]))
        self.discountLabel.setText(str(self.poList[4]))
        self.updateProductTable()

    def updateProductTable(self):
        print(self.productList)
        self.productTable.setRowCount(len(self.productList))
        print(self.productList)
        for row, item in enumerate(self.productList):
                print(item[0])
                table_item = qtw.QTableWidgetItem(str(item[0]))
                table_item.setFlags(table_item.flags() & ~Qt.ItemIsEditable) 
                self.productTable.setItem(row, 0, table_item)
                print(item[2])

                table_item = qtw.QTableWidgetItem(str(item[1]))
                table_item.setFlags(table_item.flags() & ~Qt.ItemIsEditable)
                self.productTable.setItem(row, 1, table_item)
                print(item[3])

                table_item = qtw.QTableWidgetItem(str(item[2]))
                table_item.setFlags(table_item.flags() & ~Qt.ItemIsEditable)  
                self.productTable.setItem(row, 2, table_item)

                table_item = qtw.QTableWidgetItem(str(item[3]))
                table_item.setFlags(table_item.flags() & ~Qt.ItemIsEditable)  
                self.productTable.setItem(row, 3, table_item)

    def changeStatus(self):
        sq = "UPDATE queue_order SET Queue_Status = %s WHERE Queue_ID = %s"
        val = (self.statusLineEdit.currentText(), currentQueueID)
        print(val)
        cursor.execute(sq,val)
        mydb.commit()
        self.fetchData()
    def changeStatusAcceptOrder(self):
        sq = "UPDATE queue_order SET Queue_Status = 'Accept Order' WHERE Queue_ID = %s"
        val = (currentQueueID,)
        print(val)
        cursor.execute(sq,val)
        mydb.commit()
        self.fetchData()
    def changeStatusDeclineOrder(self):
        sq = "UPDATE queue_order SET Queue_Status = 'Decline Order' WHERE Queue_ID = %s"
        val = (currentQueueID,)
        print(val)
        cursor.execute(sq,val)
        mydb.commit()
        self.fetchData()
    def exitButtonFunc(self):
        global currentQueueID
        currentQueueID = 0
        mainPagePage.fetchData()
        self.statusLineEdit.clear()
        widget.setCurrentWidget(mainPagePage)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 771, 61))
        self.label.setStyleSheet("font: 26pt \"Arial\";")
        self.label.setObjectName("label")
        self.qIDHeadLabel = QtWidgets.QLabel(self.centralwidget)
        self.qIDHeadLabel.setGeometry(QtCore.QRect(20, 120, 171, 41))
        self.qIDHeadLabel.setStyleSheet("font: 16pt \"Arial\";")
        self.qIDHeadLabel.setObjectName("qIDHeadLabel")
        self.qIDLabel = QtWidgets.QLabel(self.centralwidget)
        self.qIDLabel.setGeometry(QtCore.QRect(200, 120, 201, 41))
        self.qIDLabel.setStyleSheet("font: 16pt \"Arial\";\n"
"color: \"RED\";")
        self.qIDLabel.setObjectName("qIDLabel")
        self.customerIDHeadLabel = QtWidgets.QLabel(self.centralwidget)
        self.customerIDHeadLabel.setGeometry(QtCore.QRect(520, 120, 201, 41))
        self.customerIDHeadLabel.setStyleSheet("font: 16pt \"Arial\";")
        self.customerIDHeadLabel.setObjectName("customerIDHeadLabel")
        self.customerIDLabel = QtWidgets.QLabel(self.centralwidget)
        self.customerIDLabel.setGeometry(QtCore.QRect(750, 120, 201, 41))
        self.customerIDLabel.setStyleSheet("font: 16pt \"Arial\";\n"
"color: \"RED\";")
        self.customerIDLabel.setObjectName("customerIDLabel")
        self.qnumberHeadLabel = QtWidgets.QLabel(self.centralwidget)
        self.qnumberHeadLabel.setGeometry(QtCore.QRect(20, 220, 241, 41))
        self.qnumberHeadLabel.setStyleSheet("font: 16pt \"Arial\";")
        self.qnumberHeadLabel.setObjectName("qnumberHeadLabel")
        self.poIDLabel = QtWidgets.QLabel(self.centralwidget)
        self.poIDLabel.setGeometry(QtCore.QRect(280, 220, 81, 41))
        self.poIDLabel.setStyleSheet("font: 16pt \"Arial\";\n"
"color: \"RED\";")
        self.poIDLabel.setObjectName("poIDLabel")
        self.productTable = QtWidgets.QTableWidget(self.centralwidget)
        self.productTable.setGeometry(QtCore.QRect(520, 210, 611, 241))
        self.productTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.productTable.setObjectName("productTable")
        self.productTable.setColumnCount(4)
        self.productTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.productTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.productTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.productTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.productTable.setHorizontalHeaderItem(3, item)
        self.changeStatusButton_2 = QtWidgets.QPushButton(self.centralwidget,clicked = lambda:self.changeStatusAcceptOrder())
        self.changeStatusButton_2.setGeometry(QtCore.QRect(360, 450, 111, 31))
        self.changeStatusButton_2.setObjectName("changeStatusButton_2")
        self.changeStatusButton_3 = QtWidgets.QPushButton(self.centralwidget,clicked = lambda:self.changeStatusDeclineOrder())
        self.changeStatusButton_3.setGeometry(QtCore.QRect(360, 500, 111, 31))
        self.changeStatusButton_3.setObjectName("changeStatusButton_2")
        self.backToHomeButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda:self.exitButtonFunc())
        self.backToHomeButton.setGeometry(QtCore.QRect(70, 530, 161, 71))
        self.backToHomeButton.setStyleSheet("QPushButton {\n"
"    font: 20pt \"Arial\";\n"
"    background-color: #156d9c; \n"
"    color: white; \n"
"    padding: 15px; \n"
"}\n"
"\n"
"QPushButton:hover { \n"
"    background-color: #2891ca; \n"
"}\n"
"")
        self.backToHomeButton.setObjectName("backToHomeButton")
        self.qnumberHeadLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.qnumberHeadLabel_2.setGeometry(QtCore.QRect(20, 320, 241, 41))
        self.qnumberHeadLabel_2.setStyleSheet("font: 16pt \"Arial\";")
        self.qnumberHeadLabel_2.setObjectName("qnumberHeadLabel_2")
        self.statusLabel = QtWidgets.QLabel(self.centralwidget)
        self.statusLabel.setGeometry(QtCore.QRect(210, 320, 291, 41))
        self.statusLabel.setStyleSheet("font: 16pt \"Arial\";\n"
"color: \"RED\";")
        self.statusLabel.setObjectName("statusLabel")
        self.changeStatusButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda:self.changeStatus())
        self.changeStatusButton.setGeometry(QtCore.QRect(360, 390, 111, 31))
        self.changeStatusButton.setObjectName("changeStatusButton")
        self.priceLabel = QtWidgets.QLabel(self.centralwidget)
        self.priceLabel.setGeometry(QtCore.QRect(670, 470, 201, 41))
        self.priceLabel.setStyleSheet("font: 16pt \"Arial\";\n"
"color: \"RED\";")
        self.priceLabel.setObjectName("priceLabel")
        self.priceWithVat = QtWidgets.QLabel(self.centralwidget)
        self.priceWithVat.setGeometry(QtCore.QRect(760, 590, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.priceWithVat.setFont(font)
        self.priceWithVat.setStyleSheet("font: 16pt \"Arial\";\n"
"color: \"RED\";")
        self.priceWithVat.setObjectName("priceWithVat")
        self.vatLabe = QtWidgets.QLabel(self.centralwidget)
        self.vatLabe.setGeometry(QtCore.QRect(670, 520, 201, 41))
        self.vatLabe.setStyleSheet("font: 16pt \"Arial\";\n"
"color: \"RED\";")
        self.vatLabe.setObjectName("vatLabe")
        self.customerIDHeadLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.customerIDHeadLabel_2.setGeometry(QtCore.QRect(520, 470, 201, 41))
        self.customerIDHeadLabel_2.setStyleSheet("font: 16pt \"Arial\";")
        self.customerIDHeadLabel_2.setObjectName("customerIDHeadLabel_2")
        self.vat = QtWidgets.QLabel(self.centralwidget)
        self.vat.setGeometry(QtCore.QRect(520, 520, 201, 41))
        self.vat.setStyleSheet("font: 16pt \"Arial\";")
        self.vat.setObjectName("vat")
        self.customerIDHeadLabel_4 = QtWidgets.QLabel(self.centralwidget)
        self.customerIDHeadLabel_4.setGeometry(QtCore.QRect(520, 580, 201, 41))
        self.customerIDHeadLabel_4.setStyleSheet("font: 16pt \"Arial\";")
        self.customerIDHeadLabel_4.setObjectName("customerIDHeadLabel_4")
        self.statusLineEdit = QtWidgets.QComboBox(self.centralwidget)
        self.statusLineEdit.setGeometry(QtCore.QRect(60, 390, 251, 31))
        self.statusLineEdit.setObjectName("statusLineEdit")
        self.customerIDHeadLabel_3 = QtWidgets.QLabel(self.centralwidget)
        self.customerIDHeadLabel_3.setGeometry(QtCore.QRect(800, 470, 201, 41))
        self.customerIDHeadLabel_3.setStyleSheet("font: 16pt \"Arial\";")
        self.customerIDHeadLabel_3.setObjectName("customerIDHeadLabel_3")
        self.discountLabel = QtWidgets.QLabel(self.centralwidget)
        self.discountLabel.setGeometry(QtCore.QRect(930, 470, 201, 41))
        self.discountLabel.setStyleSheet("font: 16pt \"Arial\";\n"
"color: \"RED\";")
        self.discountLabel.setObjectName("discountLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 21))
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
        self.label.setText(_translate("MainWindow", "Order detail"))
        self.qIDHeadLabel.setText(_translate("MainWindow", "Queue ID:"))
        self.qIDLabel.setText(_translate("MainWindow", "QID001"))
        self.customerIDHeadLabel.setText(_translate("MainWindow", "Customer ID:"))
        self.customerIDLabel.setText(_translate("MainWindow", "CID001"))
        self.qnumberHeadLabel.setText(_translate("MainWindow", "Purchase Order ID:"))
        self.poIDLabel.setText(_translate("MainWindow", "1"))
        item = self.productTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Product ID"))
        item = self.productTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Product Name"))
        item = self.productTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Quantity"))
        item = self.productTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Price-Per-Product"))
        self.backToHomeButton.setText(_translate("MainWindow", "Back"))
        self.qnumberHeadLabel_2.setText(_translate("MainWindow", "Status :"))
        self.statusLabel.setText(_translate("MainWindow", "Complete"))
        self.changeStatusButton.setText(_translate("MainWindow", "Change Status"))
        self.priceLabel.setText(_translate("MainWindow", "CID001"))
        self.priceWithVat.setText(_translate("MainWindow", "CID001"))
        self.vatLabe.setText(_translate("MainWindow", "CID001"))
        self.customerIDHeadLabel_2.setText(_translate("MainWindow", "Total Price :"))
        self.vat.setText(_translate("MainWindow", "Total Vat :"))
        self.customerIDHeadLabel_4.setText(_translate("MainWindow", "Total Price with Tax :"))
        self.customerIDHeadLabel_3.setText(_translate("MainWindow", "Discount :"))
        self.discountLabel.setText(_translate("MainWindow", "CID001"))
        self.changeStatusButton_2.setText(_translate("MainWindow", "Accept Order"))
        self.changeStatusButton_3.setText(_translate("MainWindow", "Decline Order"))


class docSearch(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Dialog")
        MainWindow.resize(640, 480)
        self.EnterButton = QtWidgets.QPushButton(MainWindow, clicked = lambda: self.EnterButtonFunc())
        self.EnterButton.setGeometry(QtCore.QRect(540, 140, 75, 23))
        self.EnterButton.setStyleSheet("background-color: #1d97b5;\n"
"color: #ffffff;")
        self.EnterButton.setObjectName("EnterButton")
        self.BackButtton = QtWidgets.QPushButton(MainWindow, clicked = lambda: self.goBackButton())
        self.BackButtton.setGeometry(QtCore.QRect(550, 410, 75, 23))
        self.BackButtton.setObjectName("BackButtton")
        self.label = QtWidgets.QLabel(MainWindow)
        self.label.setGeometry(QtCore.QRect(460, 20, 131, 16))
        self.label.setStyleSheet("background-color: #1d97b5;\n"
"color: #ffffff;")
        self.label.setObjectName("label")
        self.FetchAllButton = QtWidgets.QPushButton(MainWindow, clicked = lambda: self.FetchAllButtonFunc())
        self.FetchAllButton.setGeometry(QtCore.QRect(460, 140, 75, 23))
        self.FetchAllButton.setStyleSheet("background-color: #1d97b5;\n"
"color: #ffffff;")
        self.FetchAllButton.setObjectName("FetchAllButton")
        self.documentSearch = QtWidgets.QLineEdit(MainWindow)
        self.documentSearch.setGeometry(QtCore.QRect(460, 50, 161, 20))
        self.documentSearch.setObjectName("documentSearch")
        self.tableWidget = QtWidgets.QTableWidget(MainWindow)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 431, 451))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.searchComboBox = QtWidgets.QComboBox(MainWindow)
        self.searchComboBox.setGeometry(QtCore.QRect(510, 110, 111, 22))
        self.searchComboBox.setObjectName("searchComboBox")
        self.label_2 = QtWidgets.QLabel(MainWindow)
        self.label_2.setGeometry(QtCore.QRect(460, 80, 101, 16))
        self.label_2.setStyleSheet("background-color: #1d97b5;\n"
"color: #ffffff;")
        self.label_2.setObjectName("label_2")
        self.goButton = QtWidgets.QPushButton(MainWindow, clicked = lambda:self.goButtonFunc())
        self.goButton.setGeometry(QtCore.QRect(460, 410, 75, 23))
        self.goButton.setStyleSheet("background-color: #1d97b5;\n"
"color: #ffffff;")
        self.goButton.setObjectName("goButton")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.EnterButton.setText(_translate("Dialog", "Enter"))
        self.BackButtton.setText(_translate("Dialog", "Back"))
        self.label.setText(_translate("Dialog", "Search by id"))
        self.FetchAllButton.setText(_translate("Dialog", "Fetch all"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "id"))
        self.label_2.setText(_translate("Dialog", "Document type"))
        self.goButton.setText(_translate("Dialog", "Go"))

    def fetchData(self):
        self.searchComboBox.clear() 
        self.goWhere = 0
        comboList = ["bill", "quotation","receipt","deliveryNote"]

        self.searchComboBox.addItems(comboList)
    def goButtonFunc(self):
        global currentBillID,currentReceiptID,currentInvoiceID,currentQuotationID
        if self.goWhere ==1:
            currentBillID = self.billListGet[0]
            billDetailPage.fetchData()
            widget.setCurrentWidget(billDetailPage)
        elif self.goWhere ==  2:
            currentQuotationID = self.quotationListGet[0]
            quotationDetailPage.fetchData()
            widget.setCurrentWidget(quotationDetailPage)
        elif self.goWhere == 3:
            currentReceiptID = self.receiptListGet[0]
            receiptDetailPage.fetchData()
            widget.setCurrentWidget(receiptDetailPage)
        
        elif self.goWhere == 4:
            currentInvoiceID = self.deliveryNoteGet[0]
            invoiceDetailPage.fetchData()
            widget.setCurrentWidget(invoiceDetailPage)
        else:
            print('no')
    def goBackButton(self):
        mainPagePage.fetchData()
        widget.setCurrentWidget(mainPagePage)
    def EnterButtonFunc(self):
        if self.searchComboBox.currentText():
            if self.searchComboBox.currentText() == "bill":
                self.tableWidget.cellClicked.connect(self.clickedBill)
                sq = "SELECT Bill_id FROM bill WHERE Bill_id LIKE %s"
                val = (self.documentSearch.text(),)
                cursor.execute(sq,val)
                rows = cursor.fetchall()
                self.billList = [list(row) for row in rows] 
                self.updateBillTable()
            elif self.searchComboBox.currentText() == "quotation":
                self.tableWidget.cellClicked.connect(self.clickedQuotation)
                sq = "SELECT Quotation_ID FROM quotation WHERE Quotation_ID LIKE %s"
                val = (self.documentSearch.text(),)
                cursor.execute(sq,val)
                rows = cursor.fetchall()
                self.quotationList = [list(row) for row in rows] 
                self.updateQuotationTable()
            elif self.searchComboBox.currentText() == "receipt":
                self.tableWidget.cellClicked.connect(self.clickedReceipt)

                sq = "SELECT Receipt_id FROM receipt WHERE Receipt_id LIKE %s"
                val = (self.documentSearch.text(),)
                cursor.execute(sq,val)
                rows = cursor.fetchall()
                self.receiptList = [list(row) for row in rows] 
                self.updateRecieptTable()
            elif  self.searchComboBox.currentText() == "deliveryNote":
                self.tableWidget.cellClicked.connect(self.clickedDeliveryNote)
                sq = "SELECT Tax_Invoice_Delivery_note_ID FROM tax_invoice_delivery_note WHERE Tax_Invoice_Delivery_note_ID LIKE %s"
                val = (self.documentSearch.text(),)
                cursor.execute(sq,val)
                rows = cursor.fetchall()
                self.deliveryNoteList = [list(row) for row in rows] 
                self.updateDeliveryNoteTable()
        else:
            print("enter search")
    def FetchAllButtonFunc(self):
        print('fetch')
        if self.searchComboBox.currentText():
            if self.searchComboBox.currentText() == "bill":
                self.tableWidget.cellClicked.connect(self.clickedBill)
                sq = "SELECT Bill_id FROM bill"
                cursor.execute(sq)
                rows = cursor.fetchall()
                self.billList = [list(row) for row in rows] 
                self.updateBillTable()
            elif self.searchComboBox.currentText() == "quotation":
                self.tableWidget.cellClicked.connect(self.clickedQuotation)
                print('quo')
                sq = "SELECT Quotation_ID FROM quotation"
                cursor.execute(sq)
                rows = cursor.fetchall()
                self.quotationList = [list(row) for row in rows] 
                print(self.quotationList)
                print(self.quotationList)
                self.updateQuotationTable()
            elif self.searchComboBox.currentText() == "receipt":
                self.tableWidget.cellClicked.connect(self.clickedReceipt)

                sq = "SELECT Receipt_id FROM receipt"
                cursor.execute(sq)
                rows = cursor.fetchall()
                self.receiptList = [list(row) for row in rows] 
                self.updateRecieptTable()
            elif  self.searchComboBox.currentText() == "deliveryNote":
                self.tableWidget.cellClicked.connect(self.clickedDeliveryNote)

                sq = "SELECT Tax_Invoice_Delivery_note_ID FROM tax_invoice_delivery_note"
                cursor.execute(sq)
                rows = cursor.fetchall()
                self.deliveryNoteList = [list(row) for row in rows] 
                self.updateDeliveryNoteTable()
        else:
            print("chooose type")
    def clickedBill(self,row,col):
        self.goWhere = 1
        row_data = []
        for col in range(self.tableWidget.columnCount()):
                item = self.tableWidget.item(row, col)
                if item:
                    row_data.append(item.text())
        
        self.billListGet = row_data
        print(f'Row {row} data: {row_data}')


    def updateBillTable(self):
        self.tableWidget.setRowCount(len(self.billList))
        print(self.billList)
        for row, item in enumerate(self.billList):
                print(item[0])
                table_item = qtw.QTableWidgetItem(item[0])
                table_item.setFlags(table_item.flags() & ~Qt.ItemIsEditable) 
                self.tableWidget.setItem(row, 0, table_item)
                
    def clickedDeliveryNote(self,row,col):
        self.goWhere = 4
        row_data = []
        for col in range(self.tableWidget.columnCount()):
                item = self.tableWidget.item(row, col)
                if item:
                    row_data.append(item.text())
        
        self.deliveryNoteGet = row_data
        print(f'Row {row} data: {row_data}')
    def updateDeliveryNoteTable(self):
        self.tableWidget.setRowCount(len(self.deliveryNoteList))
        print(self.deliveryNoteList)
        for row, item in enumerate(self.deliveryNoteList):
                print(item[0])
                table_item = qtw.QTableWidgetItem(item[0])
                table_item.setFlags(table_item.flags() & ~Qt.ItemIsEditable)  
                self.tableWidget.setItem(row, 0, table_item)
            
    def clickedQuotation(self,row,col):
        self.goWhere = 2
        row_data = []
        for col in range(self.tableWidget.columnCount()):
                item = self.tableWidget.item(row, col)
                if item:
                    row_data.append(item.text())
        
        self.quotationListGet = row_data
        print(f'Row {row} data: {row_data}')
    def updateQuotationTable(self):
        self.tableWidget.setRowCount(len(self.quotationList))
        print(self.tableWidget)
        for row, item in enumerate(self.quotationList):
                print(item[0])
                table_item = qtw.QTableWidgetItem(item[0])
                table_item.setFlags(table_item.flags() & ~Qt.ItemIsEditable) 
                self.tableWidget.setItem(row, 0, table_item)
    def clickedReceipt(self,row,col):
        self.goWhere = 3
        row_data = []
        for col in range(self.tableWidget.columnCount()):
                item = self.tableWidget.item(row, col)
                if item:
                    row_data.append(item.text())
        
        self.receiptListGet = row_data
        print(f'Row {row} data: {row_data}')
    def updateRecieptTable(self):
        self.tableWidget.setRowCount(len(self.receiptList))
        print(self.receiptList)
        for row, item in enumerate(self.receiptList):
                print(item[0])
                table_item = qtw.QTableWidgetItem(item[0])
                table_item.setFlags(table_item.flags() & ~Qt.ItemIsEditable) 
                self.tableWidget.setItem(row, 0, table_item)
               
class createOrder(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda:self.checkAgain())
        self.pushButton.setGeometry(QtCore.QRect(540, 400, 75, 23))
        self.pushButton.setStyleSheet("background-color: #1d97b5;\n"
"color: #ffffff;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda:self.goBack())
        self.pushButton_2.setGeometry(QtCore.QRect(20, 410, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.productTable = QtWidgets.QTableWidget(self.centralwidget)
        self.productTable.setGeometry(QtCore.QRect(370, 80, 251, 311))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.productTable.setFont(font)
        self.productTable.setObjectName("productTable")
        self.productTable.setColumnCount(4)
        self.productTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.productTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.productTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.productTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.productTable.setHorizontalHeaderItem(3, item)
        self.cusTable = QtWidgets.QTableWidget(self.centralwidget)
        self.cusTable.setGeometry(QtCore.QRect(20, 80, 301, 121))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.cusTable.setFont(font)
        self.cusTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.cusTable.setObjectName("cusTable")
        self.cusTable.setColumnCount(2)
        self.cusTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.cusTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.cusTable.setHorizontalHeaderItem(1, item)
        self.quoTable = QtWidgets.QTableWidget(self.centralwidget)
        self.quoTable.setGeometry(QtCore.QRect(20, 260, 331, 131))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.quoTable.setFont(font)
        self.quoTable.setObjectName("quoTable")
        self.quoTable.setColumnCount(4)
        self.quoTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.quoTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.quoTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.quoTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.quoTable.setHorizontalHeaderItem(3, item)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 211, 16))
        self.label.setStyleSheet("background-color: #1d97b5;\n"
"color: #ffffff;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 230, 151, 16))
        self.label_2.setStyleSheet("background-color: #1d97b5;\n"
"color: #ffffff;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(380, 50, 231, 16))
        self.label_3.setStyleSheet("background-color: #1d97b5;\n"
"color: #ffffff;")
        self.label_3.setObjectName("label_3")
        self.cusSearchLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.cusSearchLineEdit.setGeometry(QtCore.QRect(30, 50, 171, 20))
        self.cusSearchLineEdit.setObjectName("cusSearchLineEdit")
        self.cusSearchButton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda:self.customerSearch())
        self.cusSearchButton.setGeometry(QtCore.QRect(240, 50, 75, 23))
        self.cusSearchButton.setObjectName("cusSearchButton")
        self.discountSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.discountSpinBox.setGeometry(QtCore.QRect(260, 220, 71, 22))
        self.discountSpinBox.setMaximum(999999999)
        self.discountSpinBox.setObjectName("discountSpinBox")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(200, 220, 51, 16))
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
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
        self.pushButton.setText(_translate("MainWindow", "Enter"))
        self.pushButton_2.setText(_translate("MainWindow", "Back"))
        item = self.productTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.productTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.productTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Price Per Product"))
        item = self.productTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Quantity"))
        item = self.cusTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Customer ID"))
        item = self.cusTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.quoTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.quoTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Date"))
        item = self.quoTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Sale person"))
        item = self.quoTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Total Price with Vat"))
        self.label.setText(_translate("MainWindow", "Find Customer"))
        self.label_2.setText(_translate("MainWindow", "Choose Quotation"))
        self.label_3.setText(_translate("MainWindow", "Select Quantitiy of each product"))
        self.cusSearchButton.setText(_translate("MainWindow", "Search"))
        self.label_4.setText(_translate("MainWindow", "Discount :"))

    def fetchData(self):
        self.flagCheck = [0,0,0]
        self.cusList = []
        self.cusListGet = []
        self.quoList = []
        self.selectedQua = []
        self.productList = []
        self.productListGetQuantity = []
        self.productListGet = []
        self.row_data = []
        self.idToInsert = 0

        self.sumPrice = 0.00
        self.sumPriceVat = 0.00
        self.sumPriceWithVat = 0.00

        self.current_dateTime = datetime.today().strftime('%Y-%m-%d')

    
        self.cusTable.cellClicked.connect(self.clickedCusTable)
        self.quoTable.cellClicked.connect(self.clickedQuoTable)

    def checkAgain(self):
        applyPopUp = qtw.QMessageBox()
        applyPopUp.setWindowTitle("Apply")
        applyPopUp.setText("Are you really want to add?")
        applyPopUp.setIcon(qtw.QMessageBox.Question)
        applyPopUp.setStandardButtons(qtw.QMessageBox.Ok|qtw.QMessageBox.Cancel)
        applyPopUp.setDefaultButton(qtw.QMessageBox.Cancel)

        response = applyPopUp.exec_()

        if response == qtw.QMessageBox.Ok:
            print("Ok clicked")
            self.EnterButton()
    def customerSearch(self):
        sq = """SELECT 
                    c.Customer_ID, 
                    c.Customer_Name
                FROM 
                    customer c
                JOIN 
                    quotation q ON c.Customer_ID = q.Customer_ID
                WHERE 
                    c.Customer_Name LIKE %s
                GROUP BY 
                    c.Customer_ID, c.Customer_Name
                HAVING 
                    COUNT(q.Quotation_ID) > 0;
                """
        val = ('%'+self.cusSearchLineEdit.text()+'%',)
        cursor.execute(sq,val)
        rows = cursor.fetchall()
        if rows:
            self.cusTable.setRowCount(0)
            self.cusList = [list(row) for row in rows]
            print(self.cusList)
            self.updateCusTable()
        else:
            print("no")

    def SearchQuotation(self):
        print("hello",self.cusListGet)
        sq = "SELECT Quotation_ID, Quotation_Date, Quotation_Sale_Person, Quotation_Total_Price_And_VAT FROM quotation WHERE Customer_ID = %s AND Quotation_Date >= CURDATE() - INTERVAL 1 YEAR;"
        val = (str(self.cusListGet[0]),)
        cursor.execute(sq,val)
        rows = cursor.fetchall()
        self.quoList = [list(row) for row in rows]
        print(self.quoList)
        self.updateQuoTable()

    def updateCusTable(self):
        self.cusTable.setRowCount(len(self.cusList))
        print(self.cusList)
        for row, item in enumerate(self.cusList):
                print(item[0])
                table_item = qtw.QTableWidgetItem(str(item[0]))
                table_item.setFlags(table_item.flags() & ~Qt.ItemIsEditable) 
                self.cusTable.setItem(row, 0, table_item)

                table_item = qtw.QTableWidgetItem(str(item[1]))
                table_item.setFlags(table_item.flags() & ~Qt.ItemIsEditable) 
                self.cusTable.setItem(row, 1, table_item)

    def updateQuoTable(self):
        self.quoTable.setRowCount(len(self.quoList))
        print(self.quoList)
        for row, item in enumerate(self.quoList):
                print(item[0])
                table_item = qtw.QTableWidgetItem(str(item[0]))
                table_item.setFlags(table_item.flags() & ~Qt.ItemIsEditable)  
                self.quoTable.setItem(row, 0, table_item)
                print(item[2])

                table_item = qtw.QTableWidgetItem(str(item[1]))
                table_item.setFlags(table_item.flags() & ~Qt.ItemIsEditable)  
                self.quoTable.setItem(row, 1, table_item)
                print(item[3])

                table_item = qtw.QTableWidgetItem(str(item[2]))
                table_item.setFlags(table_item.flags() & ~Qt.ItemIsEditable)  
                self.quoTable.setItem(row, 2, table_item)

                table_item = qtw.QTableWidgetItem(str(item[3]))
                table_item.setFlags(table_item.flags() & ~Qt.ItemIsEditable)  
                self.quoTable.setItem(row, 3, table_item)


    def clickedCusTable(self, row, column):
        self.row_data = []
        for col in range(self.cusTable.columnCount()):
            item = self.cusTable.item(row, col)
            if item:
                self.row_data.append(item.text())
        self.cusListGet = self.row_data
        self.SearchQuotation()
        self.flagCheck[0] = 1
    def clickedQuoTable(self, row, column):
        self.row_data = []
        for col in range(self.quoTable.columnCount()):
            item = self.quoTable.item(row, col)
            if item:
                self.row_data.append(item.text())
        
        self.selectedQua =self.row_data
        print(self.selectedQua)
        self.fetchQuatationProductData()
        self.flagCheck[1]= 1
    def fetchQuatationProductData(self):
        sq = "SELECT Product_ID, Quotation_Detail_Product_Quantity, Quotation_Detail_Price_per_product, Product_Name FROM quotation_detail WHERE Quotation_ID = %s"
        val = (str(self.selectedQua[0]),)
        cursor.execute(sq,val)
        rows = cursor.fetchall()
        self.productList = [list(row) for row in rows]
        print("product", self.productList)
        self.productListCheck = self.productList.copy()
        self.updateProductTable()

    def updateProductTable(self):
        print
        self.productTable.setRowCount(len(self.productList))
        for row, data in enumerate(self.productList):
            print(data,"dededededd")
            print(data[0])
            name_item = qtw.QTableWidgetItem(data[0])
            name_item.setFlags(name_item.flags() & ~Qt.ItemIsEditable)  
            self.productTable.setItem(row, 0, name_item)
            print(data[3])

            name_item = qtw.QTableWidgetItem(str(data[3]))
            name_item.setFlags(name_item.flags() & ~Qt.ItemIsEditable)  
            self.productTable.setItem(row, 1, name_item)
            print(data[2])
        
            price_item = qtw.QTableWidgetItem(str(data[2]))
            price_item.setFlags(price_item.flags() & ~Qt.ItemIsEditable) 
            self.productTable.setItem(row, 2, price_item)
            print(data[1])

            quantity_item = qtw.QTableWidgetItem(str(data[1]))
            quantity_item.setFlags(quantity_item.flags() | Qt.ItemIsEditable) 
            self.productTable.setItem(row, 3, quantity_item)

    def getProductTableData(self):
        rows = self.productTable.rowCount()
        table_data = []
        for row in range(rows):
            id = self.productTable.item(row, 0).text()  
            name = self.productTable.item(row, 1).text()
            price = self.productTable.item(row, 2).text() 

            quantity = self.productTable.item(row, 3).text() 
            
            table_data.append([id,name,price,quantity])

        print('Table Data:', table_data)
        self.productListGet = table_data
    

    def EnterButton(self):
        self.getProductTableData()
        self.sumPrice=0.00

        flag = 0
        for i in self.productListGet:
                self.sumPrice += float(i[2])*float(i[3])
        for i in range(len(self.productListGet)):
            print('hello oifgjodsifjobid',self.productListGet,self.productListCheck)
            if int(self.productListGet[i][3]) < 0 :
                print('out')
                flag = 1
        if flag == 0 and self.flagCheck[0] and self.flagCheck[1] and self.discountSpinBox.value() <= self.sumPrice:
            self.getProductTableData()
            sq = "SELECT COUNT(*) FROM purchase_order"
            cursor.execute(sq)
            self.idToInsert = list(cursor.fetchone())
            self.idToInsert = 'PO'+str(self.idToInsert[0]+1)
            print(self.productListGet)
            print(self.productListGet[0][0])
            print(self.productListGet[0][1],self.productListGet[0][2])

            self.sumPrice = self.sumPrice - self.discountSpinBox.value()
            print(self.sumPrice,'rokokforkfork')
            if self.sumPrice >0:
                self.sumPriceVat = float(self.sumPrice)*0.07
                self.sumPriceWithVat = float(self.sumPrice) + float(self.sumPriceVat)
            else:
                self.sumPriceVat = 0.00
                self.sumPriceWithVat = 0.00
            
            self.current_dateTime = datetime.today().strftime('%Y-%m-%d')

            
            sq = "INSERT INTO purchase_order (PO_Document_ID, Quotation_ID, PO_Document_Date, PO_Total_Price, PO_Vat, PO_Total_Price_VAT, PO_Discount) VALUES (%s,%s,%s,%s,%s,%s, %s)"
            val = (str(self.idToInsert), str(self.selectedQua[0]), self.current_dateTime, self.sumPrice,self.sumPriceVat, self.sumPriceWithVat, float(self.discountSpinBox.value()))
            
            cursor.execute(sq,val)

            namelist = []

            row = 0
            print(self.productListGet)
            for i, product in enumerate(self.productListGet,1):
                print(float(product[2]))
                if float(product[2]) > 0 :
        #sq = "SELECT Product_ID, Quotation_Detail_Product_Quantity, Quotation_Detail_Price_per_product, Product_Name FROM quotation_detail WHERE Quotation_ID = %s"

                    sq = "INSERT INTO purchase_order_detail (PO_Detail_ID, PO_Document_ID, PO_Detail_Product_ID, PO_Detail_Product, PO_Detail_Price_per_product, PO_Detail_Detail_Product_Quantity) VALUES (%s,%s,%s,%s,%s,%s)"
                    val = (str(self.idToInsert)+'POD'+str(i), str(self.idToInsert) , str(product[0]), str(product[1]), product[2], product[3])
                    print(val)
                    cursor.execute(sq,val)
                    row+=1        


            sq = "SELECT COUNT(*) FROM queue_order"
            cursor.execute(sq)
            qID = list(cursor.fetchone())
            qID = 'O'+str(qID[0]+1)


            sq = "INSERT INTO queue_order (Queue_ID, Queue_Status, PO_Document_Id) VALUES (%s, %s, %s)"
            val = (qID, "Waiting For Accept Order", self.idToInsert)
            cursor.execute(sq,val)
            mydb.commit()
            information = qtw.QMessageBox()
            information.setWindowTitle("Information")
            information.setText("Added")
            information.setIcon(qtw.QMessageBox.Information)
            information.setStandardButtons(qtw.QMessageBox.Ok)
            information.setDefaultButton(qtw.QMessageBox.Ok)

            response = information.exec_()

            if response == qtw.QMessageBox.Ok:
                self.cusTable.setRowCount(0)
                self.productTable.setRowCount(0)
                self.quoTable.setRowCount(0)
                self.goBack()
        elif flag == 0 and self.flagCheck[0] and self.flagCheck[1] and self.discountSpinBox.value() > self.sumPrice:
            information = qtw.QMessageBox()
            information.setWindowTitle("Information")
            text = "Discount is exceed Total Price (Total Price is" + str(self.sumPrice)+")"
            information.setText(text)
            information.setIcon(qtw.QMessageBox.Information)
            information.setStandardButtons(qtw.QMessageBox.Ok)
            information.setDefaultButton(qtw.QMessageBox.Ok)
            response = information.exec_()
        elif flag == 1:
            information = qtw.QMessageBox()
            information.setWindowTitle("Information")
            information.setText("Product quantity is less than 0")
            information.setIcon(qtw.QMessageBox.Information)
            information.setStandardButtons(qtw.QMessageBox.Ok)
            information.setDefaultButton(qtw.QMessageBox.Ok)
            response = information.exec_()
        else:
            information = qtw.QMessageBox()
            information.setWindowTitle("Information")
            information.setText("Please fill all field")
            information.setIcon(qtw.QMessageBox.Information)
            information.setStandardButtons(qtw.QMessageBox.Ok)
            information.setDefaultButton(qtw.QMessageBox.Ok)
            response = information.exec_()

    def goBack(self):
        mainPagePage.fetchData()
        widget.setCurrentWidget(mainPagePage)

class deliverPage(QtWidgets.QMainWindow):
    def __init__(self):
         super().__init__()
         self.setupUi(self)
    def fetchData(self):
        sq = "SELECT Delivery_ID,Delivery_Date, Delivery_Type, Delivery_Status FROM delivery_order WHERE Delivery_Status != 'Finished'"
        cursor.execute(sq)
        rows = cursor.fetchall()
        self.deliveryList = [list(row) for row in rows]
        print('ok')
        print(self.deliveryList)
        self.deliveryListGet = []

        self.deliveryTable.cellClicked.connect(self.clickedList)
        self.current_dateTime = datetime.today().strftime('%Y-%m-%d')
        self.updateTable()

    def updateTable(self):
        self.deliveryTable.setRowCount(len(self.deliveryList))

        for row, item in enumerate(self.deliveryList):
            delivery_date = item[1].strftime('%Y-%m-%d')  

            table_item = QtWidgets.QTableWidgetItem(item[0])  
            table_item.setFlags(table_item.flags() & ~QtCore.Qt.ItemIsEditable)  
            self.deliveryTable.setItem(row, 0, table_item)

            table_item = QtWidgets.QTableWidgetItem(delivery_date)  
            table_item.setFlags(table_item.flags() & ~QtCore.Qt.ItemIsEditable)  
            self.deliveryTable.setItem(row, 1, table_item)

            table_item = QtWidgets.QTableWidgetItem(item[2])  
            table_item.setFlags(table_item.flags() & ~QtCore.Qt.ItemIsEditable) 
            self.deliveryTable.setItem(row, 2, table_item)

            table_item = QtWidgets.QTableWidgetItem(item[3]) 
            table_item.setFlags(table_item.flags() & ~QtCore.Qt.ItemIsEditable)  
            self.deliveryTable.setItem(row, 3, table_item)
    def clickedList(self, row, column): 
        row_data = []
        for col in range(self.deliveryTable.columnCount()):
            item = self.deliveryTable.item(row, col)
            if item:
                row_data.append(item.text())
        
        self.deliveryListGet = row_data
        print(f'Row {row} data: {row_data}')
    def enterButton(self):
        if(self.deliveryListGet):
            global currentDeliveryID
            currentDeliveryID = self.deliveryListGet[0]
            deliveryDetailPage.fetchData()
            widget.setCurrentWidget(deliveryDetailPage)
    def goMainButton(self):
        mainPagePage.fetchData()
        widget.setCurrentWidget(mainPagePage)
    def goToCreateDelivery(self):
        createDeliveryPage.fetchData()
        widget.setCurrentWidget(createDeliveryPage)
    def finishDeliveryButtonfunc(self):
        finishedDeliveryPagePage.fetchData()
        widget.setCurrentWidget(finishedDeliveryPagePage)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.deliveryTable = QtWidgets.QTableWidget(self.centralwidget)
        self.deliveryTable.setGeometry(QtCore.QRect(20, 10, 461, 421))
        self.deliveryTable.setObjectName("deliveryTable")
        self.deliveryTable.setColumnCount(4)
        self.deliveryTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.deliveryTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.deliveryTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.deliveryTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.deliveryTable.setHorizontalHeaderItem(3, item)
        self.createDeliveryButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda:self.goToCreateDelivery())
        self.createDeliveryButton.setGeometry(QtCore.QRect(510, 60, 101, 23))
        self.createDeliveryButton.setObjectName("createDeliveryButton")
        self.finishDeliveryButton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda:self.finishDeliveryButtonfunc())
        self.finishDeliveryButton.setGeometry(QtCore.QRect(510, 20, 101, 23))
        self.finishDeliveryButton.setObjectName("finishDeliveryButton")
        self.goButton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda:self.enterButton())
        self.goButton.setGeometry(QtCore.QRect(520, 360, 75, 23))
        self.goButton.setObjectName("goButton")
        self.backButton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda:self.goMainButton())
        self.backButton.setGeometry(QtCore.QRect(520, 400, 75, 23))
        self.backButton.setObjectName("backButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(490, 10, 141, 421))
        self.label.setStyleSheet("background-color: #1d97b5;\n"
"color: #ffffff;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label.raise_()
        self.deliveryTable.raise_()
        self.createDeliveryButton.raise_()
        self.finishDeliveryButton.raise_()
        self.goButton.raise_()
        self.backButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
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
        item = self.deliveryTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.deliveryTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Date"))
        item = self.deliveryTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Type"))
        item = self.deliveryTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Status"))
        self.createDeliveryButton.setText(_translate("MainWindow", "Create Delivery"))
        self.finishDeliveryButton.setText(_translate("MainWindow", "Finished Delivery"))
        self.goButton.setText(_translate("MainWindow", "Go"))
        self.backButton.setText(_translate("MainWindow", "Back"))

class finishedDeliveryPage(QtWidgets.QMainWindow):
    def __init__(self):
         super().__init__()
         self.setupUi(self)
    def fetchData(self):
        sq = "SELECT Delivery_ID,Delivery_Date, Delivery_Type, Delivery_Status FROM delivery_order WHERE Delivery_Status = 'Finished'"
        cursor.execute(sq)
        rows = cursor.fetchall()
        self.deliveryList = [list(row) for row in rows]
        self.deliveryListGet = []
        self.updateTable()
        self.deliveryTable.cellClicked.connect(self.clickedList)
        self.current_dateTime = datetime.today().strftime('%Y-%m-%d')
    def enterButton(self):
        if(self.deliveryListGet):
            global currentDeliveryID
            currentDeliveryID = self.deliveryListGet[0]
            print(self.deliveryListGet)
            deliveryDetailPage.fetchData()
            widget.setCurrentWidget(deliveryDetailPage)
    def goDeliveryButton(self):
        deliverPagePage.fetchData()
        widget.setCurrentWidget(deliverPagePage)
    def updateTable(self):
        self.deliveryTable.setRowCount(len(self.deliveryList))
        for row, item in enumerate(self.deliveryList):
            table_item = qtw.QTableWidgetItem(item[0])
            table_item.setFlags(table_item.flags() & ~Qt.ItemIsEditable) 
            self.deliveryTable.setItem(row, 0, table_item)

            table_item = qtw.QTableWidgetItem(str(item[1]))
            table_item.setFlags(table_item.flags() & ~Qt.ItemIsEditable)  
            self.deliveryTable.setItem(row, 1, table_item)

            table_item = qtw.QTableWidgetItem(item[2])
            table_item.setFlags(table_item.flags() & ~Qt.ItemIsEditable)  
            self.deliveryTable.setItem(row, 2, table_item)

            table_item = qtw.QTableWidgetItem(item[3])
            table_item.setFlags(table_item.flags() & ~Qt.ItemIsEditable)
            self.deliveryTable.setItem(row, 3, table_item)
    def clickedList(self, row, column): 
        row_data = []
        for col in range(self.deliveryTable.columnCount()):
            item = self.deliveryTable.item(row, col)
            if item:
                row_data.append(item.text())
        
        self.deliveryListGet = row_data
        print(f'Row {row} data: {row_data}')
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.deliveryTable = QtWidgets.QTableWidget(self.centralwidget)
        self.deliveryTable.setGeometry(QtCore.QRect(20, 10, 461, 421))
        self.deliveryTable.setObjectName("deliveryTable")
        self.deliveryTable.setColumnCount(4)
        self.deliveryTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.deliveryTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.deliveryTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.deliveryTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.deliveryTable.setHorizontalHeaderItem(3, item)
        self.goButton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda:self.enterButton())
        self.goButton.setGeometry(QtCore.QRect(520, 20, 75, 23))
        self.goButton.setObjectName("goButton")
        self.backButton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.goDeliveryButton())
        self.backButton.setGeometry(QtCore.QRect(520, 60, 75, 23))
        self.backButton.setObjectName("backButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(490, 10, 141, 421))
        self.label_2.setStyleSheet("background-color: #1d97b5;\n"
"color: #ffffff;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        self.deliveryTable.raise_()
        self.goButton.raise_()
        self.backButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
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
        item = self.deliveryTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.deliveryTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Date"))
        item = self.deliveryTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Type"))
        item = self.deliveryTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Status"))
        self.goButton.setText(_translate("MainWindow", "Go"))
        self.backButton.setText(_translate("MainWindow", "Back"))

class finishOrder(QtWidgets.QMainWindow):
    def __init__(self):
         super().__init__()
         self.setupUi(self)
    def fetchData(self):
        global currentUser
        print('sdfsfsdfsdfsd')
        self.queueListGet = []

        self.orderTable.cellClicked.connect(self.clickedQueueTable)

        sq = "SELECT Queue_ID, Queue_Status FROM queue_order WHERE Queue_Status = 'Finished'"        
        cursor.execute(sq)

        self.queueList = cursor.fetchall()
        self.updateQueueTable()
        print()
    def updateQueueTable(self):
        self.orderTable.setRowCount(len(self.queueList))
        for row, item in enumerate(self.queueList):
            table_item = qtw.QTableWidgetItem(item[0])
            table_item.setFlags(table_item.flags() & ~Qt.ItemIsEditable)  
            self.orderTable.setItem(row, 0, table_item)

            table_item = qtw.QTableWidgetItem(item[1])
            table_item.setFlags(table_item.flags() & ~Qt.ItemIsEditable)  
            self.orderTable.setItem(row, 1, table_item)

    def clickedQueueTable(self,row,col):
        row_data = []
        for col in range(self.orderTable.columnCount()):
            item = self.orderTable.item(row, col)
            if item:
                row_data.append(item.text())
        
        self.queueListGet = row_data
        print(f'Row {row} data: {row_data}')

    def goToQueueDetail(self):
        if self.queueListGet:
            global currentQueueID
            print(self.queueListGet)
            currentQueueID = self.queueListGet[0]
            orderDetailPage.fetchData()
            widget.setCurrentWidget(orderDetailPage)
    def goHome(self):
        mainPagePage.fetchData()
        widget.setCurrentWidget(mainPagePage)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.orderTable = QtWidgets.QTableWidget(self.centralwidget)
        self.orderTable.setGeometry(QtCore.QRect(20, 10, 461, 421))
        self.orderTable.setObjectName("orderTable")
        self.orderTable.setColumnCount(2)
        self.orderTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.orderTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.orderTable.setHorizontalHeaderItem(1, item)
        self.goButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.goToQueueDetail())
        self.goButton.setGeometry(QtCore.QRect(520, 20, 75, 23))
        self.goButton.setObjectName("goButton")
        self.backButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.goHome())
        self.backButton.setGeometry(QtCore.QRect(520, 60, 75, 23))
        self.backButton.setObjectName("backButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(490, 10, 141, 421))
        self.label.setStyleSheet("background-color: #1d97b5;\n"
"color: #ffffff;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label.raise_()
        self.orderTable.raise_()
        self.goButton.raise_()
        self.backButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
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
        item = self.orderTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.orderTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Status"))
        self.goButton.setText(_translate("MainWindow", "Go"))
        self.backButton.setText(_translate("MainWindow", "Back"))

class declineOrder(QtWidgets.QMainWindow):
    def __init__(self):
         super().__init__()
         self.setupUi(self)
    def fetchData(self):
        global currentUser
        print('sdfsfsdfsdfsd')
        self.queueListGet = []

        self.orderTable.cellClicked.connect(self.clickedQueueTable)

        sq = "SELECT Queue_ID, Queue_Status FROM queue_order WHERE Queue_Status = 'Decline Order'"        
        cursor.execute(sq)

        self.queueList = cursor.fetchall()
        self.updateQueueTable()
        print()
    def updateQueueTable(self):
        self.orderTable.setRowCount(len(self.queueList))
        for row, item in enumerate(self.queueList):
            table_item = qtw.QTableWidgetItem(item[0])
            table_item.setFlags(table_item.flags() & ~Qt.ItemIsEditable)  
            self.orderTable.setItem(row, 0, table_item)

            table_item = qtw.QTableWidgetItem(item[1])
            table_item.setFlags(table_item.flags() & ~Qt.ItemIsEditable)  
            self.orderTable.setItem(row, 1, table_item)

    def clickedQueueTable(self,row,col):
        row_data = []
        for col in range(self.orderTable.columnCount()):
            item = self.orderTable.item(row, col)
            if item:
                row_data.append(item.text())
        
        self.queueListGet = row_data
        print(f'Row {row} data: {row_data}')

    def goToQueueDetail(self):
        if self.queueListGet:
            global currentQueueID
            print(self.queueListGet)
            currentQueueID = self.queueListGet[0]
            orderDetailPage.fetchData()
            widget.setCurrentWidget(orderDetailPage)
    def goHome(self):
        mainPagePage.fetchData()
        widget.setCurrentWidget(mainPagePage)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.orderTable = QtWidgets.QTableWidget(self.centralwidget)
        self.orderTable.setGeometry(QtCore.QRect(20, 10, 461, 421))
        self.orderTable.setObjectName("orderTable")
        self.orderTable.setColumnCount(2)
        self.orderTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.orderTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.orderTable.setHorizontalHeaderItem(1, item)
        self.goButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.goToQueueDetail())
        self.goButton.setGeometry(QtCore.QRect(520, 20, 75, 23))
        self.goButton.setObjectName("goButton")
        self.backButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.goHome())
        self.backButton.setGeometry(QtCore.QRect(520, 60, 75, 23))
        self.backButton.setObjectName("backButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(490, 10, 141, 421))
        self.label.setStyleSheet("background-color: #1d97b5;\n"
"color: #ffffff;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label.raise_()
        self.orderTable.raise_()
        self.goButton.raise_()
        self.backButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
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
        item = self.orderTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.orderTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Status"))
        self.goButton.setText(_translate("MainWindow", "Go"))
        self.backButton.setText(_translate("MainWindow", "Back"))


class stockPage(QtWidgets.QMainWindow):
    def __init__(self):
         super().__init__()
         self.setupUi(self)
    def fetchData(self):
        self.productList = []
        self.warningLabel.setVisible(False)
        self.productNameLineEdit.setVisible(False)
        self.productQuanitySpinBox.setVisible(False)
        self.priceSpinBox.setVisible(False)
        self.label.setVisible(False)
        self.label_4.setVisible(False)
        self.label_5.setVisible(False)
        self.productEnterButton.setVisible(False)
        self.orderTable.cellClicked.connect(self.clickedProductTable)
    def fetchAll(self):
        
        sq = """SELECT 
                    Product_ID, 
                    Product_Name,
                    Product_Quantity,
                    Product_Price
                FROM 
                    product
                """
        cursor.execute(sq)
        rows = cursor.fetchall()
        if rows:
            self.productList = [list(row) for row in rows]
            print(self.productList)
            
            self.updateProductTable()
        else:
            print("no")
    def setCreateProductVisible(self):
        self.productNameLineEdit.setVisible(True)
        self.productQuanitySpinBox.setVisible(True)
        self.priceSpinBox.setVisible(True)
        self.label.setVisible(True)
        self.label_4.setVisible(True)
        self.label_5.setVisible(True)
        self.productEnterButton.setVisible(True)
    def checkAgain(self):
        applyPopUp = qtw.QMessageBox()
        applyPopUp.setWindowTitle("Apply")
        applyPopUp.setText("Are you really want to add Product?")
        applyPopUp.setIcon(qtw.QMessageBox.Question)
        applyPopUp.setStandardButtons(qtw.QMessageBox.Ok|qtw.QMessageBox.Cancel)
        applyPopUp.setDefaultButton(qtw.QMessageBox.Cancel)

        response = applyPopUp.exec_()

        if response == qtw.QMessageBox.Ok:
            print("Ok clicked")
            self.applyButton()
    def applyButton(self):
        sq = """SELECT 
                    Product_ID, 
                    Product_Name,
                    Product_Quantity,
                    Product_Price
                FROM 
                    product
                WHERE
                    product_Name = %s
                """
        val = (self.productNameLineEdit.text(),)
        cursor.execute(sq,val)
        rows = cursor.fetchall()
        if rows:
            print('drdrdrdrd')
            information = qtw.QMessageBox()
            information.setWindowTitle("Information")
            information.setText("This Product Name is already taken")
            information.setIcon(qtw.QMessageBox.Information)
            information.setStandardButtons(qtw.QMessageBox.Ok)
            information.setDefaultButton(qtw.QMessageBox.Ok)

            response = information.exec_()
        elif self.productNameLineEdit.text():
            sq = "SELECT COUNT(*) FROM product"
            cursor.execute(sq)
            final_result = [i[0] for i in cursor.fetchall()]
            idToInsert = "PQT"+str(final_result[0]+1)
            sq = """
            INSERT INTO `product`(`Product_ID`,
             `Product_Name`, `Product_Quantity`,
              `Product_Price`) VALUES (%s,
              %s,%s,%s)"""
            val = (idToInsert, self.productNameLineEdit.text(),
            self.productQuanitySpinBox.value(),self.priceSpinBox.value())
            cursor.execute(sq, val)

            mydb.commit()

            information = qtw.QMessageBox()
            information.setWindowTitle("Information")
            information.setText("Added")
            information.setIcon(qtw.QMessageBox.Information)
            information.setStandardButtons(qtw.QMessageBox.Ok)
            information.setDefaultButton(qtw.QMessageBox.Ok)

            response = information.exec_()

            if response == qtw.QMessageBox.Ok:
                self.fetchData()
                self.fetchAll()
        
        else:
            print('drdrdrdrd')
            information = qtw.QMessageBox()
            information.setWindowTitle("Information")
            information.setText("Please fill Product Name")
            information.setIcon(qtw.QMessageBox.Information)
            information.setStandardButtons(qtw.QMessageBox.Ok)
            information.setDefaultButton(qtw.QMessageBox.Ok)

            response = information.exec_()
    def checkChangeQuality(self):
        applyPopUp = qtw.QMessageBox()
        applyPopUp.setWindowTitle("Apply")
        applyPopUp.setText("Are you really want to change quatity?")
        applyPopUp.setIcon(qtw.QMessageBox.Question)
        applyPopUp.setStandardButtons(qtw.QMessageBox.Ok|qtw.QMessageBox.Cancel)
        applyPopUp.setDefaultButton(qtw.QMessageBox.Cancel)

        response = applyPopUp.exec_()

        if response == qtw.QMessageBox.Ok:
            print("Ok clicked")
            self.changeQuantityButton()
    def changeQuantityButton(self):
        if(self.productList):
            sq = "UPDATE product SET Product_Quantity = %s WHERE Product_ID = %s"
            val = (self.quantitySpinBox.value(), str(self.productListGet[0]))
            print(self.quantitySpinBox.value(), str(self.productListGet[0]))
            cursor.execute(sq,val)
            mydb.commit()

            information = qtw.QMessageBox()
            information.setWindowTitle("Information")
            information.setText("Changed")
            information.setIcon(qtw.QMessageBox.Information)
            information.setStandardButtons(qtw.QMessageBox.Ok)
            information.setDefaultButton(qtw.QMessageBox.Ok)

            response = information.exec_()

            if response == qtw.QMessageBox.Ok:
                self.fetchData()
                self.fetchAll()
                self.updateProductTable()
        else:
            information = qtw.QMessageBox()
            information.setWindowTitle("Information")
            information.setText("Choose a product")
            information.setIcon(qtw.QMessageBox.Information)
            information.setStandardButtons(qtw.QMessageBox.Ok)
            information.setDefaultButton(qtw.QMessageBox.Ok)

            response = information.exec_()
        
    def productSearch(self):
        sq = """SELECT 
                    Product_ID, 
                    Product_Name,
                    Product_Quantity,
                    Product_Price
                FROM 
                    product
                WHERE 
                    Product_Name LIKE %s
                """
        val = ('%'+self.productLineEdit.text()+'%',)
        print(val)
        cursor.execute(sq,val)
        rows = cursor.fetchall()
        if rows:
            print("searching...............")
            self.productList = [list(row) for row in rows]
            print(self.productList)
            self.updateProductTable()
        else:
            self.orderTable.setRowCount(0)
    def updateProductTable(self):
        self.orderTable.setRowCount(len(self.productList))
        for row, data in enumerate(self.productList):
            name_item = qtw.QTableWidgetItem(data[0])
            name_item.setFlags(name_item.flags() & ~Qt.ItemIsEditable)  
            self.orderTable.setItem(row, 0, name_item)

            name_item = qtw.QTableWidgetItem(str(data[1]))
            name_item.setFlags(name_item.flags() & ~Qt.ItemIsEditable) 
            self.orderTable.setItem(row, 1, name_item)

            name_item = qtw.QTableWidgetItem(str(data[2]))
            name_item.setFlags(name_item.flags() & ~Qt.ItemIsEditable)  
            self.orderTable.setItem(row, 3, name_item)

            name_item = qtw.QTableWidgetItem(str(data[3]))
            name_item.setFlags(name_item.flags() & ~Qt.ItemIsEditable)  
            self.orderTable.setItem(row, 2, name_item)

    def clickedProductTable(self,row,col):
        row_data = []
        for col in range(self.orderTable.columnCount()):
            item = self.orderTable.item(row, col)
            if item:
                row_data.append(item.text())

        self.productListGet = row_data
        print(f'Row {row} data: {row_data}')
    def goMain(self):
        mainPagePage.fetchData()
        self.orderTable.setRowCount(0)
        widget.setCurrentWidget(mainPagePage)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.orderTable = QtWidgets.QTableWidget(self.centralwidget)
        self.orderTable.setGeometry(QtCore.QRect(20, 10, 411, 421))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.orderTable.setFont(font)
        self.orderTable.setObjectName("orderTable")
        self.orderTable.setColumnCount(4)
        self.orderTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.orderTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.orderTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.orderTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.orderTable.setHorizontalHeaderItem(3, item)
        self.goButton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda:self.checkChangeQuality())
        self.goButton.setGeometry(QtCore.QRect(450, 190, 75, 23))
        self.goButton.setStyleSheet("background-color: #00c3ff;\n"
"color: #ffffff;")
        self.goButton.setObjectName("goButton")
        self.backButton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda:self.goMain())
        self.backButton.setGeometry(QtCore.QRect(550, 410, 75, 23))
        self.backButton.setObjectName("backButton")
        self.quantitySpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.quantitySpinBox.setGeometry(QtCore.QRect(460, 160, 42, 21))
        self.quantitySpinBox.setMinimum(1)
        self.quantitySpinBox.setObjectName("quantitySpinBox")
        self.fetchButton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda:self.fetchAll())
        self.fetchButton.setGeometry(QtCore.QRect(450, 90, 75, 23))
        self.fetchButton.setStyleSheet("background-color: #00c3ff;\n"
"color: #ffffff;")
        self.fetchButton.setObjectName("fetchButton")
        self.searchButton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.productSearch())
        self.searchButton.setGeometry(QtCore.QRect(540, 90, 75, 23))
        self.searchButton.setStyleSheet("background-color: #00c3ff;\n"
"color: #ffffff;")
        self.searchButton.setObjectName("searchButton")
        self.warningLabel = QtWidgets.QLabel(self.centralwidget)
        self.warningLabel.setGeometry(QtCore.QRect(440, 410, 101, 20))
        self.warningLabel.setObjectName("warningLabel")
        self.productLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.productLineEdit.setGeometry(QtCore.QRect(452, 50, 161, 20))
        self.productLineEdit.setObjectName("productLineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(450, 20, 181, 21))
        self.label_2.setStyleSheet("background-color: #1d97b5;\n"
"color: #ffffff;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(450, 130, 91, 21))
        self.label_3.setStyleSheet("background-color: #1d97b5;\n"
"color: #ffffff;")
        self.label_3.setObjectName("label_3")
        self.productNameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.productNameLineEdit.setGeometry(QtCore.QRect(456, 260, 113, 20))
        self.productNameLineEdit.setObjectName("productNameLineEdit")
        self.productQuanitySpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.productQuanitySpinBox.setGeometry(QtCore.QRect(466, 310, 42, 21))
        self.productQuanitySpinBox.setMinimum(1)
        self.productQuanitySpinBox.setObjectName("productQuanitySpinBox")
        self.priceSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.priceSpinBox.setGeometry(QtCore.QRect(556, 310, 61, 21))
        self.priceSpinBox.setMinimum(1)
        self.priceSpinBox.setMaximum(999999)
        self.priceSpinBox.setObjectName("priceSpinBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(456, 240, 71, 16))
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(466, 290, 47, 13))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(576, 290, 47, 13))
        self.label_5.setObjectName("label_5")
        self.addNewProduct = QtWidgets.QPushButton(self.centralwidget,clicked = lambda:self.setCreateProductVisible())
        self.addNewProduct.setGeometry(QtCore.QRect(530, 190, 101, 23))
        self.addNewProduct.setStyleSheet("background-color: #00c3ff;\n"
"color: #ffffff;")
        self.addNewProduct.setObjectName("addNewProduct")
        self.productEnterButton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda:self.checkAgain())
        self.productEnterButton.setGeometry(QtCore.QRect(560, 340, 61, 23))
        self.productEnterButton.setObjectName("productEnterButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
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
        item = self.orderTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.orderTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.orderTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Price Per Product"))
        item = self.orderTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Quantity"))
        self.goButton.setText(_translate("MainWindow", "Go"))
        self.backButton.setText(_translate("MainWindow", "Back"))
        self.fetchButton.setText(_translate("MainWindow", "Fetch All"))
        self.searchButton.setText(_translate("MainWindow", "Search"))
        self.warningLabel.setText(_translate("MainWindow", "Warning"))
        self.label_2.setText(_translate("MainWindow", "Search  Product or fetch all"))
        self.label_3.setText(_translate("MainWindow", "Change Quantity"))
        self.label.setText(_translate("MainWindow", "Product Name"))
        self.label_4.setText(_translate("MainWindow", "Quantity"))
        self.label_5.setText(_translate("MainWindow", "Price"))
        self.addNewProduct.setText(_translate("MainWindow", "Add New Product"))
        self.productEnterButton.setText(_translate("MainWindow", "Enter"))

class createDelivery(QtWidgets.QMainWindow):
    def __init__(self):
         super().__init__()
         self.setupUi(self)
    def fetchData(self):
        self.flag = 0
        self.orderTable.cellClicked.connect(self.clickedQueueList)
        sq = """SELECT q.Queue_ID, q.Queue_Status
FROM queue_order q
LEFT JOIN delivery_order d ON q.Queue_ID = d.Queue_ID
WHERE d.Queue_ID IS NULL AND q.Queue_Status = 'Send to Customer';
"""        
        cursor.execute(sq)

        self.queueList = cursor.fetchall()
        self.updateQueueTable()
    def updateQueueTable(self):
        self.orderTable.setRowCount(len(self.queueList))
        for row, item in enumerate(self.queueList):
            table_item = qtw.QTableWidgetItem(item[0])
            table_item.setFlags(table_item.flags() & ~Qt.ItemIsEditable)  
            self.orderTable.setItem(row, 0, table_item)

            table_item = qtw.QTableWidgetItem(item[1])
            table_item.setFlags(table_item.flags() & ~Qt.ItemIsEditable) 
            self.orderTable.setItem(row, 1, table_item)
    def clickedQueueList(self, row, column): 
        row_data = []
        for col in range(self.orderTable.columnCount()):
            item = self.orderTable.item(row, col)
            if item:
                row_data.append(item.text())
        
        self.queueListGet = row_data
        print(f'Row {row} data: {row_data}')
        self.flag = 1
    def checkAgain(self):
        applyPopUp = qtw.QMessageBox()
        applyPopUp.setWindowTitle("Apply")
        applyPopUp.setText("Are you really want to add?")
        applyPopUp.setIcon(qtw.QMessageBox.Question)
        applyPopUp.setStandardButtons(qtw.QMessageBox.Ok|qtw.QMessageBox.Cancel)
        applyPopUp.setDefaultButton(qtw.QMessageBox.Cancel)

        response = applyPopUp.exec_()

        if response == qtw.QMessageBox.Ok:
            print("Ok clicked")
            self.enterButtonFunc()
    def enterButtonFunc(self):
        if self.flag and ( QDateTime(self.dateCalender.selectedDate()) > QDateTime.currentDateTime() ):
            sq = "SELECT COUNT(*) FROM delivery_order"
            cursor.execute(sq)

            deliveryid = list(cursor.fetchone())
            deliveryid = 'D'+str(deliveryid[0]+1)

            dDate = self.dateCalender.selectedDate().toString("yyyy-M-d")
            print(dDate)
            sq = """
                SELECT
                    c.Customer_Company_Province
                FROM
                    queue_order qo

                JOIN
                    purchase_order po ON qo.PO_Document_Id = po.PO_Document_ID
                JOIN
                    quotation q ON po.Quotation_ID = q.Quotation_ID
                JOIN
                    customer c ON q.Customer_ID = c.Customer_ID
                WHERE
                    qo.Queue_ID = %s
                """
            val = (self.queueListGet[0],)
            cursor.execute(sq,val)

            customerProvince = list(cursor.fetchone())
            customerProvince  = customerProvince[0]
            print(customerProvince)
            if customerProvince in ['Bangkok','Nonthaburi',"Nakhon Pathom", "Pathum Thani", "Samut Prakan",  "Samut Sakho'''''''''''''n"]:
                sq = "INSERT INTO delivery_order (Delivery_ID, Delivery_Status, Delivery_Type, Delivery_Date, Queue_ID) VALUES (%s, %s, %s, %s, %s)"
                val = (str(deliveryid), "Not yet delivery", "Delivery by our", dDate, str(self.queueListGet[0]))
                cursor.execute(sq,val)
            else:
                sq = "INSERT INTO delivery_order (Delivery_ID, Delivery_Status, Delivery_Type, Delivery_Date, Queue_ID) VALUES (%s, %s, %s, %s, %s)"
                val = (str(deliveryid), "Not yet delivery", "Third party Delivery", dDate, str(self.queueListGet[0]))
                cursor.execute(sq,val)
            mydb.commit()

            information = qtw.QMessageBox()
            information.setWindowTitle("Information")
            information.setText("Added")
            information.setIcon(qtw.QMessageBox.Information)
            information.setStandardButtons(qtw.QMessageBox.Ok)
            information.setDefaultButton(qtw.QMessageBox.Ok)

            response = information.exec_()

            if response == qtw.QMessageBox.Ok:
                self.goBack()
        elif self.flag and QDateTime(self.dateCalender.selectedDate()) < QDateTime.currentDateTime():
            information = qtw.QMessageBox()
            information.setWindowTitle("Information")
            information.setText("Time is in the past")
            information.setIcon(qtw.QMessageBox.Information)
            information.setStandardButtons(qtw.QMessageBox.Ok)
            information.setDefaultButton(qtw.QMessageBox.Ok)
            response = information.exec_()

        else:
            information = qtw.QMessageBox()
            information.setWindowTitle("Information")
            information.setText("Please fill all field")
            information.setIcon(qtw.QMessageBox.Information)
            information.setStandardButtons(qtw.QMessageBox.Ok)
            information.setDefaultButton(qtw.QMessageBox.Ok)
            response = information.exec_()

    def goBack(self):
        deliverPagePage.fetchData()
        widget.setCurrentWidget(deliverPagePage)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.backButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda:self.goBack())
        self.backButton.setGeometry(QtCore.QRect(50, 380, 91, 31))
        self.backButton.setObjectName("backButton")
        self.enterButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda:self.checkAgain())
        self.enterButton.setGeometry(QtCore.QRect(480, 370, 121, 41))
        self.enterButton.setStyleSheet("background-color: #1d97b5;\n"
"color: #ffffff;")
        self.enterButton.setObjectName("enterButton")
        self.orderTable = QtWidgets.QTableWidget(self.centralwidget)
        self.orderTable.setGeometry(QtCore.QRect(40, 70, 201, 141))
        self.orderTable.setObjectName("orderTable")
        self.orderTable.setColumnCount(2)
        self.orderTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.orderTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.orderTable.setHorizontalHeaderItem(1, item)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 30, 171, 20))
        self.label.setStyleSheet("background-color: #1d97b5;\n"
"color: #ffffff;")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(300, 50, 311, 20))
        self.label_3.setStyleSheet("background-color: #1d97b5;\n"
"color: #ffffff;")
        self.label_3.setObjectName("label_3")
        self.dateCalender = QtWidgets.QCalendarWidget(self.centralwidget)
        self.dateCalender.setGeometry(QtCore.QRect(300, 80, 312, 183))
        self.dateCalender.setObjectName("dateCalender")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
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
        self.backButton.setText(_translate("MainWindow", "Back"))
        self.enterButton.setText(_translate("MainWindow", "Enter"))
        item = self.orderTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.orderTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Status"))
        self.label.setText(_translate("MainWindow", "Choose Order"))
        self.label_3.setText(_translate("MainWindow", "Choose DeadLine Date "))


class createTaxInvoice(QtWidgets.QMainWindow):
    def __init__(self):
         super().__init__()
         self.setupUi(self)
    def fetchData(self):
        self.flag = 0
        self.paymentLineEdit.addItems(['Bank','Cash'])
        self.orderTable.cellClicked.connect(self.clickedQueueTable)

        sq = """SELECT Queue_ID, PO_Document_Id, Queue_Status 
FROM queue_order 
WHERE Tax_Invoice_Delivery_note_ID IS NULL AND (Queue_Status = 'Send to Customer' OR Queue_Status = 'Customer come to recieve');"""
        cursor.execute(sq)
        print('ok')
        self.queueList = cursor.fetchall()
        self.updateQueueTable()
    def updateQueueTable(self):
        self.orderTable.setRowCount(len(self.queueList))
        print(self.queueList)
        for row, item in enumerate(self.queueList):
                print(item[0])
                table_item = qtw.QTableWidgetItem(str(item[0]))
                table_item.setFlags(table_item.flags() & ~Qt.ItemIsEditable) 
                self.orderTable.setItem(row, 0, table_item)
                print(item[2])

                table_item = qtw.QTableWidgetItem(str(item[1]))
                table_item.setFlags(table_item.flags() & ~Qt.ItemIsEditable)  
                self.orderTable.setItem(row, 1, table_item)

                table_item = qtw.QTableWidgetItem(str(item[2]))
                table_item.setFlags(table_item.flags() & ~Qt.ItemIsEditable)
                self.orderTable.setItem(row, 2, table_item)
    def clickedQueueTable(self, row, column):
        self.row_data = []
        for col in range(self.orderTable.columnCount()):
            item = self.orderTable.item(row, col)
            if item:
                self.row_data.append(item.text())
        
        self.queueListGet = self.row_data
        print(self.queueListGet)
        self.flag = 1
    def checkAgain(self):
        applyPopUp = qtw.QMessageBox()
        applyPopUp.setWindowTitle("Apply")
        applyPopUp.setText("Are you really want to add?")
        applyPopUp.setIcon(qtw.QMessageBox.Question)
        applyPopUp.setStandardButtons(qtw.QMessageBox.Ok|qtw.QMessageBox.Cancel)
        applyPopUp.setDefaultButton(qtw.QMessageBox.Cancel)

        response = applyPopUp.exec_()

        if response == qtw.QMessageBox.Ok:
            print("Ok clicked")
            self.enterButtonFunc()
    def enterButtonFunc(self):
        if self.flag and self.conditionLineEdit.text() and self.paymentLineEdit.currentText() :
            sq = "SELECT COUNT(*) FROM tax_invoice_delivery_note"
            cursor.execute(sq)
            idToInsert = list(cursor.fetchone())
            idToInsert = 'T'+str(idToInsert[0]+1)

            sq = "SELECT PO_Document_Id FROM queue_order WHERE Queue_ID = %s"
            val = (str(self.queueListGet[0]),)
            cursor.execute(sq,val)
            rows = list(cursor.fetchone())
            poId = rows[0]

            sq = "SELECT PO_Total_Price, PO_Total_Price_VAT, PO_Vat, PO_Discount FROM purchase_order WHERE PO_Document_ID = %s"
            
            val =(poId,)
            print(poId,'foietguetg8uerhguerhtegh8rtgh8tghetriguhg8eughgthugrhteighgeiuhriu')
            cursor.execute(sq,val)
            sumPrice = list(cursor.fetchone())
            self.current_dateTime = datetime.today().strftime('%Y-%m-%d')

            print(sumPrice)
            
            sq = "INSERT INTO tax_invoice_delivery_note (Tax_Invoice_Delivery_note_ID, PO_Document_Id, Tax_Invoice_Delivery_note_payment_type, Tax_Invoice_Delivery_note_document_date, Tax_Invoice_Delivery_note_condition, Tax_Invoice_Delivery_note_Total_price, Tax_Invoice_Delivery_note_Total_Price_VAT,Tax_Invoice_Delivery_note_Vat, Tax_Invoice_Delivery_note_Discount) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            val =(str(idToInsert), poId, self.paymentLineEdit.currentText(), self.current_dateTime, self.conditionLineEdit.text(), float(sumPrice[0]), float(sumPrice[1]), float(sumPrice[2]),float(sumPrice[3]))
            
            cursor.execute(sq,val)

            sq = """
                SELECT PO_Detail_ID, PO_Detail_Product,
                PO_Detail_Price_per_product, PO_Detail_Detail_Product_Quantity, PO_Detail_Product_ID
                FROM purchase_order_detail
                WHERE PO_Document_ID = %s
                """
            val = (poId,)
            cursor.execute(sq,val)
            rows = cursor.fetchall()
            self.poPorductList = [list(row) for row in rows]

            print(self.poPorductList,'freoigtrigergghrtguguthgutghthgtughutghuthuthughtughtughtughtugtugthguthguthguthgutghu')
            for i, item in enumerate(self.poPorductList,1):
                sq = """INSERT INTO tax_invoice_delivery_note_detail (Tax_Invoice_Delivery_note_ID,
                    TD_Detail_ID, TD_Detail_Product, TD_Detail_Product_Quantity, TD_Detail_Product_ID, TD_Detail_Price_per_product) 
                    VALUES (%s,%s,%s,%s,%s,%s)"""
                val = (str(idToInsert),str(idToInsert)+'TD'+str(i),str(item[1]), item[3], str(item[4]), item[2]) 
                cursor.execute(sq,val)

            sq = """UPDATE queue_order
                SET Tax_Invoice_Delivery_note_ID = %s
                WHERE Queue_ID = %s"""
            val = (str(idToInsert),self.queueListGet[0],)
            cursor.execute(sq,val)

            mydb.commit()

            information = qtw.QMessageBox()
            information.setWindowTitle("Information")
            information.setText("Added")
            information.setIcon(qtw.QMessageBox.Information)
            information.setStandardButtons(qtw.QMessageBox.Ok)
            information.setDefaultButton(qtw.QMessageBox.Ok)

            response = information.exec_()

            if response == qtw.QMessageBox.Ok:
                self.orderTable.setRowCount(0)

                self.goBack()
        else:
            information = qtw.QMessageBox()
            information.setWindowTitle("Information")
            information.setText("Please fill all field")
            information.setIcon(qtw.QMessageBox.Information)
            information.setStandardButtons(qtw.QMessageBox.Ok)
            information.setDefaultButton(qtw.QMessageBox.Ok)
            response = information.exec_()

    def goBack(self):
        self.paymentLineEdit.clear
        mainPagePage.fetchData()
        widget.setCurrentWidget(mainPagePage)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.backButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.goBack())
        self.backButton.setGeometry(QtCore.QRect(50, 380, 91, 31))
        self.backButton.setObjectName("backButton")
        self.enterButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.checkAgain())
        self.enterButton.setGeometry(QtCore.QRect(480, 370, 121, 41))
        self.enterButton.setStyleSheet("background-color: #1d97b5;\n"
"color: #ffffff;")
        self.enterButton.setObjectName("enterButton")
        self.orderTable = QtWidgets.QTableWidget(self.centralwidget)
        self.orderTable.setGeometry(QtCore.QRect(50, 70, 331, 141))
        self.orderTable.setObjectName("orderTable")
        self.orderTable.setColumnCount(3)
        self.orderTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.orderTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.orderTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.orderTable.setHorizontalHeaderItem(2, item)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 30, 171, 20))
        self.label.setStyleSheet("background-color: #1d97b5;\n"
"color: #ffffff;")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 240, 171, 20))
        self.label_3.setStyleSheet("background-color: #1d97b5;\n"
"color: #ffffff;")
        self.label_3.setObjectName("label_3")
        self.conditionLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.conditionLineEdit.setGeometry(QtCore.QRect(70, 340, 161, 20))
        self.conditionLineEdit.setObjectName("conditionLineEdit")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 310, 171, 20))
        self.label_4.setStyleSheet("background-color: #1d97b5;\n"
"color: #ffffff;")
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 240, 191, 131))
        self.label_2.setStyleSheet("background-color: #1d97b5;\n"
"color: #ffffff;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.paymentLineEdit = QtWidgets.QComboBox(self.centralwidget)
        self.paymentLineEdit.setGeometry(QtCore.QRect(70, 270, 161, 22))
        self.paymentLineEdit.setObjectName("paymentLineEdit")
        self.label_2.raise_()
        self.backButton.raise_()
        self.enterButton.raise_()
        self.orderTable.raise_()
        self.label.raise_()
        self.label_3.raise_()
        self.conditionLineEdit.raise_()
        self.label_4.raise_()
        self.paymentLineEdit.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
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
        self.backButton.setText(_translate("MainWindow", "Back"))
        self.enterButton.setText(_translate("MainWindow", "Enter"))
        item = self.orderTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.orderTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "PO ID"))
        item = self.orderTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Status"))
        self.label.setText(_translate("MainWindow", "Choose Order"))
        self.label_3.setText(_translate("MainWindow", "Fill Payment Type"))
        self.label_4.setText(_translate("MainWindow", "Fill Condition"))

class createBill(QtWidgets.QMainWindow):
    def __init__(self):
         super().__init__()
         self.setupUi(self)
    def fetchData(self):
        self.flag = 0
        self.TableCustomerName.cellClicked.connect(self.clickedCusTable)
        self.deliveryNoteTable.cellClicked.connect(self.clickedInvoiceTable)
        self.current_dateTime = datetime.today().strftime('%Y-%m-%d')
        self.invoiceListToAdd = []
        self.invoiceListGet = [0,'','']
        self.flag = 0
    def customerSearch(self):
            customerNameToSearch = self.CustomernameEditSearch.text()
            sq = "SELECT Customer_ID, Customer_Name FROM customer WHERE Customer_Name LIKE %s"
            val = ('%' + customerNameToSearch + '%',)
            cursor.execute(sq,val)

            self.cusList = list(cursor.fetchall())
            print(self.cusList)
            self.updateCusTable()
    def updateCusTable(self):
            self.TableCustomerName.setRowCount(len(self.cusList))
            for row, item in enumerate(self.cusList):
                table_item = qtw.QTableWidgetItem(item[0])
                table_item.setFlags(table_item.flags() & ~Qt.ItemIsEditable)  
                self.TableCustomerName.setItem(row, 0, table_item)

                table_item = qtw.QTableWidgetItem(item[1])
                table_item.setFlags(table_item.flags() & ~Qt.ItemIsEditable) 
                self.TableCustomerName.setItem(row, 1, table_item)
    def clickedCusTable(self, row, column):
        self.row_data = []
        for col in range(self.TableCustomerName.columnCount()):
            item = self.TableCustomerName.item(row, col)
            if item:
                self.row_data.append(item.text())
        self.cusListGet = self.row_data
        print(self.cusListGet)
        self.fetchInvoiceTable()
        self.flag = 1
    def fetchInvoiceTable(self):
        sq = """
        SELECT 
            tax_invoice_delivery_note.Tax_Invoice_Delivery_note_ID, 
            tax_invoice_delivery_note.Tax_Invoice_Delivery_note_document_date,
            tax_invoice_delivery_note.Tax_Invoice_Delivery_note_Total_Price_VAT
        FROM 
            tax_invoice_delivery_note
        JOIN 
            purchase_order ON tax_invoice_delivery_note.PO_Document_Id = purchase_order.PO_Document_ID
        JOIN 
            quotation ON purchase_order.Quotation_ID = quotation.Quotation_ID
        JOIN 
            customer ON quotation.Customer_ID = customer.Customer_ID
        WHERE 
            customer.Customer_ID = %s;
        """
        val = (str(self.cusListGet[0]),)
        cursor.execute(sq,val)
        rows = cursor.fetchall()
        
        self.invoiceList = [list(row) for row in rows]
        print(self.invoiceList)
        self.updateInvoiceTable()
            
    def addButtonFunc(self):
        if self.invoiceListGet[1]:
            getList  = self.invoiceListGet
            self.invoiceListGet = [0,'','']
            print(self.invoiceList)
            print(getList)
            self.invoiceListToAdd.append(getList)
            print(self.invoiceListToAdd)
            self.invoiceList = [sublist for sublist in self.invoiceList if sublist[0] != getList[0]]
            print(self.invoiceList)
            self.updateInvoiceTable()
            self.updateInvoiceTableGet()
    def removeButtonFunc(self):
        self.invoiceList.append(self.invoiceListToAdd.pop())
        print(self.invoiceList)
        self.updateInvoiceTable()
        self.updateInvoiceTableGet()
    def goBack(self):
        
        mainPagePage.fetchData()
        widget.setCurrentWidget(mainPagePage)
    def updateInvoiceTableGet(self):
        self.taxInvoiceGetTable.setRowCount(len(self.invoiceListToAdd))
        for row, item in enumerate(self.invoiceListToAdd):
            table_item = qtw.QTableWidgetItem(item[0])
            table_item.setFlags(table_item.flags() & ~Qt.ItemIsEditable)  
            self.taxInvoiceGetTable.setItem(row, 0, table_item)

            table_item = qtw.QTableWidgetItem(item[1])
            table_item.setFlags(table_item.flags() & ~Qt.ItemIsEditable)  
            self.taxInvoiceGetTable.setItem(row, 1, table_item)

            table_item = qtw.QTableWidgetItem(item[2])
            table_item.setFlags(table_item.flags() & ~Qt.ItemIsEditable)  
            self.taxInvoiceGetTable.setItem(row, 2, table_item)
    
    def updateInvoiceTable(self):
        self.deliveryNoteTable.setRowCount(len(self.invoiceList))
        for row, item in enumerate(self.invoiceList):
            item[1] = str(item[1])
            table_item = qtw.QTableWidgetItem(item[0])
            table_item.setFlags(table_item.flags() & ~Qt.ItemIsEditable)  
            self.deliveryNoteTable.setItem(row, 0, table_item)

            table_item = qtw.QTableWidgetItem(item[1])
            table_item.setFlags(table_item.flags() & ~Qt.ItemIsEditable)  
            self.deliveryNoteTable.setItem(row, 1, table_item)

            table_item = qtw.QTableWidgetItem(str(item[2]))
            table_item.setFlags(table_item.flags() & ~Qt.ItemIsEditable)  
            self.deliveryNoteTable.setItem(row, 2, table_item)
    def clickedInvoiceTable(self,row,col):
        row_data = []
        for col in range(self.deliveryNoteTable.columnCount()):
                item = self.deliveryNoteTable.item(row, col)
                if item:
                    row_data.append(item.text())
        
        self.invoiceListGet = row_data
        print(f'Row {row} data: {row_data}')  

    def checkAgain(self):
        applyPopUp = qtw.QMessageBox()
        applyPopUp.setWindowTitle("Apply")
        applyPopUp.setText("Are you really want to add?")
        applyPopUp.setIcon(qtw.QMessageBox.Question)
        applyPopUp.setStandardButtons(qtw.QMessageBox.Ok|qtw.QMessageBox.Cancel)
        applyPopUp.setDefaultButton(qtw.QMessageBox.Cancel)

        response = applyPopUp.exec_()

        if response == qtw.QMessageBox.Ok:
            print("Ok clicked")
            self.applyButtonFunc()
    def applyButtonFunc(self):
        if self.flag and self.taxInvoiceGetTable.rowCount():
            sq = "SELECT COUNT(*) FROM Bill"
            cursor.execute(sq)
            idToInsert = list(cursor.fetchone())
            idToInsert = 'B'+str(idToInsert[0]+1)

            sumPrice = 0
            for i in self.invoiceListToAdd:
                sumPrice += float(i[2])

            self.current_dateTime = datetime.today().strftime('%Y-%m-%d')

            sq = "INSERT INTO bill (Bill_id,Bill_Document_Date, Bill_Total_Price) VALUES (%s,%s,%s)"
            val = (idToInsert, self.current_dateTime, sumPrice)
            cursor.execute(sq,val)
            print("this is invoice list to add to bill detail ---->", self.invoiceListToAdd)
            for i, item in enumerate(self.invoiceListToAdd,1):
                    sq = "INSERT INTO bill_detail (Bill_id, Bill_Detail_id, Bill_Detail_Price, Bill_Detail_Document_Date, Bill_Detail_Document_ID) VALUES (%s,%s,%s,%s,%s)"
                    val = (idToInsert, str(idToInsert)+'BD'+str(i), item[2], item[1], item[0])
                    cursor.execute(sq,val)
            for i in self.invoiceListToAdd:
                    sq = "UPDATE tax_invoice_delivery_note SET Bill_id = %s WHERE Tax_Invoice_Delivery_note_ID = %s"
                    val = (idToInsert, i[0])
                    cursor.execute(sq,val)
            mydb.commit()

            information = qtw.QMessageBox()
            information.setWindowTitle("Information")
            information.setText("Added")
            information.setIcon(qtw.QMessageBox.Information)
            information.setStandardButtons(qtw.QMessageBox.Ok)
            information.setDefaultButton(qtw.QMessageBox.Ok)

            response = information.exec_()

            if response == qtw.QMessageBox.Ok:
                self.deliveryNoteTable.setRowCount(0)
                self.taxInvoiceGetTable.setRowCount(0)
                self.TableCustomerName.setRowCount(0)

                self.goBack()
        else:
            information = qtw.QMessageBox()
            information.setWindowTitle("Information")
            information.setText("Please fill all field")
            information.setIcon(qtw.QMessageBox.Information)
            information.setStandardButtons(qtw.QMessageBox.Ok)
            information.setDefaultButton(qtw.QMessageBox.Ok)
            response = information.exec_()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.backButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda:self.goBack())
        self.backButton.setGeometry(QtCore.QRect(50, 380, 91, 31))
        self.backButton.setObjectName("backButton")
        self.enterButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda:self.checkAgain())
        self.enterButton.setGeometry(QtCore.QRect(480, 380, 121, 41))
        self.enterButton.setStyleSheet("background-color: #1d97b5;\n"
"color: #ffffff;")
        self.enterButton.setObjectName("enterButton")
        self.deliveryNoteTable = QtWidgets.QTableWidget(self.centralwidget)
        self.deliveryNoteTable.setGeometry(QtCore.QRect(280, 50, 331, 111))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.deliveryNoteTable.setFont(font)
        self.deliveryNoteTable.setObjectName("deliveryNoteTable")
        self.deliveryNoteTable.setColumnCount(3)
        self.deliveryNoteTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.deliveryNoteTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.deliveryNoteTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.deliveryNoteTable.setHorizontalHeaderItem(2, item)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 20, 201, 20))
        self.label.setStyleSheet("background-color: #1d97b5;\n"
"color: #ffffff;")
        self.label.setObjectName("label")
        self.TableCustomerName = QtWidgets.QTableWidget(self.centralwidget)
        self.TableCustomerName.setGeometry(QtCore.QRect(40, 130, 211, 192))
        self.TableCustomerName.setObjectName("TableCustomerName")
        self.TableCustomerName.setColumnCount(2)
        self.TableCustomerName.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.TableCustomerName.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableCustomerName.setHorizontalHeaderItem(1, item)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 20, 171, 20))
        self.label_2.setStyleSheet("background-color: #1d97b5;\n"
"color: #ffffff;")
        self.label_2.setObjectName("label_2")
        self.searchButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda:self.customerSearch())
        self.searchButton.setGeometry(QtCore.QRect(170, 80, 75, 23))
        self.searchButton.setStyleSheet("background-color: #1d97b5;\n"
"color: #ffffff;")
        self.searchButton.setObjectName("searchButton")
        self.CustomernameEditSearch = QtWidgets.QLineEdit(self.centralwidget)
        self.CustomernameEditSearch.setGeometry(QtCore.QRect(40, 50, 211, 20))
        self.CustomernameEditSearch.setObjectName("CustomernameEditSearch")
        self.taxInvoiceGetTable = QtWidgets.QTableWidget(self.centralwidget)
        self.taxInvoiceGetTable.setGeometry(QtCore.QRect(280, 230, 331, 131))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.taxInvoiceGetTable.setFont(font)
        self.taxInvoiceGetTable.setObjectName("taxInvoiceGetTable")
        self.taxInvoiceGetTable.setColumnCount(3)
        self.taxInvoiceGetTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.taxInvoiceGetTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.taxInvoiceGetTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.taxInvoiceGetTable.setHorizontalHeaderItem(2, item)
        self.addButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda:self.addButtonFunc())
        self.addButton.setGeometry(QtCore.QRect(520, 170, 75, 23))
        self.addButton.setStyleSheet("background-color: #00ff1e;\n"
"color: #111111;")
        self.addButton.setObjectName("addButton")
        self.removeButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda:self.removeButtonFunc())
        self.removeButton.setGeometry(QtCore.QRect(300, 170, 75, 23))
        self.removeButton.setStyleSheet("background-color: #ff0004;\n"
"color: #111111;")
        self.removeButton.setObjectName("removeButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(280, 200, 171, 20))
        self.label_3.setStyleSheet("background-color: #1d97b5;\n"
"color: #ffffff;")
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
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
        self.backButton.setText(_translate("MainWindow", "Back"))
        self.enterButton.setText(_translate("MainWindow", "Enter"))
        item = self.deliveryNoteTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.deliveryNoteTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Date"))
        item = self.deliveryNoteTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Total Price with tax"))
        self.label.setText(_translate("MainWindow", "Choose Tax invoice/Delivery note"))
        item = self.TableCustomerName.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.TableCustomerName.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        self.label_2.setText(_translate("MainWindow", "Choose Customer"))
        self.searchButton.setText(_translate("MainWindow", "Search"))
        item = self.taxInvoiceGetTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.taxInvoiceGetTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Date"))
        item = self.taxInvoiceGetTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Total Price with tax"))
        self.addButton.setText(_translate("MainWindow", "Add"))
        self.removeButton.setText(_translate("MainWindow", "Remove"))
        self.label_3.setText(_translate("MainWindow", "Selected Tax Invoice"))

class createReceipt(QtWidgets.QMainWindow):
    def __init__(self):
         super().__init__()
         self.setupUi(self)
    def fetchData(self):
        self.flag = [0,0,0]

        self.deliveryNoteTable.cellClicked.connect(self.clickedInvoiceTable)
        self.billTable.cellClicked.connect(self.clickedBillTable)

        sq = "SELECT Bill_id, Bill_Document_Date, Bill_Total_Price FROM bill"
        cursor.execute(sq)
        rows = cursor.fetchall()
        self.billList = [list(row) for row in rows]
        self.updateBillTable()

        self.bankList = []
    def clickedBillTable(self,row,col):
        row_data = []
        for col in range(self.billTable.columnCount()):
                item = self.billTable.item(row, col)
                if item:
                    row_data.append(item.text())
        
        self.billListGet = row_data
        print(self.billListGet)


        sq = "SELECT Bill_Detail_Document_ID, Bill_Detail_Document_Date, Bill_Detail_Price FROM bill_detail WHERE Bill_id = %s"
        val = (self.billListGet[0],)
        cursor.execute(sq,val)

        rows = cursor.fetchall()
        self.invoiceList = [list(row) for row in rows]
        self.updateInvoiceTable()
        print(self.invoiceList)  

        self.flag[0] = 1
        
    def clickedInvoiceTable(self,row,col):
        row_data = []
        for col in range(self.deliveryNoteTable.columnCount()):
                item = self.deliveryNoteTable.item(row, col)
                if item:
                    row_data.append(item.text())
        
        self.invoiceListGet = row_data
        print(f'Row {row} data: {row_data}')  
    
        self.flag[1] = 1

    def updateInvoiceTable(self):
        
        self.deliveryNoteTable.setRowCount(len(self.invoiceList))
        for row, item in enumerate(self.invoiceList):
            table_item = qtw.QTableWidgetItem(item[0])
            table_item.setFlags(table_item.flags() & ~Qt.ItemIsEditable)  
            self.deliveryNoteTable.setItem(row, 0, table_item)

            table_item = qtw.QTableWidgetItem(str(item[1]))
            table_item.setFlags(table_item.flags() & ~Qt.ItemIsEditable)  
            self.deliveryNoteTable.setItem(row, 1, table_item)

            table_item = qtw.QTableWidgetItem(str(item[2]))
            table_item.setFlags(table_item.flags() & ~Qt.ItemIsEditable)  
            self.deliveryNoteTable.setItem(row, 2, table_item)
    def updateBillTable(self):
        
        self.billTable.setRowCount(len(self.billList))
        for row, item in enumerate(self.billList):
            table_item = qtw.QTableWidgetItem(item[0])
            table_item.setFlags(table_item.flags() & ~Qt.ItemIsEditable)  
            self.billTable.setItem(row, 0, table_item)

            table_item = qtw.QTableWidgetItem(str(item[1]))
            table_item.setFlags(table_item.flags() & ~Qt.ItemIsEditable)  
            self.billTable.setItem(row, 1, table_item)

            table_item = qtw.QTableWidgetItem(str(item[2]))
            table_item.setFlags(table_item.flags() & ~Qt.ItemIsEditable)  
            self.billTable.setItem(row, 2, table_item)
    def updateBankTable(self):
        
        self.detailTable.setRowCount(len(self.bankList))
        for row, item in enumerate(self.bankList):
            table_item = qtw.QTableWidgetItem(item[0])
            table_item.setFlags(table_item.flags() & ~Qt.ItemIsEditable)  
            self.detailTable.setItem(row, 0, table_item)

            table_item = qtw.QTableWidgetItem(item[1])
            table_item.setFlags(table_item.flags() & ~Qt.ItemIsEditable)  
            self.detailTable.setItem(row, 1, table_item)

            table_item = qtw.QTableWidgetItem(item[2])
            table_item.setFlags(table_item.flags() & ~Qt.ItemIsEditable)  
            self.detailTable.setItem(row, 2, table_item)
    
            table_item = qtw.QTableWidgetItem(item[3])
            table_item.setFlags(table_item.flags() & ~Qt.ItemIsEditable)  
            self.detailTable.setItem(row, 3, table_item)

            table_item = qtw.QTableWidgetItem(item[4])
            table_item.setFlags(table_item.flags() & ~Qt.ItemIsEditable)  
            self.detailTable.setItem(row, 4, table_item)

            table_item = qtw.QTableWidgetItem(item[5])
            table_item.setFlags(table_item.flags() & ~Qt.ItemIsEditable)  
            self.detailTable.setItem(row, 5, table_item)
    def addButtonFunc(self):
        if self.bankLineEdit.text() and self.BranchLineEdit.text() and self.chequeNumberLineEdit.text() and self.chequeDateCalender.selectedDate().toString("yyyy-M-d") and self.bankNumberLineEdit.text() and str(self.amountSpinBox.value()) :
            self.bankList.append([self.bankLineEdit.text(),self.BranchLineEdit.text(),self.chequeNumberLineEdit.text(),self.chequeDateCalender.selectedDate().toString("yyyy-M-d"),self.bankNumberLineEdit.text(),str(self.amountSpinBox.value())])
            self.updateBankTable()
        else:
            information = qtw.QMessageBox()
            information.setWindowTitle("Information")
            information.setText("Please fill all field")
            information.setIcon(qtw.QMessageBox.Information)
            information.setStandardButtons(qtw.QMessageBox.Ok)
            information.setDefaultButton(qtw.QMessageBox.Ok)
            response = information.exec_()
    def removeButtonFunc(self):
        self.bankList.pop()
        self.updateBankTable()
    def goBack(self):
        mainPagePage.fetchData()
        widget.setCurrentWidget(mainPagePage)
    def checkAgain(self):
        applyPopUp = qtw.QMessageBox()
        applyPopUp.setWindowTitle("Apply")
        applyPopUp.setText("Are you really want to add?")
        applyPopUp.setIcon(qtw.QMessageBox.Question)
        applyPopUp.setStandardButtons(qtw.QMessageBox.Ok|qtw.QMessageBox.Cancel)
        applyPopUp.setDefaultButton(qtw.QMessageBox.Cancel)

        response = applyPopUp.exec_()

        if response == qtw.QMessageBox.Ok:
            print("Ok clicked")
            self.applyButton()
    def applyButton(self):
        if self.flag[0] ==1 and self.flag[1] ==1 and self.detailTable.rowCount() > 0:
            sq ="""SELECT COUNT(*) FROM  receipt"""
            cursor.execute(sq)
            idToInsert = list(cursor.fetchone())
            idToInsert = 'R'+str(idToInsert[0]+1)

            sumPrice = 0
            for i in self.bankList:
                sumPrice += float(i[5])    

            self.current_dateTime = datetime.today().strftime('%Y-%m-%d')
            cheqeuDate =  self.chequeDateCalender.selectedDate()
            sq = """INSERT INTO receipt (Receipt_id, Bill_id, Receipt_Deliver_Note_ID, Receipt_Date, Receipt_Total_Price)
            VALUES (%s,%s,%s,%s,%s)"""
            val = (idToInsert, self.billListGet[0],self.invoiceListGet[0],self.current_dateTime, sumPrice)
            cursor.execute(sq,val)

            for i, item in enumerate(self.bankList,1):
                sq = """INSERT INTO receipt_detail (
                Receipt_Detail_ID, 
                Receipt_id, 
                Receipt_Detail_Cheque_number, 
                Receipt_Detail_Total_Price, 
                Receipt_Detail_Received_Account,
                Receipt_Detail_Branch, 
                Receipt_Detail_Bank,
                Receipt_Detail_Cheque_Date
                )
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
                
                val = (str(idToInsert)+'RD'+str(i), idToInsert, item[2], float(item[5]), item[4], item[1], item[0], item[3])
                print(val)



                cursor.execute(sq,val)
            mydb.commit()

            information = qtw.QMessageBox()
            information.setWindowTitle("Information")
            information.setText("Added")
            information.setIcon(qtw.QMessageBox.Information)
            information.setStandardButtons(qtw.QMessageBox.Ok)
            information.setDefaultButton(qtw.QMessageBox.Ok)

            response = information.exec_()

            if response == qtw.QMessageBox.Ok:
                self.billTable.setRowCount(0)
                self.detailTable.setRowCount(0)
                self.deliveryNoteTable.setRowCount(0)

                self.goBack()
        else:
            information = qtw.QMessageBox()
            information.setWindowTitle("Information")
            information.setText("Please add all field")
            information.setIcon(qtw.QMessageBox.Information)
            information.setStandardButtons(qtw.QMessageBox.Ok)
            information.setDefaultButton(qtw.QMessageBox.Ok)
            response = information.exec_()



    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(791, 604)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.backButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda:self.goBack())
        self.backButton.setGeometry(QtCore.QRect(20, 530, 71, 21))
        self.backButton.setObjectName("backButton")
        self.enterButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.checkAgain())
        self.enterButton.setGeometry(QtCore.QRect(660, 520, 91, 31))
        self.enterButton.setStyleSheet("background-color: #1d97b5;\n"
"color: #ffffff;")
        self.enterButton.setObjectName("enterButton")
        self.billTable = QtWidgets.QTableWidget(self.centralwidget)
        self.billTable.setGeometry(QtCore.QRect(20, 40, 191, 171))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.billTable.setFont(font)
        self.billTable.setObjectName("billTable")
        self.billTable.setColumnCount(3)
        self.billTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.billTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.billTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.billTable.setHorizontalHeaderItem(2, item)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 171, 20))
        self.label.setStyleSheet("background-color: #1d97b5;\n"
"color: #ffffff;")
        self.label.setObjectName("label")
        self.detailTable = QtWidgets.QTableWidget(self.centralwidget)
        self.detailTable.setGeometry(QtCore.QRect(20, 350, 721, 161))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.detailTable.setFont(font)
        self.detailTable.setObjectName("detailTable")
        self.detailTable.setColumnCount(6)
        self.detailTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.detailTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.detailTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.detailTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.detailTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.detailTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.detailTable.setHorizontalHeaderItem(5, item)
        self.deliveryNoteTable = QtWidgets.QTableWidget(self.centralwidget)
        self.deliveryNoteTable.setGeometry(QtCore.QRect(220, 40, 181, 171))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.deliveryNoteTable.setFont(font)
        self.deliveryNoteTable.setObjectName("deliveryNoteTable")
        self.deliveryNoteTable.setColumnCount(3)
        self.deliveryNoteTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.deliveryNoteTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.deliveryNoteTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.deliveryNoteTable.setHorizontalHeaderItem(2, item)
        self.bankLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.bankLineEdit.setGeometry(QtCore.QRect(40, 250, 113, 20))
        self.bankLineEdit.setObjectName("bankLineEdit")
        self.BranchLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.BranchLineEdit.setGeometry(QtCore.QRect(40, 310, 113, 20))
        self.BranchLineEdit.setObjectName("BranchLineEdit")
        self.chequeNumberLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.chequeNumberLineEdit.setGeometry(QtCore.QRect(180, 260, 113, 20))
        self.chequeNumberLineEdit.setObjectName("chequeNumberLineEdit")
        self.bankNumberLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.bankNumberLineEdit.setGeometry(QtCore.QRect(180, 310, 113, 20))
        self.bankNumberLineEdit.setObjectName("bankNumberLineEdit")
        self.addButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda:self.addButtonFunc())
        self.addButton.setGeometry(QtCore.QRect(330, 230, 75, 23))
        self.addButton.setStyleSheet("background-color: #00ff1e;\n"
"color: #111111;")
        self.addButton.setObjectName("addButton")
        self.removeButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda:self.removeButtonFunc())
        self.removeButton.setGeometry(QtCore.QRect(330, 260, 75, 23))
        self.removeButton.setStyleSheet("background-color: #ff0004;\n"
"color: #111111;")
        self.removeButton.setObjectName("removeButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 230, 47, 13))
        self.label_2.setStyleSheet("background-color: #1d97b5;\n"
"color: #ffffff;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 290, 47, 13))
        self.label_3.setStyleSheet("background-color: #1d97b5;\n"
"color: #ffffff;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(190, 230, 81, 20))
        self.label_4.setStyleSheet("background-color: #1d97b5;\n"
"color: #ffffff;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(190, 290, 71, 16))
        self.label_5.setStyleSheet("background-color: #1d97b5;\n"
"color: #ffffff;")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(450, 80, 171, 16))
        self.label_6.setStyleSheet("background-color: #1d97b5;\n"
"color: #ffffff;")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(310, 290, 47, 13))
        self.label_7.setStyleSheet("background-color: #1d97b5;\n"
"color: #ffffff;")
        self.label_7.setObjectName("label_7")
        self.amountSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.amountSpinBox.setGeometry(QtCore.QRect(310, 310, 111, 22))
        self.amountSpinBox.setMaximum(1000000000)
        self.amountSpinBox.setSingleStep(1000)
        self.amountSpinBox.setObjectName("amountSpinBox")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(220, 10, 171, 20))
        self.label_8.setStyleSheet("background-color: #1d97b5;\n"
"color: #ffffff;")
        self.label_8.setObjectName("label_8")
        self.chequeDateCalender = QtWidgets.QCalendarWidget(self.centralwidget)
        self.chequeDateCalender.setGeometry(QtCore.QRect(450, 110, 321, 221))
        self.chequeDateCalender.setObjectName("chequeDateCalender")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(20, 220, 411, 121))
        self.label_9.setStyleSheet("background-color: #1d97b5;\n"
"color: #ffffff;")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_9.raise_()
        self.backButton.raise_()
        self.enterButton.raise_()
        self.billTable.raise_()
        self.label.raise_()
        self.detailTable.raise_()
        self.deliveryNoteTable.raise_()
        self.bankLineEdit.raise_()
        self.BranchLineEdit.raise_()
        self.chequeNumberLineEdit.raise_()
        self.bankNumberLineEdit.raise_()
        self.addButton.raise_()
        self.removeButton.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.amountSpinBox.raise_()
        self.label_8.raise_()
        self.chequeDateCalender.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 791, 21))
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
        self.backButton.setText(_translate("MainWindow", "Back"))
        self.enterButton.setText(_translate("MainWindow", "Enter"))
        item = self.billTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.billTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Date"))
        item = self.billTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Total Price"))
        self.label.setText(_translate("MainWindow", "Choose Bill"))
        item = self.detailTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Bank"))
        item = self.detailTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Branch"))
        item = self.detailTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Cheque number"))
        item = self.detailTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Cheque date"))
        item = self.detailTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Bank number"))
        item = self.detailTable.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Amount"))
        item = self.deliveryNoteTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.deliveryNoteTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Date"))
        item = self.deliveryNoteTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Total Price With Tax"))
        self.addButton.setText(_translate("MainWindow", "Add"))
        self.removeButton.setText(_translate("MainWindow", "Remove"))
        self.label_2.setText(_translate("MainWindow", "Bank"))
        self.label_3.setText(_translate("MainWindow", "Branch"))
        self.label_4.setText(_translate("MainWindow", "Cheque Number"))
        self.label_5.setText(_translate("MainWindow", "Bank Number"))
        self.label_6.setText(_translate("MainWindow", "Cheque Date"))
        self.label_7.setText(_translate("MainWindow", "Amount"))
        self.label_8.setText(_translate("MainWindow", "Choose Tax invoice/Delivery note"))

class deliveryDetail(QtWidgets.QMainWindow):
    def __init__(self):
         super().__init__()
         self.setupUi(self)
    def fetchData(self):
        global currentDeliveryID
        self.statusLineEdit.clear()
        self.statusLineEdit.addItems(['Sent', 'Finished'])

        sq = """
            SELECT
                Delivery_ID,
                Queue_ID,
                Tax_Invoice_Delivery_note_ID,
                Delivery_Status,
                Delivery_Date,
                Delivery_Type
            FROM
                delivery_order
            WHERE
                Delivery_ID = %s
            """
        val = (currentDeliveryID,)
        cursor.execute(sq,val)
        deliveryList = list(cursor.fetchone())

        self.deliveryIdLabel.setText(str(deliveryList[0]))
        self.qIDLabel.setText(str(deliveryList[1]))
        self.invoiceIdLabel.setText(str(deliveryList[2]))
        self.statusLabel.setText(str(deliveryList[3]))
        self.dateLabel.setText(str(deliveryList[4]))
        self.deliveryTypeLabel.setText(str(deliveryList[5]))
    
    def changeStatus(self):
        global currentDeliveryID
        sq = "UPDATE delivery_order SET Delivery_Status = %s WHERE Delivery_ID = %s"
        val = (self.statusLineEdit.currentText(), currentDeliveryID)
        cursor.execute(sq,val)
        mydb.commit()
        self.fetchData()
    def exitButtonFunc(self):
        global currentDeliveryID
        self.statusLineEdit.clear()
        currentDeliveryID = 0
        deliverPagePage.fetchData()
        widget.setCurrentWidget(deliverPagePage)
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(794, 574)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 771, 61))
        self.label.setStyleSheet("font: 26pt \"Arial\";")
        self.label.setObjectName("label")
        self.qIDHeadLabel = QtWidgets.QLabel(self.centralwidget)
        self.qIDHeadLabel.setGeometry(QtCore.QRect(20, 160, 171, 41))
        self.qIDHeadLabel.setStyleSheet("font: 16pt \"Arial\";")
        self.qIDHeadLabel.setObjectName("qIDHeadLabel")
        self.qIDLabel = QtWidgets.QLabel(self.centralwidget)
        self.qIDLabel.setGeometry(QtCore.QRect(220, 170, 201, 41))
        self.qIDLabel.setStyleSheet("font: 16pt \"Arial\";\n"
"color: \"RED\";")
        self.qIDLabel.setObjectName("qIDLabel")
        self.customerIDHeadLabel = QtWidgets.QLabel(self.centralwidget)
        self.customerIDHeadLabel.setGeometry(QtCore.QRect(470, 110, 201, 41))
        self.customerIDHeadLabel.setStyleSheet("font: 16pt \"Arial\";")
        self.customerIDHeadLabel.setObjectName("customerIDHeadLabel")
        self.deliveryTypeLabel = QtWidgets.QLabel(self.centralwidget)
        self.deliveryTypeLabel.setGeometry(QtCore.QRect(670, 110, 201, 41))
        self.deliveryTypeLabel.setStyleSheet("font: 16pt \"Arial\";\n"
"color: \"RED\";")
        self.deliveryTypeLabel.setObjectName("deliveryTypeLabel")
        self.qnumberHeadLabel = QtWidgets.QLabel(self.centralwidget)
        self.qnumberHeadLabel.setGeometry(QtCore.QRect(20, 220, 311, 41))
        self.qnumberHeadLabel.setStyleSheet("font: 16pt \"Arial\";")
        self.qnumberHeadLabel.setObjectName("qnumberHeadLabel")
        self.invoiceIdLabel = QtWidgets.QLabel(self.centralwidget)
        self.invoiceIdLabel.setGeometry(QtCore.QRect(360, 220, 81, 41))
        self.invoiceIdLabel.setStyleSheet("font: 16pt \"Arial\";\n"
"color: \"RED\";")
        self.invoiceIdLabel.setObjectName("invoiceIdLabel")
        self.backToHomeButton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda:self.exitButtonFunc())
        self.backToHomeButton.setGeometry(QtCore.QRect(50, 450, 161, 71))
        self.backToHomeButton.setStyleSheet("QPushButton {\n"
"    font: 20pt \"Arial\";\n"
"    background-color: #156d9c; \n"
"    color: white; \n"
"    padding: 15px; \n"
"}\n"
"\n"
"QPushButton:hover { \n"
"    background-color: #2891ca; \n"
"}\n"
"")
        self.backToHomeButton.setObjectName("backToHomeButton")
        self.qnumberHeadLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.qnumberHeadLabel_2.setGeometry(QtCore.QRect(20, 320, 241, 41))
        self.qnumberHeadLabel_2.setStyleSheet("font: 16pt \"Arial\";")
        self.qnumberHeadLabel_2.setObjectName("qnumberHeadLabel_2")
        self.statusLabel = QtWidgets.QLabel(self.centralwidget)
        self.statusLabel.setGeometry(QtCore.QRect(210, 320, 201, 41))
        self.statusLabel.setStyleSheet("font: 16pt \"Arial\";\n"
"color: \"RED\";")
        self.statusLabel.setObjectName("statusLabel")
        self.changeStatusButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda:self.changeStatus())
        self.changeStatusButton.setGeometry(QtCore.QRect(360, 390, 111, 31))
        self.changeStatusButton.setObjectName("changeStatusButton")
        self.deliveryIdnah = QtWidgets.QLabel(self.centralwidget)
        self.deliveryIdnah.setGeometry(QtCore.QRect(20, 110, 171, 41))
        self.deliveryIdnah.setStyleSheet("font: 16pt \"Arial\";")
        self.deliveryIdnah.setObjectName("deliveryIdnah")
        self.deliveryIdLabel = QtWidgets.QLabel(self.centralwidget)
        self.deliveryIdLabel.setGeometry(QtCore.QRect(220, 110, 201, 41))
        self.deliveryIdLabel.setStyleSheet("font: 16pt \"Arial\";\n"
"color: \"RED\";")
        self.deliveryIdLabel.setObjectName("deliveryIdLabel")
        self.qnumberHeadLabel_3 = QtWidgets.QLabel(self.centralwidget)
        self.qnumberHeadLabel_3.setGeometry(QtCore.QRect(20, 270, 221, 41))
        self.qnumberHeadLabel_3.setStyleSheet("font: 16pt \"Arial\";")
        self.qnumberHeadLabel_3.setObjectName("qnumberHeadLabel_3")
        self.dateLabel = QtWidgets.QLabel(self.centralwidget)
        self.dateLabel.setGeometry(QtCore.QRect(330, 270, 81, 41))
        self.dateLabel.setStyleSheet("font: 16pt \"Arial\";\n"
"color: \"RED\";")
        self.dateLabel.setObjectName("dateLabel")
        self.statusLineEdit = QtWidgets.QComboBox(self.centralwidget)
        self.statusLineEdit.setGeometry(QtCore.QRect(70, 380, 241, 31))
        self.statusLineEdit.setObjectName("statusLineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 794, 21))
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
        self.label.setText(_translate("MainWindow", "Delivery"))
        self.qIDHeadLabel.setText(_translate("MainWindow", "Queue ID:"))
        self.qIDLabel.setText(_translate("MainWindow", "QID001"))
        self.customerIDHeadLabel.setText(_translate("MainWindow", "Delivery Type:"))
        self.deliveryTypeLabel.setText(_translate("MainWindow", "CID001"))
        self.qnumberHeadLabel.setText(_translate("MainWindow", "Tax Invoice/Delivery Note ID"))
        self.invoiceIdLabel.setText(_translate("MainWindow", "1"))
        self.backToHomeButton.setText(_translate("MainWindow", "Back"))
        self.qnumberHeadLabel_2.setText(_translate("MainWindow", "Status :"))
        self.statusLabel.setText(_translate("MainWindow", "Complete"))
        self.changeStatusButton.setText(_translate("MainWindow", "Change Status"))
        self.deliveryIdnah.setText(_translate("MainWindow", "Delivery ID:"))
        self.deliveryIdLabel.setText(_translate("MainWindow", "QID001"))
        self.qnumberHeadLabel_3.setText(_translate("MainWindow", "Deadline  Date:"))
        self.dateLabel.setText(_translate("MainWindow", "1"))

class quotationDetail(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    def fetchData(self):
        global currentQuotationID 
        sq = "SELECT Quotation_ID, Customer_ID, Employee_ID, Quotation_Date, Quotation_Sale_Person, Quotation_Total_Price, Quotation_Total_Price_And_VAT, Quotation_VAT FROM quotation WHERE Quotation_ID = %s"
        val = (currentQuotationID,)
        cursor.execute(sq,val)

        self.quoList = list(cursor.fetchall())
        self.quoList = self.quoList[0]
        sq = "SELECT Quotation_Detail_ID, Product_ID, Quotation_Detail_Product_Quantity, Quotation_Detail_Price_per_product,Product_Name FROM quotation_detail WHERE Quotation_ID = %s"
        val = (str(currentQuotationID),)
        cursor.execute(sq,val)
        rows = cursor.fetchall()
        self.productList = [list(row) for row in rows]

        sq = """
SELECT `Customer_ID`, `Customer_Address`,
 `Customer_Company_Name`, `Customer_Phone_Number`,
   `Customer_Fax`, `Customer_Tax_ID_Number`,
     `Customer_Name`, `Customer_Company_Province`,
       `Customer_Company_Branch` FROM 
       `customer` WHERE Customer_ID = %s
                """
        val = (self.quoList[1],)
        cursor.execute(sq,val)
        self.cusList = list(cursor.fetchall())
        self.cusList = self.cusList[0]


        self.IDLabel.setText(str(self.quoList[0]))
        self.employeeIDLabel.setText(str(self.quoList[2]))
        self.cusIDLabel.setText(str(self.quoList[1]))
        self.dateLabel.setText(str(self.quoList[3]))
        self.salePersonLabel.setText(str(self.quoList[4]))
        self.priceLabel.setText(str(self.quoList[5]))
        self.vatLabe.setText(str(self.quoList[7]))
        self.priceWithVat.setText(str(self.quoList[6]))

        self.productDoc = []
        for i,item in enumerate(self.productList,1):
            print(i)
            self.productDoc.append([i,item[1],item[4],item[2],item[3]])

        self.updateProductTable()
    def updateProductTable(self):
        print(self.productList)
        self.productTable.setRowCount(len(self.productList))
        print(self.productList)
        for row, item in enumerate(self.productList):
                print(item[0])
                table_item = qtw.QTableWidgetItem(str(item[1]))
                table_item.setFlags(table_item.flags() & ~Qt.ItemIsEditable)  
                self.productTable.setItem(row, 0, table_item)
                print(item[2])

                table_item = qtw.QTableWidgetItem(str(item[4]))
                table_item.setFlags(table_item.flags() & ~Qt.ItemIsEditable)  
                self.productTable.setItem(row, 1, table_item)
                print(item[3])

                table_item = qtw.QTableWidgetItem(str(item[2]))
                table_item.setFlags(table_item.flags() & ~Qt.ItemIsEditable)  
                self.productTable.setItem(row, 2, table_item)

                table_item = qtw.QTableWidgetItem(str(item[3]))
                table_item.setFlags(table_item.flags() & ~Qt.ItemIsEditable)  
                self.productTable.setItem(row, 3, table_item)
    def goBack(self):
        documentSearchPage.fetchData()
        widget.setCurrentWidget(documentSearchPage)
    def makeDocument(self):
        doc = DocxTemplate("quotationTemplate.docx")

        context = ({"document_id":self.quoList[0],"document_date":self.quoList[3],
                   "sales":self.quoList[4],"Customer_name":self.cusList[6],"Customer_company_name":self.cusList[2],
                   "Customer_address":self.cusList[1], "phone_number":self.cusList[3],"fax_number":self.cusList[4],"customer_tax":self.cusList[5],"total_price":self.quoList[5],"total_vat":self.quoList[7],
                   "total_priceVat":self.quoList[6],"invoice_list": self.productDoc})
        
        doc.render(context)
        doc.save("Quotation"+str(self.quoList[0])+".docx")
        
        
        information = qtw.QMessageBox()
        information.setWindowTitle("Information")
        information.setText("Document has been made")
        information.setIcon(qtw.QMessageBox.Information)
        information.setStandardButtons(qtw.QMessageBox.Ok)
        information.setDefaultButton(qtw.QMessageBox.Ok)
        response = information.exec_()

        if response:
            try:       
                os.startfile("Quotation"+str(self.quoList[0])+".docx")
            except AttributeError:
                subprocess.call(['open' if os.name == 'posix' else 'xdg-open', "Quotation"+str(self.quoList[0])+".docx"])


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(993, 626)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 10, 771, 61))
        self.label.setStyleSheet("font: 26pt \"Arial\";")
        self.label.setObjectName("label")
        self.qIDHeadLabel = QtWidgets.QLabel(self.centralwidget)
        self.qIDHeadLabel.setGeometry(QtCore.QRect(30, 120, 171, 41))
        self.qIDHeadLabel.setStyleSheet("font: 16pt \"Arial\";")
        self.qIDHeadLabel.setObjectName("qIDHeadLabel")
        self.IDLabel = QtWidgets.QLabel(self.centralwidget)
        self.IDLabel.setGeometry(QtCore.QRect(240, 120, 201, 41))
        self.IDLabel.setStyleSheet("font: 16pt \"Arial\";\n"
"color: \"RED\";")
        self.IDLabel.setObjectName("IDLabel")
        self.qnumberHeadLabel = QtWidgets.QLabel(self.centralwidget)
        self.qnumberHeadLabel.setGeometry(QtCore.QRect(30, 230, 241, 41))
        self.qnumberHeadLabel.setStyleSheet("font: 16pt \"Arial\";")
        self.qnumberHeadLabel.setObjectName("qnumberHeadLabel")
        self.documentLabel = QtWidgets.QLabel(self.centralwidget)
        self.documentLabel.setGeometry(QtCore.QRect(780, 500, 161, 16))
        self.documentLabel.setObjectName("label_2")
        self.documentButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda:self.makeDocument())
        self.documentButton.setGeometry(QtCore.QRect(780, 520, 121, 23))
        self.documentButton.setObjectName("documentButton")
        self.productTable = QtWidgets.QTableWidget(self.centralwidget)
        self.productTable.setGeometry(QtCore.QRect(360, 90, 611, 291))
        self.productTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.productTable.setObjectName("productTable")
        self.productTable.setColumnCount(4)
        self.productTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.productTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.productTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.productTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.productTable.setHorizontalHeaderItem(3, item)
        self.backToHomeButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda:self.goBack())
        self.backToHomeButton.setGeometry(QtCore.QRect(80, 470, 161, 71))
        self.backToHomeButton.setStyleSheet("QPushButton {\n"
"    font: 20pt \"Arial\";\n"
"    background-color: #156d9c; \n"
"    color: white; \n"
"    padding: 15px; \n"
"}\n"
"\n"
"QPushButton:hover { \n"
"    background-color: #2891ca; \n"
"}\n"
"")
        self.backToHomeButton.setObjectName("backToHomeButton")
        self.priceLabel = QtWidgets.QLabel(self.centralwidget)
        self.priceLabel.setGeometry(QtCore.QRect(510, 410, 201, 41))
        self.priceLabel.setStyleSheet("font: 16pt \"Arial\";\n"
"color: \"RED\";")
        self.priceLabel.setObjectName("priceLabel")
        self.priceWithVat = QtWidgets.QLabel(self.centralwidget)
        self.priceWithVat.setGeometry(QtCore.QRect(600, 550, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.priceWithVat.setFont(font)
        self.priceWithVat.setStyleSheet("font: 16pt \"Arial\";\n"
"color: \"RED\";")
        self.priceWithVat.setObjectName("priceWithVat")
        self.vatLabe = QtWidgets.QLabel(self.centralwidget)
        self.vatLabe.setGeometry(QtCore.QRect(510, 480, 201, 41))
        self.vatLabe.setStyleSheet("font: 16pt \"Arial\";\n"
"color: \"RED\";")
        self.vatLabe.setObjectName("vatLabe")
        self.customerIDHeadLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.customerIDHeadLabel_2.setGeometry(QtCore.QRect(360, 410, 201, 41))
        self.customerIDHeadLabel_2.setStyleSheet("font: 16pt \"Arial\";")
        self.customerIDHeadLabel_2.setObjectName("customerIDHeadLabel_2")
        self.vat = QtWidgets.QLabel(self.centralwidget)
        self.vat.setGeometry(QtCore.QRect(360, 480, 201, 41))
        self.vat.setStyleSheet("font: 16pt \"Arial\";")
        self.vat.setObjectName("vat")
        self.customerIDHeadLabel_4 = QtWidgets.QLabel(self.centralwidget)
        self.customerIDHeadLabel_4.setGeometry(QtCore.QRect(360, 540, 201, 41))
        self.customerIDHeadLabel_4.setStyleSheet("font: 16pt \"Arial\";")
        self.customerIDHeadLabel_4.setObjectName("customerIDHeadLabel_4")
        self.qnumberHeadLabel_3 = QtWidgets.QLabel(self.centralwidget)
        self.qnumberHeadLabel_3.setGeometry(QtCore.QRect(30, 280, 241, 41))
        self.qnumberHeadLabel_3.setStyleSheet("font: 16pt \"Arial\";")
        self.qnumberHeadLabel_3.setObjectName("qnumberHeadLabel_3")
        self.qnumberHeadLabel_5 = QtWidgets.QLabel(self.centralwidget)
        self.qnumberHeadLabel_5.setGeometry(QtCore.QRect(30, 180, 241, 41))
        self.qnumberHeadLabel_5.setStyleSheet("font: 16pt \"Arial\";")
        self.qnumberHeadLabel_5.setObjectName("qnumberHeadLabel_5")
        self.employeeIDLabel = QtWidgets.QLabel(self.centralwidget)
        self.employeeIDLabel.setGeometry(QtCore.QRect(240, 180, 201, 41))
        self.employeeIDLabel.setStyleSheet("font: 16pt \"Arial\";\n"
"color: \"RED\";")
        self.employeeIDLabel.setObjectName("employeeIDLabel")
        self.cusIDLabel = QtWidgets.QLabel(self.centralwidget)
        self.cusIDLabel.setGeometry(QtCore.QRect(240, 230, 201, 41))
        self.cusIDLabel.setStyleSheet("font: 16pt \"Arial\";\n"
"color: \"RED\";")
        self.cusIDLabel.setObjectName("cusIDLabel")
        self.dateLabel = QtWidgets.QLabel(self.centralwidget)
        self.dateLabel.setGeometry(QtCore.QRect(240, 280, 201, 41))
        self.dateLabel.setStyleSheet("font: 16pt \"Arial\";\n"
"color: \"RED\";")
        self.dateLabel.setObjectName("dateLabel")
        self.qnumberHeadLabel_4 = QtWidgets.QLabel(self.centralwidget)
        self.qnumberHeadLabel_4.setGeometry(QtCore.QRect(30, 320, 241, 41))
        self.qnumberHeadLabel_4.setStyleSheet("font: 16pt \"Arial\";")
        self.qnumberHeadLabel_4.setObjectName("qnumberHeadLabel_4")
        self.salePersonLabel = QtWidgets.QLabel(self.centralwidget)
        self.salePersonLabel.setGeometry(QtCore.QRect(240, 320, 201, 41))
        self.salePersonLabel.setStyleSheet("font: 16pt \"Arial\";\n"
"color: \"RED\";")
        self.salePersonLabel.setObjectName("salePersonLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 993, 21))
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
        self.label.setText(_translate("MainWindow", "Quotation Detail"))
        self.qIDHeadLabel.setText(_translate("MainWindow", "ID :"))
        self.IDLabel.setText(_translate("MainWindow", "QID001"))
        self.qnumberHeadLabel.setText(_translate("MainWindow", "Customer ID:"))
        item = self.productTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Product ID"))
        item = self.productTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Product Name"))
        item = self.productTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Quantity"))
        item = self.productTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Price-Per-Product"))
        self.backToHomeButton.setText(_translate("MainWindow", "Back"))
        self.priceLabel.setText(_translate("MainWindow", "CID001"))
        self.priceWithVat.setText(_translate("MainWindow", "CID001"))
        self.vatLabe.setText(_translate("MainWindow", "CID001"))
        self.customerIDHeadLabel_2.setText(_translate("MainWindow", "Total Price :"))
        self.vat.setText(_translate("MainWindow", "Total Vat :"))
        self.customerIDHeadLabel_4.setText(_translate("MainWindow", "Total Price with Tax :"))
        self.qnumberHeadLabel_3.setText(_translate("MainWindow", "Date"))
        self.qnumberHeadLabel_5.setText(_translate("MainWindow", "employee ID:"))
        self.employeeIDLabel.setText(_translate("MainWindow", "QID001"))
        self.cusIDLabel.setText(_translate("MainWindow", "QID001"))
        self.dateLabel.setText(_translate("MainWindow", "QID001"))
        self.qnumberHeadLabel_4.setText(_translate("MainWindow", "Sale Person:"))
        self.salePersonLabel.setText(_translate("MainWindow", "QID001"))
        self.documentLabel.setText(_translate("MainWindow", "Get Document Here"))
        self.documentButton.setText(_translate("MainWindow", "Get Document"))

class invoiceDetail(QtWidgets.QMainWindow):
    def __init__(self):
         super().__init__()
         self.setupUi(self)
    def fetchData(self):
        global currentInvoiceID
        
        sq = "SELECT Tax_Invoice_Delivery_note_ID, PO_Document_Id, Tax_Invoice_Delivery_note_payment_type, Tax_Invoice_Delivery_note_document_date, Tax_Invoice_Delivery_note_condition, Tax_Invoice_Delivery_note_Total_price, Tax_Invoice_Delivery_note_Total_Price_VAT,Tax_Invoice_Delivery_note_Vat,Bill_id,Tax_Invoice_Delivery_note_Discount FROM tax_invoice_delivery_note WHERE Tax_Invoice_Delivery_note_ID = %s"
        val =(currentInvoiceID,)
        cursor.execute(sq,val)
        self.invoiceList = list(cursor.fetchone())

        sq = """SELECT 
                TD_Detail_ID, TD_Detail_Product, TD_Detail_Product_Quantity, TD_Detail_Product_ID, TD_Detail_Price_per_product
                FROM tax_invoice_delivery_note_detail
                WHERE Tax_Invoice_Delivery_note_ID = %s 
                """
        val = (currentInvoiceID,)
        cursor.execute(sq,val)
        rows = cursor.fetchall()
        self.productList = [list(row) for row in rows]
        print(self.productList)
        sq = """
        SELECT q.Customer_ID
        FROM tax_invoice_delivery_note t
        JOIN purchase_order p ON t.PO_Document_Id = p.PO_Document_ID
        JOIN quotation q ON p.Quotation_ID = q.Quotation_ID
        WHERE t.Tax_Invoice_Delivery_note_ID = %s;
        """
        val = (currentInvoiceID,)
        cursor.execute(sq,val)
        cusID = list(cursor.fetchall())
        cusID = cusID[0]

        sq = """
SELECT `Customer_ID`, `Customer_Address`,
 `Customer_Company_Name`, `Customer_Phone_Number`,
   `Customer_Fax`, `Customer_Tax_ID_Number`,
     `Customer_Name`, `Customer_Company_Province`,
       `Customer_Company_Branch` FROM 
       `customer` WHERE Customer_ID = %s
                """
        val = (cusID[0],)
        cursor.execute(sq,val)
        self.cusList = list(cursor.fetchall())
        self.cusList = self.cusList[0]

        self.IDLabel.setText(str(self.invoiceList[0]))
        self.poIdLabel.setText(str(self.invoiceList[1]))
        self.billIdLabel.setText(str(self.invoiceList[8]))
        self.dateLabel.setText(str(self.invoiceList[3]))
        self.conditionLabel.setText(str(self.invoiceList[4]))
        self.typeLabel.setText(str(self.invoiceList[2]))
        self.priceLabel.setText(str(self.invoiceList[5]))
        self.vatLabe.setText(str(self.invoiceList[7]))
        self.priceWithVat.setText(str(self.invoiceList[6]))
        self.discounntLabel.setText(str(self.invoiceList[9]))
        self.updateProductTable()

        self.productDoc = []
        for i,item in enumerate(self.productList,1):
            self.productDoc.append([i,item[3],item[1],item[2],item[4]])
    def goBack(self):
        global currentInvoiceID
        currentInvoiceID = 0
        documentSearchPage.fetchData()
        widget.setCurrentWidget(documentSearchPage)
    def makeDocument(self):
        doc = DocxTemplate("invoiceTemplete.docx")
       
        context = ({"document_id":self.invoiceList[0],"document_date":self.invoiceList[3],
                   "taxNumber":"0105545084231","Customer_name":self.cusList[6],"Customer_company_name":self.cusList[2],
                   "Customer_address":self.cusList[1], "phone_number":self.cusList[3],"fax_number":self.cusList[4],"Customer_tax":self.cusList[5],"total_price":self.invoiceList[5],"total_vat":self.invoiceList[7],
                   "total_priceVat":self.invoiceList[6],"invoice_list": self.productDoc,
                   "payment" :self.invoiceList[2],"condition":self.invoiceList[4],
                   "discount":self.invoiceList[9]})



        doc.render(context)
        doc.save("Invoice"+self.invoiceList[0]+".docx")

        information = qtw.QMessageBox()
        information.setWindowTitle("Information")
        information.setText("Document has been made")
        information.setIcon(qtw.QMessageBox.Information)
        information.setStandardButtons(qtw.QMessageBox.Ok)
        information.setDefaultButton(qtw.QMessageBox.Ok)
        response = information.exec_()

        if response:
            try:       
                os.startfile("Invoice"+self.invoiceList[0]+".docx")
            except AttributeError:
                subprocess.call(['open' if os.name == 'posix' else 'xdg-open', "Invoice"+self.invoiceList[0]+".docx"])


    def updateProductTable(self):
        print(self.productList)
        self.productTable.setRowCount(len(self.productList))
        print(self.productList)
        for row, item in enumerate(self.productList):
                print(item[0])
                table_item = qtw.QTableWidgetItem(str(item[3]))
                table_item.setFlags(table_item.flags() & ~Qt.ItemIsEditable)  
                self.productTable.setItem(row, 0, table_item)
                print(item[2])

                table_item = qtw.QTableWidgetItem(str(item[1]))
                table_item.setFlags(table_item.flags() & ~Qt.ItemIsEditable)  
                self.productTable.setItem(row, 1, table_item)
                print(item[3])

                table_item = qtw.QTableWidgetItem(str(item[2]))
                table_item.setFlags(table_item.flags() & ~Qt.ItemIsEditable)  
                self.productTable.setItem(row, 2, table_item)

                table_item = qtw.QTableWidgetItem(str(item[4]))
                table_item.setFlags(table_item.flags() & ~Qt.ItemIsEditable)  
                self.productTable.setItem(row, 3, table_item)
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(993, 626)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 10, 771, 61))
        self.label.setStyleSheet("font: 26pt \"Arial\";")
        self.label.setObjectName("label")
        self.qIDHeadLabel = QtWidgets.QLabel(self.centralwidget)
        self.qIDHeadLabel.setGeometry(QtCore.QRect(30, 120, 171, 41))
        self.qIDHeadLabel.setStyleSheet("font: 16pt \"Arial\";")
        self.qIDHeadLabel.setObjectName("qIDHeadLabel")
        self.IDLabel = QtWidgets.QLabel(self.centralwidget)
        self.IDLabel.setGeometry(QtCore.QRect(240, 120, 201, 41))
        self.IDLabel.setStyleSheet("font: 16pt \"Arial\";\n"
"color: \"RED\";")
        self.IDLabel.setObjectName("IDLabel")
        self.documentLabel = QtWidgets.QLabel(self.centralwidget)
        self.documentLabel.setGeometry(QtCore.QRect(780, 500, 161, 16))
        self.documentLabel.setObjectName("label_2")
        self.qnumberHeadLabel = QtWidgets.QLabel(self.centralwidget)
        self.qnumberHeadLabel.setGeometry(QtCore.QRect(30, 230, 241, 41))
        self.qnumberHeadLabel.setStyleSheet("font: 16pt \"Arial\";")
        self.qnumberHeadLabel.setObjectName("qnumberHeadLabel")
        self.productTable = QtWidgets.QTableWidget(self.centralwidget)
        self.productTable.setGeometry(QtCore.QRect(360, 90, 611, 291))
        self.productTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.productTable.setObjectName("productTable")
        self.productTable.setColumnCount(4)
        self.productTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.productTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.productTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.productTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.productTable.setHorizontalHeaderItem(3, item)
        self.backToHomeButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda:self.goBack())
        self.backToHomeButton.setGeometry(QtCore.QRect(80, 470, 161, 71))
        self.backToHomeButton.setStyleSheet("QPushButton {\n"
"    font: 20pt \"Arial\";\n"
"    background-color: #156d9c; \n"
"    color: white; \n"
"    padding: 15px; \n"
"}\n"
"\n"
"QPushButton:hover { \n"
"    background-color: #2891ca; \n"
"}\n"
"")
        self.backToHomeButton.setObjectName("backToHomeButton")
        self.priceLabel = QtWidgets.QLabel(self.centralwidget)
        self.priceLabel.setGeometry(QtCore.QRect(510, 410, 201, 41))
        self.priceLabel.setStyleSheet("font: 16pt \"Arial\";\n"
"color: \"RED\";")
        self.priceLabel.setObjectName("priceLabel")
        self.priceWithVat = QtWidgets.QLabel(self.centralwidget)
        self.priceWithVat.setGeometry(QtCore.QRect(600, 550, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.priceWithVat.setFont(font)
        self.priceWithVat.setStyleSheet("font: 16pt \"Arial\";\n"
"color: \"RED\";")
        self.priceWithVat.setObjectName("priceWithVat")
        self.vatLabe = QtWidgets.QLabel(self.centralwidget)
        self.vatLabe.setGeometry(QtCore.QRect(510, 480, 201, 41))
        self.vatLabe.setStyleSheet("font: 16pt \"Arial\";\n"
"color: \"RED\";")
        self.vatLabe.setObjectName("vatLabe")
        self.customerIDHeadLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.customerIDHeadLabel_2.setGeometry(QtCore.QRect(360, 410, 201, 41))
        self.customerIDHeadLabel_2.setStyleSheet("font: 16pt \"Arial\";")
        self.customerIDHeadLabel_2.setObjectName("customerIDHeadLabel_2")
        self.vat = QtWidgets.QLabel(self.centralwidget)
        self.vat.setGeometry(QtCore.QRect(360, 480, 201, 41))
        self.vat.setStyleSheet("font: 16pt \"Arial\";")
        self.vat.setObjectName("vat")
        self.customerIDHeadLabel_4 = QtWidgets.QLabel(self.centralwidget)
        self.customerIDHeadLabel_4.setGeometry(QtCore.QRect(360, 540, 201, 41))
        self.customerIDHeadLabel_4.setStyleSheet("font: 16pt \"Arial\";")
        self.customerIDHeadLabel_4.setObjectName("customerIDHeadLabel_4")
        self.documentButton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda:self.makeDocument())
        self.documentButton.setGeometry(QtCore.QRect(780, 520, 121, 23))
        self.documentButton.setObjectName("documentButton")
        self.qnumberHeadLabel_3 = QtWidgets.QLabel(self.centralwidget)
        self.qnumberHeadLabel_3.setGeometry(QtCore.QRect(30, 280, 241, 41))
        self.qnumberHeadLabel_3.setStyleSheet("font: 16pt \"Arial\";")
        self.qnumberHeadLabel_3.setObjectName("qnumberHeadLabel_3")
        self.qnumberHeadLabel_5 = QtWidgets.QLabel(self.centralwidget)
        self.qnumberHeadLabel_5.setGeometry(QtCore.QRect(30, 180, 241, 41))
        self.qnumberHeadLabel_5.setStyleSheet("font: 16pt \"Arial\";")
        self.qnumberHeadLabel_5.setObjectName("qnumberHeadLabel_5")
        self.poIdLabel = QtWidgets.QLabel(self.centralwidget)
        self.poIdLabel.setGeometry(QtCore.QRect(240, 180, 201, 41))
        self.poIdLabel.setStyleSheet("font: 16pt \"Arial\";\n"
"color: \"RED\";")
        self.poIdLabel.setObjectName("poIdLabel")
        self.billIdLabel = QtWidgets.QLabel(self.centralwidget)
        self.billIdLabel.setGeometry(QtCore.QRect(240, 230, 201, 41))
        self.billIdLabel.setStyleSheet("font: 16pt \"Arial\";\n"
"color: \"RED\";")
        self.billIdLabel.setObjectName("billIdLabel")
        self.dateLabel = QtWidgets.QLabel(self.centralwidget)
        self.dateLabel.setGeometry(QtCore.QRect(240, 280, 201, 41))
        self.dateLabel.setStyleSheet("font: 16pt \"Arial\";\n"
"color: \"RED\";")
        self.dateLabel.setObjectName("dateLabel")
        self.qnumberHeadLabel_4 = QtWidgets.QLabel(self.centralwidget)
        self.qnumberHeadLabel_4.setGeometry(QtCore.QRect(30, 320, 241, 41))
        self.qnumberHeadLabel_4.setStyleSheet("font: 16pt \"Arial\";")
        self.qnumberHeadLabel_4.setObjectName("qnumberHeadLabel_4")
        self.qnumberHeadLabel_6 = QtWidgets.QLabel(self.centralwidget)
        self.qnumberHeadLabel_6.setGeometry(QtCore.QRect(30, 370, 241, 41))
        self.qnumberHeadLabel_6.setStyleSheet("font: 16pt \"Arial\";")
        self.qnumberHeadLabel_6.setObjectName("qnumberHeadLabel_6")
        self.conditionLabel = QtWidgets.QLabel(self.centralwidget)
        self.conditionLabel.setGeometry(QtCore.QRect(240, 320, 201, 41))
        self.conditionLabel.setStyleSheet("font: 16pt \"Arial\";\n"
"color: \"RED\";")
        self.conditionLabel.setObjectName("conditionLabel")
        self.typeLabel = QtWidgets.QLabel(self.centralwidget)
        self.typeLabel.setGeometry(QtCore.QRect(240, 370, 201, 41))
        self.typeLabel.setStyleSheet("font: 16pt \"Arial\";\n"
"color: \"RED\";")
        self.typeLabel.setObjectName("typeLabel")
        self.customerIDHeadLabel_3 = QtWidgets.QLabel(self.centralwidget)
        self.customerIDHeadLabel_3.setGeometry(QtCore.QRect(630, 410, 201, 41))
        self.customerIDHeadLabel_3.setStyleSheet("font: 16pt \"Arial\";")
        self.customerIDHeadLabel_3.setObjectName("customerIDHeadLabel_3")
        self.discounntLabel = QtWidgets.QLabel(self.centralwidget)
        self.discounntLabel.setGeometry(QtCore.QRect(760, 410, 201, 41))
        self.discounntLabel.setStyleSheet("font: 16pt \"Arial\";\n"
"color: \"RED\";")
        self.discounntLabel.setObjectName("discounntLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 993, 21))
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
        self.label.setText(_translate("MainWindow", "Tax Invoice / Delivery Note Detail"))
        self.qIDHeadLabel.setText(_translate("MainWindow", "ID :"))
        self.IDLabel.setText(_translate("MainWindow", "QID001"))
        self.qnumberHeadLabel.setText(_translate("MainWindow", "Bill ID:"))
        item = self.productTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Product ID"))
        item = self.productTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Product Name"))
        item = self.productTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Quantity"))
        item = self.productTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Price-Per-Product"))
        self.backToHomeButton.setText(_translate("MainWindow", "Back"))
        self.priceLabel.setText(_translate("MainWindow", "CID001"))
        self.priceWithVat.setText(_translate("MainWindow", "CID001"))
        self.vatLabe.setText(_translate("MainWindow", "CID001"))
        self.customerIDHeadLabel_2.setText(_translate("MainWindow", "Total Price :"))
        self.vat.setText(_translate("MainWindow", "Total Vat :"))
        self.customerIDHeadLabel_4.setText(_translate("MainWindow", "Total Price with Tax :"))
        self.qnumberHeadLabel_3.setText(_translate("MainWindow", "Date"))
        self.qnumberHeadLabel_5.setText(_translate("MainWindow", "Purchase Order Id:"))
        self.poIdLabel.setText(_translate("MainWindow", "QID001"))
        self.billIdLabel.setText(_translate("MainWindow", "QID001"))
        self.dateLabel.setText(_translate("MainWindow", "QID001"))
        self.qnumberHeadLabel_4.setText(_translate("MainWindow", "Conditon :"))
        self.qnumberHeadLabel_6.setText(_translate("MainWindow", "Payment Type :"))
        self.conditionLabel.setText(_translate("MainWindow", "QID001"))
        self.typeLabel.setText(_translate("MainWindow", "QID001"))
        self.documentLabel.setText(_translate("MainWindow", "Get Document Here"))
        self.documentButton.setText(_translate("MainWindow", "Get Document"))
        self.customerIDHeadLabel_3.setText(_translate("MainWindow", "Discount :"))
        self.discounntLabel.setText(_translate("MainWindow", "CID001"))

class billDetail(QtWidgets.QMainWindow):
    def __init__(self):
         super().__init__()
         self.setupUi(self)
    def fetchData(self):
        global currentBillID
        print(currentBillID,'thisisBillID')
        sq = """
SELECT `Bill_id`, `Bill_Total_Price`, `Bill_Document_Date` FROM `bill` WHERE Bill_id = %s
"""
        val = (currentBillID,)
        cursor.execute(sq,val)
        self.billList = list(cursor.fetchone())

        sq = """ 
            SELECT `Bill_Detail_id`, `Bill_Detail_Price`, `Bill_Detail_Document_Date`, `Bill_Detail_Document_ID` 
            FROM `bill_detail` 
            WHERE Bill_id LIKE %s
            """
        val = (str(currentBillID),)
        cursor.execute(sq,val)
        rows = cursor.fetchall()
        self.billDetailList = [list(row) for row in rows]
        print(self.billDetailList)

        sq = """
            SELECT c.Customer_ID
            FROM bill b
            JOIN tax_invoice_delivery_note tdn ON b.Bill_id = tdn.Bill_id
            JOIN queue_order qo ON tdn.Tax_Invoice_Delivery_note_ID = qo.Tax_Invoice_Delivery_note_ID
            JOIN purchase_order po ON qo.PO_Document_Id = po.PO_Document_ID
            JOIN quotation q ON po.Quotation_ID = q.Quotation_ID
            JOIN customer c ON q.Customer_ID = c.Customer_ID
            WHERE b.Bill_id = %s;
            """
        val = (currentBillID,)
        cursor.execute(sq,val)
        cusID = list(cursor.fetchall())
        cusID = cusID[0]

        sq = """
SELECT `Customer_ID`, `Customer_Address`,
 `Customer_Company_Name`, `Customer_Phone_Number`,
   `Customer_Fax`, `Customer_Tax_ID_Number`,
     `Customer_Name`, `Customer_Company_Province`,
       `Customer_Company_Branch` FROM 
       `customer` WHERE Customer_ID = %s
                """
        val = (cusID[0],)
        cursor.execute(sq,val)
        self.cusList = list(cursor.fetchall())
        self.cusList = self.cusList[0]

        
        self.IDLabel.setText(str(self.billList[0]))
        self.priceLabel.setText(str(self.billList[1]))
        self.dateLabel.setText(str(self.billList[2]))
        self.updateBillTable()

        self.billDetailListDoc = []
        for i,item in enumerate(self.billDetailList,1):
            self.billDetailListDoc.append([i,item[3],item[2],item[1]])


    def updateBillTable(self):
        print(self.billDetailList)
        self.productTable.setRowCount(len(self.billDetailList))
        print(self.billDetailList)
        for row, item in enumerate(self.billDetailList):
                print(item[0])
                table_item = qtw.QTableWidgetItem(str(item[3]))
                table_item.setFlags(table_item.flags() & ~Qt.ItemIsEditable)  
                self.productTable.setItem(row, 0, table_item)
                print(item[2])

                table_item = qtw.QTableWidgetItem(str(item[2]))
                table_item.setFlags(table_item.flags() & ~Qt.ItemIsEditable)  
                self.productTable.setItem(row, 1, table_item)
                print(item[3])

                table_item = qtw.QTableWidgetItem(str(item[1]))
                table_item.setFlags(table_item.flags() & ~Qt.ItemIsEditable)  
                self.productTable.setItem(row, 2, table_item)

    def goBack(self):
        global currentBillID
        currentBillID = 0
        documentSearchPage.fetchData()
        widget.setCurrentWidget(documentSearchPage)

    def makeDocument(self):
        doc = DocxTemplate("billtemplete.docx")
        context = ({"document_id":self.billList[0],"document_date":self.billList[2],
                   "taxNumber":"0105545084231","Customer_name":self.cusList[6],"Customer_company_name":self.cusList[2],
                   "Customer_address":self.cusList[1], "phone_number":self.cusList[3],"fax_number":self.cusList[4],"Customer_tax":self.cusList[5],"total_price":self.billList[1],
                   "invoice_list": self.billDetailListDoc})
        print(context)
        doc.render(context)
        doc.save("Bill"+self.billList[0]+".docx")

        information = qtw.QMessageBox()
        information.setWindowTitle("Information")
        information.setText("Document has been made")
        information.setIcon(qtw.QMessageBox.Information)
        information.setStandardButtons(qtw.QMessageBox.Ok)
        information.setDefaultButton(qtw.QMessageBox.Ok)
        response = information.exec_()
    
        if response:
                try:       
                    os.startfile("Bill"+self.billList[0]+".docx")
                except AttributeError:
                    subprocess.call(['open' if os.name == 'posix' else 'xdg-open', "Bill"+self.billList[0]+".docx"])

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(993, 593)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 10, 771, 61))
        self.label.setStyleSheet("font: 26pt \"Arial\";")
        self.label.setObjectName("label")
        self.qIDHeadLabel = QtWidgets.QLabel(self.centralwidget)
        self.qIDHeadLabel.setGeometry(QtCore.QRect(30, 120, 171, 41))
        self.qIDHeadLabel.setStyleSheet("font: 16pt \"Arial\";")
        self.qIDHeadLabel.setObjectName("qIDHeadLabel")
        self.documentLabel = QtWidgets.QLabel(self.centralwidget)
        self.documentLabel.setGeometry(QtCore.QRect(780, 500, 161, 16))
        self.documentLabel.setObjectName("label_2")
        self.documentButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda:self.makeDocument())
        self.documentButton.setGeometry(QtCore.QRect(780, 520, 121, 23))
        self.documentButton.setObjectName("documentButton")
        self.IDLabel = QtWidgets.QLabel(self.centralwidget)
        self.IDLabel.setGeometry(QtCore.QRect(240, 120, 201, 41))
        self.IDLabel.setStyleSheet("font: 16pt \"Arial\";\n"
"color: \"RED\";")
        self.IDLabel.setObjectName("IDLabel")
        self.productTable = QtWidgets.QTableWidget(self.centralwidget)
        self.productTable.setGeometry(QtCore.QRect(360, 90, 611, 291))
        self.productTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.productTable.setObjectName("productTable")
        self.productTable.setColumnCount(3)
        self.productTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.productTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.productTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.productTable.setHorizontalHeaderItem(2, item)
        self.backToHomeButton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.goBack())
        self.backToHomeButton.setGeometry(QtCore.QRect(80, 430, 161, 71))
        self.backToHomeButton.setStyleSheet("QPushButton {\n"
"    font: 20pt \"Arial\";\n"
"    background-color: #156d9c; \n"
"    color: white; \n"
"    padding: 15px; \n"
"}\n"
"\n"
"QPushButton:hover { \n"
"    background-color: #2891ca; \n"
"}\n"
"")
        self.backToHomeButton.setObjectName("backToHomeButton")
        self.priceLabel = QtWidgets.QLabel(self.centralwidget)
        self.priceLabel.setGeometry(QtCore.QRect(510, 410, 201, 41))
        self.priceLabel.setStyleSheet("font: 16pt \"Arial\";\n"
"color: \"RED\";")
        self.priceLabel.setObjectName("priceLabel")
        self.customerIDHeadLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.customerIDHeadLabel_2.setGeometry(QtCore.QRect(360, 410, 201, 41))
        self.customerIDHeadLabel_2.setStyleSheet("font: 16pt \"Arial\";")
        self.customerIDHeadLabel_2.setObjectName("customerIDHeadLabel_2")
        self.qnumberHeadLabel_3 = QtWidgets.QLabel(self.centralwidget)
        self.qnumberHeadLabel_3.setGeometry(QtCore.QRect(30, 190, 241, 41))
        self.qnumberHeadLabel_3.setStyleSheet("font: 16pt \"Arial\";")
        self.qnumberHeadLabel_3.setObjectName("qnumberHeadLabel_3")
        self.dateLabel = QtWidgets.QLabel(self.centralwidget)
        self.dateLabel.setGeometry(QtCore.QRect(240, 180, 201, 41))
        self.dateLabel.setStyleSheet("font: 16pt \"Arial\";\n"
"color: \"RED\";")
        self.dateLabel.setObjectName("dateLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 993, 21))
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
        self.label.setText(_translate("MainWindow", "Bill Detail"))
        self.qIDHeadLabel.setText(_translate("MainWindow", "ID :"))
        self.IDLabel.setText(_translate("MainWindow", "QID001"))
        item = self.productTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Invoice ID"))
        item = self.productTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Date"))
        item = self.productTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Amount"))
        self.backToHomeButton.setText(_translate("MainWindow", "Back"))
        self.priceLabel.setText(_translate("MainWindow", "CID001"))
        self.customerIDHeadLabel_2.setText(_translate("MainWindow", "Total Price :"))
        self.qnumberHeadLabel_3.setText(_translate("MainWindow", "Date"))
        self.dateLabel.setText(_translate("MainWindow", "QID001"))
        self.documentLabel.setText(_translate("MainWindow", "Get Document Here"))
        self.documentButton.setText(_translate("MainWindow", "Get Document"))

class receiptDetail(QtWidgets.QMainWindow):
    def __init__(self):
         super().__init__()
         self.setupUi(self)
    def fetchData(self):
        global currentReceiptID

        sq = """SELECT `Receipt_id`, `Bill_id`, `Receipt_Deliver_Note_ID`, `Receipt_Date`, `Receipt_Total_Price` 
        FROM 
        `receipt` WHERE Receipt_id = %s"""
        val = (currentReceiptID,)
        cursor.execute(sq,val)

        self.receiptList = list(cursor.fetchone())
        print(self.receiptList)
        sq = """SELECT `Receipt_Detail_ID`, `Receipt_id`, `Receipt_Detail_Cheque_number`,
          `Receipt_Detail_Total_Price`, `Receipt_Detail_Received_Account`, `Receipt_Detail_Branch`,
            `Receipt_Detail_Bank`,`Receipt_Detail_Cheque_Date` FROM `receipt_detail` WHERE Receipt_id = %s"""
        val = (currentReceiptID,)
        cursor.execute(sq,val)

        rows = cursor.fetchall()
        self.bankList = [list(row) for row in rows]
        print(self.bankList)

        sq = """
            SELECT c.Customer_ID
            FROM receipt r
            JOIN bill b ON r.Bill_id = b.Bill_id
            JOIN tax_invoice_delivery_note tdn ON b.Bill_id = tdn.Bill_id
            JOIN queue_order qo ON tdn.Tax_Invoice_Delivery_note_ID = qo.Tax_Invoice_Delivery_note_ID
            JOIN purchase_order po ON qo.PO_Document_Id = po.PO_Document_ID
            JOIN quotation q ON po.Quotation_ID = q.Quotation_ID
            JOIN customer c ON q.Customer_ID = c.Customer_ID
            WHERE r.Receipt_id = %s;
            """
        val = (currentReceiptID,)
        cursor.execute(sq,val)
        cusID = list(cursor.fetchall())
        cusID = cusID[0]

        sq = """
SELECT `Customer_ID`, `Customer_Address`,
 `Customer_Company_Name`, `Customer_Phone_Number`,
   `Customer_Fax`, `Customer_Tax_ID_Number`,
     `Customer_Name`, `Customer_Company_Province`,
       `Customer_Company_Branch` FROM 
       `customer` WHERE Customer_ID = %s
                """
        val = (cusID[0],)
        cursor.execute(sq,val)
        self.cusList = list(cursor.fetchall())
        self.cusList = self.cusList[0]

        self.bankListDoc = []   
        for i, item in enumerate(self.bankList,1):
                self.bankListDoc.append([item[6],item[5],item[2],item[7],item[4],item[3]])

        self.IDLabel.setText(str(self.receiptList[0]))
        self.invoiceIdLabel.setText(str(self.receiptList[2]))
        self.billIdLabel.setText(str(self.receiptList[1]))
        self.dateLabel.setText(str(self.receiptList[3]))
        self.priceLabel.setText(str(self.receiptList[4]))
        self.updateBankTable()

    def updateBankTable(self):
        
        self.bankTable.setRowCount(len(self.bankList))
        for row, item in enumerate(self.bankList):
            table_item = qtw.QTableWidgetItem(str(item[6]))
            table_item.setFlags(table_item.flags() & ~Qt.ItemIsEditable)  
            self.bankTable.setItem(row, 0, table_item)

            table_item = qtw.QTableWidgetItem(str(item[5]))
            table_item.setFlags(table_item.flags() & ~Qt.ItemIsEditable)  
            self.bankTable.setItem(row, 1, table_item)

            table_item = qtw.QTableWidgetItem(str(item[2]))
            table_item.setFlags(table_item.flags() & ~Qt.ItemIsEditable)  
            self.bankTable.setItem(row, 2, table_item)
    
            table_item = qtw.QTableWidgetItem(str(item[7]))
            table_item.setFlags(table_item.flags() & ~Qt.ItemIsEditable)  
            self.bankTable.setItem(row, 3, table_item)

            table_item = qtw.QTableWidgetItem(str(item[4]))
            table_item.setFlags(table_item.flags() & ~Qt.ItemIsEditable)  
            self.bankTable.setItem(row, 4, table_item)

            table_item = qtw.QTableWidgetItem(str(item[3]))
            table_item.setFlags(table_item.flags() & ~Qt.ItemIsEditable)  
            self.bankTable.setItem(row, 5, table_item)
            
             
    def goBack(self):
        global currentReceiptID
        currentReceiptID = 0
        documentSearchPage.fetchData()
        widget.setCurrentWidget(documentSearchPage)
    
    def makeDocument(self):
        doc = DocxTemplate("receiptTemplate.docx")
        context = ({"document_id":self.receiptList[0],"document_date":self.receiptList[3],
                   "taxNumber":"0105545084231","Customer_name":self.cusList[6],"Customer_company_name":self.cusList[2],
                   "Customer_address":self.cusList[1], "phone_number":self.cusList[3],"fax_number":self.cusList[4],"Customer_tax":self.cusList[5],"total_price":self.receiptList[4],
                   "invoice_list": self.bankListDoc, "invoice_id":self.receiptList[2],"bill_id":self.receiptList[1]})
        print(context)
        doc.render(context)
        doc.save("Receipt"+self.receiptList[0]+".docx")

        information = qtw.QMessageBox()
        information.setWindowTitle("Information")
        information.setText("Document has been made")
        information.setIcon(qtw.QMessageBox.Information)
        information.setStandardButtons(qtw.QMessageBox.Ok)
        information.setDefaultButton(qtw.QMessageBox.Ok)
        response = information.exec_()
        
        if response:
            try:       
                os.startfile("Receipt"+self.receiptList[0]+".docx")
            except AttributeError:
                subprocess.call(['open' if os.name == 'posix' else 'xdg-open', "Receipt"+self.receiptList[0]+".docx"])

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(993, 596)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 10, 771, 61))
        self.label.setStyleSheet("font: 26pt \"Arial\";")
        self.label.setObjectName("label")
        self.qIDHeadLabel = QtWidgets.QLabel(self.centralwidget)
        self.qIDHeadLabel.setGeometry(QtCore.QRect(30, 120, 171, 41))
        self.qIDHeadLabel.setStyleSheet("font: 16pt \"Arial\";")
        self.qIDHeadLabel.setObjectName("qIDHeadLabel")
        self.documentLabel = QtWidgets.QLabel(self.centralwidget)
        self.documentLabel.setGeometry(QtCore.QRect(780, 500, 161, 16))
        self.documentLabel.setObjectName("label_2")
        self.documentButton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda:self.makeDocument())
        self.documentButton.setGeometry(QtCore.QRect(780, 520, 121, 23))
        self.documentButton.setObjectName("documentButton")
        self.IDLabel = QtWidgets.QLabel(self.centralwidget)
        self.IDLabel.setGeometry(QtCore.QRect(240, 120, 201, 41))
        self.IDLabel.setStyleSheet("font: 16pt \"Arial\";\n"
"color: \"RED\";")
        self.IDLabel.setObjectName("IDLabel")
        self.qnumberHeadLabel = QtWidgets.QLabel(self.centralwidget)
        self.qnumberHeadLabel.setGeometry(QtCore.QRect(30, 230, 241, 41))
        self.qnumberHeadLabel.setStyleSheet("font: 16pt \"Arial\";")
        self.qnumberHeadLabel.setObjectName("qnumberHeadLabel")
        self.bankTable = QtWidgets.QTableWidget(self.centralwidget)
        self.bankTable.setGeometry(QtCore.QRect(360, 90, 611, 291))
        self.bankTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.bankTable.setObjectName("bankTable")
        self.bankTable.setColumnCount(6)
        self.bankTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.bankTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.bankTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.bankTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.bankTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.bankTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.bankTable.setHorizontalHeaderItem(5, item)
        self.backToHomeButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda:self.goBack())
        self.backToHomeButton.setGeometry(QtCore.QRect(80, 470, 161, 71))
        self.backToHomeButton.setStyleSheet("QPushButton {\n"
"    font: 20pt \"Arial\";\n"
"    background-color: #156d9c; \n"
"    color: white; \n"
"    padding: 15px; \n"
"}\n"
"\n"
"QPushButton:hover { \n"
"    background-color: #2891ca; \n"
"}\n"
"")
        self.backToHomeButton.setObjectName("backToHomeButton")
        self.priceLabel = QtWidgets.QLabel(self.centralwidget)
        self.priceLabel.setGeometry(QtCore.QRect(510, 410, 201, 41))
        self.priceLabel.setStyleSheet("font: 16pt \"Arial\";\n"
"color: \"RED\";")
        self.priceLabel.setObjectName("priceLabel")
        self.customerIDHeadLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.customerIDHeadLabel_2.setGeometry(QtCore.QRect(360, 410, 201, 41))
        self.customerIDHeadLabel_2.setStyleSheet("font: 16pt \"Arial\";")
        self.customerIDHeadLabel_2.setObjectName("customerIDHeadLabel_2")
        self.qnumberHeadLabel_3 = QtWidgets.QLabel(self.centralwidget)
        self.qnumberHeadLabel_3.setGeometry(QtCore.QRect(30, 280, 241, 41))
        self.qnumberHeadLabel_3.setStyleSheet("font: 16pt \"Arial\";")
        self.qnumberHeadLabel_3.setObjectName("qnumberHeadLabel_3")
        self.qnumberHeadLabel_5 = QtWidgets.QLabel(self.centralwidget)
        self.qnumberHeadLabel_5.setGeometry(QtCore.QRect(30, 180, 241, 41))
        self.qnumberHeadLabel_5.setStyleSheet("font: 16pt \"Arial\";")
        self.qnumberHeadLabel_5.setObjectName("qnumberHeadLabel_5")
        self.invoiceIdLabel = QtWidgets.QLabel(self.centralwidget)
        self.invoiceIdLabel.setGeometry(QtCore.QRect(240, 180, 201, 41))
        self.invoiceIdLabel.setStyleSheet("font: 16pt \"Arial\";\n"
"color: \"RED\";")
        self.invoiceIdLabel.setObjectName("invoiceIdLabel")
        self.billIdLabel = QtWidgets.QLabel(self.centralwidget)
        self.billIdLabel.setGeometry(QtCore.QRect(240, 230, 201, 41))
        self.billIdLabel.setStyleSheet("font: 16pt \"Arial\";\n"
"color: \"RED\";")
        self.billIdLabel.setObjectName("billIdLabel")
        self.dateLabel = QtWidgets.QLabel(self.centralwidget)
        self.dateLabel.setGeometry(QtCore.QRect(240, 280, 201, 41))
        self.dateLabel.setStyleSheet("font: 16pt \"Arial\";\n"
"color: \"RED\";")
        self.dateLabel.setObjectName("dateLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 993, 21))
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
        self.label.setText(_translate("MainWindow", "Receipt  Detail"))
        self.qIDHeadLabel.setText(_translate("MainWindow", "ID :"))
        self.IDLabel.setText(_translate("MainWindow", "QID001"))
        self.qnumberHeadLabel.setText(_translate("MainWindow", "Bill ID:"))
        item = self.bankTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Bank"))
        item = self.bankTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Branch"))
        item = self.bankTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Cheque Number"))
        item = self.bankTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Cheque Date"))
        item = self.bankTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Bank Number"))
        item = self.bankTable.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Amount"))
        self.backToHomeButton.setText(_translate("MainWindow", "Back"))
        self.priceLabel.setText(_translate("MainWindow", "CID001"))
        self.customerIDHeadLabel_2.setText(_translate("MainWindow", "Total Price :"))
        self.qnumberHeadLabel_3.setText(_translate("MainWindow", "Date"))
        self.qnumberHeadLabel_5.setText(_translate("MainWindow", "Invoice / Delivery ID:"))
        self.invoiceIdLabel.setText(_translate("MainWindow", "QID001"))
        self.billIdLabel.setText(_translate("MainWindow", "QID001"))
        self.dateLabel.setText(_translate("MainWindow", "QID001"))
        self.documentLabel.setText(_translate("MainWindow", "Get Document Here"))
        self.documentButton.setText(_translate("MainWindow", "Get Document"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()

    
    createQuotationPage = createQuotation()
    widget.addWidget(createQuotationPage)

    finishedDeliveryPagePage = finishedDeliveryPage()
    widget.addWidget(finishedDeliveryPagePage)
    
    deliveryDetailPage = deliveryDetail()
    widget.addWidget(deliveryDetailPage)

    deliverPagePage = deliverPage()
    widget.addWidget(deliverPagePage)

    stockPagePage = stockPage()
    widget.addWidget(stockPagePage)

    receiptDetailPage = receiptDetail()
    widget.addWidget(receiptDetailPage)

    finishOrderPage = finishOrder()
    widget.addWidget(finishOrderPage)

    declineOrderPage = declineOrder()
    widget.addWidget(declineOrderPage)

    loginPage = login()
    widget.addWidget(loginPage)

    billDetailPage = billDetail()
    widget.addWidget(billDetailPage)

    documentSearchPage = docSearch()
    widget.addWidget(documentSearchPage)

    quotationDetailPage = quotationDetail()
    widget.addWidget(quotationDetailPage)

    orderDetailPage = orderDetail()
    widget.addWidget(orderDetailPage)

    createDeliveryPage = createDelivery()
    widget.addWidget(createDeliveryPage)

    invoiceDetailPage = invoiceDetail()
    widget.addWidget(invoiceDetailPage)

    createTaxInvoicePage = createTaxInvoice()
    widget.addWidget(createTaxInvoicePage)

    mainPagePage = mainPage()
    widget.addWidget(mainPagePage)

    createBillPage = createBill()
    widget.addWidget(createBillPage)

    createReceiptPage = createReceipt()
    widget.addWidget(createReceiptPage)

    createOrderPage = createOrder()
    widget.addWidget(createOrderPage)

    MainWindow = QtWidgets.QMainWindow()

    widget.setCurrentWidget(loginPage)

    screen = app.primaryScreen()
    screen_size = screen.size()
    widget.resize(1200, 800)

    widget.show()
    sys.exit(app.exec_())

