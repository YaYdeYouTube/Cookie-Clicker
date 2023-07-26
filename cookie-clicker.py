from tkinter import *
# -*-coding:UTF-8*-

# Cookie clicker

window = Tk()
window.title("Cookie Clicker")
window.geometry("720x420+250+125")
window.minsize(400, 350)
window.iconbitmap("./img/clicker.ico")
window.config(bg="#C68B4F")

clicker_frame = Frame(window, bg="#C68B4F")
click_text = Label(clicker_frame, text="Clickez pour gagner des cookies !", font=("MV BOLI", 20), bg="#C68B4F", fg="Black")
click_text.grid(row=0, column=0, sticky=E)
clicker_frame.pack()

width = 200
height = 200
cookie = PhotoImage(file="./img/biscuit.png")
canvas = Canvas(window, width=width, height=height, bg="#C68B4F", bd=0, highlightthickness=0)
canvas.create_image(width/2, height/2, image=cookie)
canvas.pack()

def counter_add():
    global counter
    counter += 1
    counter_message.config(text="Vous avez {} cookies !".format(counter))

def counter_addx2():
    global counter
    counter += 2
    counter_message.config(text="Vous avez {} cookies !".format(counter))

def counter_addx2_verif():
    global counter
    if counter >= 100:
        counter -= 100
        button.config(command=counter_addx2)

b_width = 30
b_height = 3

button = Button(window, text="CLIQUEZ !", width=b_width, height=b_height, bg="#7E5E3E", fg="white",bd=5, command=counter_add)
button.pack(expand=YES)

counter = 0
counter_frame = Frame(window, bg="#C68B4F")
counter_message = Label(counter_frame, text="Vous avez {} cookies".format(counter), font=("MV BOLI ", 25), bg="#C68B4F", fg="white")
counter_message.grid(row=0, column=0, sticky=S)
counter_frame.pack()
counter_error = Label(text="", font=("MV BOLI", 25), bg="#7E5E3E", fg="white")

# boutique de cookies
menu_bar = Menu(window)
menu_store = Menu(menu_bar, tearoff=0)
menu_store.add_command(label="2x plus de cookies : 100", command=counter_addx2_verif)
menu_bar.add_cascade(label="Store", menu=menu_store)

window.config(menu=menu_bar)

window.mainloop()