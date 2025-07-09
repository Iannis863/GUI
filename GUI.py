import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QCheckBox, QRadioButton, QButtonGroup, QLineEdit
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My First App')
        self.setWindowIcon(QIcon('Romania_Bulgaria_U20_ (131).jpg'))
        #self.setGeometry(100, 100, 800, 600)
        #self.label = QLabel('Hello World!', self)
        #self.button = QPushButton('Click Me!', self)
        #self.checkbox = QCheckBox('Do you like food?', self)
        """
        self.radio1 = QRadioButton('Visa', self)
        self.radio2 = QRadioButton('Mastercard', self)
        self.radio3 = QRadioButton('American Express', self)
        self.radio4 = QRadioButton('In-Store', self)
        self.radio5 = QRadioButton('Online', self)
        self.button_group1 = QButtonGroup(self)
        self.button_group2 = QButtonGroup(self)
        """
        #self.line_edit = QLineEdit(self)
        #self.button_line_edit = QPushButton('Submit', self)
        self.button1 = QPushButton('Button 1')
        self.button2 = QPushButton('Button 2')
        self.button3 = QPushButton('Button 3')
        #self.init_label()
        #self.init_picture()
        #self.init_layout()
        #self.init_button()
        #self.init_checkbox()
        #self.init_radio()
        #self.init_line_edit()
        self.init_css()

    def init_label(self):
        self.label.setFont(QFont('Arial', 20))
        self.label.setGeometry(150, 300, 500, 100)
        self.label.setStyleSheet("color: blue; background-color: yellow; font-weight: bold; font-style: italic; text-decoration: underline; font-size: 50px")
        self.label.setAlignment(Qt.AlignCenter)

    def init_picture(self):
        picture = QLabel(self)
        picture.setGeometry(0, 100, 500, 500)
        picture.setPixmap(QPixmap('Romania_Bulgaria_U20_ (131).jpg'))
        picture.setScaledContents(True)

    def init_layout(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        label1 = QLabel('Label 1', self)
        label2 = QLabel('Label 2', self)
        label3 = QLabel('Label 3', self)
        label4 = QLabel('Label 4', self)
        label5 = QLabel('Label 5', self)

        label1.setStyleSheet('background-color: red;')
        label2.setStyleSheet('background-color: green;')
        label3.setStyleSheet('background-color: blue;')
        label4.setStyleSheet('background-color: yellow;')
        label5.setStyleSheet('background-color: purple;')

        grid = QGridLayout()
        grid.addWidget(label1, 0, 0)
        grid.addWidget(label2, 0, 1)
        grid.addWidget(label3, 1, 0)
        grid.addWidget(label4, 1, 1)
        grid.addWidget(label5, 2, 2)

        central_widget.setLayout(grid)

    def init_button(self):
        self.button.setGeometry(150, 200, 200, 100)
        self.button.setStyleSheet('background-color: red; color: white; font-weight: bold; font-size: 30px;')
        self.button.clicked.connect(self.button_click)

    def button_click(self):
        self.label.setText('Button Clicked!')

    def init_checkbox(self):
        self.checkbox.setGeometry(150, 200, 300, 100)
        self.checkbox.setStyleSheet('background-color: red; color: white; font-weight: bold; font-size: 30px;')
        self.checkbox.stateChanged.connect(self.checkbox_state)

    def checkbox_state(self):
        if self.checkbox.isChecked():
            self.label.setText('Yes')
        else:
            self.label.setText('No')

    def init_radio(self):
        self.radio1.setGeometry(0, 0, 300, 50)
        self.radio2.setGeometry(0, 50, 300, 50)
        self.radio3.setGeometry(0, 100, 300, 50)
        self.radio4.setGeometry(0, 150, 300, 50)
        self.radio5.setGeometry(0, 200, 300, 50)

        self.setStyleSheet('QRadioButton { font-size: 30px; padding: 10px; }')

        self.button_group1.addButton(self.radio1)
        self.button_group1.addButton(self.radio2)
        self.button_group1.addButton(self.radio3)
        self.button_group2.addButton(self.radio4)
        self.button_group2.addButton(self.radio5)

        self.radio1.toggled.connect(self.radio_button_changed)
        self.radio2.toggled.connect(self.radio_button_changed)
        self.radio3.toggled.connect(self.radio_button_changed)
        self.radio4.toggled.connect(self.radio_button_changed)
        self.radio5.toggled.connect(self.radio_button_changed)

    def radio_button_changed(self):
        radio_button = self.sender()
        if radio_button.isChecked():
            print(radio_button.text())

    def init_line_edit(self):
        self.line_edit.setGeometry(10, 10, 300, 40)
        self.line_edit.setPlaceholderText('Enter your name')
        self.line_edit.setStyleSheet('font-weight: bold; font-size: 30px;')

        self.button_line_edit.setGeometry(320, 10, 100, 40)
        self.button_line_edit.setStyleSheet('font-weight: bold; font-size: 20px;')
        self.button_line_edit.clicked.connect(self.submit)

    def submit(self):
        text = self.line_edit.text()
        print(f"Hello {text}!")

    def init_css(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        hbox = QHBoxLayout()
        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)

        central_widget.setLayout(hbox)

        self.button1.setObjectName('button1')
        self.button2.setObjectName('button2')
        self.button3.setObjectName('button3')
        self.setStyleSheet('''
            QPushButton { 
                font-size: 30px; 
                padding: 15px 75px; 
                margin: 25px; 
                border: 3px solid; 
                border-radius: 10px; 
            }
            QPushButton#button1 { 
                background-color: hsl(0, 100%, 50%); 
            }
            QPushButton#button2 { 
                background-color: hsl(120, 100%, 50%); 
            }
            QPushButton#button3 { 
                background-color: hsl(240, 100%, 50%); 
            }
            QPushButton#button1:hover { 
                background-color: hsl(0, 100%, 70%); 
            }
            QPushButton#button2:hover { 
                background-color: hsl(120, 100%, 70%); 
            }
            QPushButton#button3:hover { 
                background-color: hsl(240, 100%, 70%); 
            }''')

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
