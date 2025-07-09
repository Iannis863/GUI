import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt

class StopWatch(QWidget):
    def __init__(self):
        super().__init__()
        self.timer = QTimer()
        self.time = QTime(0, 0, 0)
        self.timeDisplay = QLabel(self.time.toString('hh:mm:ss'))
        self.startButton = QPushButton('Start')
        self.stopButton = QPushButton('Stop')
        self.resetButton = QPushButton('Reset')
        self.initUI()

    def initUI(self):
        self.timer.timeout.connect(self.updateTime)

        self.startButton.setObjectName('start_button')
        self.stopButton.setObjectName('stop_button')
        self.resetButton.setObjectName('reset_button')
        self.setStyleSheet('''
                            QPushButton{
                                font-size: 20px;
                            }
                            QPushButton#start_button{
                                background-color: hsl(120, 100%, 50%);
                            }
                            QPushButton#stop_button{
                                background-color: hsl(0, 100%, 50%);
                            }
                            QPushButton#reset_button{
                                background-color: hsl(240, 100%, 50%);
                            }
                            QPushButton#start_button:hover{
                                background-color: hsl(120, 100%, 70%);
                            }
                            QPushButton#stop_button:hover{
                                background-color: hsl(0, 100%, 70%);
                            }
                            QPushButton#reset_button:hover{
                                background-color: hsl(240, 100%, 70%);
                            }
                            ''')
        self.timeDisplay.setStyleSheet('font-size: 30px; font-weight: bold; color: black;')
        self.timeDisplay.setAlignment(Qt.AlignCenter)


        self.startButton.clicked.connect(self.startTimer)
        self.stopButton.clicked.connect(self.stopTimer)
        self.resetButton.clicked.connect(self.resetTimer)

        hbox = QHBoxLayout()
        hbox.addWidget(self.startButton)
        hbox.addWidget(self.stopButton)
        hbox.addWidget(self.resetButton)

        vbox = QVBoxLayout()
        vbox.addWidget(self.timeDisplay)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setWindowTitle('Stop Watch')
        self.setGeometry(100, 100, 200, 100)
        self.show()

    def startTimer(self):
        self.timer.start(1000)
        self.timeDisplay.setStyleSheet('background-color: hsl(120, 100%, 50%); font-size: 30px; font-weight: bold; color: white;')

    def stopTimer(self):
        self.timer.stop()
        self.timeDisplay.setStyleSheet('background-color: hsl(0, 100%, 50%); font-size: 30px; font-weight: bold; color: white;')

    def resetTimer(self):
        self.time = QTime(0, 0, 0)
        self.timeDisplay.setText(self.time.toString('hh:mm:ss'))
        self.timeDisplay.setStyleSheet('font-size: 30px; font-weight: bold; color: black;')

    def updateTime(self):
        self.time = self.time.addSecs(1)
        self.timeDisplay.setText(self.time.toString('hh:mm:ss'))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    stop_watch = StopWatch()
    sys.exit(app.exec_())