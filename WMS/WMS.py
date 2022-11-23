import qrcode, serial, time, sys, os, sqlite3, threading

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtGui import *
from PyQt5 import QtCore

class ThreebyThree(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        #################### Change Path ####################
        self.ui = loadUi("/Users/ppr/Desktop/Project/AUTOMATEDWAREHOUSE/allData/GUI/3x3Rack.ui", self)
        self.A1 = self.ui.A1
        self.A2 = self.ui.A2
        self.A3 = self.ui.A3
        self.B1 = self.ui.B1
        self.B2 = self.ui.B2
        self.B3 = self.ui.B3
        self.C1 = self.ui.C1
        self.C2 = self.ui.C2
        self.C3 = self.ui.C3
        self.checkData()
    
    def checkData(self):
        self.opensqlSection = str(self.parent.opensqlSection)
        self.connection = sqlite3.connect("automatedwarehouseDatabase.db")  
        if (self.opensqlSection == "Section 1"):
            queryRack = "SELECT * FROM Warehouse WHERE Section = '1' and TimeOut = '-'"
        elif (self.opensqlSection == "Section 2"):
            queryRack = "SELECT * FROM Warehouse WHERE Section = '2' and TimeOut = '-'"
        elif (self.opensqlSection == "Section 3"):
            queryRack = "SELECT * FROM Warehouse WHERE Section = '3' and TimeOut = '-'"
        allRack = self.connection.execute(queryRack).fetchall()
        self.connection.commit()
        for rack in allRack:
            productCode = rack[2]
            if (rack[1] == "A1"):
                self.A1.setText(productCode)
                self.A1.setAlignment(QtCore.Qt.AlignCenter)
            elif (rack[1] == "A2"):
                self.A2.setText(productCode)
                self.A2.setAlignment(QtCore.Qt.AlignCenter)
            elif (rack[1] == "A3"):
                self.A3.setText(productCode)
                self.A3.setAlignment(QtCore.Qt.AlignCenter)
            elif (rack[1] == "B1"):
                self.B1.setText(productCode)
                self.B1.setAlignment(QtCore.Qt.AlignCenter)
            elif (rack[1] == "B2"):
                self.B2.setText(productCode)
                self.B2.setAlignment(QtCore.Qt.AlignCenter)
            elif (rack[1] == "B3"):
                self.B3.setText(productCode)
                self.B3.setAlignment(QtCore.Qt.AlignCenter)
            elif (rack[1] == "C1"):
                self.C1.setText(productCode)
                self.C1.setAlignment(QtCore.Qt.AlignCenter)
            elif (rack[1] == "C2"):
                self.C2.setText(productCode)
                self.C2.setAlignment(QtCore.Qt.AlignCenter)
            elif (rack[1] == "C3"):
                self.C3.setText(productCode)
                self.C3.setAlignment(QtCore.Qt.AlignCenter)

class FourbyFour(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.connection = self.parent.connection
        #################### Change Path ####################
        self.ui = loadUi("/Users/ppr/Desktop/Project/AUTOMATEDWAREHOUSE/allData/GUI/4x4Rack.ui", self)
        self.A1 = self.ui.A1
        self.A2 = self.ui.A2
        self.A3 = self.ui.A3
        self.A4 = self.ui.A4
        self.B1 = self.ui.B1
        self.B2 = self.ui.B2
        self.B3 = self.ui.B3
        self.B4 = self.ui.B4
        self.C1 = self.ui.C1
        self.C2 = self.ui.C2
        self.C3 = self.ui.C3
        self.C4 = self.ui.C4
        self.D1 = self.ui.D1
        self.D2 = self.ui.D2
        self.D3 = self.ui.D3
        self.D4 = self.ui.D4
        self.checkData(self.parent.opensqlSection)
    
    def checkData(self, dataSection):
        self.opensqlSection = str(self.parent.opensqlSection)
        self.connection = sqlite3.connect("automatedwarehouseDatabase.db")  
        if (self.opensqlSection == "Section 1"):
            queryRack = "SELECT * FROM Warehouse WHERE Section = '1' and TimeOut = '-'"
        elif (self.opensqlSection == "Section 2"):
            queryRack = "SELECT * FROM Warehouse WHERE Section = '2' and TimeOut = '-'"
        elif (self.opensqlSection == "Section 3"):
            queryRack = "SELECT * FROM Warehouse WHERE Section = '3' and TimeOut = '-'"
        allRack = self.connection.execute(queryRack).fetchall()
        self.connection.commit()
        for rack in allRack:
            productCode = rack[2]
            if (rack[1] == "A1"):
                self.A1.setText(productCode)
                self.A1.setAlignment(QtCore.Qt.AlignCenter)
            elif (rack[1] == "A2"):
                self.A2.setText(productCode)
                self.A2.setAlignment(QtCore.Qt.AlignCenter)
            elif (rack[1] == "A3"):
                self.A3.setText(productCode)
                self.A3.setAlignment(QtCore.Qt.AlignCenter)
            elif (rack[1] == "A4"):
                self.A3.setText(productCode)
                self.A3.setAlignment(QtCore.Qt.AlignCenter)
            elif (rack[1] == "B1"):
                self.B1.setText(productCode)
                self.B1.setAlignment(QtCore.Qt.AlignCenter)
            elif (rack[1] == "B2"):
                self.B2.setText(productCode)
                self.B2.setAlignment(QtCore.Qt.AlignCenter)
            elif (rack[1] == "B3"):
                self.B3.setText(productCode)
                self.B3.setAlignment(QtCore.Qt.AlignCenter)
            elif (rack[1] == "B4"):
                self.B3.setText(productCode)
                self.B3.setAlignment(QtCore.Qt.AlignCenter)
            elif (rack[1] == "C1"):
                self.C1.setText(productCode)
                self.C1.setAlignment(QtCore.Qt.AlignCenter)
            elif (rack[1] == "C2"):
                self.C2.setText(productCode)
                self.C2.setAlignment(QtCore.Qt.AlignCenter)
            elif (rack[1] == "C3"):
                self.C3.setText(productCode)
                self.C3.setAlignment(QtCore.Qt.AlignCenter)
            elif (rack[1] == "C4"):
                self.C3.setText(productCode)
                self.C3.setAlignment(QtCore.Qt.AlignCenter)
            elif (rack[1] == "D1"):
                self.C1.setText(productCode)
                self.C1.setAlignment(QtCore.Qt.AlignCenter)
            elif (rack[1] == "D2"):
                self.C2.setText(productCode)
                self.C2.setAlignment(QtCore.Qt.AlignCenter)
            elif (rack[1] == "D3"):
                self.C3.setText(productCode)
                self.C3.setAlignment(QtCore.Qt.AlignCenter)
            elif (rack[1] == "D4"):
                self.C3.setText(productCode)
                self.C3.setAlignment(QtCore.Qt.AlignCenter)

class WMS(QMainWindow):
    def __init__(self):
        try:
            super().__init__()
            self.connection = sqlite3.connect("automatedwarehouseDatabase.db")  
            self.cursor_ = self.connection.cursor()
            self.cursor_.execute('''CREATE TABLE IF NOT EXISTS Warehouse (Section      TEXT     NOT NULL, 
                                Rack          TEXT     NOT NULL, ProductCode   TEXT     NOT NULL, 
                                Quantity      TEXT     NOT NULL, Weight        TEXT     NOT NULL, 
                                QRTimestamp   TEXT     NOT NULL, TimeIn        TEXT     NOT NULL, 
                                TimeOut       TEXT     NOT NULL)''') 
            self.connection.commit()
            #################### Change port ####################
            self.ser = serial.Serial('/dev/cu.usbmodem113301', 9600)
        except:
            pass
        #################### Change Path ####################
        self.ui = loadUi("/Users/ppr/Desktop/Project/AUTOMATEDWAREHOUSE/allData/GUI/AutomatedWarehouse.ui", self)
        self.productcodeList = ["PCA001", "PCA002", "PCA003", "PCA004", "PCA005", "PCA006", "PCA007", "PCA008", "PCA009"]
        self.seq = 1
        self.weight = 80
        self.paramsList = []
        self.listdataSize = []
        self.listdataSection = []
        self.opensqlSection = ""
        self.productCode = self.ui.product_1
        self.quantity = self.ui.quantity_1
        self.generate = self.ui.generate_1
        self.section1 = self.ui.section_1
        self.rack = self.ui.rack_1
        self.time = self.ui.time_1
        self.QR = self.ui.QR_1 
        self.table = self.ui.table_2
        self.section3 = self.ui.section_3
        self.createSection = self.ui.createSection_3
        self.btn_page1 = self.ui.btn_page_1
        self.btn_page2 = self.ui.btn_page_2
        self.btn_page3 = self.ui.btn_page_3
        self.sizeText = self.ui.sizeText_3
        self.sectionTable = self.ui.sectionTable_3
        self.btn_page1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_1))
        self.btn_page2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
        self.btn_page3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_3))
        self.sectionTable.doubleClicked.connect(self.doubleClicked)
        self.generate.clicked.connect(self.generateQR)
        self.btn_page2.clicked.connect(self.dataBase)
        self.btn_page2.clicked.connect(self.receivedInsert)
        self.btn_page3.clicked.connect(self.readText)
        self.btn_page3.clicked.connect(self.receivedInsert)
        self.createSection.clicked.connect(self.fuccreateSection)
        self.statusBar().setStyleSheet("color: white")
        self.event = threading.Event()
        self.setScreen()
        self.readText()
        self.dataBase()
        self.wait2receivedData()
    
    def doubleClicked(self):
        item = str(self.sectionTable.model().data(self.sectionTable.selectedIndexes()[0]))
        self.opensqlSection, dataSize = item.split(", ")
        if (dataSize == "Size 3x3"):
            self.connect3by3()
        elif (dataSize == "Size 4x4"):
            self.connect4by4()
    
    def connect3by3(self):
        window3by3 = ThreebyThree(self)
        cp = QDesktopWidget().availableGeometry().center()
        fg_blue = window3by3.frameGeometry()
        fg_blue.moveCenter(cp)
        fg_blue.setX(fg_blue.x() + 490)
        fg_blue.setY(fg_blue.y() + 20)
        window3by3.move(fg_blue.topLeft())
        window3by3.show()
    
    def connect4by4(self):
        window4by4 = FourbyFour(self)
        cp = QDesktopWidget().availableGeometry().center()
        fg_blue = window4by4.frameGeometry()
        fg_blue.moveCenter(cp)
        fg_blue.setX(fg_blue.x() + 490)
        fg_blue.setY(fg_blue.y() + 20)
        window4by4.move(fg_blue.topLeft())
        window4by4.show()
    
    def wait2receivedData(self):
        try:
            self.received = threading.Thread(target = self.receivedData)
            self.received.start()
        except:
            pass
    
    def receivedData(self):
        try:
            while True:
                if self.ser.is_open == True:
                    if self.ser.in_waiting:
                        readLine = self.ser.readline().decode("utf-8")
                        data = readLine.rstrip()
                        dataList = data.split(", ")
                        if len(dataList) == 6:
                            dataSection, dataRack, dataProductCode, dataQuantity, dataWeight, dataQRTimestamp = dataList
                            if (dataSection == "1" or dataSection == "2"):
                                if (dataProductCode in self.productcodeList):
                                    print("Data: ", str(dataSection) + ", " + str(dataRack) + ", " + str(dataProductCode) + ", " + str(dataQuantity)  + ", " + str(dataWeight)  + ", " + str(dataQRTimestamp))
                                    params = (str(dataSection), str(dataRack), str(dataProductCode), str(dataQuantity), str(dataWeight), str(dataQRTimestamp), time.strftime("%m/%d/%Y %H:%M:%S", time.localtime()), "-")
                                    self.paramsList.append(params)
                        elif len(dataList) == 1:
                            calWeight = float(dataList[0]) * 1000
                            if (int(calWeight)>0):
                                self.weight = int(calWeight)
                                print("Weight: ", self.weight)
                            else:
                                self.weight = 999
                                self.statusBar().showMessage("[ ERROR: Weight measurement ]")
                        else:
                            self.weight = 999
        except:
            pass
    
    def generateQR(self, rack):
        try:
            self.statusBar().clearMessage()
            section_ = self.section1.text()
            productCode_ = self.productCode.text()
            q_ = self.quantity.text()
            q = q_.split()
            quantity = int(q[1])
            weight = int(self.weight)
            if (weight != 999):
                if (1 <= quantity <= 15 and 0 <= weight <= 100):
                    section_ = section_.split()
                    section = section_[1]
                    rack = self.calRack(quantity, weight)
                    if (rack != "FULL"):
                        if (section == '1' or section == '2'):
                            productCode_ = productCode_.split()
                            productCode = productCode_[2]
                            if (productCode in self.productcodeList):
                                timeQR = time.strftime("%m/%d/%Y %H:%M:%S", time.localtime())
                                rackText = "Rack: " + rack
                                data = str(section) + ", " + str(rack) + ", " + str(productCode) + ", " + str(quantity) + ", " + str(self.weight) + ", " +  str(timeQR)
                                qr = qrcode.QRCode(version = 40, error_correction = qrcode.constants.ERROR_CORRECT_H, box_size = 100, border = 5)
                                qr.add_data(data)
                                qr.make(fit = True)
                                img = qrcode.make(data)
                                #################### Change Path ####################
                                os.chdir("/Users/ppr/Desktop/Project/AUTOMATEDWAREHOUSE/allData/qrcodeFolder")
                                save_img = img.resize((400, 400))
                                save_img.save("QRCode_{}.PNG".format(self.seq))
                                save_img = img.resize((200, 200))
                                save_img.save("QRCode_{}.PDF".format(self.seq))
                                #################### Change Path ####################
                                pic_path_PNG = "/Users/ppr/Desktop/Project/AUTOMATEDWAREHOUSE/allData/qrcodeFolder" + '/' + "QRCode_{}.PNG".format(self.seq)
                                #################### Change Path ####################
                                pic_path_PDF = "/Users/ppr/Desktop/Project/AUTOMATEDWAREHOUSE/allData/qrcodeFolder" + '/' + "QRCode_{}.PDF".format(self.seq)
                                self.QR.setPixmap(QPixmap(pic_path_PNG))
                                self.time.setText(timeQR)
                                self.time.setAlignment(QtCore.Qt.AlignCenter)
                                self.rack.setText(rackText)
                                self.rack.setAlignment(QtCore.Qt.AlignCenter)
                                self.statusBar().showMessage(data)
                                self.seq += 1
                                #################### Change Printer ####################
                                os.system("lp -d HP_Color_LaserJet_MFP_M277dw -o scaling=75 -o media=A5,Upper {}".format(pic_path_PDF))
                            else:
                                self.statusBar().showMessage("[ ERROR: Wrong product code ]")
                        else:
                            self.statusBar().showMessage("[ ERROR: Wrong section ]")
                    else:
                        self.statusBar().showMessage("[ ERROR: Full rack ]")
                else:
                    self.statusBar().showMessage("[ ERROR: Wrong quantity or weight]")
            else:
                self.statusBar().showMessage("[ ERROR: Weight measurement ]")
        except:
            pass
    
    def calRow(self, List, Row):
        for rack in Row:
            if rack in List:
                if rack == Row[8]:
                    return "FULL"
                continue
            else:
                return rack
    
    def calRack(self, quantity, weight):
        try:
            List = self.checkRack()
            if (11 <= quantity <= 15):
                Row3 = ["A3", "B3", "C3"]
                Row2 = ["A2", "B2", "C2"]
                Row1 = ["A1", "B1", "C1"]
                if (61 <= weight <= 90):
                    return self.calRow(List, Row1+Row2+Row3)
                elif (31 <= weight <= 60):
                    return self.calRow(List, Row2+Row1+Row3)
                elif (0 <= weight <= 30):
                    return self.calRow(List, Row3+Row2+Row1)
            elif (6 <= quantity <= 10):
                Row3 = ["B3", "C3", "A3"]
                Row2 = ["B2", "C2", "A2"]
                Row1 = ["B1", "C1", "A1"]
                if (61 <= weight <= 90):
                    return self.calRow(List, Row1+Row2+Row3)
                elif (31 <= weight <= 60):
                    return self.calRow(List, Row2+Row1+Row3)
                elif (0 <= weight <= 30):
                    return self.calRow(List, Row3+Row2+Row1)
            elif (1 <= quantity <= 5):
                Row3 = ["C3", "A3", "B3"]
                Row2 = ["C2", "A2", "B2"]
                Row1 = ["C1", "A1", "B1"]
                if (61 <= weight <= 90):
                    return self.calRow(List, Row1+Row2+Row3)
                elif (31 <= weight <= 60):
                    return self.calRow(List, Row2+Row1+Row3)
                elif (0 <= weight <= 30):
                    return self.calRow(List, Row3+Row2+Row1)
        except:
            pass
    
    def checkRack(self):
        try:
            queryRack = "SELECT * FROM Warehouse WHERE Section = '2' and TimeOut = '-'"
            allRack = self.connection.execute(queryRack).fetchall()
            rackList = []
            for rack in allRack:
                rack_ = rack[1]
                rackList.append(rack_)
            return rackList
        except:
            pass
    
    def dataBase(self):
        try:
            self.statusBar().clearMessage()
            query = "SELECT * FROM Warehouse"			
            self.cursor = self.connection.execute(query)
            row_len = []
            for i in self.cursor:
                row_len.append(len(i))
            if len(row_len) != 0:
                self.col_num = max(row_len)
                self.table.setRowCount(0)	
                self.table.setColumnCount(int(self.col_num))
                self.cursor = self.connection.execute(query)
                for row, row_data in enumerate(self.cursor):
                    self.table.insertRow(row)
                    for col, col_data in enumerate(row_data):
                        item = QTableWidgetItem(str(col_data)) 
                        item.setTextAlignment(int(Qt.AlignHCenter | Qt.AlignVCenter))
                        self.table.setItem(row, col, item)
                self.connection.commit()
        except:
            pass
    
    def insertDatebase(self, params):
        self.statusBar().clearMessage()
        self.table.clearContents()
        self.connection.execute("INSERT INTO Warehouse (Section, Rack, ProductCode, Quantity, Weight, QRTimestamp, TimeIn, TimeOut) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", params)
        self.connection.commit()
        self.dataBase()
    
    def receivedInsert(self):
        if (len(self.paramsList) != 0):
            for param in self.paramsList:
                self.insertDatebase(param)
            self.paramsList = []
    
    def readText(self):
        try:
            #################### Change Path ####################
            f_ = open("/Users/ppr/Desktop/Project/AUTOMATEDWAREHOUSE/allData/GUI/Section.txt", "r")
            if (f_.mode == 'r'):
                data = f_.read()
                data_into_list = data.split("\n")
            f_.close()
            rowCount = int(len(data_into_list)) - 1
            self.sectionTable.setColumnCount(1)
            self.sectionTable.setRowCount(rowCount)
            if len(data_into_list) != 0:
                for index in range(rowCount):
                    item = QTableWidgetItem(data_into_list[index]) 
                    item.setTextAlignment(int(Qt.AlignHCenter | Qt.AlignVCenter))
                    self.sectionTable.setItem(index, 0, item)
                    dataSection, _ = data_into_list[index].split(", ")
                    self.listdataSection.append(dataSection)
        except:
            pass
    
    def fuccreateSection(self):
        try:
            #################### Change Path ####################
            f = open("/Users/ppr/Desktop/Project/AUTOMATEDWAREHOUSE/allData/GUI/Section.txt", "a+")
            size = self.sizeText.text()
            section_ = self.section3.text()
            if (section_ not in self.listdataSection):
                if (size == "Size 3x3" or size == "Size 4x4"):
                    f.write("{}, {}\n".format(section_, size))
                    f.close()
                    self.listdataSection = []
                    self.listdataSize = []
                    #################### Change Path ####################
                    f_ = open("/Users/ppr/Desktop/Project/AUTOMATEDWAREHOUSE/allData/GUI/Section.txt", "r")
                    if (f_.mode == 'r'):
                        data = f_.read()
                        data_into_list = data.split("\n")
                    f_.close()
                    rowCount = int(len(data_into_list)) - 1
                    if len(data_into_list) != 0:
                        for index in range(rowCount):
                            dataSection, dataSize = data_into_list[index].split(", ")
                            self.listdataSection.append(dataSection)
                            self.listdataSize.append(dataSize)
                    self.sectionTable.setColumnCount(1)
                    self.sectionTable.setRowCount(rowCount)
                    if len(data_into_list) != 0:
                        for index in range(rowCount):
                            item = QTableWidgetItem(data_into_list[index]) 
                            item.setTextAlignment(int(Qt.AlignHCenter | Qt.AlignVCenter))
                            self.sectionTable.setItem(index, 0, item)
                else:
                    self.statusBar().showMessage("[ ERROR: Not available for this size ]")
            else:
                self.statusBar().showMessage("[ ERROR: This section already exists ]")
        except:
            pass
    
    def setScreen(self):
        center = QDesktopWidget().availableGeometry().center()
        fg_app = self.frameGeometry()
        fg_app.moveCenter(center)
        fg_app.setY(fg_app.y())
        self.move(fg_app.topLeft())
    
    def closeEvent(self, event):
        try:
            self.event.set()
            i = 1
            int_seq = int(self.seq)
            for i in range(1, int_seq):
                #################### Change Path ####################
                pic = "/Users/ppr/Desktop/Project/AUTOMATEDWAREHOUSE/allData/qrcodeFolder" + '/' + "QRCode_{}.PNG".format(i)
                #################### Change Path ####################
                pic_pdf = "/Users/ppr/Desktop/Project/AUTOMATEDWAREHOUSE/allData/qrcodeFolder" + '/' + "QRCode_{}.PDF".format(i)
                os.remove(pic)
                os.remove(pic_pdf)
                i = i + 1
            self.connection.close()
        except:
            pass
        event.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    App = WMS()
    App.show()
    app.exec_()