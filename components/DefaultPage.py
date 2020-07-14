from tkinter import *
from PIL import Image,ImageTk

class DefaultPage:
    def __init__(self,root):
        self.root=root

        self.root.title('Classroom management')
        #ensure that size of image is same as/greater than size of frame
        self.f=Frame(root,width=1600,height=900)
        self.f.pack()

        self.raw_image = Image.open("images/5.jpg")
        # define the size of the image, which will also determine the size of the button
        self.raw_image = self.raw_image.resize((1600, 900))
        self.img = ImageTk.PhotoImage(self.raw_image)

        self.panel = Label(self.f, image=self.img)
        self.panel.pack()
        self.panel.pack_propagate(0)
        #Add the message saying "Foodzapp"
        self.m = Message(self.panel, width=600, font=("Monotype Corsiva",20,"bold","italic"),text="Classroom management",bg="white",relief=SOLID,borderwidth=2)
        self.m.place(x=620, y=20)
        #The footer at the bottom
        self.footer=Label(self.panel,bg="yellow",height=1,text="kNOWLEDGE IS POWER")
        self.footer.pack(side=BOTTOM,fill=X)
        self.f.pack_propagate(0)


if(__name__=="__main__"):
    root=Tk()
    d=DefaultPage(root)
    root.mainloop()
#Agar->> DefaultPage-->initial page--> __NAME__==> __main__
#ELSE-> __NAME___==> DEFAULTPAGE

