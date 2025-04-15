from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class studentclass:
    def __init__(self,root):
        self.root=root
        self.root.title("Sudent Detail Management System")
        self.root.geometry("1200x480+60+100")
        self.root.config(bg="white")
        self.root.focus_force()
        #______title-------
        titie=Label(self.root,text="Manage Course Details",font=("goudy old style",20,"bold"),bg="#033050",fg="white").place(x=10,y=15,width=1180,height=35)
        #_____lable_____
        #_____colum1____
        ldl_roll=Label(self.root,text="Roll No",font=("goudy old style",15,"bold"),bg="white",fg="black").place(x=10,y=60)
        lai_name=Label(self.root,text="Name",font=("goudy old style",15,"bold"),bg="white",fg="black").place(x=10,y=100)
        lbl_email=Label(self.root,text="Email",font=("goudy old style",15,"bold"),bg="white",fg="black").place(x=10,y=140)
        lbl_gender=Label(self.root,text="Gender",font=("goudy old style",15,"bold"),bg="white",fg="black").place(x=10,y=180)
        lbl_state=Label(self.root,text="State",font=("goudy old style",15,"bold"),bg="white",fg="black").place(x=10,y=220)
        lbl_city=Label(self.root,text="City",font=("goudy old style",15,"bold"),bg="white",fg="black").place(x=310,y=220)
        lbl_pin=Label(self.root,text="pin",font=("goudy old style",15,"bold"),bg="white",fg="black").place(x=500,y=220)
        lbl_address=Label(self.root,text="Address",font=("goudy old style",15,"bold"),bg="white",fg="black").place(x=10,y=260)

        self.var_rollno=StringVar()
        self.var_name=StringVar()
        self.var_email=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_contact=StringVar()
        self.var_course=StringVar()
        self.var_a_date=StringVar()
        self.var_state=StringVar()
        self.var_city=StringVar()
        self.var_pin=StringVar()
        
        #____input box____
        self.text_roll=Entry(self.root,textvariable=self.var_rollno,font=("goudy old style",15,"bold"),bg="lightyellow",fg="black")
        self.text_roll.place(x=150,y=60,width=200)
        text_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15,"bold"),bg="lightyellow",fg="black").place(x=150,y=100,width=200)
        text_email=Entry(self.root,textvariable=self.var_email,font=("goudy old style",15,"bold"),bg="lightyellow",fg="black").place(x=150,y=140,width=200)
        text_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=("Male","Female","Other"),font=("goudy old style",15,"bold"),state="readonly",justify=CENTER)
        text_gender.place(x=150,y=180,width=200)
        text_gender.set("Select")
        text_state=Entry(self.root,textvariable=self.var_state,font=("goudy old style",15,"bold"),bg="lightyellow",fg="black").place(x=150,y=220,width=150)
        text_city=Entry(self.root,textvariable=self.var_city,font=("goudy old style",15,"bold"),bg="lightyellow",fg="black").place(x=380,y=220,width=100)
        text_pin=Entry(self.root,textvariable=self.var_pin,font=("goudy old style",15,"bold"),bg="lightyellow",fg="black").place(x=560,y=220,width=120)
        

        #_____textaddress__
        self.text_address=Text(self.root,font=("goudy old style",15,"bold"),bg="lightyellow",fg="black")
        self.text_address.place(x=150,y=260,width=504,height=100)

        #____colum2___
        lbl_dob=Label(self.root,text="D.O.B",font=("goudy old style",15,"bold"),bg="white",fg="black").place(x=360,y=60)
        lbl_contact=Label(self.root,text="Contact",font=("goudy old style",15,"bold"),bg="white",fg="black").place(x=360,y=100)
        lbl_admission=Label(self.root,text="Admission",font=("goudy old style",15,"bold"),bg="white",fg="black").place(x=360,y=140)
        lbl_course=Label(self.root,text="Course",font=("goudy old style",15,"bold"),bg="white",fg="black").place(x=360,y=180)

        #_____colum2 inputbox____
        self.course_list=[]
        # function call to update list__
        self.fetch_course()
        self.dobl=Entry(self.root,textvariable=self.var_dob,font=("goudy old style",15,"bold"),bg="lightyellow",fg="black").place(x=480,y=60,width=200)
        text_contact=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15,"bold"),bg="lightyellow",fg="black").place(x=480,y=100,width=200)
        text_admission=Entry(self.root,textvariable=self.var_a_date,font=("goudy old style",15,"bold"),bg="lightyellow",fg="black").place(x=480,y=140,width=200)
        text_course=ttk.Combobox(self.root,textvariable=self.var_course,values=self.course_list,font=("goudy old style",15,"bold"),state="readonly",justify=CENTER)
        text_course.place(x=480,y=180,width=200)
        text_course.set("Select")

        
        #__button___
        self.btn_add=Button(self.root,text="Add",font=("goudy old style",15,"bold"),bg="#4287f5",fg="white",cursor="hand2",command=self.add)
        self.btn_add.place(x=150,y=400,width=110,height=40)
        self.btn_update=Button(self.root,text="Update",font=("goudy old style",15,"bold"),bg="#37ed2d",fg="white",cursor="hand2",command=self.update)
        self.btn_update.place(x=270,y=400,width=110,height=40)
        self.btn_delete=Button(self.root,text="Delete",font=("goudy old style",15,"bold"),bg="#d90921",fg="white",cursor="hand2",command=self.delete)
        self.btn_delete.place(x=390,y=400,width=110,height=40)
        self.btn_clear=Button(self.root,text="Clear",font=("goudy old style",15,"bold"),bg="#c2c4c2",fg="white",cursor="hand2",command=self.clear)
        self.btn_clear.place(x=510,y=400,width=110,height=40)
        
        #______search course____
        self.search_=StringVar()
        ldl_rollno=Label(self.root,text="Roll no:-",font=("goudy old style",15,"bold"),bg="white").place(x=720,y=60)
        ldl_rollno=Entry(self.root,textvariable=self.search_,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=870,y=60,width=180)
        
        btn_search=Button(self.root,text="Search",font=("goudy old style",15,"bold"),bg="#fc0303",fg="white",cursor="hand2",command=self.search).place(x=1070,y=60,width=120,height=28)
          
        # ___meanurame___
        self.c_frame=Frame(self.root,bd=2,relief=RIDGE)
        self.c_frame.place(x=720,y=100,width=470,height=340)

        Xscroll_bar=Scrollbar(self.c_frame,orient=HORIZONTAL)
        Yscroll_bar=Scrollbar(self.c_frame,orient=VERTICAL)

        self.c_table=ttk.Treeview(self.c_frame,columns=("roll","name","email","gender","dob","contact","admission","course","state","city","pin","address"),xscrollcommand=Xscroll_bar,yscrollcommand=Yscroll_bar)
        Xscroll_bar.pack(side=BOTTOM,fill=X)
        Yscroll_bar.pack(side=RIGHT,fill=Y)
        Xscroll_bar.config(command=self.c_table.xview)
        Yscroll_bar.config(command=self.c_table.yview)
        self.c_table.heading("roll",text="Roll no")
        self.c_table.heading("name",text="Name")
        self.c_table.heading("email",text="Email")
        self.c_table.heading("gender",text="Gender")
        self.c_table.heading("dob",text="DOB")
        self.c_table.heading("contact",text="Contact")
        self.c_table.heading("admission",text="Admission")
        self.c_table.heading("course",text="Course")
        self.c_table.heading("state",text="State")
        self.c_table.heading("city",text="City")
        self.c_table.heading("pin",text="Pin")
        self.c_table.heading("address",text="Address")
        
        self.c_table["show"]='headings'

        self.c_table.column("roll",width=100)
        self.c_table.column("name",width=100)
        self.c_table.column("email",width=100)
        self.c_table.column("gender",width=100)
        self.c_table.column("dob",width=100)
        self.c_table.column("contact",width=100)
        self.c_table.column("admission",width=100)
        self.c_table.column("course",width=100)
        self.c_table.column("state",width=100)
        self.c_table.column("city",width=100)
        self.c_table.column("pin",width=100)
        self.c_table.column("address",width=200)
        self.c_table.pack(fill=BOTH,expand=1)
        self.c_table.bind("<ButtonRelease-1>",self.get_data)
        self.show()
        #==================================================db
    def clear(self):
        self.show()
        self.var_rollno.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_dob.set("")
        self.var_contact.set("")
        self.var_a_date.set("")
        self.var_course.set("Select")
        self.var_state.set("")
        self.var_city.set("")
        self.var_pin.set("")
        self.text_address.delete('1.0',END)
        self.text_roll.config(state=NORMAL)
        self.search_.set("")

    def delete(self):
        con=con=sqlite3.connect(database="python project.db")
        cur=con.cursor()
        try:
            if self.var_rollno.get()=="":
                messagebox.showerror("Error","Please enter roll no.",parent=self.root)
            else:
                cur.execute("select * from student where roll=?",(self.var_rollno.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Select student form list",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from student where roll=?",(self.var_rollno.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","student deleted successfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}") 
            

    def get_data(self,ev):
        self.text_roll.config(state="readonly")
        r=self.c_table.focus()
        contant=self.c_table.item(r)
        row=contant['values']
        #print(row)
        self.var_rollno.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_gender.set(row[3])
        self.var_dob.set(row[4])
        self.var_contact.set(row[5])
        self.var_a_date.set(row[6])
        self.var_course.set(row[7])
        self.var_state.set(row[8])
        self.var_city.set(row[9])
        self.var_pin.set(row[10])
        self.text_address.delete('1.0',END)
        self.text_address.insert(END,row[11])

    def add(self):
        con=con=sqlite3.connect(database="python project.db")
        cur=con.cursor()
        try:
            if self.var_rollno.get()=="":
                messagebox.showerror("Error","Roll no should be required",parent=self.root)
            else:
                cur.execute("select * from student where roll=?",(self.var_rollno.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Roll no. already exist",parent=self.root)
                else:
                    cur.execute("insert into student(roll,name,email,gender,dob,contact,admission,course,state,city,pin,address) values(?,?,?,?,?,?,?,?,?,?,?,?)",(
                        self.var_rollno.get(),
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_a_date.get(),
                        self.var_course.get(),
                        self.var_state.get(),
                        self.var_city.get(),
                        self.var_pin.get(),
                        self.text_address.get('1.0',END)
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Student Added Succsfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}") 

    def update(self):
        con=con=sqlite3.connect(database="python project.db")
        cur=con.cursor()
        try:
            if self.var_rollno.get()=="":
                messagebox.showerror("Error","Please enter Roll no.",parent=self.root)
            else:
                cur.execute("select * from student where roll=?",(self.var_rollno.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Select student form list",parent=self.root)
                else:
                    cur.execute("update student set name=?,email=?,gender=?,dob=?,contact=?,admission=?,course=?,state=?,city=?,pin=?,address=? where roll=?",(
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_a_date.get(),
                        self.var_course.get(),
                        self.var_state.get(),
                        self.var_city.get(),
                        self.var_pin.get(),
                        self.text_address.get('1.0',END),
                        self.var_rollno.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Student update Succsfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")    
           

    

    def show(self):
        con=con=sqlite3.connect(database="python project.db")
        cur=con.cursor()
        try:
            cur.execute("select * from student")
            rows=cur.fetchall()
            self.c_table.delete(*self.c_table.get_children())
            for row in rows:
                self.c_table.insert('',END,values=row)   
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}") 


    def fetch_course(self):
        con=con=sqlite3.connect(database="python project.db")
        cur=con.cursor()
        try:
            cur.execute("select name from course")
            rows=cur.fetchall()
            if len(rows)>0:
              for row in rows:
                self.course_list.append(row[0] )  
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")  

    def search(self):
        con=con=sqlite3.connect(database="python project.db")
        cur=con.cursor()
        try:
            cur.execute("select * from student where roll=?",(self.search_.get(),))
            row=cur.fetchone()
            if row!=None:
               self.c_table.delete(*self.c_table.get_children())
               self.c_table.insert('',END,values=row) 
            else:
                messagebox.showerror("Error","No record found",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")    


if __name__=="__main__":
    root=Tk()
    obj=studentclass(root)
    root.mainloop()