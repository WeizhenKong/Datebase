# Import Needed Libraries
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

# Define Form as a Class
class Form( QDialog):
    # Form Constructor
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        cryptokey = 50
        self.pbuttonName = QPushButton("Developer's Name")
        self.lineeditName = QLineEdit("")
        self.pbuttonSemester = QPushButton("Current Semester")
        self.lineeditSemester = QLineEdit("")
        self.pbutton0 = QPushButton("Load File")
        self.lineedit0 = QLineEdit("Enter Input File Name")
        self.pbutton1 = QPushButton("Show Input Row Count")
        self.lineedit1 = QLineEdit("Total Input Rows Parsed")
        self.pbutton2 = QPushButton("Table Rows Count")
        self.lineedit2 = QLineEdit("Enter Table Name")
        self.pbutton3 = QPushButton("List Table")
        self.lineedit3 = QLineEdit("Enter Table Name")
        self.pbutton4 = QPushButton("Customer SQL")
        self.lineedit4 = QLineEdit("Enter Custom SQL")
        self.pbutton5 = QPushButton("Distince Values")
        self.lineedit5 = QLineEdit("Enter Tablename, ColumnName")
        self.pbuttonQuit = QPushButton("Quit")
        layout = QVBoxLayout()
        layout.addWidget(self.pbuttonName)
        layout.addWidget(self.lineeditName)
        layout.addWidget(self.pbuttonSemester)
        layout.addWidget(self.lineeditSemester)       
        layout.addWidget(self.pbutton0)
        layout.addWidget(self.lineedit0)
        layout.addWidget(self.pbutton1)
        layout.addWidget(self.lineedit1)
        layout.addWidget(self.pbutton2)
        layout.addWidget(self.lineedit2)
        layout.addWidget(self.pbutton3)
        layout.addWidget(self.lineedit3)
        layout.addWidget(self.pbutton4)
        layout.addWidget(self.lineedit4)
        layout.addWidget(self.pbutton5)
        layout.addWidget(self.lineedit5)
        layout.addWidget(self.pbuttonQuit)
        self.setLayout(layout)
        ck = cryptokey
        self.lineeditName.setFocus()
        self.connect(self.pbuttonName, SIGNAL("clicked()"),self.buttonNamePressed)
        self.connect(self.pbuttonSemester, SIGNAL("clicked()"),self.buttonSemesterPressed)
        self.connect(self.pbutton0, SIGNAL("clicked()"),self.button0Pressed)
        self.connect(self.pbutton1, SIGNAL("clicked()"),self.button1Pressed)
        self.connect(self.pbutton2, SIGNAL("clicked()"),self.button2Pressed)
        self.connect(self.pbutton3, SIGNAL("clicked()"),self.button3Pressed)
        self.connect(self.pbutton4, SIGNAL("clicked()"),self.button4Pressed)
        self.connect(self.pbutton5, SIGNAL("clicked()"),self.button5Pressed)
        self.connect(self.pbuttonQuit, SIGNAL("clicked()"),self.buttonQuitPressed)
        s = chr(ck + 20) + chr(ck) + chr(ck-2) +chr(ck-1)+chr(ck+6)
        self.setWindowTitle(s)
    # Form Methods
    def MakeDbfile(self):
        import sqlite
        if not os.path.exists("info.db"):
            conn=sqlite3.connect("Kong.db")
            c=conn.cursor()
            c.execute('''Create TABLE Kong(Trxid int not null, Doy int, Dow varchar(50), Holiday boolean,Weather varchar(50),Storeid int, Location varchar(50), Elevation varchar(50), Size varchar(50), Mgrid int,MgrName varchar(50), Grade varchar(50), Years int, Soupid int, Type varchar(50),Vender varchar(50), Mode varchar(50), Style varchar(50), Ptomold int, Medium varchar(50),Target varchar(50), Interval varchar(50), Sales double)''')
            conn.commit()
            conn.close
        conn=sqlite3.connect("Kong.db")
        c=conn.cursor()
        c.execute("delete from Kong;")
        conn.commit()
        conn.close()
    import sqlite3
    conn=sqlite3.connect(fileName)
    c=conn.cursor()
    ret=c.execute("select * from Kong")
    for row in ret:
        print([row1])
    conn.close()
    def buttonNamePressed(self):
        self.lineeditName.setText("My Name is Weizhen Kong")
    def buttonSemesterPressed(self):
        self.lineeditSemester.setText("F2018")
    def button0Pressed(self):
        global filename
        filename=(self.lineedit0.text())
        import os
        if os.path.exists(filename) is True:
            import sqlite3
            
            def CreateTables():
                cur.execute("Drop Table if Exists Kong")
                cur.execute("create table Kong(Trxid int not null, Doy int, Dow str, Holiday int,Weather str,Storeid int, Location str, Elevation str, Size str, Mgrid int,MgrName str, Grade str, Years int, Soupid number, Type str,Vender str, Mode str, Style str, Ptomold int, Medium str,Target str, Interval str, Sales int);")
            def Kong(record):
                Trxid=int(record[0])
                Doy=int(record[1])
                Dow=int(record[2])
                Holiday=int(record[3])
                Weather=int(record[4])
                Storeid=int(record[5])
                Location=int(record[6])
                Elevation=int(record[7])
                Size=int(record[8])
                Mgrid=int(record[9])
                MgrName=int(record[10])
                Grade=int(record[11])
                Years=int(record[12])
                Soupid=int(record[13])
                Type=int(record[14])
                Vender=int(record[15])
                Mode=int(record[16])
                style=int(record[17])
                Ptomold=int(record[18])
                Medium=int(record[19])
                Target=int(record[20])
                Interval=int(record[21])
                Sales=float(record[22])
                row=[Trxid,Doy,Dow,Holiday,Weather,Storeid,Location,Elevation,Size,Mgrid,MgrName,Grade,Years,Soupid,Type,Vendor,Mode,Style,Ptomold,Medium,Target,Interval,Sales]
                cur.executemany("INSERT or ignore INTO Kong VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",row)
                print"Row Inserted:",row
                
            open (filename,"r")
            conn=sqlite3.connect("Kong.db")
            cur=conn.cursor()
            CreateTables()
            f=open(filename,"r")
            linecount=0
            line=f.readline()
            while line!="" and linecount<5:
                linecount=linecount +1
                line=line.replace("\n","")
                linelist=line.split("\t")
                line=f.readline()
            conn.commit()
            f.close()

            self.lineedit0.setText("File Parsed")
        else:
            self.lineedit0.setText("File Not Opened")       
    def button1Pressed(self):
        f=open(filename,"r")
        count=0
        line=f.readline()
        while line !="":
            if line.strip():
                count=count+1
            line=f.readline()
        line=f.readline()
        f.close()
        x2=str(count)
        self.lineedit1.setText(x2)
    def button2Pressed(self):
        self.lineedit2.setText("xxxx non empty lines counted")
    def button3Pressed(self):
        self.lineedit3.setText("xxxx words counted")
    def button4Pressed(self):
        self.lineedit4.setText("xxx occurrences of _ counted")
    def button5Pressed(self):
        self.lineedit5.setText("xxx occurrences of _ counted")
    def buttonQuitPressed(self):
        self.done(1)
        app.quit()
# End of Form Class Definition

app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
