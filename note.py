import tkinter as tk
import threading
import speech_recognition as sr
from tkinter import messagebox


class NoteWindow:
    def __init__(self):
        self.master = tk.Tk()
        self.master.title("Note Taker")

        self.text_box = tk.Text(self.master)
        self.text_box.pack(fill=tk.BOTH, expand=True)

        self.status_label = tk.Label(self.master, text="Click Start or press Ctrl + S to begin recording.")
        self.status_label.pack()

        self.start_button = tk.Button(self.master, text="Start (Ctrl + S)", command=self.start_recording)
        self.start_button.pack(side=tk.LEFT)

        self.stop_button = tk.Button(self.master, text="Stop", command=self.stop_recording, state=tk.DISABLED)
        self.stop_button.pack(side=tk.RIGHT)

        self.recording_thread = None
        self.keep_recording = True

        self.master.bind("<Control-s>", self.start_recording)
        self.master.bind("q", self.stop_recording)

    def start_recording(self, event=None):
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.recording_thread = threading.Thread(target=self.record_loop)
        self.recording_thread.start()

    def stop_recording(self, event=None):
        self.keep_recording = False  # set flag to stop recording
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        messagebox.showinfo("Note Taker", "Notes have been saved successfully.")

    def record_loop(self):
        r = sr.Recognizer()
        note_num = 0  # initialize note number
        with sr.Microphone() as source:
            # adjust for ambient noise before starting the main loop
            r.adjust_for_ambient_noise(source)
            self.status_label.config(text="Recording in progress... (Press Q to stop recording)")
            while self.keep_recording:
                print("Recording...")
                audio = r.listen(source, timeout=5)
                try:
                    text = r.recognize_google(audio)
                    note_num += 1  # increment note number
                    text_with_num = f"{note_num}. {text}"  # add number to beginning of text
                    self.text_box.insert(tk.END, text_with_num + "\n")
                    with open("notes.txt", "a") as f:
                        f.write(text_with_num + "\n")
                except sr.UnknownValueError:
                    messagebox.showinfo("Note Taker", "Could not understand audio.")
                except sr.RequestError as e:
                    messagebox.showinfo("Note Taker", f"Could not request results; {e}")
            self.status_label.config(text="Click Start or press Ctrl + S to begin recording.")
            print("Stopped recording.")
        self.master.destroy()


if __name__ == '__main__':
    gui = NoteWindow()
    gui.master.mainloop()

