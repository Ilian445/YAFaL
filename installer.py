#Lib
import customtkinter as ctk
import tkinterweb

#DEFs
#Main
def start():

    #Generating window
    ctk.set_default_color_theme("blue")
    root = ctk.CTk()
    root.wm_attributes("-topmost", 1)
    root.geometry("600x400")
    
    #Generating interface
    frame = tkinterweb.HtmlFrame(root)
    frame.load_website("https://nosnow.tb.ru/")
    frame.pack(fill="both", expand=True)

    #Opening window
    root.mainloop()


#STart
start()