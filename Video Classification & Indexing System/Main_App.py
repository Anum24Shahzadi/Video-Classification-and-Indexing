import os
from tkinter import *
from tkinter import messagebox, filedialog
from os import system
import cv2
import moviepy.editor
import pymysql
root=Tk()
#upload= Tk()
def spliting(filename):
    cam = cv2.VideoCapture(filename)
    videoename = os.path.basename(filename)
    try:
        # creating a folder named data
        if not os.path.exists('data/'+videoename.rsplit('.', 1)[0]):
            os.makedirs('data/'+videoename.rsplit('.', 1)[0])
        # if not created then raise error
    except OSError:
        print('Error: Creating directory ')
    #audio extraction
    video = moviepy.editor.VideoFileClip(filename)  # Entering the videofile
    audio = video.audio
    audio.write_audiofile(r"./data/"+ videoename.rsplit('.', 1)[0]+"/"+videoename.rsplit('.', 1)[0]+".mp3")
    # frame
    currentframe = 0
    while (True):
        # reading from frame
        ret, frame = cam.read()

        if ret:
            # if video is still left continue creating images
            name = './data/'+ videoename.rsplit('.', 1)[0]+"/"+videoename.rsplit('.', 1)[0] + str(currentframe) + '.jpg'
            # if video is still left continue creating

            name = './data/'+ videoename.rsplit('.', 1)[0]+"/F" + str(currentframe) + '.jpg'
            print('Creating...' + name)

            # writing the extracted images
            cv2.imwrite(name, frame)
            # increasing counter so that it will
            # show how many frames are created
            currentframe += 1
        else:
            currentframe-=1
        return currentframe
        break

        # Release all space and windows once done
    cam.release()
    cv2.destroyAllWindows()


class Main_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("500x500")
        self.root.resizable(False, False)
        self.root.configure(background="lightgrey")
        self.root.title("Main_App")
        frame_mainbar=Frame(root,bg='White')
        frame_mainbar.place(x=0, y=4, width=500, height=50)
        #btn_bar = Frame(root, width=490, highlightbackground='white', height='40').place(x='5', y='10')
        Frame.txt_name = Entry(root)
        Frame.txt_name.place(x=290, y=15)
        btn_search = Button(root, text='Search', width=10, bg='#078fc9',font=('goudy old style', 10,'bold'), fg='white', command=self.search).place(x=415, y=12)
        btn_upload = Button(root, text='Upload', width=10, bg='#078fc9',font=('goudy old style', 10,'bold'), fg='white', command=self.upload).place(x=200, y=12)
        btn_logout = Button(root, text='Logout', width=10,font=('goudy old style', 10,'bold'), bg='#078fc9', fg='white', command=self.logout).place(x=5, y=12)
        video_box = Frame(root, width=400, highlightbackground='white', height='300').place(x='50', y='100')
        btn_next = Button(root, text='>', width=4, bg='#078fc9', fg='white', command=self.next).place(x=250, y=450)
        btn_back = Button(root, text='<', width=4, bg='#078fc9', fg='white', command=self.back).place(x=210, y=450)

    # to search the user required category
    def search(self):
        messagebox.showinfo("search", "we are searching here", parent=self.root)

    def upload(self):
        filename = filedialog.askopenfilename(initialdir="/", title="select a file",
                                              filetype=(("mp4", "*.mp4"), ("All Files", "*.*")))
        if (filename != ""):
            spliting(filename)
            frameno = spliting(filename)
            no_f = str(frameno)
            videoename = os.path.basename(filename)
            try:
                connection = pymysql.connect(host="localhost", user="root", password="", database="db-connectivity")
                cursor = connection.cursor()
                cursor.execute("insert into video_db (video) values (%s)", (filename))
                connection.commit()
                connection.close()
                messagebox.showinfo("Success", "Successfuly upload", parent=self.root)
                messagebox.showinfo("Success",
                                    "Successfuly upload\n video splite into " + no_f + " frames and audio saved in /data/ " +
                                    videoename.rsplit('.', 1)[0], parent=self.root)
                # system('Main_App.py')
            except Exception as es:
                messagebox.showerror("Error", f"Error due to:{str(es)}", parent=self.root)

    def logout(self):
        root.destroy()
        system('User_Login.py')

    def next(self):
        messagebox.showinfo("next", "move to next video", parent=self.root)

    def back(self):
        messagebox.showinfo("back", "go to previous video", parent=self.root)


obj = Main_App(root)
root.mainloop()