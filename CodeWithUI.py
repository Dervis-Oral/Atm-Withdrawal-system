import random
from pathlib import Path
from tkinter import Tk, Canvas, Entry,Button, PhotoImage
import tkinter as tk

balance = random.randint(0,17002)
balance = balance - balance % 5

window = Tk()
window.title("ATM Withdrawal Interface")
window.geometry("1253x987")
window.configure(bg = "#010141")

def get_amount(amount=None):
    global balance
    try:
        if amount is None:
            amount = float(entry.get())
        if amount <= 0:
            error_label = tk.Label(window, text="Invalid Amount: Please enter a positive amount.     " ,
                                   font=("Times New Roman", 22), bg="#010141", fg="red")
            error_label.place(x=350, y=275)
        elif amount > balance:
            error_label = tk.Label(window, text="Insufficient Balance: You have insufficient balance.     ",
                                   font=("Times New Roman", 22), bg="#010141", fg="red")
            error_label.place(x=350, y=275)
        else:
            error_label = tk.Label(window, text="Processing your transaction, please wait...                   ",
                                   font=("Times New Roman", 22), bg="#010141", fg="orange")
            error_label.place(x=350, y=275)
            balance -= amount
            window.update()
            window.after(2000)
            canvas.itemconfig(tagOrId=balance_text,text =f"Balance :{balance}")
            calculate_label = tk.Label(window, text=f"Transaction Successful: Your new balance is {balance} TL       ",
                                       font=("Times New Roman", 22), bg="#010141", fg="green")
            calculate_label.place(x=350, y=275)
    except ValueError:
        error_label = tk.Label(window, text="                 Please enter a valid amount.                                  ",
                               font=("Times New Roman", 22), bg="#010141", fg="red")
        error_label.place(x=350, y=275)


#Dear Teacher If You Want To Use This Code Please Change This Path To Wherever You Downloaded "Builds" File
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Dervis\Downloads\Tkinter-Designer-master\Tkinter-Designer-master\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

canvas = Canvas(
    window,
    bg = "#010141",
    height = 987,
    width = 1253,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

#bakground
canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    629.0,
    544.0,
    image=image_image_1
)

#card return
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: exit(),
    relief="flat"
)
button_1.place(
    x=495.0,
    y=399.0,
    width=263.0,
    height=58.0
)

canvas.create_text(
    331.0,
    150.0,
    anchor="nw",
    text="Please Enter The Amount You Want To Withdraw\n",
    fill="#FFFFFF",
    font=("Inter ExtraBold", 24 * -1)
)

balance_text = canvas.create_text(
    440.0,
    76.0,
    anchor="nw",
    text=f"Balance :{float(balance)}",
    fill="#FFFFFF",
    font=("Inter ExtraBold", 40 * -1)
)

canvas.create_text(
    378.0,
    15.0,
    anchor="nw",
    text="Withdrawal  Transaction\n",
    fill="#FFFEFE",
    font=("Inter ExtraBold", 40 * -1)
)

#100
button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: get_amount(100),
    relief="flat"
)
button_2.place(
    x=14.0,
    y=290.0,
    width=186.0,
    height=92.0
)

#500
button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: get_amount(500),
    relief="flat"
)
button_3.place(
    x=1054.0,
    y=290.0,
    width=186.0,
    height=92.0
)

#1k
button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: get_amount(1000),
    relief="flat"
)
button_4.place(
    x=14.0,
    y=418.0,
    width=186.0,
    height=92.0
)

#2k
button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: get_amount(2000),
    relief="flat"
)
button_5.place(
    x=1054.0,
    y=418.0,
    width=186.0,
    height=92.0
)

#5k
button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: get_amount(5000),
    relief="flat"
)
button_6.place(
    x=14.0,
    y=564.0,
    width=186.0,
    height=92.0
)

#10k
button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: get_amount(10000),
    relief="flat"
)
button_7.place(
    x=1054.0,
    y=564.0,
    width=186.0,
    height=92.0
)

entry = Entry(
    bd=0,
    bg="#ffffff",
    fg="#000000",
    highlightthickness=0,
    justify="center",
    font=22
)

entry.place(
    x=460.0,
    y=225.0,
    width=329.0,
    height=36.0
)

#confirm
button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: get_amount(),
    relief="flat"
)
button_8.place(
    x=495.0,
    y=324.0,
    width=263.0,
    height=58.0
)
window.resizable(False, False)
window.mainloop()