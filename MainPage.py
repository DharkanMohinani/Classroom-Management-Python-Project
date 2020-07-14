from DefaultPage import *
from tkinter import messagebox
from components.ButtonComponent import GrayButton
from components.messagecomponent import WhiteMessage
from DatabaseHelper import *

class MainPage(DefaultPage):
    def __init__(self,root):
        #Calls the parent DefaultPage and adds its own widgets using add_widgets()
        super().__init__(root)
        self.root.geometry('900x600')
        #this is the reverse of 'zoomed' effect in AdminPage
        self.root.state('normal')
        self.add_widgets()

    def add_widgets(self):

        self.admin_button = GrayButton(self.panel, "Teacher login", lambda: self.get_login_screen("Admin"),bd=5,bg="black",fg="white",font=("berlin sens fb","12"),height="2")
        self.admin_button.place(x=240, y=130)
        self.user_button = GrayButton(self.panel, "Student login", lambda: self.get_login_screen("User"),bd=5,bg="black",fg="white",font=("berlin sens fb","12"),height="2")
        self.user_button.place(x=490, y=130)
        self.new_user_button = GrayButton(self.panel, "New Teacher? Sign up here",self.sign_up_form, borderwidth=5, relief=RIDGE,width=22,bg="black",fg="white",font=("berlin sens fb","12"),height="2")
        self.new_user_button.place(x=375, y=240)

        self.contact=WhiteMessage(self.f,text="Contact Details Here!",font=("forte", 16),bg="brown")
        self.contact_detail=WhiteMessage(self.f,text="classroom@yahoo.com,\n+68 35 7234 3456",font=("Times New Roman", 15, "bold", "italic"))
        self.contact.place(x=360, y=350)
        self.contact.bind("<Button-1>", self.show_contact_details)

    def show_contact_details(self, event):
        self.contact_detail.place(x=360, y=430)

    def reset(self):
        self.e_username.delete(0,END)
        self.e_password.delete(0, END)


    def get_login_screen(self,login_type):
        # Creates a temporary window to login
        # 2 labels-> username,password
        #2 entry-> take username, password
        # 2 Button-> submit, reset
        login_window = Toplevel()
        login_window.title(login_type)
        f = Frame(login_window, bg = 'brown',height=200, width=430)
        l1 = Label(f, width=20, text="Enter username: ",font=("consolas","13"))
        #storing this inside self because we need this later to get data
        self.e_username = Entry(f, width=30, fg='black', bg='white',font=("13"))
        #activative the cursor here
        self.e_username.focus_set()
        self.e_password = Entry(f, width=30, fg='black', bg='white', show='*',font=("13"))
        l2 = Label(f, width=20, text="Enter password: ",font=("consolas","13"))
        l1.grid(row=1, column=1, padx=10, pady=10)
        l2.grid(row=2, column=1, padx=10, pady=10)
        self.e_username.grid(row=1, column=4, padx=10, pady=10)
        self.e_password.grid(row=2, column=4, padx=10, pady=10)
        b1 = Button(f, text="Submit", height=2, width=10,bd=5,bg="silver",command=lambda: self.validate(login_window, login_type))
        #Whenever enter is pressed anywhere on this temporary root, call my validate function.
        login_window.bind('<Return>', lambda event: self.validate(login_window, login_type))
        b1.grid(row=3, column=1, padx=10,pady=20, sticky='e')
        b2 = Button(f, text="Reset", height=2, width=10,bd=5,bg="silver", command=lambda: self.reset())
        b2.grid(row=3, column=4, padx=10, sticky='w')
        f.pack()
        f.grid_propagate(0)

    def validate(self,login_window,login_type):
        username=self.e_username.get()
        pwd = self.e_password.get()
        if(login_type=="Admin"):
            query = "Select * from world.Teacher1 where username= '%s' and password='%s'"
        else:
            query = "Select * from world.Student1 where StudentName= '%s' and StudentPassword='%s'"
        parameters=(username,pwd)
        result=DatabaseHelper.get_data(query,parameters)
        if(result is None or len(result)==0):
            messagebox.showerror("Login Failed","Incorrect credentials")
            login_window.tkraise()
            self.e_username.focus()
        else:
            messagebox.showinfo('Login Success',"Login successfuly completed")
            #Destorying the temporary window created for login
            login_window.destroy()
            self.f.destroy()
            self.panel.destroy()
            #the type of login was admin so go to adminhomepage
            if(login_type=="Admin"):
                import adminpage
                self.redirect=adminpage.AdminHomePage(self.root, result)
            else:
                #the type of login was user, so go to user home page
                import customerpage
                self.redirect=customerpage.CustomerHomePage(self.root,result)
        print(username)
        print(pwd)

    def sign_up_form(self):
        text_font = ("MS Serif", 12)
        registration_window = Toplevel()
        f = Frame(registration_window, width=450, height=500, bg="steelblue")
        Message(f, width=300, font=("harlow solid italic", 20), text="Classroom management", bg="white", fg="maroon",
                borderwidth=2).grid(row=0, column=0, columnspan=3, pady=5)
        f.pack()

        l = Label(f, text="Name", font=("forte"), bg="lightgrey", fg="black")
        l.grid(row=2, column=0, padx=10, pady=10)
        self.register_e1 = Entry(f)
        self.register_e1.grid(row=2, column=1, padx=10, pady=10)
        self.register_e1.focus_set()

        '''l = Label(f, text="Qualification", font=("forte"), bg="lightgrey", fg="black")
        l.grid(row=3, column=0, padx=10, pady=10)
        self.register_e2 = Entry(f)
        self.register_e2.grid(row=3, column=1, padx=10, pady=10)'''

        l = Label(f, text="Age", font=("forte"), bg="lightgrey", fg="black")
        l.grid(row=4, column=0, padx=10, pady=10)
        self.register_e3 = Entry(f)
        self.register_e3.grid(row=4, column=1, padx=10, pady=10)

        '''l = Label(f, text="Subject", font=("forte"), bg="lightgrey", fg="black")
        l.grid(row=5, column=0, padx=10, pady=10)
        self.register_e4 = Entry(f)
        self.register_e4.grid(row=5, column=1, padx=10, pady=10)'''

        l = Label(f, text="Username", font=("forte"), bg="lightgrey", fg="black")
        l.grid(row=6, column=0, padx=10, pady=10)
        self.register_e5 = Entry(f)
        self.register_e5.grid(row=6, column=1, padx=10, pady=10)

        l = Label(f, text="Password", font=("forte"), bg="lightgrey", fg="black")
        l.grid(row=7, column=0, padx=10, pady=10)
        self.register_e6 = Entry(f, show="*")
        self.register_e6.grid(row=7, column=1, padx=10, pady=10)

        l = Label(f, text="Re-enter Password", font=("forte"), bg="lightgrey", fg="black")
        l.grid(row=8, column=0, padx=10, pady=10)
        self.register_e7 = Entry(f, show="*")
        self.register_e7.grid(row=8, column=1, padx=10, pady=10)

        b1 = Button(f, text="Register", width=20, height=2, bg="lightgrey", fg="black", activebackground="gray",
                    command=lambda: self.register_user(registration_window))
        b1.grid(row=9, column=0, padx=10, pady=10, sticky="e")

        b2 = Button(f, text="Reset", width=20, height=2, bg="lightgrey", fg="black", activebackground="gray",
                    command=self.register_reset)
        b2.grid(row=9, column=1, padx=10, pady=10, sticky="w")
        f.grid_propagate(0)

    def register_reset(self):
        self.register_e1.delete(0, END)
        #self.register_e2.delete(0, END)
        self.register_e3.delete(0, END)
        #self.register_e4.delete(0, END)
        self.register_e5.delete(0, END)
        self.register_e6.delete(0,END)
        self.register_e7.delete(0, END)

    def register_user(self, registration_window):
        name = self.register_e1.get()
        # qualification = self.register_e2.get()
        age = self.register_e3.get()
        # subject = self.register_e4.get()
        username = self.register_e5.get()
        pwd = self.register_e6.get()
        pwd2 = self.register_e7.get()
        if (
                name == "" or age == "" or username == "" or pwd == "" or pwd2 == ""):
            messagebox.showwarning("Mandatory fields", "Please fill all the fields")
            registration_window.tkraise()
        elif (pwd != pwd2):
            messagebox.showerror("Password Error", "Passwords don't match.Please re-enter")
            registration_window.tkraise()
        else:
            query = "Insert into Teacher1(name,age,username,password) Values ('%s','%s','%s','%s')"
            args = (name, age, username, pwd)
            DatabaseHelper.execute_query(query, args)
            messagebox.showinfo("Success", "Admin registered successfully. Please login")
            registration_window.destroy()


if (__name__ == "__main__"):
    root = Tk()
    m = MainPage(root)
    root.mainloop()


