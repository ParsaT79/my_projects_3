from tkinter import *
import tkinter.messagebox as msg
from data_access.data_management import *
from tools.validators import *


def save_click():
    try:
        username_validator(username.get())
        password_validator(password.get())
        nickname_validator(nickname.get())
        save_user(username.get(), password.get(), nickname.get(), account_access.get())
        msg.showinfo("Saved", "User saved!")
        username.set("")
        password.set("")
        nickname.set("")
        account_access.set(False)
    except Exception as e:
        e.with_traceback()
        msg.showerror("Error", f"{e}")


window = Tk()
window.title("User App v0.1")
window.geometry("340x300")

# username
username = StringVar()
Label(window, text="Username").place(x=30, y=30)
Entry(window, textvariable=username).place(x=100, y=30)

# password
password = StringVar()
Label(window, text="Password").place(x=30, y=70)
Entry(window, textvariable=password, show="*").place(x=100, y=70)

# nickname
nickname = StringVar()
Label(window, text="Nickname").place(x=30, y=110)
Entry(window, textvariable=nickname).place(x=100, y=110)

# account status
account_access = BooleanVar()
Label(window, text="Account Access").place(x=30, y=150)
Checkbutton(window, variable=account_access).place(x=120, y=150)

Button(window, text="Save", width=13, command=save_click).place(x=120, y=220)

window.mainloop()
