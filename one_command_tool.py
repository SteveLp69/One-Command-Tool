from PIL import Image, ImageTk
from system import command
import tkinter as tk

root = tk.Tk()
root.title("One Command Tool")
root.resizable(False, False)
root.geometry("300x265")

#variablen
commandblock_index = 0
data = []

#funktions
def load_image(path: str, resize: tuple = None, mode=Image.NEAREST):
    bild = Image.open(path)
    global bild_tk
    if type(resize) == tuple:
        bild_groesser = bild.resize(resize, mode)
        bild_tk = ImageTk.PhotoImage(bild_groesser)
    else:
        bild_tk = ImageTk.PhotoImage(bild)
    return bild_tk

def copy_to_clipboard(text: str):
    if text:
        root.clipboard_clear()
        root.clipboard_append(text)
        root.update()

#button funktions
def button_1():
    global commandblock_index
    if commandblock_index != 9:
        commandblock_index += 1
    if commandblock_index == 0:
        looping = var2.get()
        if looping:
            bild_tk = load_image("assets/repeting commandblock.png", resize=(64, 64))
            label.config(image=bild_tk)
        else:
            bild_tk = load_image("assets/commandblock.png", resize=(64, 64))
            label.config(image=bild_tk)
    else:
        bild_tk = load_image("assets/chain commandblock.png", resize=(64, 64))
        label.config(image=bild_tk)
    label2.config(text=str(commandblock_index + 1))
    button3.config(text=f"Save Command in {commandblock_index + 1}")
    entry.delete(0, tk.END)
    try:
        entry.insert(0, data[commandblock_index])
    except:
        entry.insert(0, "None")

def button_2():
    global commandblock_index
    if commandblock_index != 0:
        commandblock_index -= 1
    if commandblock_index == 0:
        looping = var2.get()
        if looping:
            bild_tk = load_image("assets/repeting commandblock.png", resize=(64, 64))
            label.config(image=bild_tk)
        else:
            bild_tk = load_image("assets/commandblock.png", resize=(64, 64))
            label.config(image=bild_tk)
    else:
        bild_tk = load_image("assets/chain commandblock.png", resize=(64, 64))
        label.config(image=bild_tk)
    label2.config(text=str(commandblock_index + 1))
    button3.config(text=f"Save Command in {commandblock_index + 1}")
    entry.delete(0, tk.END)
    try:
        entry.insert(0, data[commandblock_index])
    except:
        entry.insert(0, "None")

def button_3():
    global data
    if len(data) < commandblock_index + 1:
        for _ in range(commandblock_index + 1 - len(data)):
            data.append("/")
            #print(len(data), "/", commandblock_index + 1)
    data[commandblock_index] = entry.get() if entry.get().startswith("/") else f"/{entry.get()}"

def button_4():
    command_data = command.create(
        data, 
        auto_start=var.get(), 
        starting_loc=entry2.get(), 
        looping=var2.get()
    )
    #print(command_data)
    copy_to_clipboard(command_data)

#check funktions
def check_2():
    if commandblock_index == 0:
        looping = var2.get()
        if looping:
            bild_tk = load_image("assets/repeting commandblock.png", resize=(64, 64))
            label.config(image=bild_tk)
        else:
            bild_tk = load_image("assets/commandblock.png", resize=(64, 64))
            label.config(image=bild_tk)


bild_tk = load_image("assets/commandblock.png", resize=(64, 64))

label = tk.Label(root, image=bild_tk)
label.pack()

button1 = tk.Button(root, text="/\\", command=button_1)
button1.pack()
button1.place(x=90, y=7)

button2 = tk.Button(root, text="\\/", command=button_2)
button2.pack()
button2.place(x=90, y=37)

label2 = tk.Label(root, text=str(commandblock_index + 1))
label2.pack()
label2.place(x=60, y=24)

label3 = tk.Label(root, text="Command:")
label3.pack(pady=5)

entry = tk.Entry(root)
entry.pack(pady=5)
entry.insert(0, "None")

button3 = tk.Button(root, text=f"Save Command in {commandblock_index + 1}", command=button_3)
button3.pack(pady=5)

button4 = tk.Button(root, text="Copy command to clipboard", command=button_4)
button4.pack(pady=5)

label4 = tk.Label(root, text="Starting Pos.:")
label4.pack(pady=5)

entry2 = tk.Entry(root)
entry2.pack(pady=5)
entry2.insert(0, "~ ~ ~2")

var = tk.BooleanVar()
var2 = tk.BooleanVar()
var.set(True)
check = tk.Checkbutton(root, text="Auto Start", variable=var)
check.pack()
check.place(x=182, y=15)
check2 = tk.Checkbutton(root, text="Loop", variable=var2, command=check_2)
check2.pack()
check2.place(x=182, y=35)

root.mainloop()