from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import sqlite3
import os

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        # bg image 
        self.bg=ImageTk.PhotoImage(file="images/b2.jpg")
        bg=Label(self.root,image=self.bg).place(x=230,y=0,relwidth=1,relheight=1)

      # bg image 
        self.left=ImageTk.PhotoImage(file="images/side.png")
        left=Label(self.root,image=self.left).place(x=80,y=100,width=400,height=500)

        #frame
        frame1=Frame(self.root,bg="white")
        frame1.place(x=480,y=100,width=700,height=500)

        title=Label(frame1,text="Register Here",font=("times new roman",20,"bold"),bg="white",fg="green").place(x=50,y=30)

        f_name=Label(frame1,text="First Name",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=50,y=100)
        self.txt_fname=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_fname.place(x=50,y=130,width=250)

        l_name=Label(frame1,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=370,y=100)
        self.text_lname=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.text_lname.place(x=370,y=130,width=250)
        #______

        contact=Label(frame1,text="Contact no.",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=50,y=170)
        self.text_contact=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.text_contact.place(x=50,y=200,width=250)

        email=Label(frame1,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=370,y=170)
        self.text_email=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.text_email.place(x=370,y=200,width=250)

        #_____
        question=Label(frame1,text="Security Question",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=50,y=240)
        self.com_question=ttk.Combobox(frame1,font=("times new roman",13),state="readonly",justify=CENTER)
        self.com_question['values']=("Select","Your School Name?","Your Best Friend Name?","Your Pat name?")
        self.com_question.place(x=50,y=270,width=250)
        self.com_question.current(0)

        answer=Label(frame1,text="Answer",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=370,y=240)
        self.text_answer=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.text_answer.place(x=370,y=270,width=250)
        #______

        
        password=Label(frame1,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=50,y=310)
        self.text_password=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.text_password.place(x=50,y=340,width=250)

        cpass=Label(frame1,text="Confirm Passwoed",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=370,y=310)
        self.text_cpass=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.text_cpass.place(x=370,y=340,width=250)
        #______terms
        self.var_check=IntVar()
        check=Checkbutton(frame1,text="I Agree THe Terms & Condistion",variable=self.var_check,onvalue=1,offvalue=0,font=("times new eoman",12),bg="white").place(x=50,y=370)

        rbutton=Button(frame1,text="Registor Now",font=("times new roman",15),bd=0,bg="green",fg="white",activebackground="green",cursor="hand2",command=self.register_data).place(x=50,y=400)

        sign_in=Button(self.root,text="Sign In",font=("times new roman",15),cursor="hand2",command=self.login).place(x=200,y=460,width=150)

    def clear(self):
        self.txt_fname.delete(0,END)
        self.text_lname.delete(0,END)
        self.text_contact.delete(0,END)
        self.text_email.delete(0,END)
        self.com_question.current(0)
        self.text_answer.delete(0,END)
        self.text_password.delete(0,END)
        self.text_cpass.delete(0,END)

    def login(self):
        self.root.destroy()
        os.system("python login.py")       

    def register_data(self):
        if self.txt_fname.get()=="" or self.text_lname.get()=="" or self.text_contact.get()=="" or self.text_email.get()=="" or self.text_answer.get()=="" or self.com_question.get()=="Select" or self.text_password.get()=="" or self.text_cpass.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        elif self.text_password.get()!=self.text_cpass.get():
            messagebox.showerror("Error","Password & Confirm Password Should Be Same",parent=self.root)    
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please Confirm Our Terms & Condition",parent=self.root)  
        else:
            try:
                con=con=sqlite3.connect(database="python project.db")
                cur=con.cursor()
                cur.execute("Select * from employee where email=?",(self.text_email.get(),))
                row=cur.fetchone()
                #print(row)
                if row!=None:
                     messagebox.showerror("Error","User already exist,Please try another Email",parent=self.root) 
                else:     
                    cur.execute("insert into employee(f_name,l_name,contact,email,question,answer,password) values(?,?,?,?,?,?,?)",           
                             (self.txt_fname.get(),
                              self.text_lname.get(),
                              self.text_contact.get(),
                              self.text_email.get(),
                              self.com_question.get(),
                              self.text_answer.get(),
                              self.text_password.get()
                             ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Registor successful",parent=self.root)
                    self.clear()
                    self.login() 

            except Exception as ex:
              messagebox.showerror("Error",f"Error due to {str(ex)}") 
             
       



         

if __name__=="__main__":
    root=Tk()
    obj=Register(root)
    root.mainloop()       