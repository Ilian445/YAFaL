import sys
import elevate
import wget
import shutil
import winreg
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

elevate.elevate()


#wget.download('https://no-snow.ru/index.html')
#wget.download('https://no-snow.ru/index.html')


#os.system('mkdir C:\Program Files\YAFaL')
#shutil.copy('YAFaL.exe', 'C:\Program Files\YAFaL')
#shutil.copy('YAFaL.ink', 'C:\ProgramData\Microsoft\Windows\Start Menu\Programs')


key = winreg.HKEY_CURRENT_USER
key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
app_name = "MyApp"
app_path = r"C:\Program Files\YAFaL\YAFal.exe"

try:
    reg_key = winreg.OpenKey(key, key_path, 0, winreg.KEY_ALL_ACCESS)
    winreg.SetValueEx(reg_key, app_name, 0, winreg.REG_SZ, app_path)
    winreg.CloseKey(reg_key)
    print("Приложение успешно добавлено в автозагрузку!")
except Exception as e:
    print("Что-то пошло не так:", e)



app = QApplication(sys.argv)
QApplication.setApplicationName('App installed!')
window = MainWindow()
app.exec_()