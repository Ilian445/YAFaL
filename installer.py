#Lib
import customtkinter as ctk

#DEFs
#Instalation
def install():

    #Get data
    with open('example.txt') as f:
    # работа с файлом

    #Kill old window
    root.destroy()

    #Create new
    install = ctk.CTk()
    install.title("Идёт установка...")
    install.wm_attributes("-topmost", 1)
    install.geometry("600x400")

    #Generating interface
    ctk.CTkLabel(install, text="Идет установка программы...", font=('Arial', 23)).pack(expand=True)
    ctk.CTkLabel(install, text="Подождите пожалуйста", font=('Arial', 17)).pack()

    #Start window
    install.mainloop()


#Main
def start():
    global root, entry1, entry2, entry

    #Generating window
    ctk.set_default_color_theme("blue")
    root = ctk.CTk()
    root.title("Установка YAFaL")
    root.wm_attributes("-topmost", 1)
    root.geometry("600x400")
    
    #Generating interface
    frame = ctk.CTkFrame(root)
    font=('Arial', 20)
    label = ctk.CTkLabel(root, text="Добро пожаловать в установщик YAFaL!\nПеред установкой пожалуйта заполните поля ниже:", font=font)
    entry = ctk.CTkEntry(frame, placeholder_text="Пароль родителя", width=400)
    entry1 = ctk.CTkEntry(frame, placeholder_text="Дневное ограничение (в формате ЧЧ:ММ)", width=400)
    entry2 = ctk.CTkEntry(frame, placeholder_text="Запрещённые сайты (в формате ''example.com', 'google.xom'')", width=400)
    label.pack(pady = 5)
    entry.pack(pady=2)
    entry1.pack(pady=2)
    entry2.pack(pady=2)
    frame.pack(anchor="center", expand=True)
    btn = ctk.CTkButton(root, text="Установить", command=install)
    btn.pack(anchor="s", pady=10)

    #Opening window
    root.mainloop()

#STart
start()