import ctypes
import sys
import psutil
import customtkinter
import keyboard
from customtkinter import *



#Переменные
blocked_sites = ['www.tinkoff.ru', 'tinkoff.ru', 'www.google.com', 'www.yandex.ru', 'google.com', 'yandex.ru', 'yandex.com', 'www.yandex.ru', 'youtube.com', 'www.youtube.com', 'ya.ru', 'www.ya.ru', 'dzen.ru']

redirect_url = '127.0.0.1'

hosts=r'C:\Windows\System32\drivers\etc\hosts'

correct = '5642'



#DEFs
#Блокировка
def block():
    #Блокируют клавишы, указанные в ковычках
    keyboard.add_hotkey("alt + f4", lambda: None, suppress =True)
    keyboard.add_hotkey("ctrl+shift+esc", lambda: None, suppress =True)
    keyboard.add_hotkey("ctrl+alt+del", lambda: None, suppress =True)
    keyboard.add_hotkey("win+d", lambda: None, suppress =True)
    keyboard.add_hotkey("win+m", lambda: None, suppress =True)

    #Блокировка сайтов
    with open(hosts, 'r+') as file:
        src= file.read()
        for site in blocked_sites:
            if site in src:
                pass
            else:
                file.write(redirect_url+" "+site+"\n")

def block_login():
    global correct
    global block_passwd_entry
    global block_screen

    #Переменная пароль - значение введеное в поле ввода пароля
    password = block_passwd_entry.get()

    #Проверка пароля на правильность
    if password == correct:
        block_screen.destroy()
        maindef()
        print('Unlocked!')

#Авторизация
def login():
    global correct
    global password_entry

    #Переменная пароль - значение введеное в поле ввода пароля
    password = password_entry.get()

    #Проверка пароля на правильность
    if password == correct:
        print('Unlocked!')
        #Разблокировка сочетаний клавиш
        keyboard.remove_hotkey("alt + f4")
        keyboard.remove_hotkey("ctrl+shift+esc")
        keyboard.remove_hotkey("ctrl+alt+del")
        keyboard.remove_hotkey("win+d")
        keyboard.remove_hotkey("win+m")

        #Разблокировка сайтов
        with open(hosts, 'r+') as file:
            src= file.readlines()
            file.seek(0)
            for line in src:
                if not any(site in line for site in blocked_sites):
                    file.write(line)
            file.truncate()

        #Закрытие окна
        app.destroy()

#Гостевой режим
def guest():
    print('Login with guest')
    block()
    app.destroy()
    totalblock()

#Полная блокировка (активируется по истечению таймера или по нажатию ctrl+shift)
def totalblock():
    global block_screen
    global block_passwd_entry

    #Ожидает нажатие сочеания ctrl + shift
    keyboard.wait('ctrl+shift')

    #Блокирует клавишу win
    keyboard.add_hotkey("win", lambda: None, suppress =True)

    #Настройки экрана блокировки
    block_screen = customtkinter.CTk()
    customtkinter.set_default_color_theme("green")
    block_screen.attributes('-fullscreen', True)
    block_screen.overrideredirect(1)
    block_screen.state('zoomed')

    #Рендеринг экрана блокировки
    block_passwd_entry = customtkinter.CTkEntry(block_screen, placeholder_text="Введите пароль")
    block_login_button = customtkinter.CTkButton(block_screen, text="Войти", command=block_login)
    block_passwd_entry.pack(expand=1)
    block_login_button.pack(expand=1)

    #Запуск экрана блокировки
    block_screen.mainloop()

def maindef():
    #Настраиваем окно авторизации
    global app
    global password_entry

    customtkinter.set_default_color_theme("green")
    app = customtkinter.CTk()
    app.wm_attributes("-topmost", 1)
    app.resizable(width=False, height=False)
    app.overrideredirect(1)
    app.geometry("300x420+500+200")

    #Рендерим виджеты в окне авторизации
    frame_main_page = CTkFrame(app)
    password_entry = customtkinter.CTkEntry(app, placeholder_text="Введите пароль")
    login_button = customtkinter.CTkButton(frame_main_page, text="Войти", command=login)
    guest_button = customtkinter.CTkButton(frame_main_page, text="Гостевой режим", command=guest)
    password_entry.pack(expand=1)
    frame_main_page.pack(expand=1)
    guest_button.pack(expand=1)
    login_button.pack(expand=1, pady=2)

    #Запускаем окно авторизации
    block()
    app.mainloop()

#Запуск программы
maindef()