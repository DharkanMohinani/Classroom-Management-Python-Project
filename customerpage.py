from DefaultPage import *
from components.messagecomponent import WhiteMessage
from components.ButtonComponent import *
from DatabaseHelper import *
from components.table import SimpleTable
from PIL import Image,ImageTk
from tkinter import messagebox
from functools import reduce
import datetime
import requests

class CustomerHomePage(DefaultPage):
    def __init__(self, root, customer_details):
        super().__init__(root)
        # store customer details tuple here
        self.details = customer_details
        print(customer_details)
        self.root.state('zoomed')
        # create dictionary for food menu items
        self.dct_IntVar = {}
        self.m = WhiteMessage(self.panel, text=f"Welcome {self.details[1]}")
        self.m.place(x=50, y=20)
        self.add_buttons()
        # Add the menu frame that has an image

    def add_buttons(self):
        # Add 3 buttons- logout, check order status, order history
        self.logout = Button(self.f, text="Logout", width=21, height=2, font=("20"),bd=6,bg="brown",
                                  command=self.customer_logout)
        self.logout.place(x=1260, y=200)

        self.Download = WhiteButton(self.f, text="Downloads", width=25, font=("20"), height=2, bg="brown",bd=6,
                                    command=self.downloads)
        self.Download.place(x=940, y=200)

        self.holiday = WhiteButton(self.f, text="View Holidays", width=25, font=("20"), height=2,bg="brown",bd=6,
                                   command=self.view_holiday)
        self.holiday.place(x=630, y=200)

        self.book = WhiteButton(self.f, text="View Books", height=2, font=("20"), width=25, bg="brown",bd=6,
                                command=self.view_books)
        self.book.place(x=320, y=200)

        self.Schedule = WhiteButton(self.f, text="View Schedule", width=25, height=2, bg="brown",bd=6, font=("20"),
                                    command=self.view_schedule)
        self.Schedule.place(x=10, y=200)

    def customer_logout(self):
        import MainPage
        self.f.destroy()
        self.redirect = MainPage.MainPage(self.root)

    def view_schedule(self):
        print(self.details)
        query = """ select faculty_name,lecday,subjectid,start_time,end_time from Lecture1 as lo join Teacher1 as tr on lo.faculty_name=tr.name """
        result = DatabaseHelper.get_all_data(query)
        print(result)
        self.c = Canvas(self.f, height=500, width=600)
        self.i = ImageTk.PhotoImage(Image.open("images/12.jpg"))
        self.c.create_image(0, 0, anchor=NW, image=self.i)
        self.c.pack()
        self.menu_frame = SimpleTable(self.f, rows=len(result), columns=len(result[0]), height=300, width=350)
        self.menu_frame.place(x=500, y=350)
        self.menu_frame.grid_propagate(0)
        text_font = ("Calibri", 25)
        for i in range(len(result)):
            for j in range(len(result[0])):
                self.menu_frame.set(row=i, column=j, value=result[i][j])

    def view_holiday(self):
        query = """select holiday_date,reason_for_Holiday from holiday """
        result = DatabaseHelper.get_all_data(query)
        print(result)
        self.menu_frame = SimpleTable(self.f, rows=len(result), columns=len(result[0]), height=300, width=350)
        self.menu_frame.place(x=500, y=350)
        self.menu_frame.grid_propagate(0)
        text_font = ("Calibri", 25)
        for i in range(len(result)):
            for j in range(len(result[0])):
                self.menu_frame.set(row=i, column=j, value=result[i][j])

    def view_books(self):

        query = """ select subject_name,book_name,author_name from book """
        result = DatabaseHelper.get_all_data(query)
        print(result)
        self.menu_frame1 = SimpleTable(self.f, rows=len(result), columns=len(result[0]), height=300, width=350)
        self.menu_frame1.place(x=500, y=350)
        self.menu_frame1.grid_propagate(0)
        self.text_font = ("Calibri", 25)

        for i in range(len(result)):
            for j in range(len(result[0])):
                self.menu_frame1.set(row=i, column=j, value=result[i][j])

    def ri(self, download_frame):
        python_url = "https://www.engbookspdf.com/uploads/pdf-books/PythonandHackingMadeSimple-1.pdf"
        res1 = requests.get(python_url)
        print(res1)
        with open("python.pdf", "wb") as f1:
            f1.write(res1.content)

    def sh(self, download_frame):
        datastructures_url = "https://www.engbookspdf.com/uploads/pdf-books/LearningFunctionalDataStructuresandAlgorithmsbyKhotandrMishra-1.pdf"
        res2 = requests.get(datastructures_url)
        print(res2)
        with open("datastructures.pdf", "wb") as f2:
            f2.write(res2.content)


    def ik(self, download_frame):
        CProgram_url = "https://www.engbookspdf.com/uploads/pdf-books/ProgramminginCforEngineeringandScience-1.pdf"
        res3 = requests.get(CProgram_url)
        print(res3)
        messagebox.showinfo("Downloaded","Your E-Book has been Downloaded")
        with open("CProgram.pdf", "wb") as f3:
            f3.write(res3.content)

    def av(self, download_frame):
        HTML_url = "https://www.engbookspdf.com/uploads/pdf-books/HTMLandCSSLearnTheFundamentalsIn7daysbyKnapp-1.pdf"
        res4 = requests.get(HTML_url)
        print(res4)
        with open("HTML.pdf", "wb") as f4:
            f4.write(res4.content)

    def downloads(self):

        download_frame = Frame(self.f, height=300, width=350)
        download_frame.place(x=500, y=350)
        self.c = Canvas(download_frame, height=500, width=350)
        self.i = ImageTk.PhotoImage(Image.open("images/12.jpg"))
        self.c.create_image(0, 0, anchor=NW, image=self.i)
        self.c.pack()
        download_frame.pack_propagate(0)

        '''self.faculty_label = Label(download_frame, text="Download your E-Book now", bg="yellow", fg="black",
                                   font=("monotype corsiva", "18"), height=1)
        self.faculty_label.place(x=128, y=310)'''

        self.Label = Label(download_frame, text="Download your E-Book now!!", bg="yellow", fg="black",
                                   font=("monotype corsiva", "18"), height=1)
        self.Label.place(x=10, y=50)
        '''self.label2 = Label(download_frame, text="Python Programming", bg="black", fg="white",
                            font=("book antiqua", "16"),
                            height=1)
        self.label2.place(x=10, y=100)'''
        self.student_label = Label(download_frame, text="Python Programming", bg="black", fg="white",
                                   font=("monotype corsiva", "18"), height=1)
        self.student_label.place(x=10, y=100)

        self.a = Button(download_frame, text="Download",  bg="brown",width=15,height=1,bd=6,
                             command=lambda: self.ri(download_frame))
        self.a.place(x=225, y=100)

        self.label3 = Label(download_frame, text="Data Structures", bg="black", fg="white",
                                   font=("monotype corsiva", "18"), height=1)
        self.label3.place(x=10, y=150)

        self.b = Button(download_frame, text="Download", bg="brown",width=15,height=1,bd=6,
                             command=lambda: self.sh(download_frame))
        self.b.place(x=225, y=150)

        self.label4 = Label(download_frame, text="Programming in C", bg="black", fg="white",
                                   font=("monotype corsiva", "18"), height=1)
        self.label4.place(x=10, y=200)

        self.c = Button(download_frame, text="Download",  bg="brown",width=15,height=1,bd=6,
                             command=lambda: self.ik(download_frame))
        self.c.place(x=225, y=200)

        self.label5 = Label(download_frame, text="HTML and CSS", bg="black", fg="white",
                                   font=("monotype corsiva", "18"), height=1)
        self.label5.place(x=10, y=250)


        self.d = Button(download_frame, text="Download", height=1,bd=6, bg="brown",width=15,
                             command=lambda: self.av(download_frame))
        self.d.place(x=225, y=250)


if __name__ == '__main__':
    root = Tk()
    c = CustomerHomePage(root, (3, 'Agicha', 3, 4))
    root.mainloop()
