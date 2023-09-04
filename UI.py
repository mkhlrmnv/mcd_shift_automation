from tkinter import *


class RegistrationForm:
    def __init__(self):  # makes new tkinter window
        f = open("secrets.txt", "r")
        # if file with secrets is empty creates window that asks for username and etc.
        if len(f.readlines()) == 0:
            self.base = Tk()
            self.base.geometry('500x500')
            self.base.title("Registration Form")

            self.labl_0 = Label(self.base, text="Auto Cal",
                                width=20, font=("bold", 20))  # names window
            self.labl_0.place(x=90, y=53)

            self.labl_1 = Label(self.base, text="username", width=20, font=(
                "bold", 10))  # places username text and make entry for it
            self.labl_1.place(x=80, y=130)
            self.entry_1 = Entry(self.base)
            self.entry_1.place(x=240, y=130)

            self.labl_2 = Label(self.base, text="password", width=20, font=(
                "bold", 10))  # places password text and make entry for it
            self.labl_2.place(x=68, y=180)
            self.entry_2 = Entry(self.base, show="*")
            self.entry_2.place(x=240, y=180)

            self.labl_3 = Label(self.base, text="Do you want to get", width=20, font=(
                "bold", 10))  # makes title for radio buttons
            self.labl_3.place(x=70, y=230)

            self.varblbl = StringVar()
            Radiobutton(self.base, text="previous", padx=5, variable=self.varblbl, value="<").place(
                x=235, y=230)  # three radio buttons for entering what shifts
            Radiobutton(self.base, text="ongoing", padx=5, variable=self.varblbl, value="=").place(
                x=310, y=230)  # person wants to get
            Radiobutton(self.base, text="next", padx=5,
                        variable=self.varblbl, value=">").place(x=385, y=230)

            # check box "remember me" that if selected saves credentials for next time
            self.remember_me = IntVar()
            Checkbutton(self.base, text="Remember me", width=10,
                        variable=self.remember_me, onvalue=1, offvalue=0).place(x=200, y=280)

            Button(self.base, text='Run', width=20, bg='brown', fg='white', command=self.save_close_1).place(
                x=180, y=330)  # submit button that runst save_close funktion when pressed
        else:  # if there was something in the file, creates window with only start button and checkbox "Remember me"
            self.base = Tk()
            self.base.geometry('500x500')
            self.base.title("Start Button")

            self.varblbl = StringVar()
            Radiobutton(self.base, text="previous", padx=5, variable=self.varblbl, value="<").place(
                x=180, y=180)  # three radio buttons for entering what shifts
            Radiobutton(self.base, text="ongoing", padx=5, variable=self.varblbl, value="=").place(
                x=255, y=180)  # person wants to get
            Radiobutton(self.base, text="next", padx=5,
                        variable=self.varblbl, value=">").place(x=330, y=180)

            # check box "remember me" that if selected saves credentials for next time
            self.remember_me = IntVar()
            self.remember_me.set(1)
            Checkbutton(self.base, text="Remember me", width=20,
                        variable=self.remember_me, onvalue=1, offvalue=0).place(x=180, y=230)

            Button(self.base, text='Run', width=20, bg='brown',
                   fg='white', command=self.save_close_2).place(x=180, y=280)
        f.close()

    def get_credentials(self):
        username = self.entry_1.get()
        password = self.entry_2.get()
        selection = self.varblbl.get()
        remember_value = self.remember_me.get()
        return username, password, selection, remember_value

    def print_credentials(self):
        username, password, selection, remember_me = self.get_credentials()
        print("Username:", username)
        print("Password:", password)
        print("Selection:", selection)
        print("Remember me value:", remember_me)

    def save_close_2(self):
        f = open("secrets.txt", "r")
        lines = f.readlines()
        lines[2] = str(self.varblbl.get()) + '\n'
        lines[3] = str(self.remember_me.get())
        f_out = open("secrets.txt", "w")
        f_out.writelines(lines)
        f_out.close()
        self.base.destroy()

    def save_close_1(self):
        username, password, selection, remember_me = self.get_credentials()
        f = open("secrets.txt", "w+")
        f.write(f"{username}\n")
        f.write(f"{password}\n")
        f.write(f"{selection}\n")
        f.write(f"{remember_me}")
        f.close()
        self.base.destroy()

    def run(self):  # runs loop for a window
        self.base.mainloop()


class Startbutton:
    def __init__(self):
        self.base = Tk()
        self.base.geometry('500x500')
        self.base.title("Start Button")

        self.remember_me = IntVar()
        self.remember_me.set(1)
        Checkbutton(self.base, text="Remember me", width=20,
                    variable=self.remember_me, onvalue=1, offvalue=0).place(x=180, y=230)

        Button(self.base, text='Run', width=20, bg='brown', fg='white',
               command=self.print_credentials).place(x=180, y=280)

    def run(self):  # runs loop for a window
        self.base.mainloop()

    def print_credentials(self):
        remember_value = self.remember_me.get()
        print(remember_value)

    def close(self):
        self.base.destroy()


if __name__ == "__main__":
    registration = RegistrationForm()
    registration.run()
