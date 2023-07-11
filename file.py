import tkinter
import customtkinter
import webbrowser
import ctypes

import self

ctypes.windll.shcore.SetProcessDpiAwareness(1)


customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Set theme to orange and white

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("400x240")
app.title("File share")  # Set the app title

def open_whatsapp():
    whatsapp_url = "https://web.whatsapp.com/"
    webbrowser.open_new_tab(whatsapp_url)

def open_gmail():
    gmail_url = "https://mail.google.com/"
    webbrowser.open_new_tab(gmail_url)

def open_gdrive():
    gdrive_url = "https://drive.google.com/"
    webbrowser.open_new_tab(gdrive_url)

# Use CTkButton instead of tkinter Button
whatsapp_button = customtkinter.CTkButton(master=app, text="WhatsApp ", command=open_whatsapp)
whatsapp_button.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

gmail_button = customtkinter.CTkButton(master=app, text="Gmail", command=open_gmail)
gmail_button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

gdrive_button = customtkinter.CTkButton(master=app, text="Google Drive", command=open_gdrive)
gdrive_button.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

app.mainloop()
