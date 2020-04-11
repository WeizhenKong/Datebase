# Import Needed Libraries
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sqlite3
conn=sqlite3.connect("Kong.db")
cur=conn.cursor()

def CreateTables():
    cur.execute("Drop Table if Exists Sales")
    cur.execute("""create table sales
                (TrxId int not null,DoY int,StoreID int,
                SoupID int,PromoId int,Sales number, Unique(TrxId));""")
  
    
    cur.execute("Drop Table if Exists Days")
    cur.execute("""create table Days
                (DoY int not null,DoW text,Holiday int, Weather text,Unique(DoY));""")
   
    
    cur.execute("Drop Table if Exists Managers")
    cur.execute("""create table managers
                (MgrId int not null,MgrName text,Grade text, Years int,Unique(MgrId));""")
    
    
    cur.execute("Drop Table if Exists Promotions")
    cur.execute("""create table promotions
                (PromoId int not null,Medium text,Target text, Interval text,Unique(PromoId));""")
   
    
    cur.execute("Drop Table if Exists Soups")
    cur.execute("""create table soups
                (SoupId int not null,Type text,Vendor text, Mode text,Style text,Unique(SoupId));""")
    
    
    cur.execute("Drop Table if Exists Stores")
    cur.execute("""create table stores
                (StoreId int not null,Location text,Size text, Elevation text,MgrId int,Unique(StoreId));""")
    
def InsertSales(record):
                TrxId=int(record[0])
                DoY=int(record[1])
                StoreId=int(record[5])
                SoupId=int(record[13])
                PromoId=int(record[18])
                Sales=float(record[22])
                row=[TrxId,DoY,StoreId,SoupId,PromoId,Sales]
                cur.execute("INSERT or ignore INTO Sales VALUES(?,?,?,?,?,?)",row)
                
def InsertDays(record):
                DoY=int(record[1])
                DoW=str(record[2])
                Holiday=int(record[3])
                Weather=str(record[4])
                row=[DoY,DoW,Holiday,Weather]
                cur.execute("INSERT or ignore Into Days VALUES(?,?,?,?)",row)
                
def InsertManagers(record):
                MgrId=int(record[9])
                MgrName=str(record[10])
                Grade=str(record[11])
                Years=int(record[12])
                row=[MgrId,MgrName,Grade,Years]
                cur.execute("INSERT or ignore Into Managers VALUES(?,?,?,?)",row)
                
def InsertPromotions(record):
                PromoId=int(record[18])
                Medium=str(record[19])
                Target=str(record[20])
                Interval=str(record[21])
                row=[PromoId,Medium,Target,Interval]
                cur.execute("INSERT or ignore Into Promotions VALUES(?,?,?,?)",row)
                
def InsertSoups(record):
                SoupId=int(record[13])
                Type=str(record[14])
                Vendor=str(record[15])
                Mode=str(record[16])
                Style=str(record[17])
                row=[SoupId,Type,Vendor,Mode,Style]
                cur.execute("INSERT or ignore Into Soups VALUES(?,?,?,?,?)",row)
                
def InsertStores(record):
                StoreId=int(record[5])
                Location=str(record[6])
                Size=str(record[8])
                Elevation=str(record[7])
                MgrId=int(record[9])
                row=[StoreId,Location,Size,Elevation,MgrId]
                cur.execute("INSERT or ignore Into Stores VALUES(?,?,?,?,?)",row)
                
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
    def buttonNamePressed(self):
        self.lineeditName.setText("My Name is Weizhen Kong")
    def buttonSemesterPressed(self):
        self.lineeditSemester.setText("F2018")
    def button0Pressed(self):
        global filename
        filename=(self.lineedit0.text())
        import os
        if os.path.exists(filename) is True:
            conn=sqlite3.connect("Kong.db")
            cur=conn.cursor()
            CreateTables()
            f=open(filename,"r")
            linecount=0
            line=f.readline()
            while line !=""and linecount<500:
                linecount=linecount + 1
                line=line.replace("\n","")
                linelist=line.split("\t")
                InsertSales(linelist)
                InsertDays(linelist)
                InsertManagers(linelist)
                InsertPromotions(linelist)
                InsertSoups(linelist)
                InsertStores(linelist)
                line=f.readline()
            conn.commit()
            f.close()
            #open(filename,"r")
            self.lineedit0.setText("File Parsed")
        else:
            self.lineedit0.setText("File Not Found")
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
        f=open(filename,"r")
        #global tablename
        tablename = str(self.lineedit2.text())
        cur.execute("Select Count(*) from " + tablename)
        x1=cur.fetchall()[0][0]
        f.close
        self.lineedit2.setText(str(x1))
    def button3Pressed(self):
        
        f=open(filename,"r")
        tablename = str(self.lineedit3.text())
        c= cur.execute("Select * from " + tablename)
        for member in c.description:
            print member[0],
        print("\n")
        for a in cur:
            print a
        self.lineedit3.setText("")
    def button4Pressed(self):

        a=str(self.lineedit4.text())
        cur.execute(a)
        ans=cur.fetchall()
        print(ans)
    def button5Pressed(self):
        
        a =str(self.lineedit5.text())
        com=a.split(',')
        c=cur.execute("select count(Distinct " + com[1]+") from "  +com[0])
        rowcount=c.fetchone()[0]
        self.lineedit5.setText(str(rowcount))
                               
    def buttonQuitPressed(self):
        self.done(1)
        app.quit()
# End of Form Class Definition

app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
