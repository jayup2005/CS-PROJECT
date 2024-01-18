from tkinter import *

def con():
    co = Tk()
    
    co.geometry("842x463")
    co.configure(bg = "#ffffff")
    canvas = Canvas(
        co,
        bg = "#ffffff",
        height = 463,
        width = 842,
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
        bg = "#fffdfd")

    entry1.place(
        x = 553, y = 106,
        width = 149,
        height = 25)



    entry2 = Entry(
        bg = "#fcfcfc")

    entry2.place(
        x = 177, y = 161,
        width = 149,
        height = 25)



    entry3 = Entry(
        bg = "#fcfcfc")

    entry3.place(
        x = 553, y = 161,
        width = 149,
        height = 25)


    entry4 = Entry(
        bg = "#fcfcfc")

    entry4.place(
        x = 177, y = 225,
        width = 149,
        height = 25)



    entry5 = Entry(
        bg = "#fcfcfc")

    entry5.place(
        x = 553, y = 219,
        width = 149,
        height = 25)



    entry6 = Entry(
        bg = "#fcfcfc")

    entry6.place(
        x = 177, y = 287,
        width = 149,
        height = 25)



    entry7 = Entry(
        bg = "#fcfcfc")

    entry7.place(
        x = 177, y = 345,
        width = 149,
        height = 25)

    canvas.create_text(
        62.0, 113.5,
        text = "Name",
        fill = "#000000",
        font = ("None", int(15.0)))

    canvas.create_text(
        472.0, 122.5,
        text = "FROM",
        fill = "#000000",
        font = ("None", int(15.0)))

    b0 = Button(
        text = "Book Tickets",
        relief = "flat")

    b0.place(
        x = 628, y = 415,
        width = 156,
        height = 37)

    canvas.create_text(
        70.0, 174.5,
        text = "No Of\nPassengers",
        fill = "#000000",
        font = ("None", int(15.0)))

    canvas.create_text(
        470.5, 175.0,
        text = "TO",
        fill = "#000000",
        font = ("None", int(15.0)))

    canvas.create_text(
        65.5, 239.0,
        text = "Contact.No",
        fill = "#000000",
        font = ("None", int(15.0)))

    canvas.create_text(
        470.5, 232.0,
        text = "FARE PRICE",
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
        395.5, 35.5,
        text = "CONFIRM TICKETS",
        fill = "#000000",
        font = ("None", int(20.0)))

    co.resizable(False, False)
    co.mainloop()
