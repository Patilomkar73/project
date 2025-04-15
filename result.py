from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class resultclass:
    def __init__(self,root):
        self.root=root
        self.root.title("Sudent Result Management System")
        self.root.geometry("1200x480+60+100")
        self.root.config(bg="white")
        self.root.focus_force()
         #______title-------
        titie=Label(self.root,text="Add Student Result",font=("goudy old style",20,"bold"),bg="orange",fg="#262626").place(x=10,y=15,width=1180,height=50)
        #___variable____
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_course=StringVar()
        self.var_marks=StringVar()
        self.var_fullmarks=StringVar()
        self.roll_List=[]
        self.fetch_roll()
        #_____widgets_____
        ldl_select=Label(self.root,text="Select Student",font=("goudy old style",20,"bold"),bg="white").place(x=50,y=100)
        lai_name=Label(self.root,text="Name",font=("goudy old style",20,"bold"),bg="white").place(x=50,y=160)
        lbl_course=Label(self.root,text="Course",font=("goudy old style",20,"bold"),bg="white").place(x=50,y=220)
        lbl_marks_ob=Label(self.root,text="Marks Obtained",font=("goudy old style",20,"bold"),bg="white").place(x=50,y=280)
        lbl_full_marks=Label(self.root,text="Full Marks",font=("goudy old style",20,"bold"),bg="white").place(x=50,y=340)

        text_student=ttk.Combobox(self.root,textvariable=self.var_roll,values=self.roll_List,font=("goudy old style",15,"bold"),state="readonly",justify=CENTER)
        text_student.place(x=280,y=100,width=200)
        text_student.set("Select")
        tn_search=Button(self.root,text="Search",font=("goudy old style",15,"bold"),bg="#fc0303",fg="white",cursor="hand2",command=self.search).place(x=500,y=100,width=100,height=28)
        
        #______input box__________
        ext_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",20,"bold"),bg="lightyellow",fg="black",state="readonly").place(x=280,y=160,width=320)
        ext_course=Entry(self.root,textvariable=self.var_course,font=("goudy old style",20,"bold"),bg="lightyellow",fg="black",state="readonly").place(x=280,y=220,width=320)
        ext_marks_ob=Entry(self.root,textvariable=self.var_marks,font=("goudy old style",20,"bold"),bg="lightyellow",fg="black").place(x=280,y=280,width=320)
        ext_full_marks=Entry(self.root,textvariable=self.var_fullmarks,font=("goudy old style",20,"bold"),bg="lightyellow",fg="black").place(x=280,y=340,width=320)

        #___button___
        btn_add=Button(self.root,text="Submit",font=("times new roman",15),bg="lightgreen",activebackground="lightgreen",cursor="hand2",command=self.add).place(x=300,y=420,width=120,height=35)
        btn_clear=Button(self.root,text="Clear",font=("times new roman",15),bg="lightgray",activebackground="lightgray",cursor="hand2",command=self.clear).place(x=430,y=420,width=120,height=35)
        
        #_______image_______
        self.bg_image=Image.open("images/result.jpg")
        self.bg_image=self.bg_image.resize((500,300),Image.LANCZOS)
        self.bg_image=ImageTk.PhotoImage(self.bg_image)

        self.lab_bg=Label(self.root,image=self.bg_image).place(x=650,y=100)

        #_____function___
    def fetch_roll(self):
        con=con=sqlite3.connect(database="python project.db")
        cur=con.cursor()
        try:
            cur.execute("select roll from student")
            rows=cur.fetchall()
            if len(rows)>0:
              for row in rows:
                self.roll_List.append(row[0] )  
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")  

    def search(self):
        con=con=sqlite3.connect(database="python project.db")
        cur=con.cursor()
        try:
            cur.execute("select name,course from student where roll=?",(self.var_roll.get(),))
            row=cur.fetchone()
            if row!=None:
                self.var_name.set(row[0])
                self.var_course.set(row[1])
            else:
                messagebox.showerror("Error","No record found",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")    

    def add(self):
        con=con=sqlite3.connect(database="python project.db")
        cur=con.cursor()
        try:
            if self.var_name.get()=="":
                messagebox.showerror("Error","Please first search student recode",parent=self.root)
            else:
                cur.execute("select * from result where roll=? and course=?",(self.var_roll.get(),self.var_course.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Result already exist",parent=self.root)
                else:
                    per=(int(self.var_marks.get())*100)/(int(self.var_fullmarks.get()))
                    cur.execute("insert into result(roll,name,course,marks_ob,full_marks,per) values(?,?,?,?,?,?)",(
                        self.var_roll.get(),
                        self.var_name.get(),
                        self.var_course.get(),
                        self.var_marks.get(),
                        self.var_fullmarks.get(),
                        str(per)
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Result Added Succsfully",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")         

    
    def clear(self):
        self.var_roll.set("Select")
        self.var_name.set("")
        self.var_course.set("")
        self.var_marks.set("")
        self.var_fullmarks.set("")
        


if __name__=="__main__":
    root=Tk()
    obj=resultclass(root)
    root.mainloop()       