import tkinter as tk
import smtplib as sm
from tkinter import ttk
import ttkbootstrap as t

smtp_server = "smtp.gmail.com"
email = "[GMAIL]" # ENTER YOUR GMAIL 
password = "[APP_PASSWORD]" # MAKE A APP PASSWORD FROM GMAIL SETTINGS OR SEARCH FOR IT AND PASTE IT
def send_mail():
    to = to_var.get()
    sub = sub_var.get()
    msg = msg_var.get()

    try:
        with sm.SMTP(smtp_server) as connection:
            connection.starttls()
            connection.login(email, password)
            connection.sendmail(email, to, f"Subject:{sub}\n\n{msg}")
            status_var.set(value="Email was sent.")
    except sm.SMTPException as e:
        print(f"SMTP Exception: {e}")
        status_var.set(value="Oops! Email wasn't sent")



window = tk.Tk()
window.title("Email Sender")

status_var = tk.StringVar(value="")

status = ttk.Label(master=window, textvariable=status_var)
status.pack(pady=10)

frame = ttk.Frame(master=window)
label_to = ttk.Label(master=frame, text="To: ")
label_to.grid(row=0, column=0, sticky='e', pady=5)

label_subject = ttk.Label(master=frame, text="Subject: ")
label_subject.grid(row=1, column=0, sticky='e', pady=5)

label_message = ttk.Label(master=frame, text="Message: ")
label_message.grid(row=2, column=0, sticky='e', pady=5)

to_var = tk.StringVar()
entry_to = ttk.Entry(master=frame, textvariable=to_var)
entry_to.grid(row=0, column=1, sticky='e', pady=5)

sub_var = tk.StringVar()
entry_subject = ttk.Entry(master=frame, textvariable=sub_var)
entry_subject.grid(row=1, column=1, sticky='e', pady=5)

msg_var = tk.StringVar()
entry_msg = ttk.Entry(master=frame, textvariable=msg_var)
entry_msg.grid(row=2, column=1, sticky='e', pady=5)

frame.pack(padx=10, pady=10)

button = t.Button(master=window, text="Send", command=send_mail)
button.pack(pady=10)

# Run the Tkinter main loop
window.mainloop()
