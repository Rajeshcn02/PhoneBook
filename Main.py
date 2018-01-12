import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MainWidget(QWidget):
    def __init__(self):
        super(MainWidget, self).__init__()
        self.initUI()
        # self.center()
        self.contact = ['','','','','','','','']
        self.contacts = [self.contact]

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)


    #initializing the groupbox
        groupBoxMenu = QGroupBox('&Choose option')
    #initializing the subgrid
        gridMenu = QGridLayout()
        self.setLayout(gridMenu)
    #btn
        LookupBtn = QPushButton("Look up")
        LookupBtn.clicked.connect(self.lookup)
        AddBtn = QPushButton("Add")
        AddBtn.clicked.connect(self.add)
        QuitBtn = QPushButton("Quit")
        QuitBtn.clicked.connect(QCoreApplication.instance().quit)
    #positioning
        gridMenu.addWidget(LookupBtn,0,0)
        gridMenu.addWidget(AddBtn,0,1)
        gridMenu.addWidget(QuitBtn,0,2)
    #making the groupbox
        groupBoxMenu.setLayout(gridMenu)
        BoxMenuLayout = QGridLayout()
        BoxMenuLayout.addWidget(groupBoxMenu)


    # .... 2nd groupbox.........
        groupBoxShow = QGroupBox('&Entries')
        gridShow = QGridLayout()
        self.setLayout(gridShow)
        self.fname = QLineEdit()
        self.lname = QLineEdit()
        self.street = QLineEdit()
        self.city = QLineEdit()
        self.state = QLineEdit()
        self.zip = QLineEdit()
        self.home = QLineEdit()
        self.mobile = QLineEdit()
        labelfname = QLabel("First Name")
        labellname = QLabel("Last Name")
        labelstreet = QLabel("Street")
        labelcity = QLabel("City")
        labelstate = QLabel("State")
        labelzip = QLabel("ZIP")
        labelhome = QLabel("Home")
        labelmobile = QLabel("Mobile")

        gridShow.addWidget(labelfname,0,0)
        gridShow.addWidget(self.fname,0,1)
        gridShow.addWidget(labellname,0,2)
        gridShow.addWidget(self.lname,0,3)
        gridShow.addWidget(labelstreet,1,0)
        gridShow.addWidget(self.street,1,1)
        gridShow.addWidget(labelcity,1,2)
        gridShow.addWidget(self.city,1,3)
        gridShow.addWidget(labelstate,1,4)
        gridShow.addWidget(self.state,1,5)
        gridShow.addWidget(labelzip,1,6)
        gridShow.addWidget(self.zip,1,7)
        gridShow.addWidget(labelhome,2,0)
        gridShow.addWidget(self.home,2,1)
        gridShow.addWidget(labelmobile,2,2)
        gridShow.addWidget(self.mobile,2,3)

        groupBoxShow.setLayout(gridShow)
        BoxMenuLayout = QGridLayout()
        BoxMenuLayout.addWidget(groupBoxShow)

    # .........Big GrouBox ..................
        grid.addWidget(groupBoxMenu, 1, 0)
        grid.addWidget(groupBoxShow, 0, 0)
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def lookup(self):
        lastname = self.lname.text()
        found = False
        rightcontact = []
        while (found == False):
            for contact in self.contacts:
                if (lastname == contact[1]):
                    rightcontact = contact
                    found = True

        if (found == True):
            self.fname.setText(rightcontact[0])
            self.street.setText(rightcontact[2])
            self.city.setText(rightcontact[3])
            self.state.setText(rightcontact[4])
            self.zip.setText(rightcontact[5])
            self.home.setText(rightcontact[6])
            self.mobile.setText(rightcontact[7])
        else:
            print("no such contact")

    def add(self):
        Fname = self.fname.text()
        Lname = self.lname.text()
        St = self.street.text()
        City = self.city.text()
        State = self.state.text()
        Zip = self.zip.text()
        Home = self.home.text()
        Mobile = self.mobile.text()
        print(Fname,Lname,St,City,State,Zip,Home,Mobile)
        self.contact = [Fname,Lname,St,City,State,Zip,Home,Mobile]
        self.contacts.append(self.contact)
        print(self.contacts)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWidget()
    sys.exit(app.exec_())