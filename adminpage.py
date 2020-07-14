from DefaultPage import *
from components.ButtonComponent import *
from DatabaseHelper import *
from components.table import SimpleTable
from components.messagecomponent import WhiteMessage
from tkinter import messagebox
from PIL import Image,ImageTk
class AdminHomePage(DefaultPage):
    def __init__(self, root, admin_details):
        print("Admin home page called")
        super().__init__(root)
        self.root.state('zoomed')  # Maximize the screen
        # Tuple received from DATABASE. Eg=> (2, 'Ritesh', 'SGT', 'riteshagicha@gmail.com', 'RiteshPic3.jpg')
        self.details = admin_details
        print(admin_details)
        # Dictionary to store the pending order checkbox IntVars
        self.dct_IntVar = {}

        self.admin_page = WhiteMessage(self.f, text=f"Welcome {self.details[0]}")
        self.admin_page.place(x=220, y=20)

        # self.add_admin_details()
        self.add_buttons()
        self.c = Canvas(self.f, width=900, height=800)

    def add_buttons(self):
        self.lecture = GrayButton(self.f, "Add Lecture Details", self.lecture_details,bd=7, bg="brown", fg="white")
        self.lecture.place(x=100, y=90)
        self.marks = GrayButton(self.f, "Student Marks", self.marks_details, bg="brown", bd=7,fg="white")
        self.marks.place(x=300, y=90)
        self.holiday = GrayButton(self.f, "Add Holiday", self.holiday_details, bg="brown",bd=7, fg="white")
        self.holiday.place(x=500, y=90)
        self.attendance = GrayButton(self.f, "Student Attendance", self.attendance_details, bg="brown", bd=7,fg="white")
        self.attendance.place(x=700, y=90)
        self.books = GrayButton(self.f, "Add Books", self.add_books, bg="brown",bd=7, fg="white")
        self.books.place(x=900, y=90)
        self.assign = GrayButton(self.f, "Assign Students", self.assign_student, bg="brown",bd=7, fg="white")
        self.assign.place(x=1100, y=90)
        self.logout = GrayButton(self.f, "Log out", self.admin_logout, bg="brown",bd=7, fg="white")
        self.logout.place(x=1300, y=90)




    def lecture_details(self):
        lecture_frame = Frame(self.panel, height=600, width=600, bg="darkgray")
        lecture_frame.place(x=450, y=150)
        self.c = Canvas(lecture_frame, height=600, width=600)
        self.i = ImageTk.PhotoImage(Image.open("images/12.jpg"))
        self.c.create_image(0, 0, anchor=NW, image=self.i)
        self.c.pack()
        lecture_frame.pack_propagate(0)

        self.lecture_label = Label(lecture_frame, text="Lecture", bg="black", fg="white", font=("book antiqua", "16"),
                                   height=1)
        self.lecture_label.place(x=130, y=10)

        self.lecture_entry = Entry(lecture_frame, bg="white", fg="black", font=("10"))
        self.lecture_entry.place(x=270, y=10)

        self.faculty_label = Label(lecture_frame, text="Enter name", bg="black", fg="white",
                                   font=("book antiqua", "16"), height=1)
        self.faculty_label.place(x=130, y=70)

        self.faculty_entry = Entry(lecture_frame, bg="white", fg="black", font=("10"))
        self.faculty_entry.place(x=270, y=70)

        self.day_label = Label(lecture_frame, text="Enter day", bg="black", fg="white",
                               font=("book antiqua", "16"), height=1)
        self.day_label.place(x=130, y=130)

        self.day_entry = Entry(lecture_frame, bg="white", fg="black", font=("10"))
        self.day_entry.place(x=270, y=130)

        self.start_label = Label(lecture_frame, text="Start time", bg="black", fg="white", font=("book antiqua", "16"),
                                 height=1)
        self.start_label.place(x=130, y=190)

        self.start_entry = Entry(lecture_frame, bg="white", fg="black", font=("10"))
        self.start_entry.place(x=270, y=190)

        self.end_label = Label(lecture_frame, text="End time", bg="black", fg="white", font=("book antiqua", "16"),
                               height=1)
        self.end_label.place(x=130, y=250)

        self.end_entry = Entry(lecture_frame, bg="white", fg="black", font=("10"))
        self.end_entry.place(x=270, y=250)

        self.submitl_button = Button(lecture_frame, text="Submit", bg="grey", fg="black", font=("4"),bd=4,
                                     command=lambda: self.add_lecture(lecture_frame))
        self.submitl_button.place(x=210, y=310)

        self.submit2_button = Button(lecture_frame, text="View Lectures", bg="grey", fg="black", font=("4"),bd=4,
                                     command=lambda: self.view_lec(lecture_frame))
        self.submit2_button.place(x=300, y=310)

    def add_lecture(self, lecture_frame):
        lecture = self.lecture_entry.get()
        day = self.day_entry.get()
        faculty = self.faculty_entry.get()
        start = self.start_entry.get()
        end = self.end_entry.get()
        print("done")
        parameters = (lecture, day, faculty, start, end)
        DatabaseHelper.execute_query(
            "insert into Lecture1 (subjectid,lecday,faculty_name,start_time,end_time) values ('%s','%s','%s','%s','%s')",
            parameters)

        messagebox.showinfo("Success", "Lecture entered  successfully")

    def view_lec(self, lecture_frame):

        query = """select faculty_name,lecday,subjectid,start_time,end_time from Lecture1 as lo join Teacher1 as tr on lo.faculty_name=tr.name """
        result = DatabaseHelper.get_all_data(query)
        print(result)

        # self.menu_frame = SimpleTable(self.f, rows=len(result), columns=len(result[0]), height=300, width=300)
        self.menu_frame = SimpleTable(lecture_frame, rows=len(result), columns=len(result[0]), height=200, width=310)
        self.menu_frame.place(x=150, y=360)
        self.menu_frame.grid_propagate(0)
        text_font = ("Calibri", 25)
        for i in range(len(result)):
            for j in range(len(result[0])):
                self.menu_frame.set(row=i, column=j, value=result[i][j])

    def marks_details(self):
        marks_frame = Frame(self.panel, height=600, width=600, bg="darkseagreen")
        marks_frame.place(x=450, y=150)
        self.c = Canvas(marks_frame, height=600, width=600)
        self.i = ImageTk.PhotoImage(Image.open("C:/Users/Dhadkan/Downloads/8.jpg"))
        self.c.create_image(0, 0, anchor=NW, image=self.i)
        self.c.pack()
        marks_frame.pack_propagate(0)

        self.student_label = Label(marks_frame, text="Student ID", bg="sandybrown", fg="black",
                                   font=("monotype corsiva", "18"), height=1)
        self.student_label.place(x=90, y=30)

        self.studentId_entry = Entry(marks_frame, bg="white", fg="black", font=("10"))
        self.studentId_entry.place(x=270, y=30)

        self.name_label = Label(marks_frame, text="Python marks", bg="sandybrown", fg="black",
                                font=("monotype corsiva", "18"),
                                height=1)
        self.name_label.place(x=90, y=100)

        self.python_entry = Entry(marks_frame, bg="white", fg="black", font=("10"))
        self.python_entry.place(x=270, y=100)

        self.password_label = Label(marks_frame, text="Data Structures ", bg="sandybrown", fg="black",
                                    font=("monotype corsiva", "18"), height=1)
        self.password_label.place(x=90, y=170)

        self.java_entry = Entry(marks_frame, bg="white", fg="black", font=("10"))
        self.java_entry.place(x=270, y=170)

        self.faculty_label = Label(marks_frame, text="C programming mks", bg="sandybrown", fg="black",
                                   font=("monotype corsiva", "18"), height=1)
        self.faculty_label.place(x=90, y=240)

        self.maths_entry = Entry(marks_frame, bg="white", fg="black", font=("10"))
        self.maths_entry.place(x=270, y=240)

        self.faculty_label = Label(marks_frame, text="HTML&CSS mks", bg="sandybrown", fg="black",
                                   font=("monotype corsiva", "18"), height=1)
        self.faculty_label.place(x=90, y=310)

        self.mech_entry = Entry(marks_frame, bg="white", fg="black", font=("10"))
        self.mech_entry.place(x=275, y=310)

        self.submita_button = Button(marks_frame, text="Add", bg="grey", fg="black",
                                     font=("monotype corsiva", "14"), command=lambda: self.add_marks(marks_frame))
        self.submita_button.place(x=200, y=360)

        self.submita2_button = Button(marks_frame, text="View", bg="grey", fg="black",
                                      font=("monotype corsiva", "14"), command=lambda: self.view_marks(marks_frame))
        self.submita2_button.place(x=260, y=360)

    def view_marks(self, marks_frame):
        query = """ select StudentName,python,ds,C_Prog,HTML_CSS from marks as m join student1 as s on m.StudentId=s.StudentId """
        result = DatabaseHelper.get_all_data(query)
        print(result)
        # self.menu_frame = SimpleTable(self.f, rows=len(result), columns=len(result[0]), height=300, width=300)
        self.menu_frame = SimpleTable(marks_frame, rows=len(result), columns=len(result[0]), height=170, width=270)
        self.menu_frame.place(x=150, y=410)
        self.menu_frame.grid_propagate(0)
        text_font = ("Calibri", 25)
        for i in range(len(result)):
            for j in range(len(result[0])):
                self.menu_frame.set(row=i, column=j, value=result[i][j])

    def add_marks(self, marks_frame):
        studId = self.studentId_entry.get()
        python = self.python_entry.get()
        java = self.java_entry.get()
        maths = self.maths_entry.get()
        mechanics = self.mech_entry.get()
        print("done")
        parameters = (studId, python, java, maths, mechanics)
        DatabaseHelper.execute_query("insert into marks values ('%s','%s','%s','%s','%s')", parameters)
        messagebox.showinfo("Success", "Marks entered  successfully")

    def holiday_details(self):
        button_frame = Frame(self.panel, height=600, width=600, bg="peru")
        button_frame.place(x=450, y=150)
        self.c = Canvas(button_frame, height=600, width=600)
        self.i = ImageTk.PhotoImage(Image.open("C:/Users/Dhadkan/Downloads/1.png"))
        self.c.create_image(0, 0, anchor=NW, image=self.i)
        self.c.pack()
        button_frame.pack_propagate(0)

        self.frame_label = Label(button_frame, text="Enter date", bg="snow", fg="black",
                                 font=("freestyle script", "22"), height=1)
        self.frame_label.place(x=130, y=130)
        self.frame_label = Label(button_frame, text="Enter reason", bg="snow", fg="black",
                                 font=("freestyle script", "22"), height=1)
        self.frame_label.place(x=130, y=200)
        self.date_entry = Entry(button_frame, bg="white", fg="black", font=("10"))
        self.date_entry.place(x=270, y=130)
        self.reason_entry = Entry(button_frame, text="Enter reason", bg="white", fg="black", font=("10"))
        self.reason_entry.place(x=270, y=200)
        frame_button = Button(button_frame, text="Add Holiday", bg="white", fg="black", font=("10"),bd=6,
                              command=lambda: self.add_holiday(button_frame))
        frame_button.place(x=250, y=270)

    def add_holiday(self, button_frame):
        date = self.date_entry.get()
        reason = self.reason_entry.get()
        print("done")
        parameters = (date, reason)
        DatabaseHelper.execute_query("insert into holiday values ('%s','%s')", parameters)
        messagebox.showinfo("Success", "Holiday entered  successfully")

    def attendance_details(self):

        atten_frame = Frame(self.panel, height=600, width=600, bg="darkseagreen")
        atten_frame.place(x=450, y=150)
        self.c = Canvas(atten_frame, height=600, width=600)
        self.i = ImageTk.PhotoImage(Image.open("C:/Users/Dhadkan/Downloads/9.jpg"))
        self.c.create_image(0, 0, anchor=NW, image=self.i)
        self.c.pack()
        atten_frame.pack_propagate(0)

        self.student_label = Label(atten_frame, text="Student ID", bg="sandybrown", fg="black",
                                   font=("monotype corsiva", "18"), height=1)
        self.student_label.place(x=90, y=30)

        self.studentId_entry = Entry(atten_frame, bg="white", fg="black", font=("10"))
        self.studentId_entry.place(x=300, y=30)

        self.name_label = Label(atten_frame, text="Python attendance", bg="sandybrown", fg="black",
                                font=("monotype corsiva", "18"),
                                height=1)
        self.name_label.place(x=80, y=100)

        self.python_entry = Entry(atten_frame, bg="white", fg="black", font=("10"))
        self.python_entry.place(x=300, y=100)

        self.password_label = Label(atten_frame, text="Data Structures", bg="sandybrown", fg="black",
                                    font=("monotype corsiva", "18"), height=1)
        self.password_label.place(x=90, y=170)

        self.java_entry = Entry(atten_frame, bg="white", fg="black", font=("10"))
        self.java_entry.place(x=300, y=170)

        self.faculty_label = Label(atten_frame, text="C Programming ", bg="sandybrown", fg="black",
                                   font=("monotype corsiva", "18"), height=1)
        self.faculty_label.place(x=90, y=250)

        self.maths_entry = Entry(atten_frame, bg="white", fg="black", font=("10"))
        self.maths_entry.place(x=300, y=250)

        self.faculty_label = Label(atten_frame, text="HTML & CSS ", bg="sandybrown", fg="black",
                                   font=("monotype corsiva", "18"), height=1)
        self.faculty_label.place(x=90, y=310)

        self.mech_entry = Entry(atten_frame, bg="white", fg="black", font=("10"))
        self.mech_entry.place(x=300, y=310)

        self.submita_button = Button(atten_frame, text="Add", bg="grey", fg="black",
                                     font=("monotype corsiva", "14"), command=lambda: self.add_attendance(atten_frame))
        self.submita_button.place(x=200, y=360)

        self.submita2_button = Button(atten_frame, text="View", bg="grey", fg="black",
                                      font=("monotype corsiva", "14"),
                                      command=lambda: self.view_attendance(atten_frame))
        self.submita2_button.place(x=260, y=360)

    def view_attendance(self, atten_frame):
        query = """ select StudentName,python,Ds,C_Prog,HTML_CSS from attendance as a join student1 as s on a.StudentId=s.StudentId """
        result = DatabaseHelper.get_all_data(query)
        print(result)
        # self.menu_frame = SimpleTable(self.f, rows=len(result), columns=len(result[0]), height=300, width=300)
        self.menu_frame = SimpleTable(atten_frame, rows=len(result), columns=len(result[0]), height=170, width=270)
        self.menu_frame.place(x=150, y=410)
        self.menu_frame.grid_propagate(0)
        text_font = ("Calibri", 25)
        for i in range(len(result)):
            for j in range(len(result[0])):
                self.menu_frame.set(row=i, column=j, value=result[i][j])

    def add_attendance(self, atten_frame):
        studId = self.studentId_entry.get()
        python = self.python_entry.get()
        java = self.java_entry.get()
        maths = self.maths_entry.get()
        mechanics = self.mech_entry.get()
        print("done")
        parameters = (studId, python, java, maths, mechanics)
        DatabaseHelper.execute_query("insert into attendance values ('%s','%s','%s','%s','%s')", parameters)
        messagebox.showinfo("Success", "Attendance entered  successfully")

    def add_books(self):
        book_frame = Frame(self.panel, height=600, width=600, bg="rosybrown")

        book_frame.place(x=450, y=150)
        self.c = Canvas(book_frame, height=600, width=600)
        self.i = ImageTk.PhotoImage(Image.open("C:/Users/Dhadkan/Downloads/4.png"))
        self.c.create_image(0, 0, anchor=NW, image=self.i)
        self.c.pack()
        book_frame.pack_propagate(0)

        self.subject_label = Label(book_frame, text="Subject Name", bg="darkseagreen", fg="black",
                                   font=("baskerville old face", "16"), height=1)
        self.subject_label.place(x=110, y=100)
        self.subject_entry = Entry(book_frame, bg="white", fg="black", font=("10"))
        self.subject_entry.place(x=270, y=100)

        self.books_label = Label(book_frame, text="Book Name", bg="darkseagreen", fg="black",
                                 font=("baskerville old face", "16"), height=1)
        self.books_label.place(x=110, y=170)
        self.books_entry = Entry(book_frame, bg="white", fg="black", font=("10"))
        self.books_entry.place(x=270, y=170)

        self.author_label = Label(book_frame, text="Author Name", bg="darkseagreen", fg="black",
                                  font=("baskerville old face", "16"), height=1)
        self.author_label.place(x=110, y=240)
        self.author_entry = Entry(book_frame, bg="white", fg="black", font=("10"))
        self.author_entry.place(x=270, y=240)

        self.books_button = Button(book_frame, text="Add Book", bg="white", fg="black",height=1,width=10,bd=6,
                                   font=("baskerville old face", "15"), command=lambda: self.books_sql(book_frame))
        self.books_button.place(x=230, y=320)

    def books_sql(self, book_frame):
        subject_name = self.subject_entry.get()
        book_name = self.books_entry.get()
        author_name = self.author_entry.get()
        print("done")
        parameters = (subject_name, book_name, author_name)
        DatabaseHelper.execute_query("insert into book values ('%s','%s','%s')", parameters)
        messagebox.showinfo("Success", "Book stored successfully")

    def assign_student(self):
        assign_frame = Frame(self.panel, height=600, width=600, bg="darkseagreen")
        assign_frame.place(x=450, y=150)
        self.c = Canvas(assign_frame, height=600, width=600)
        self.i = ImageTk.PhotoImage(Image.open("C:/Users/Dhadkan/Downloads/11.jpg"))
        self.c.create_image(0, 0, anchor=NW, image=self.i)
        self.c.pack()
        assign_frame.pack_propagate(0)

        self.student_label = Label(assign_frame, text="Student ID", bg="sandybrown", fg="black",
                                   font=("monotype corsiva", "18"), height=1)
        self.student_label.place(x=130, y=30)

        self.student_entry = Entry(assign_frame, bg="white", fg="black", font=("10"))
        self.student_entry.place(x=270, y=30)

        self.name_label = Label(assign_frame, text="Name", bg="sandybrown", fg="black", font=("monotype corsiva", "18"),
                                height=1)
        self.name_label.place(x=130, y=100)

        self.name_entry = Entry(assign_frame, bg="white", fg="black", font=("10"))
        self.name_entry.place(x=270, y=100)

        self.password_label = Label(assign_frame, text="password", bg="sandybrown", fg="black",
                                    font=("monotype corsiva", "18"), height=1)
        self.password_label.place(x=130, y=170)

        self.password_entry = Entry(assign_frame, bg="white", fg="black", font=("10"))
        self.password_entry.place(x=270, y=170)

        self.faculty_label = Label(assign_frame, text="Faculty name", bg="sandybrown", fg="black",
                                   font=("monotype corsiva", "18"), height=1)
        self.faculty_label.place(x=130, y=250)

        self.faculty_entry = Entry(assign_frame, bg="white", fg="black", font=("10"))
        self.faculty_entry.place(x=270, y=250)

        self.contact_label = Label(assign_frame, text="Contact No.", bg="sandybrown", fg="black",
                                   font=("monotype corsiva", "18"), height=1)
        self.contact_label.place(x=130, y=320)

        self.contact_entry = Entry(assign_frame, bg="white", fg="black", font=("10"))
        self.contact_entry.place(x=270, y=320)

        self.gender_label = Label(assign_frame, text="Gender", bg="sandybrown", fg="black",
                                  font=("monotype corsiva", "18"),
                                  height=1)
        self.gender_label.place(x=130, y=390)

        self.gender_entry = Entry(assign_frame, bg="white", fg="black", font=("10"))
        self.gender_entry.place(x=270, y=390)

        self.age_label = Label(assign_frame, text="Age", bg="sandybrown", fg="black", font=("monotype corsiva", "18"),
                               height=1)
        self.age_label.place(x=130, y=460)

        self.age_entry = Entry(assign_frame, bg="white", fg="black", font=("10"))
        self.age_entry.place(x=270, y=460)

        self.submita_button = Button(assign_frame, text="Assign", bg="grey", fg="black",
                                     font=("monotype corsiva", "14"), command=lambda: self.add_students(assign_frame))
        self.submita_button.place(x=230, y=500)

    def add_students(self, assign_frame):
        student = self.student_entry.get()
        name = self.name_entry.get()
        password = self.password_entry.get()
        faculty = self.faculty_entry.get()
        contact = self.contact_entry.get()
        gender = self.gender_entry.get()
        age = self.age_entry.get()
        # subject = self.subject_entry.get()

        print("done")
        parameters = (student, name, password, faculty, contact, age, gender)
        DatabaseHelper.execute_query(
            "insert into student1 (studentId,StudentName,StudentPassword,faculty_name,contact,age,gender) values ('%s','%s','%s','%s','%s','%s','%s')",
            parameters)
        messagebox.showinfo("Success", "student stored successfully")


    def admin_logout(self):
        import MainPage
        self.f.destroy()
        self.panel.destroy()
        self.redirect = MainPage.MainPage(self.root)


if (__name__ == "__main__"):
    root = Tk()
    admin_details = (2, 'Ritesh', 'SGT', 'riteshagicha@gmail.com', 'RiteshPic3.jpg')
    a = AdminHomePage(root, admin_details)
    root.mainloop()