from struct import pack
from tkinter import *
from tkinter import font as tkfont 
from tkinter import filedialog
from tkinter import messagebox
from src.back import call_back
import os


class SampleApp(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.geometry("500x250")
        self.title('--- JORGE ---')


        self.frames = {}
        for F in (StartPage, SendVideo, SendMessage, LoadUsernames, UserAccess, ConfirMation):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("StartPage")

    def show_frame(self, page_name, arg=None):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()
        if arg:
            frame.arg = arg


class StartPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="Hola!\n\n Que quieres enviar por Instagram ? \n\n", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        top = Frame(self)
        top.pack(side=TOP)
        button1 = Button(self, text="Message", width=10, height=2, command= lambda: controller.show_frame("SendMessage"))
        button2 = Button(self, text="Flyer", width=10, height=2, command= self.browse_files)
        button3 = Button(self, text="Video", width=10, height=2, command=lambda: controller.show_frame("SendVideo"))
        button1.pack(in_=top, side=LEFT)
        button2.pack(in_=top, side=LEFT)
        button3.pack(in_=top, side=LEFT)


    def browse_files(self):
        filepath = filedialog.askopenfilename(
            initialdir = os.getcwd(),
            title = "Select a File",
            filetypes = ((("all files","*.*"),("python files","*.py"))
            ))
        if filepath == () or filepath == '':
            messagebox.showerror("Jorge", "Mi flyer ???")
        else:
            arg = {'type': 'file','value': filepath}
            self.controller.show_frame("LoadUsernames",arg) 
    

class SendMessage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        message = Text(self)
        message.place(x = 50, y = 10, width=400, height=180)

        def run_code():
            msg_path = message.get("1.0", "end-1c")
            if msg_path == '':
                messagebox.showerror("Jorge", "Oye! Y que ? Nada ???")
            else:
                arg = {'type': 'message','value': msg_path}
                self.controller.show_frame("LoadUsernames",arg) 
        bottom = Frame(self)
        bottom.pack(side=BOTTOM, pady=12)

        button_run = Button(self, text="Send", command= run_code)
        button_run.pack(in_=bottom, side=LEFT)

        button = Button(self, text="return", command=lambda: controller.show_frame("StartPage"))
        button.pack(in_=bottom, side=LEFT)


class SendVideo(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="Cual es el id de la video ?", font=controller.title_font)
        label.pack(side="top", fill="x", pady=5)

        label = Label(self, text="La encontraras en la url de la video que esta en REEL", font=("Helvetica", 11))
        label.pack(side="top", fill="x", pady=5)

        message = Entry(self)
        message.place(x = 165, y = 100, width=175, height=20)

        def run_code():
            videoid = message.get()
            if videoid == '':
                messagebox.showerror("Jorge", "Oye, y el ID ? Nada ???")
            else:
                arg = {'type': 'video','value': videoid}
                self.controller.show_frame("LoadUsernames",arg) 

        button_run = Button(self, text="Send", command= run_code)
        button_run.pack(side="bottom", pady=50)


class LoadUsernames(Frame):

    def __init__(self, parent, controller, arg = None):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="A quien lo quieres enviar ?\n\n", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button_run = Button(self, text="Buscar", command= self.browse_files)
        button_run.pack()

    def browse_files(self):
        arg = self.arg
        filepath = filedialog.askopenfilename(
            initialdir = os.getcwd(),
            title = "Select a text file",
            filetypes = ((("python files","*.txt"), ("all files","*.*"))
            ))
        if filepath == () or filepath == '':
            messagebox.showerror("Jorge", f"Oye, y a quien envio este {arg['type']}?")
        else:
            arg['username'] = filepath
            self.controller.show_frame("UserAccess",arg) 


class UserAccess(Frame):
    def __init__(self, parent, controller, arg = None):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="Y QUIEN ERES TU ???\n\n", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        self.username =StringVar(self)
        username_entry = Entry(self, textvariable = self.username)
        username_entry.insert(END, 'Username')
        username_entry.pack()

        self.password =StringVar(self)
        password_entry = Entry(self, textvariable = self.password)
        password_entry.insert(END, 'Password')
        password_entry.pack()

        def send():
            arg = self.arg
            username = self.username.get()
            password = self.password.get()
            arg['con'] = {'username': username, 'password': password}
            self.controller.destroy()
            call_back(arg)

        button = Button(self, text="Si", command = send)
        button.pack(side='bottom', pady=10)
    


class ConfirMation(Frame):
    def __init__(self, parent, controller, arg = None):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="Has bebido sufficiente agua, hoy ?\n\n", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        top = Frame(self)
        top.pack(side=TOP)

        button = Button(self, text="Si", command= self.send)
        button.pack(in_=top, side=LEFT)
        button = Button(self, text="No", command= self.open)
        button.pack(in_=top, side=LEFT)
    
    def open(self):
        import webbrowser
        webbrowser.open("https://medvisit.io/es/importancia-beber-agua/")
        self.controller.destroy()

    def send(self):
        arg = self.arg
        self.controller.destroy()
        call_back(arg)

def run_front():
    app = SampleApp()
    app.mainloop()

