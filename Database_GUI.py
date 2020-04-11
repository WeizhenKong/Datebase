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
        self.pbutton0 = QPushButton("Open Input File")
        self.lineedit0 = QLineEdit("Input File Name")
        self.label1 = QLabel("Select a Function")
        self.pbutton1 = QPushButton("Character Count")
        self.lineedit1 = QLineEdit("")
        self.pbutton2 = QPushButton("Line Count")
        self.lineedit2 = QLineEdit("")
        self.pbutton3 = QPushButton("Unique Word Count")
        self.lineedit3 = QLineEdit("")
        self.pbutton4 = QPushButton("Average Characters Per Word")
        self.lineedit4 = QLineEdit("")
        self.pbuttonQuit = QPushButton("Quit")
        layout = QVBoxLayout()
        layout.addWidget(self.pbuttonName)
        layout.addWidget(self.lineeditName)
        layout.addWidget(self.pbuttonSemester)
        layout.addWidget(self.lineeditSemester)       
        layout.addWidget(self.pbutton0)
        layout.addWidget(self.lineedit0)
        layout.addWidget(self.lineedit0)
        layout.addWidget(self.label1)
        layout.addWidget(self.pbutton1)
        layout.addWidget(self.lineedit1)
        layout.addWidget(self.pbutton2)
        layout.addWidget(self.lineedit2)
        layout.addWidget(self.pbutton3)
        layout.addWidget(self.lineedit3)
        layout.addWidget(self.pbutton4)
        layout.addWidget(self.lineedit4)
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
            open(filename,"r")
            self.lineedit0.setText("File Opened")
        else:
            self.lineedit0.setText("File Not Found")
        
    def button1Pressed(self):
        import string
        characters=[]
        with open(filename,"r")as f:
            for c in f.read():
                characters.append(c)
        x=len(characters)
        y=0
        for c in characters:
            if c in string.ascii_letters:
                y+=1
        self.lineedit1.setText(str(y))        
    def button2Pressed(self):
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
        self.lineedit2.setText(x2)
    def button3Pressed(self):
        uniqueWordCount = 0
        count={}
        f=open(filename,"r")
        unique=set(filename)
        for word in unique:
            if word in count :
                count[word] += 1
            else:
                count[word] = 1
        self.lineedit3.setText(str(count[word])+" words counted")
    def button4Pressed(self):
        import string
        chars=[]
        with open(filename,"r")as f:
            for c in f.read():
                chars.append(c)
        x=len(chars)
        y=0
        for c in chars:
            if c in string.ascii_letters:
                y+=1
        word_count=0
        with open(filename,'r') as file:
            for line in file:
                word_count += len(line.split())
        x3=str(y/word_count)
        self.lineedit4.setText(x3)
    def buttonQuitPressed(self):
        self.done(1)
        app.quit()
# End of Form Class Definition

app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
