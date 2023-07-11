import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import subprocess


class AuthenticationWindow:
    def __init__(self, master):
        self.master = master
        self.master.geometry("500x400")
        self.master.title("Authentication")

        self.label = ttk.Label(self.master, text="Enter username and password")
        self.label.pack(pady=10)

        self.username_label = ttk.Label(self.master, text="Username:")
        self.username_label.pack()

        self.username_entry = ttk.Entry(self.master)
        self.username_entry.pack(pady=5)

        self.password_label = ttk.Label(self.master, text="Password:")
        self.password_label.pack()

        self.password_entry = ttk.Entry(self.master, show="*")
        self.password_entry.pack(pady=5)

        self.submit_button = ttk.Button(self.master, text="Submit", command=self.submit_credentials)
        self.submit_button.pack(pady=10)

    def submit_credentials(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "root" and password == "password":
            self.master.destroy()
            root = tk.Tk()
            app = MainWindow(root)
            root.mainloop()
        else:
            ttk.Label(self.master, text="Invalid username or password").pack(pady=10)

class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.geometry("900x800")
        self.master.title("Smart Meet Management Tool")
        self.master.configure(bg="#f7f7f7")
        self.label = ttk.Label(
            self.master,
            text="Welcome to the Smart Meet Management Tool!",
            anchor="center",
            justify="center",
            font=("Open Sans", 20, "bold"),
            foreground="#333333",
            background="#f7f7f7",
        )
        self.label.grid(row=0, columnspan=9, padx=20, pady=20, sticky="nswe")

        self.master.iconbitmap("main.ico")

        # Define custom button style
        style = ttk.Style()
        style.configure(
            "Custom.TButton",
            background="#0077B6",
            foreground="#0000FF",
            font=("Open Sans", 16, "bold"),
            padding=20,
        )

        # Load images
        record_img = Image.open("record.png").resize((100, 100))
        self.record_icon = ImageTk.PhotoImage(record_img)

        note_img = Image.open("note.png").resize((100, 100))
        self.note_icon = ImageTk.PhotoImage(note_img)

        schedule_img = Image.open("schedule.png").resize((100, 100))
        self.schedule_icon = ImageTk.PhotoImage(schedule_img)

        file_img = Image.open("file.png").resize((100, 100))
        self.file_icon = ImageTk.PhotoImage(file_img)

        # Create buttons with custom style
        self.record_button = ttk.Button(
            self.master,
            text="Online Meeting Recording",
            image=self.record_icon,
            compound="top",
            style="Custom.TButton",
            command=self.open_record_window,
        )
        self.note_button = ttk.Button(
            self.master,
            text="Auto Note Taking",
            image=self.note_icon,
            compound="top",
            style="Custom.TButton",
            command=self.open_note_window,
        )
        self.schedule_button = ttk.Button(
            self.master,
            text="Meeting Remainder",
            image=self.schedule_icon,
            compound="top",
            style="Custom.TButton",
            command=self.open_schedule_window,
        )
        self.file_button = ttk.Button(
            self.master,
            text="File Sharing",
            image=self.file_icon,
            compound="top",
            style="Custom.TButton",
            command=self.open_file_window,
        )


        # Add buttons to layout
        self.record_button.grid(row=1, column=0, padx=20, pady=5, sticky="NSEW")
        self.note_button.grid(row=1, column=1, padx=20, pady=5, sticky="NSEW")
        self.schedule_button.grid(row=2, column=0, padx=20, pady=5, sticky="NSEW")
        self.file_button.grid(row=2, column=1, padx=20, pady=5, sticky="NSEW")

        # Set column and row weights to resize buttons when window is resized
        self.master.columnconfigure(0, weight=1)
        self.master.columnconfigure(1, weight=1)
        self.master.rowconfigure(1, weight=1)
        self.master.rowconfigure(2, weight=1)

        self.record_url = "record.py"
        self.note_url = "note.py"
        self.schedule_url = "schedule.py"
        self.file_url = "file.py"

    def open_record_window(self):
        subprocess.Popen(["python", self.record_url], shell=True)

    def open_note_window(self):
        subprocess.Popen(["python", self.note_url], shell=True)

    def open_schedule_window(self):
        subprocess.Popen(["python", self.schedule_url], shell=True)

    def open_file_window(self):
        subprocess.Popen(["python", self.file_url], shell=True)


if __name__ == '__main__':
    root = tk.Tk()
    app = AuthenticationWindow(root)
    root.mainloop()
