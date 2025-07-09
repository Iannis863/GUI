import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel('Enter city name', self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton('Get Weather', self)
        self.temperature = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Weather App')
        self.setWindowIcon(QIcon('Icon.webp'))

        layout = QVBoxLayout()
        layout.addWidget(self.city_label)
        layout.addWidget(self.city_input)
        layout.addWidget(self.get_weather_button)
        layout.addWidget(self.temperature)
        layout.addWidget(self.emoji_label)
        layout.addWidget(self.description_label)
        self.setLayout(layout)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName('city_label')
        self.city_input.setObjectName('city_input')
        self.get_weather_button.setObjectName('get_weather_button')
        self.temperature.setObjectName('temperature')
        self.emoji_label.setObjectName('emoji_label')
        self.description_label.setObjectName('description_label')
        self.setStyleSheet('''
            QLabel QPushButton {
                font-size: 20px;
                font-family: Calibri;
            }   
            QLabel#city_label {
                font-size: 40px;
                font-style: Italic;
            }
            QLineEdit#city_input {
                font-size: 40px;
            }
            QPushButton#get_weather_button {
                font-size: 30px;
                font-weight: bold;
            }
            QLabel#temperature {
                font-size: 80px;
            }
            QLabel#emoji_label {
                font-size: 80px;
                font-family: Segoe UI Emoji;
            }
            QLabel#description_label {
                font-size: 50px;
            }
        ''')

        self.get_weather_button.clicked.connect(self.get_weather)

    def get_weather(self):
        city = self.city_input.text()
        api_key = '1c82ab7c2d0316d179845109a86cc311'
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
        try:
            response = requests.get(url)
            response.raise_for_status()
            weather_data = response.json()
            temperature = weather_data['main']['temp']
            description = weather_data['weather'][0]['description']
            id = weather_data['weather'][0]['id']
            self.display_weather(temperature, description, id)
        except requests.exceptions.HTTPError as http_error:
            match response.status_code:
                case 400:
                    self.display_error('Bad request')
                case 401:
                    self.display_error('Unauthorized')
                case 403:
                    self.display_error('Forbidden')
                case 404:
                    self.display_error('City not found')
                case 500:
                    self.display_error('Internal server error')
                case 502:
                    self.display_error('Bad gateway')
                case 503:
                    self.display_error('Service unavailable')
                case 504:
                    self.display_error('Gateway timeout')
                case _:
                    self.display_error(f'Something went wrong {http_error}')
        except requests.exceptions.ConnectionError:
            self.display_error('Connection error')
        except requests.exceptions.Timeout:
            self.display_error('Request timed out')
        except requests.exceptions.TooManyRedirects:
            self.display_error('Too many redirects')
        except requests.exceptions.RequestException as req_error:
            self.display_error(f'Request error: {req_error}')

    def display_error(self, message:str):
        self.temperature.setStyleSheet('font-size: 30px; color: red;')
        self.temperature.setText(message)
        self.emoji_label.clear()
        self.description_label.clear()

    def display_weather(self, temperature, description, id):
        self.temperature.setStyleSheet('font-size: 80px;')
        self.temperature.setText(f'{temperature - 273.15:.1f}°C')
        self.emoji_label.setText(self.get_weather_emoji(id))
        self.description_label.setText(description.capitalize())

    @staticmethod
    def get_weather_emoji(weather_id):
        if 200 <= weather_id < 300:
            return '⛈️'
        elif 300 <= weather_id < 400:
            return '🌧️'
        elif 500 <= weather_id < 600:
            return '🌧️'
        elif 600 <= weather_id < 700:
            return '❄️'
        elif 700 <= weather_id < 800:
            return '🌫️'
        elif weather_id == 800:
            return '☀️'
        elif 801 <= weather_id < 900:
            return '☁️'
        else:
            return ''

if __name__ == '__main__':
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())