import csv
import re
from tkinter import *
from drive import checkmail
from drive import checkphone
from drive import checkname
from drive import checkdob
from tkinter.messagebox import showerror
from tkinter.messagebox import showinfo





class App(Frame):


    def exitt(self):
        exit()

    def abt(self):
        showinfo(title= "Thank you" , message ="Thank you for your time , Your Feedback is submitted successfully")

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.output()

    def output(self):
        list1 = ['Product 0', 'Product 1', 'Product 2', 'Product 3', 'Product 4', 'Product 5']
        self.co = StringVar(root)
        self.droplist = OptionMenu(root, self.co, *list1)
        self.co.set("Select Product")
        self.droplist.place(x=200, y=186)

        label_0 = Label(root, text="BYJU'S", fg="purple", width=20, font='Courier 45 bold ', bg= '#FFFFFF' )
        lable_r1 = Label(root,
                         text="Thank you for taking the time for provide feedback . We appreciate hearing from you and"
                              " will review your comments carefully.", fg="black", font='times 13 italic', bg= '#FFFFFF')
        feedback = Label(root, text="Product Feedback", fg="gray", font='times 20 bold ', bg= '#FFFFFF')

        label_0.place(x=132 , y=11)
        feedback.place(x= 385 , y=84)
        lable_r1.place(x= 51 , y= 138)

        Label(text='Product :', font='times 15 bold' ,  bg= '#FFFFFF').place(x=75 , y=185)

        Label(text='Name:' ,  bg= '#FFFFFF').place(x=75,y=225)
        self.n = Text(root,  borderwidth=4, relief="groove" ,width = 60 , height = 1.5)
        self.n.place(x=75 , y=250)

        Label(text='Email Address:' ,  bg= '#FFFFFF').place(x=75 , y=300)
        self.e = Text(root, borderwidth=4, relief="groove" , width = 60 , height = 1.5)
        self.e.place(x=75 , y=325)

        Label(text='Phone Number:' ,  bg= '#FFFFFF').place(x=75 , y=375)
        self.p = Text(root,  borderwidth=4 , relief="groove" , width = 60 , height = 1.5)
        self.p.place(x=75, y=400)

        Label(text='Date Of Birth [dd/mm/yyyy]:' , bg= '#FFFFFF').place(x=75, y=450)
        self.d = Text(root, borderwidth=4, relief="groove", width=60, height=1.5)
        self.d.place(x=75, y=475)

        Label(text='Comment:' , bg= '#FFFFFF').place(x=75, y=525)
        self.c = Text(root,borderwidth=4, relief="groove" , width = 100 , height = 5)
        self.c.place(x=75 , y=550)

        self.b = Button(root, text = 'Submit',font ='bold' , width = 20,  bg = "purple", fg="white" ,  command=self.intermid)
        self.b.place(x=200 , y=660)

        self.exit = Button(root, text='Cancel', font ='bold', width=20, bg='purple', fg='white', command=self.exitt).place(x=550, y=660)
    def writeToFile(self):
        if self.co.get() is '':
            showerror(title="Error", message="Please select the product")

        checkdob(self.d.get('1.0', END))
        checkname(self.n.get('1.0', END))
        checkmail(self.e.get('1.0', END))
        checkphone(self.p.get('1.0', END))
        with open('WorkOrderLog.csv', 'a') as f:
            w = csv.writer(f, quoting=csv.QUOTE_ALL)

            w.writerow([self.co.get(), self.c.get('1.0', END), self.n.get('1.0', END), self.p.get('1.0', END),
                       self.e.get('1.0', END), self.d.get('1.0', END)])

    def intermid(self):
        self.writeToFile()
        self.abt()



if __name__ == "__main__":
    root=Tk()
    root.title('Buyjus')
    root.geometry('1000x740')
    root.config( bg= '#FFFFFF')
    app=App(master=root)
    app.mainloop()
    root.mainloop()
