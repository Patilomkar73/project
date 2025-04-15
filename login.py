from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk, ImageDraw
from datetime import datetime
from math import sin, cos, radians
import sqlite3
import time
import os

class Login_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Page")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#021e2f")
      #_______background
        left_lbl = Label(self.root, bg="#08A3D2")
        left_lbl.place(x=0, y=0, relheight=1, width=600)

        right_lbl = Label(self.root, bg="#031F3c")
        right_lbl.place(x=600, y=0, relheight=1, relwidth=1)
       
        #_______login frame
        login_frame=Frame(self.root,bg="white")
        login_frame.place(x=250,y=100,height=500,width=800)

        login_lbl=Label(login_frame,text="LOGIN HERE",font=("times new roman",30,"bold"),bg="white",fg="#0352fc").place(x=250,y=50)

        email=Label(login_frame,text="EMAIL ADDRESS",font=("times new roman",18,"bold"),bg="white",fg="BLACK").place(x=250,y=150)
        self.text_email=Entry(login_frame,font=("times new roman",17),bg="lightgray")
        self.text_email.place(x=250,y=180,width=350,height=35)

        password=Label(login_frame,text="PASSWORD",font=("times new roman",18,"bold"),bg="white",fg="BLACK").place(x=250,y=250)
        self.text_password=Entry(login_frame,font=("times new roman",17),bg="lightgray")
        self.text_password.place(x=250,y=280,width=350,height=35)

        but_reg=Button(login_frame,text="Register New Account",font=("times new roman",14),bd=0,bg="white",fg="#B00857",cursor="hand2",command=self.register_window).place(x=250,y=320)

        but_log=Button(login_frame,text="Login",font=("times new roman",20),bd=0,fg="white",bg="#B00857",cursor="hand2",command=self.login).place(x=250,y=380,height=40,width=150)

    

       #_______clock
        self.lbl = Label(self.root,text="\n Welcome",font=("book Antiqua",30,"bold"),compound=BOTTOM, bg="#081923",fg="white")
        self.lbl.place(x=90, y=120, height=450, width=350)

        self.working()
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
    def register_window(self):
        self.root.destroy()
        os.system("python register.py")   

    def login(self):
        if self.text_email.get()=="" or self.text_password.get()=="":
            messagebox.showerror("Error","All Fields Are Requried",parent=self.root)
        else:
            try:
                con=con=sqlite3.connect(database="python project.db")
                cur=con.cursor()
                cur.execute("Select * from employee where email=? and password=?",(self.text_email.get(),self.text_password.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Email or Password",parent=self.root)
                else:
                    messagebox.showinfo("Success",f"Welcome:{self.text_email.get()}",parent=self.root)
                    self.root.destroy()
                    os.system("python dashboard.py")
                con.close()    

            except Exception as ex:
              messagebox.showerror("Error",f"Error due to {str(ex)}")     
        



if __name__ == "__main__":
    root = Tk()
    obj = Login_window(root)
    root.mainloop()
