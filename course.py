from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class courseclass:
    def __init__(self,root):
        self.root=root
        self.root.title("Sudent Result Management System")
        self.root.geometry("1200x480+60+100")
        self.root.config(bg="white")
        self.root.focus_force()
        #______title-------
        titie=Label(self.root,text="Manage Course Details",font=("goudy old style",20,"bold"),bg="#033050",fg="white").place(x=10,y=15,width=1180,height=35)
        #_____lable_____
        ldl_coursename=Label(self.root,text="Coursename",font=("goudy old style",15,"bold"),bg="white",fg="black").place(x=10,y=60)
        lai_duration=Label(self.root,text="Duration",font=("goudy old style",15,"bold"),bg="white",fg="black").place(x=10,y=100)
        lbl_charges=Label(self.root,text="Charges",font=("goudy old style",15,"bold"),bg="white",fg="black").place(x=10,y=140)
        lbl_description=Label(self.root,text="Description",font=("goudy old style",15,"bold"),bg="white",fg="black").place(x=10,y=180)

        self.str_course=StringVar()
        self.str_duration=StringVar()
        self.str_charges=StringVar()
        
        #____input box____
        self.text_coursename=Entry(self.root,textvariable=self.str_course,font=("goudy old style",15,"bold"),bg="lightyellow",fg="black")
        self.text_coursename.place(x=150,y=60,width=200)

        text_duration=Entry(self.root,textvariable=self.str_duration,font=("goudy old style",15,"bold"),bg="lightyellow",fg="black").place(x=150,y=100,width=200)
        text_charges=Entry(self.root,textvariable=self.str_charges,font=("goudy old style",15,"bold"),bg="lightyellow",fg="black").place(x=150,y=140,width=200)
        self.text_description=Text(self.root,font=("goudy old style",15,"bold"),bg="lightyellow",fg="black")
        self.text_description.place(x=150,y=180,width=500,height=130)
        
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
        self.search_crs=StringVar()
        ldl_searchtitle=Label(self.root,text="Course Name",font=("goudy old style",15,"bold"),bg="white").place(x=720,y=60)
        ldl_searchname=Entry(self.root,textvariable=self.search_crs,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=870,y=60,width=180)
        
        btn_search=Button(self.root,text="Search",font=("goudy old style",15,"bold"),bg="#fc0303",fg="white",cursor="hand2",command=self.search).place(x=1070,y=60,width=120,height=28)
          
        # ___meanurame___
        self.c_frame=Frame(self.root,bd=2,relief=RIDGE)
        self.c_frame.place(x=720,y=100,width=470,height=340)

        Xscroll_bar=Scrollbar(self.c_frame,orient=HORIZONTAL)
        Yscroll_bar=Scrollbar(self.c_frame,orient=VERTICAL)

        self.c_table=ttk.Treeview(self.c_frame,columns=("cid","name","duration","charges","description"),xscrollcommand=Xscroll_bar,yscrollcommand=Yscroll_bar)
        Xscroll_bar.pack(side=BOTTOM,fill=X)
        Yscroll_bar.pack(side=RIGHT,fill=Y)
        Xscroll_bar.config(command=self.c_table.xview)
        Yscroll_bar.config(command=self.c_table.yview)
        self.c_table.heading("cid",text="Course ID")
        self.c_table.heading("name",text="Name")
        self.c_table.heading("duration",text="Duration")
        self.c_table.heading("charges",text="Charges")
        self.c_table.heading("description",text="Dscription")
        self.c_table["show"]='headings'
        self.c_table.column("cid",width=100)
        self.c_table.column("name",width=100)
        self.c_table.column("duration",width=100)
        self.c_table.column("charges",width=100)
        self.c_table.column("description",width=150)
        self.c_table.pack(fill=BOTH,expand=1)
        self.c_table.bind("<ButtonRelease-1>",self.get_data)
        self.show()
        #==================================================db
    def clear(self):
        self.show()
        self.str_course.set("")
        self.str_duration.set("")
        self.str_charges.set("")
        self.search_crs.set("")
        self.text_description.delete('1.0',END)
        self.text_coursename.config(state=NORMAL)

    def delete(self):
        con=con=sqlite3.connect(database="python project.db")
        cur=con.cursor()
        try:
            if self.str_course.get()=="":
                messagebox.showerror("Error","Please enter course name",parent=self.root)
            else:
                cur.execute("select * from course where name=?",(self.str_course.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Select course form list",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from course where name=?",(self.str_course.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Course deleted successfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}") 
            

    def get_data(self,ev):
        self.text_coursename.config(state="readonly")
        r=self.c_table.focus()
        contant=self.c_table.item(r)
        row=contant['values']
        #print(row)
        self.str_course.set(row[1])
        self.str_duration.set(row[2])
        self.str_charges.set(row[3])
        #self.str_description.set(row[4])
        self.text_description.delete('1.0',END)
        self.text_description.insert(END,row[4])

    def add(self):
        con=con=sqlite3.connect(database="python project.db")
        cur=con.cursor()
        try:
            if self.str_course.get()=="":
                messagebox.showerror("Error","Please enter course name",parent=self.root)
            else:
                cur.execute("select * from course where name=?",(self.str_course.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Course already exist",parent=self.root)
                else:
                    cur.execute("insert into course(name,duration,charges,description) values(?,?,?,?)",(
                        self.str_course.get(),
                        self.str_duration.get(),
                        self.str_charges.get(),
                        self.text_description.get('1.0',END)
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Course Added Succsfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}") 

    def update(self):
        con=con=sqlite3.connect(database="python project.db")
        cur=con.cursor()
        try:
            if self.str_course.get()=="":
                messagebox.showerror("Error","Please enter course name",parent=self.root)
            else:
                cur.execute("select * from course where name=?",(self.str_course.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Select course form list",parent=self.root)
                else:
                    cur.execute("update course set duration=?,charges=?,description=? where name=?",(
                        self.str_duration.get(),
                        self.str_charges.get(),
                        self.text_description.get('1.0',END).strip(),
                        self.str_course.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Course update Succsfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")    
           

    

    def show(self):
        con=con=sqlite3.connect(database="python project.db")
        cur=con.cursor()
        try:
            cur.execute("select * from course")
            rows=cur.fetchall()
            self.c_table.delete(*self.c_table.get_children())
            for row in rows:
                self.c_table.insert('',END,values=row)   
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")  

    def search(self):
        con=con=sqlite3.connect(database="python project.db")
        cur=con.cursor()
        try:
            cur.execute(f"select * from course where name LIKE '%{self.search_crs.get()}%'")
            rows=cur.fetchall()
            self.c_table.delete(*self.c_table.get_children())
            for row in rows:
                self.c_table.insert('',END,values=row)   
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")    

         


if __name__=="__main__":
    root=Tk()
    obj=courseclass(root)
    root.mainloop()