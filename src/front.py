from tkinter import *
from tkinter import font as tkfont 
from tkinter import filedialog
from src.back import call_back
import os

class SampleApp(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, SendMessage, SendFile, SendVideo, ConfirMation):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
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
        label = Label(self, text="Bienvenido in InstaBot", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = Button(self, text="Message", command=lambda: controller.show_frame("SendMessage"))
        button2 = Button(self, text="File", command=lambda: controller.show_frame("SendFile"))
        button3 = Button(self, text="Video", command=lambda: controller.show_frame("SendVideo"))

        button1.pack()
        button2.pack()
        button3.pack()

class SendMessage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="Message", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        message = Entry(self)
        message.place(x = 10, y = 10, width=200, height=100)
        message.pack()

        def run_code():
            msg_path = message.get()
            arg = {'type': 'message','value': msg_path}
            self.controller.show_frame("ConfirMation",arg) 

        button_run = Button(self, text="Run", command= run_code)
        button_run.pack()


class SendFile(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="File", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)


        def browseFiles():
            filepath = filedialog.askopenfilename(
                initialdir = os.getcwd(),
                title = "Select a File",
                filetypes = ((("all files","*.*"),("python files","*.py"))
                ))
            arg = {'type': 'file','value': filepath}
            self.controller.show_frame("ConfirMation",arg) 

        button_run = Button(self, text="Browse", command= browseFiles)
        button_run.pack()


class SendVideo(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="Insert video id", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        message = Entry(self)
        message.place(x = 10, y = 10, width=200, height=100)
        message.pack()

        def run_code():
            videoid = message.get()
            arg = {'type': 'video','value': videoid}
            self.controller.show_frame("ConfirMation",arg) 

        button_run = Button(self, text="Run", command= run_code)
        button_run.pack()


class ConfirMation(Frame):

    def __init__(self, parent, controller, arg = None):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="Confirmation", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        def run():
            arg = self.arg
            self.controller.destroy()
            call_back(arg)

        button_run = Button(self, text="Run", command= run)
        button_run.pack()



def run_front():
    app = SampleApp()
    app.mainloop()

