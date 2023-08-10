from tkinter import*

class RegistrationForm:
    def __init__(self):  #makes new tkinter window
        self.base = Tk()
        self.base.geometry('500x500')
        self.base.title("Registration Form")

        self.labl_0 = Label(self.base, text="Auto Cal", width=20, font=("bold", 20)) #names window
        self.labl_0.place(x=90, y=53)

        self.labl_1 = Label(self.base, text="username", width=20, font=("bold", 10))  #places username text and make entry for it
        self.labl_1.place(x=80, y=130)
        self.entry_1 = Entry(self.base)
        self.entry_1.place(x=240, y=130)

        self.labl_2 = Label(self.base, text="password", width=20, font=("bold", 10))#places password text and make entry for it
        self.labl_2.place(x=68, y=180)
        self.entry_2 = Entry(self.base, show="*")
        self.entry_2.place(x=240, y=180)

        self.labl_3 = Label(self.base, text="Do you want to get", width=20, font=("bold", 10)) # makes title for radio buttons
        self.labl_3.place(x=70, y=230)

        self.varblbl = StringVar()
        Radiobutton(self.base, text="previous", padx=5, variable=self.varblbl, value="<").place(x=235, y=230) #three radio buttons for entering what shifts 
        Radiobutton(self.base, text="ongoing", padx=5, variable=self.varblbl, value="=").place(x=310, y=230) #person wants to get
        Radiobutton(self.base, text="next", padx=5, variable=self.varblbl, value=">").place(x=385, y=230)

        Button(self.base, text='Run', width=20, bg='brown', fg='white', command=self.save_close).place(x=180, y=280) #submit button that runst save_close funktion when pressed
        
    def save_close(self):  #saves username, password and selection to secret file
        username, password, selection = self.get_credentials()
        f = open("secrets.txt", "w+")
        f.write(f"{username}\n")
        f.write(f"{password}\n")
        f.write(f"{selection}")
        self.base.destroy()
        

    def run(self): #runs loop for a window
        self.base.mainloop()


if __name__ == "__main__":
    registration = RegistrationForm()
    registration.run()