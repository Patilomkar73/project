from tkinter import*
from PIL import Image,ImageTk,ImageDraw
from course import courseclass
from student import studentclass
from result import resultclass
from report import reportclass
from tkinter import messagebox
import os
from datetime import datetime
from math import sin, cos, radians
import sqlite3
import time
import os
class RMS:
    def __init__(self,root):
        self.root=root
        self.root.title("Sudent Result Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
         #__icon__
        self.icon=Image.open("images/logo_p.png")  #for open image
        self.logo_dash=ImageTk.PhotoImage(file="images/logo_p.png")#convert to photoimage



        # ___title___
        title=Label(self.root,text="Student Result Management System",padx=10,compound=LEFT,image=self.logo_dash,font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=0,y=0,relwidth=1,height=50)
        #__menu--
        m_frame=LabelFrame(self.root,text="menus",font=("times new roman",15),bg="white")
        m_frame.place(x=10,y=70,width=1340,height=80)
        #___menu buttons---
        but_course=Button(m_frame,text="course",font=("goudy old style",15,"bold"),bg="#26347a",fg="white",cursor="hand2",command=self.add_course).place(x=20,y=5,width=200,height=40)
        but_student=Button(m_frame,text="Student",font=("goudy old style",15,"bold"),bg="#26347a",fg="white",cursor="hand2",command=self.add_student).place(x=240,y=5,width=200,height=40)
        but_result=Button(m_frame,text=" Result",font=("goudy old style",15,"bold"),bg="#26347a",fg="white",cursor="hand2",command=self.add_result).place(x=460,y=5,width=200,height=40)
        but_view=Button(m_frame,text="View student result",font=("goudy old style",15,"bold"),bg="#26347a",fg="white",cursor="hand2",command=self.add_report).place(x=680,y=5,width=200,height=40)
        but_logout=Button(m_frame,text="Logout",font=("goudy old style",15,"bold"),bg="#26347a",fg="white",cursor="hand2",command=self.logout).place(x=900,y=5,width=200,height=40)
        but_exit=Button(m_frame,text="Exit",font=("goudy old style",15,"bold"),bg="#26347a",fg="white",cursor="hand2",command=self.exit_page).place(x=1120,y=5,width=200,height=40)

        #window image
        self.bg_image=Image.open("images/bg.png")
        self.bg_image=self.bg_image.resize((920,350),Image.LANCZOS)
        self.bg_image=ImageTk.PhotoImage(self.bg_image)

        self.lab_bg=Label(self.root,image=self.bg_image).place(x=400,y=180,width=920,height=350)

        # ___update___
        self.lbl_course=Label(self.root,text="Total Courses\n [ 0 ]",font=("goudy old style",18),bd=10,relief=RIDGE,bg="#e43b06",fg="white")
        self.lbl_course.place(x=400,y=530,width=300,height=80)

        self.lbl_student=Label(self.root,text="Total Students\n [ 0 ]",font=("goudy old style",18),bd=10,relief=RIDGE,bg="#0676ab",fg="white")
        self.lbl_student.place(x=710,y=530,width=300,height=80)

        self.lbl_result=Label(self.root,text="Total Result\n [ 0 ]",font=("goudy old style",18),bd=10,relief=RIDGE,bg="#038073",fg="white")
        self.lbl_result.place(x=1020,y=530,width=300,height=80)
        # clock

        self.lbl = Label(self.root,text="\n Welcome",font=("book Antiqua",30,"bold"),compound=BOTTOM, bg="#081923",fg="white")
        self.lbl.place(x=10, y=170, height=450, width=350)

        self.working()

         #footer__
        footer=Label(self.root,text=" SRMS-Student Result Management System \nContact us for any technical issue :91-8xxxxxx663",font=("goudy old style",12),bg="#21143b",fg="white").pack(side=BOTTOM,fill=X)
        self.update_detail()
#========================================================
    def update_detail(self):
        con=con=sqlite3.connect(database="python project.db")
        cur=con.cursor()
        try:
            cur.execute("select * from course")
            cr=cur.fetchall()
            self.lbl_course.config(text=f"Total Courses\n [ {len(cr)} ]")

            cur.execute("select * from student")
            cr=cur.fetchall()
            self.lbl_student.config(text=f"Total Student\n [ {len(cr)} ]")

            cur.execute("select * from result")
            cr=cur.fetchall()
            self.lbl_result.config(text=f"Total Results\n [ {len(cr)} ]")


            self.lbl_course.after(200,self.update_detail)
            
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")  

    def clock_image(self, hr, min_, sec_):
        clock = Image.new("RGB", (400, 400), (8, 25, 35))
        draw = ImageDraw.Draw(clock)

        # Background Image
        bg = Image.open("images/c.png")
        bg = bg.resize((300, 300), Image.LANCZOS)
        clock.paste(bg, (50, 50))

        origin = (200, 200)

        # Hour hand
        hour_length = 50
        hour_x = 200 + hour_length * sin(radians(hr))
        hour_y = 200 - hour_length * cos(radians(hr))
        draw.line((origin, (hour_x, hour_y)), fill="yellow", width=4)

        # Minute hand
        min_length = 80
        min_x = 200 + min_length * sin(radians(min_))
        min_y = 200 - min_length * cos(radians(min_))
        draw.line((origin, (min_x, min_y)), fill="blue", width=3)

        # Second hand
        sec_length = 100
        sec_x = 200 + sec_length * sin(radians(sec_))
        sec_y = 200 - sec_length * cos(radians(sec_))
        draw.line((origin, (sec_x, sec_y)), fill="red", width=2)

        # Center Circle
        draw.ellipse((195, 195, 210, 210), fill="#03fcfc")

        clock.save("clock_new.png")

    def working(self):
        h = datetime.now().time().hour
        m = datetime.now().time().minute
        s = datetime.now().time().second

        hr_angle = (h % 12) * 30 + (m / 60) * 30  # 360 degrees / 12 hours
        min_angle = (m / 60) * 360  # 360 degrees / 60 minutes
        sec_angle = (s / 60) * 360  # 360 degrees / 60 seconds

        self.clock_image(hr_angle, min_angle, sec_angle)

        self.image = ImageTk.PhotoImage(file="clock_new.png")
        self.lbl.config(image=self.image)

        self.root.after(1000, self.working)  # Update every second
        # function

        
    def add_course(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=courseclass(self.new_win)

    def add_student(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=studentclass(self.new_win)

    def add_result(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=resultclass(self.new_win) 

    
    def add_report(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=reportclass(self.new_win)  

    def logout(self):
        op=messagebox.askyesno("Confirm","Do You Really Want To Logout?",parent=self.root)
        if op==True:
            self.root.destroy()
            os.system("python login.py")

    def exit_page(self):
        op=messagebox.askyesno("Confirm","Do You Really Want To Exit?",parent=self.root)
        if op==True:
            self.root.destroy()
            
       
    


if __name__=="__main__":
    root=Tk()
    obj=RMS(root)
    root.mainloop()