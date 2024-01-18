from tkinter import *
import co


def book():
   
    def reset():
        name = entry0.get()
        no = entry1.get()
        contact = entry2.get()
        gen = entry3.get()
        em = entry4.get()
        print(name,no,contact,gen,em)

    def confirm():
        window.destroy()
        co.con()
    window = Tk()

    window.geometry("398x487")
    window.configure(bg = "#ffffff")
    canvas = Canvas(
        window,
        bg = "#ffffff",
        height = 487,
        width = 398,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)



    entry0 = Entry(
        bg = "#fffdfd")

    entry0.place(
        x = 177, y = 102,
        width = 149,
        height = 25)

    entry1 = Entry(
        bg = "#fcfcfc")

    entry1.place(
        x = 177, y = 161,
        width = 149,
        height = 25)



    entry2 = Entry(
        bg = "#fcfcfc")

    entry2.place(
        x = 177, y = 225,
        width = 149,
        height = 25)


    entry3 = Entry(
        bg = "#fcfcfc")

    entry3.place(
        x = 177, y = 287,
        width = 149,
        height = 25)

    entry4 = Entry(
        bg = "#fcfcfc")

    entry4.place(
        x = 177, y = 345,
        width = 149,
        height = 25)

   

    canvas.create_text(
        62.0, 113.5,
        text = "Name",
        fill = "#000000",
        font = ("None", int(15.0)))


    b0 = Button(
        text = "Go Back",
        borderwidth = 0,
        relief = "flat")

    b0.place(
        x = 15, y = 426,
        width = 101,
        height = 37)


    b1 = Button(
        text = "Reset",
        relief = "flat")

    b1.place(
        x = 135, y = 426,
        width = 101,
        height = 37)


    b2 = Button(
        text = "Confirm",
        command = confirm,
        relief = "flat")

    b2.place(
        x = 261, y = 426,
        width = 101,
        height = 37)

    canvas.create_text(
        70.0, 174.5,
        text = "No Of\nPassengers",
        fill = "#000000",
        font = ("None", int(15.0)))

    canvas.create_text(
        65.5, 239.0,
        text = "Contact.No",
        fill = "#000000",
        font = ("None", int(15.0)))

    canvas.create_text(
        65.5, 301.0,
        text = "Gender",
        fill = "#000000",
        font = ("None", int(15.0)))

    canvas.create_text(
        65.5, 359.0,
        text = "Email ID",
        fill = "#000000",
        font = ("None", int(15.0)))

    canvas.create_text(
        65.5, 359.0,
        text = "Email ID",
        fill = "#000000",
        font = ("None", int(15.0)))

    canvas.create_text(
        182.5, 45.5,
        text = "TRAIN BOOKING",
        fill = "#000000",
        font = ("None", int(20.0)))

    window.resizable(False, False)
    window.mainloop()
