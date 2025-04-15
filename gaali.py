import tkinter as tk
from tkinter import messagebox
import random
import time
import threading
import keyboard

def start_sending():
    try:
        messages = message_text.get("1.0", tk.END).strip().split("\n")
        repetitions = int(repeat_entry.get())
        
        if not messages or repetitions <= 0:
            messagebox.showerror("Error", "Please enter valid messages and number of repetitions.")
            return
        
        messagebox.showinfo("Instructions", "You have 10 seconds to open your messenger/chat window.")
        
        def send():
            time.sleep(10)
            for _ in range(repetitions):
                msg = random.choice(messages)
                keyboard.write(msg)
                time.sleep(0.2)
                keyboard.press("enter")
                time.sleep(0.3)
            messagebox.showinfo("Done", "Messages sent successfully!")
        
        threading.Thread(target=send).start()

    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI setup
root = tk.Tk()
root.title("Auto Messenger Bot by Gagan Rai")
root.geometry("400x400")
root.resizable(False, False)

tk.Label(root, text="Enter your messages (one per line):").pack(pady=10)
message_text = tk.Text(root, height=10, width=40)
message_text.pack()

tk.Label(root, text="Number of repetitions:").pack(pady=10)
repeat_entry = tk.Entry(root)
repeat_entry.pack()

start_button = tk.Button(root, text="Start Sending", bg="green", fg="white", command=start_sending)
start_button.pack(pady=20)

tk.Label(root, text="Created by Gagan Rai", fg="blue").pack(side="bottom", pady=10)

root.mainloop()
