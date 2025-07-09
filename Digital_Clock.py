import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.timer = QTimer(self)
        self.label = QLabel(self)
        self.initUI()

    def initUI(self):
        self.timer.timeout.connect(self.showTime)
        self.timer.start(1000)

        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet('font-size: 100px; font-family: ; font-weight: bold; color: purple;')
        self.setStyleSheet('background-color: yellow;')
        self.showTime()

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

        self.setGeometry(100, 100, 400, 100)
        self.setWindowTitle('Digital Clock')

    def showTime(self):
        time = QTime.currentTime()
        text = time.toString('hh:mm:ss AP')
        self.label.setText(text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())