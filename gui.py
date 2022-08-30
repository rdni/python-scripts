import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import ctypes, sys


class App(tk.Tk):
    def __init__(self):
        super().__init__()


        self.loggedIn = False

        self.title("Testing App")
        self.geometry("600x600")
        
        self.label = ttk.Label(self, text="A testing app")
        self.label.pack(side=tk.TOP)

        self.protectedNames()
        self.startGUI_NL()
    
    def protectedNames(self):
        self.blacklistNames = ["admin", "user", "guest", "username"]

    def isAnAdmin(self):
        check = self.loggedInTo.lower()
        self.protectedNames()
        self.count = 0
        for i in range(0, len(self.blacklistNames), 1):
            blacklistCheck = self.blacklistNames[i]
            blacklistCheck = blacklistCheck.lower()
            if check == blacklistCheck:
                return True
            else:
                self.count = self.count + 1
        if self.count == len(self.blacklistNames):
            return False


    def button_clicked(self):
        self.text = tk.Text(self)
        self.text.pack(padx=10, pady=5)
        self.button2 = ttk.Button(self, text="Exit me!")
        self.button2["command"] = self.button2_clicked
        self.button2.pack(side=tk.BOTTOM)
        self.buttonClear = ttk.Button(self, text="Clear text")
        self.buttonClear["command"] = self.buttonClear_clicked
        self.buttonClear.pack(side=tk.BOTTOM)
        self.buttonTitle = ttk.Button(self, text="Set to title")
        self.buttonTitle["command"] = self.buttonTitle_clicked
        self.buttonTitle.pack(side=tk.BOTTOM)
        self.buttonReset = ttk.Button(self, text="Reset everything")
        self.buttonReset["command"] = self.buttonReset_clicked
        self.buttonReset.pack(side=tk.BOTTOM)
        self.buttonText.pack_forget()
        self.buttonConvert.pack_forget()
        self.loginButton.pack_forget()
        self.registerButton.pack_forget()
        self.logoutButton.pack_forget()

    def button_convert_clicked(self):
        self.registerButton.pack_forget()
        self.loginButton.pack_forget()
        self.logoutButton.pack_forget()
        self.mileEntry = ttk.Entry(self, text="Enter miles here")
        self.kiloLabel = ttk.Label(self, text="Enter miles")
        self.convertButton = ttk.Button(self, text="Convert")
        self.convertButton["command"] = self.mile_to_kilo
        self.buttonText.pack_forget()
        self.label.pack_forget()
        self.buttonConvert.pack_forget()
        self.label = ttk.Label(self, text="A testing app")
        self.label.grid(row=0, column=1)
        self.mileEntry.grid(row=1, column=0)
        self.kiloLabel.grid(row=1, column=2)
        self.convertButton.grid(row=1, column=1)
        self.buttonConvertBack = ttk.Button(text="Reset everything")
        self.buttonConvertBack["command"] = self.convertBack
        self.buttonConvertBack.grid(row=4, column=1)

    def convertBack(self):
        self.mileEntry.grid_forget()
        self.kiloLabel.grid_forget()
        self.convertButton.grid_forget()
        self.buttonConvertBack.grid_forget()
        self.label.grid_forget()

        self.startGUI()

    def button2_clicked(self):
        exit()

    def buttonClear_clicked(self):
        self.text.delete("1.0", tk.END)

    def buttonTitle_clicked(self):
        self.title(self.text.get("1.0", tk.END))
        self.text.delete("1.0", tk.END)

    def buttonReset_clicked(self):
        self.text.pack_forget()
        self.button2.pack_forget()
        self.buttonClear.pack_forget()
        self.buttonTitle.pack_forget()
        self.buttonReset.pack_forget()

        self.startGUI()
        
    def mile_to_kilo(self):
        try:
            self.mile = self.mileEntry.get()
            self.kilo = float(self.mile) * 1.6
            self.kiloLabel.configure(text=str(self.kilo) + " Kilometers")
        except ValueError:
            self.kiloLabel.configure(text="Please enter a valid number")

    def login(self):
        self.registerButton.pack_forget()
        self.loginButton.pack_forget()
        self.loginConfirm = ttk.Button(self, text="Login")
        self.loginConfirm["command"] = self.loginAttempt
        self.username = tk.Entry(self)
        self.password = tk.Entry(self)
        self.username.pack(side=tk.TOP)
        self.password.pack(side=tk.TOP)
        self.loginConfirm.pack(side=tk.TOP)
        self.username.insert(0, "Username")
        self.password.insert(0, "Password")
        self.loginB = ttk.Button(text="Back")
        self.loginB["command"] = self.loginBack
        self.loginB.pack()


    def loginAttempt(self):
        self.usernameTry = self.username.get()
        self.passwordTry = self.password.get()
        try:
            for line in open("guiData.txt","r").readlines():
                login_info = line.split()
                if len(login_info) == 0:
                    continue
                if self.usernameTry == login_info[0] and self.passwordTry == login_info[1]:
                    self.loggedIn = True
                    self.loggedInTo = self.usernameTry
            if self.loggedIn == True:
                showinfo(message="Succefully logged in.")
                self.loginConfirm.pack_forget()
                self.username.pack_forget()
                self.password.pack_forget()
                self.loginB.pack_forget()
                self.startGUI()
        except FileNotFoundError:
            showinfo(message="No data file found (looking for 'guiData.txt')")

    def loginBack(self):
        self.username.pack_forget()
        self.password.pack_forget()
        self.loginConfirm.pack_forget()
        self.loginB.pack_forget()

        self.startGUI_NL()

    def register(self):
        self.registerButton.pack_forget()
        self.loginButton.pack_forget()
        self.registerConfirm = ttk.Button(self, text="Register")
        self.registerConfirm["command"] = self.registerAttempt
        self.username = tk.Entry(self)
        self.password = tk.Entry(self)
        self.username.pack(side=tk.TOP)
        self.password.pack(side=tk.TOP)
        self.registerConfirm.pack(side=tk.TOP)
        self.username.insert(0, "Username")
        self.password.insert(0, "Password")
        self.registerB = ttk.Button(text="Back")
        self.registerB["command"] = self.registerBack
        self.registerB.pack()

    def registerBack(self):
        self.username.pack_forget()
        self.password.pack_forget()
        self.registerConfirm.pack_forget()
        self.registerB.pack_forget()

        self.startGUI_NL()
        
    def registerAttempt(self):
        self.usernameTest = 0
        self.usernameTaken = True
        registerUser = self.username.get()
        self.spaceCheck = registerUser
        registerUser = registerUser.replace(" ", "")
        registerUser = registerUser.replace(".", "")
        registerUser = registerUser.replace("\\", "")
        if self.spaceCheck != registerUser:
            showinfo("Spaces are not allowed, they have been removed.")
        registerPass = self.password.get()
        self.spaceCheck = registerPass
        registerPass = registerPass.replace(" ", "")
        registerPass = registerPass.replace(".", "")
        registerPass = registerPass.replace("\\", "")
        if self.spaceCheck != registerPass:
            showinfo("Spaces are not allowed, they have been removed.")
        self.spaceCheck = ""
        try:
            for line in open("guiData.txt","r").readlines():
                self.registerTry = line.split()
                if len(self.registerTry) == 0:
                    continue
                if registerUser == self.registerTry[0]:
                    self.usernameTest = self.usernameTest + 1
                else:
                    pass
            if self.usernameTest == 0:
                self.protectedNames()
                for i in range(0, len(self.blacklistNames), 1):
                    if registerUser.lower() == self.blacklistNames[i]:
                        self.usernameTest = True
                        i = len(self.blacklistNames) + 1
                if self.usernameTest == True:
                    showinfo(message="Username blocked")
                else:
                    file = open("guiData.txt", "a")
                    file.write(registerUser)
                    file.write(" ")
                    file.write(registerPass)
                    file.write("\n")
                    file.close()
                    showinfo(message="Username " + registerUser + " registered.")
                    self.loggedIn = True
                    self.loggedInTo = registerUser
                    self.loggedInTo = registerUser
                    self.username.pack_forget()
                    self.password.pack_forget()
                    self.registerConfirm.pack_forget()
                    self.registerB.pack_forget()
                    self.startGUI()
            else:
                showinfo(message="Username taken.")
        except FileNotFoundError:
            with open("guiData.txt", "w") as file:
                file.write("\n")
            for line in open("guiData.txt","r").readlines():
                self.registerTry = line.split()
            file = open("guiData.txt", "a")
            file.write(registerUser)
            file.write(" ")
            file.write(registerPass)
            file.write("\n")
            file.close()
            showinfo(message="Username " + registerUser + " registered.")
            self.loggedIn = True
            self.loggedInTo = registerUser
            self.username.pack_forget()
            self.password.pack_forget()
            self.registerConfirm.pack_forget()
            self.registerB.pack_forget()
            self.startGUI()
            
    def adminFullCheck(self):
        if self.isAnAdmin():
            showinfo(message="Yes they are an admin")
        else:
            showinfo(message="Nope")

    def startGUI(self):
        self.buttonText = ttk.Button(self, text="Open Text Editor")
        self.buttonText["command"] = self.button_clicked
        self.buttonText.pack(side=tk.TOP)
        self.buttonConvert = ttk.Button(self, text="Open Miles to kilometers")
        self.buttonConvert["command"] = self.button_convert_clicked
        self.buttonConvert.pack(side=tk.TOP)
        self.logoutButton = ttk.Button(self, text="Logout")
        self.logoutButton["command"] = self.logout
        self.logoutButton.pack(side=tk.TOP)

    def startGUI_NL(self):
        self.loginButton = ttk.Button(self, text="Login")
        self.loginButton["command"] = self.login
        self.loginButton.pack(side=tk.TOP)
        self.registerButton = ttk.Button(self, text="Register")
        self.registerButton["command"] = self.register
        self.registerButton.pack(side=tk.TOP)

    def logout(self):
        self.loggedIn = False
        self.buttonText.pack_forget()
        self.buttonConvert.pack_forget()
        self.logoutButton.pack_forget()
        self.loggedInTo = ""
        self.startGUI_NL()
        showinfo(message="You have been successfully logged out.")
        
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    if __name__ == "__main__":
        app = App()
        app.mainloop()
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)