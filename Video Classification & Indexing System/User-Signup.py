from tkinter import *
from tkinter import messagebox
import pymysql
from os import system


class Signup:
    def __init__(self, root):
        self.root = root
        self.root.geometry("700x700")
        self.root.resizable(False, False)
        self.root.configure(background="lightgray")
        self.root.title("Signup")

        frame_signup=Frame(root,bg='#078fc9')
        frame_signup.place(x=100, y=80, width=500, height=55)
        title = Label(text="Signup", width=20, font=('Arial Rounded MT Bold', 25) ,bg='#078fc9' ,fg='white')
        title.place(x=140, y=90)


        #title = Label(root, text="*-*-* Signup *-*-* ", width=20, font=("bold", 20), bg="black", fg='grey')
        #title.place(x=90, y=53)

        frame_entry=Frame(root,bg='white')
        frame_entry.place(x=100,y=140,width=500,height=440)

        username = Label(root, text="Name:", width=20, font=('goudy old style', 15,'bold'), bg="white", fg='black')
        username.place(x=125, y=170)
        self.txt_username = Entry(root,font=('times new roman',15),bg='lightgray')
        self.txt_username.place(x=210, y=200,width=270,height=30)

        #name = Label(root, text="Name", width=20, font=("bold", 10), bg="black", fg='grey')
        #name.place(x=48, y=130)
        #self.txt_name = Entry(root)
        #self.txt_name.place(x=240, y=130)


        Gender = Label(root, text="Gender", width=20, font=('goudy old style', 15,'bold'), bg="white", fg='black')
        Gender.place(x=130, y=250)
        self.gender = StringVar()
        self.gender.set("Female")
        self.btn_male = Radiobutton(root, text="Male", padx=5, variable=self.gender, value='Male', bg="white",font=(5),
                                    fg='black').place(x=315, y=255)
        self.btn_female = Radiobutton(root, text="Female", padx=20, variable=self.gender, value='Female', bg="white",font=(5),
                                      fg='black').place(x=380, y=255)

        username = Label(root, text="User Name", width=20, font=('goudy old style', 15,'bold'), bg="white", fg='Black')
        username.place(x=145, y=290)
        self.txt_username = Entry(root,font=('times new roman',15),bg='lightgray')
        self.txt_username.place(x=210, y=320,width=270,height=30)

        password = Label(root, text="Password", width=20, font=('goudy old style', 15,'bold'), bg="white", fg='black')
        password.place(x=140, y=360)
        self.txt_password = Entry(root, show="*",font=('times new roman',15),bg='lightgray')
        self.txt_password.place(x=210, y=390,width=270,height=30)

        conpass = Label(root, text="Conform Password", width=20, font=('goudy old style', 15,'bold'), bg="white", fg='black')
        conpass.place(x=180, y=430)
        self.txt_conpass = Entry(root, show="*",font=('times new roman',15),bg='lightgray')
        self.txt_conpass.place(x=210, y=460,width=270,height=30)
        btn_submit = Button(root, text='SUBMIT', width=8, bg='#078fc9', fg='white',font=('goudy old style', 15,'bold') ,command=self.DB_Conactivity).place(
            x=210, y=510, height=35,width=270)

    def DB_Conactivity(self):
        if self.txt_name.get() == "" or self.txt_username.get() == "" or self.gender.get() == "Select" or self.txt_password.get() == "" or self.txt_conpass.get() == "":
            messagebox.showwarning("Error", "All fields are Required", parent=self.root)
        elif self.txt_password.get() != self.txt_conpass.get():
            messagebox.showwarning("Error", "Password & confirm password should be same", parent=self.root)

        else:

            try:
                connection = pymysql.connect(host="localhost", user="root", password="", database="db-connectivity")
                cursor = connection.cursor()

                cursor.execute("select * from userdb where username=%s ",
                               (self.txt_username.get()
                                ))

                results = cursor.fetchall()
                if results:
                    for i in results:
                        results == self.txt_username.get()
                        messagebox.showwarning("warning", "User name already exist", parent=self.root)


                else:
                    cursor.execute("insert into userdb(Name,Gender,UserName,Password) values(%s,%s,%s,%s)",
                                   (self.txt_name.get(),
                                    self.gender.get(),
                                    self.txt_username.get(),
                                    self.txt_password.get(),

                                    ))
                    messagebox.showinfo("Success", "Successfuly Signup", parent=self.root)
                    root.destroy()
                    system('User_Login.py')
                connection.commit()
                connection.close()


            except Exception as es:
                messagebox.showerror("Error", f"Error due to:{str(es)}", parent=self.root)



root = Tk()
obj = Signup(root)
root.mainloop()