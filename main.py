from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")  
        self.root.title("Sharda University Attendance Page")
        

        # Sharda University LOGO
        img=Image.open(r"C:\Users\DELL\OneDrive\Desktop\automated+attendance_system\photo\sharda_logo.png")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        #Sharda University ABOVE
        img1=Image.open(r"C:\Users\DELL\OneDrive\Desktop\automated+attendance_system\photo\Sharda_full_view.jpeg")
        img1=img1.resize((1000,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=1050,height=130)

        # BAGROUND Image
        img3=Image.open(r"C:\Users\DELL\OneDrive\Desktop\automated+attendance_system\photo\Sharda_full_view.jpeg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="FACE RECOGNITION AUTOMATIC ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",28,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #Buttons
        img2=Image.open(r"C:\Users\DELL\OneDrive\Desktop\automated+attendance_system\photo\student.png")
        img2=img2.resize((300,300),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        b1=Button(bg_img,image=self.photoimg2,command=self.student_details,cursor="hand2")
        b1.place(x=600,y=200,width=300,height=280)

        b1_l=Button(bg_img,text="Attendance System",command=self.student_details,cursor="hand2",font=("times new roman",12,"bold"),bg="White",fg="Dark Blue")
        b1_l.place(x=600,y=480,width=300,height=40)


       
    def student_details(self):
        import attendance
        
if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()