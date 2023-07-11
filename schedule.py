import tkinter as tk
import webbrowser
import datetime
import time
import threading
from tkinter import ttk

from win10toast import ToastNotifier
import ctypes

class ScheduleWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Link Opener")
        self.root.geometry("700x500")
        self.root.iconbitmap("schedule.ico")

        # Create a style to customize the widgets
        style = ttk.Style()
        style.configure("TLabel", padding=20)
        style.configure("TEntry", padding=20)
        style.configure("TButton", padding=20)

        # Create a frame to hold the input fields
        input_frame = ttk.LabelFrame(self.root, text="Set Alarm", padding=20)
        input_frame.pack(fill="both", expand=True)

        # Create input fields
        link_label = ttk.Label(input_frame, text="Link:", font=20)
        link_entry = ttk.Entry(input_frame, width=40, font=20)
        time_label = ttk.Label(input_frame, text="Time (HH:MM:SS):", font=20)
        time_entry = ttk.Entry(input_frame, width=40, font=20)


        # Position input fields in the frame
        link_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)
        link_entry.grid(row=0, column=1, columnspan=2, sticky="ew", padx=10, pady=10)
        time_label.grid(row=2, column=0, sticky="w", padx=10, pady=10)
        time_entry.grid(row=2, column=1, sticky="ew", padx=10, pady=10)

        # Create a frame to hold the buttons
        button_frame = ttk.Frame(self.root)
        button_frame.pack(pady=30)



        import tkinter.messagebox as mbox

        def set_alarm():
            # Get the link and time entered by the user
            link = link_entry.get()
            alarm_time = time_entry.get()


            # Check if either field is empty
            if not link or not alarm_time:
                mbox.showerror("Error", "Please fill in both Link and Alarm Time fields.")
                return

            # Parse the alarm time into a datetime object
            alarm_datetime = datetime.datetime.strptime(alarm_time, "%H:%M:%S")


            reminder_datetime = alarm_datetime
            set_alarm_button.config(state=tk.DISABLED)

            # Create a new thread to handle the time-consuming tasks
            alarm_thread = threading.Thread(target=alarm_handler, args=(link, reminder_datetime, alarm_datetime))
            alarm_thread.start()

        set_alarm_button = tk.Button(button_frame, text="Set Meet Alarm", command=set_alarm, width=15, background="green", foreground="white", font=20)
        set_alarm_button.pack()

        # Define the alarm handler function
        def alarm_handler(link, reminder_datetime, alarm_datetime):
            # Wait until it's time to display the reminder
            while datetime.datetime.now().time() < reminder_datetime.time():
                print("Waiting for the reminder...")
                time.sleep(1)

            # Display the reminder message using a Windows 10 toast notification
            toaster = ToastNotifier()
            toaster.show_toast("Reminder", "The meet will open on time. So be ready.", duration=10)


            set_alarm_button.config(state=tk.NORMAL)

            # Open the link
            print("Opening the link now...")
            webbrowser.open(link)



        # Set the process DPI awareness for Windows 10
        ctypes.windll.shcore.SetProcessDpiAwareness(1)

    def run(self):
        # Run the root window
        self.root.mainloop()

if __name__ == "__main__":
    window = ScheduleWindow()
    window.run()
