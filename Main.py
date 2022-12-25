from tkinter import *
import mysql.connector as sqLtor

#===================GLOBAL VARIABLES================================
fromd = ''
tod = ''

#====================SQL CONNECTION=================================
mycon =sqLtor.connect(host = "localhost", user = "root", passwd = "2005", database =  "proj")
c1 = mycon.cursor()
if mycon.is_connected():
    print("Python is connectod to SQL")

#====================BOOK===========================================


def book(fromd,tod,val):
    
       
    
    
    def confirm():
        name = entry0.get()
        no = entry1.get()
        contact = entry2.get()
        gen = entry3.get()
        em = entry4.get()
        window.destroy()
        con(name,no,contact,gen,em,fromd,tod,val)
    def reset():
        entry0.delete(0,END)
        entry1.delete(0,END)
        entry2.delete(0,END)
        entry3.delete(0,END)
        entry4.delete(0,END) 
 


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
        command = reset,
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

#======================CONFIRM TICKETS============================================


def con(name,no,contact,gen,em,fromd,tod,val):
   
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
        bg = "#fcfcfc")

    entry0.place(
        x = 177, y = 102,
        width = 149,
        height = 25)



    entry1 = Entry(
        bg = "#fcfcfc")

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

    entry0.insert(0,name)


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

    entry1.insert(0,fromd)
    entry2.insert(0,no)
    entry6.insert(0,gen)
    entry7.insert(0,em)
    entry3.insert(0,tod)
    entry4.insert(0,contact)
    if val == 3:
        price = 3500
    elif val == 2:
        price = 750
    elif val == 1:
        price = 250
    x = int(val) 
    fp = x * price
    entry5.insert(0,fp)       

#==========================CALL FUNCTIONS==========================================
def train(): 
            
            fromd = entry0.get()
            tod = entry2.get()
            ct = mycon.cursor()
            ct.execute("select * from trains")
            data = ct.fetchall()
            entry1.delete(1.0,END)
            entry1.insert(END,'Train Name\t\t\t Timings')
            for i in data:
                if i[2] == fromd and i[3] == tod:
                    print(i)
                    tname = i[1]
                    time = i[7]
                    entry1.insert(END,f'\n\n{tname}\t\t\t{time}')
               
                    
                     
                     
def flight():  
            fromd = entry0.get()
            tod = entry2.get()
            ct = mycon.cursor()
            ct.execute("select * from flights")
            data = ct.fetchall()
            entry1.delete(1.0,END)
            entry1.insert(END,'Train Name\t\t\t Timings')
            for i in data:
                if i[2] == fromd and i[3] == tod:
                     print(i)
                     tname = i[1]
                     time = i[6]
                     entry1.insert(END,f'\n\n{tname}\t\t\t{time}')
                     
                     
                     
def bus():  
            fromd = entry0.get()
            tod = entry2.get()
            ct = mycon.cursor()
            ct.execute("select * from buses")
            data = ct.fetchall()
            entry1.delete(1.0,END)
            entry1.insert(END,'Train Name\t\t\t Timings')
            for i in data:
                if i[2] == fromd and i[3] == tod:
                     print(i)
                     tname = i[1]
                     time = i[5]
                     entry1.insert(END,f'\n\n{tname}\t\t\t{time}')
                     
                  


def search(val):
        fromd = entry0.get()
        tod = entry2.get()
        ma.destroy()
        book(fromd,tod,val)
              
        
        
#================================MAIN======================================
ma = Tk()

ma.geometry("671x381")
ma.configure(bg = "#ffffff")
canvas = Canvas(
    ma,
    bg = "#ffffff",
    height = 381,
    width = 671,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)




entry0 = Entry(
    bg = "#fffdfd",)

entry0.place(
    x = 122, y = 85,
    width = 217,
    height = 30)

canvas.create_text(
    61.0, 162.5,
    text = "To",
    fill = "#000000",
    font = ("Jaldi-Regular", int(26.0)))



entry1 = Text(font = 'arial 8',
    bg = "#ffffff",)

entry1.place(
    x = 392, y = 85,
    width = 230,
    height = 275)


entry2 = Entry(
    bg = "#fff")

entry2.place(
    x = 122, y = 159,
    width = 217,
    height = 30)

canvas.create_text(
    61.0, 100.5,
    text = "From",
    fill = "#000000",
    font = ("Jaldi-Regular", int(26.0)))

var1 = IntVar()
b0 = Radiobutton(text="Flight",variable = var1,value = 3,command = flight)

b0.place(
    x = 256, y = 256,
    width = 96,
    height = 36)

b1 = Button(
    text = "Next",
    command = lambda:search(var1.get()),
    relief = "flat")

b1.place(
    x = 145, y = 326,
    width = 96,
    height = 36)

b2 = Radiobutton(text="Bus",variable = var1,value = 2,command = bus)

b2.place(
    x = 160, y = 256,
    width = 81,
    height = 36)


b3 = Radiobutton(text="Trains",variable = var1,value = 1,command = train)

b3.place(
    x = 50, y = 256,
    width = 95,
    height = 36)

canvas.create_text(
    324.0, 34.5,
    text = "SEARCH DESTINATION",
    fill = "#000000",
    font = ("Jaldi-Regular", int(24.0)))

ma.resizable(False, False)
ma.mainloop()


