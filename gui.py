import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import os.path


class App(tk.Tk):
    def __init__(self):#Runs on start
        super().__init__()

        self.loggedIn = False
        self.completeName = os.path.join("C:\\Users\\peque\\", "guiData.txt")#Path of file

        self.title("Testing App")#Setting window settings
        self.geometry("600x600")
        
        self.label = ttk.Label(self, text="A testing app")
        self.label.pack(side=tk.TOP)#Adding a label

        self.protectedNames()
        self.startGUI_NL()
    
    def protectedNames(self):#List of blacklisted names
        self.blacklistNames = ["admin", "user", "guest", "username"]#Protected names

    def isAnAdmin(self):#Check for admin permission
        check = self.loggedInTo.lower()
        self.protectedNames()
        self.count = 0

        for i in range(0, len(self.blacklistNames), 1):
            blacklistCheck = self.blacklistNames[i]
            blacklistCheck = blacklistCheck.lower()#Checking for admin permissions
            if check == blacklistCheck:
                return True
            else:
                self.count = self.count + 1
        if self.count == len(self.blacklistNames):
            return False


    def textEditButtonPressed(self):#Text editor screen
        self.buttonText.pack_forget()
        self.buttonConvert.pack_forget()
        self.loginButton.pack_forget()
        self.registerButton.pack_forget()
        self.logoutButton.pack_forget()#Removes all components from main screen

        self.textbox = tk.Text(self)
        self.textbox.pack(padx=10, pady=5)

        self.exitButton = ttk.Button(self, text="Exit me!")
        self.exitButton["command"] = self.exitButtonPressed
        self.exitButton.pack(side=tk.BOTTOM)#Exit program button

        self.buttonClear = ttk.Button(self, text="Clear text")
        self.buttonClear["command"] = self.buttonClearPressed
        self.buttonClear.pack(side=tk.BOTTOM)#Clear text button

        self.buttonTitle = ttk.Button(self, text="Set to title")
        self.buttonTitle["command"] = self.buttonTitle_clicked
        self.buttonTitle.pack(side=tk.BOTTOM)#Set window title button

        self.buttonReset = ttk.Button(self, text="Reset everything")
        self.buttonReset["command"] = self.buttonReset_clicked
        self.buttonReset.pack(side=tk.BOTTOM)#Exit text editor button

    def convertButtonPressed(self):#Miles to km screen
        self.registerButton.pack_forget()
        self.loginButton.pack_forget()
        self.logoutButton.pack_forget()
        self.buttonText.pack_forget()
        self.label.pack_forget()
        self.buttonConvert.pack_forget()#Removes all components

        self.mileEntry = ttk.Entry(self, text="Enter miles here")
        self.kiloLabel = ttk.Label(self, text="Enter miles")#Instructions
        
        self.convertButton = ttk.Button(self, text="Convert")
        self.convertButton["command"] = self.mile_to_kilo#Miles to km button

        self.label = ttk.Label(self, text="A testing app")#Top label

        self.buttonConvertBack = ttk.Button(text="Reset everything")
        self.buttonConvertBack["command"] = self.convertBack#Exit to start screen button

        self.label.grid(row=0, column=1)
        self.mileEntry.grid(row=1, column=0)
        self.kiloLabel.grid(row=1, column=2)
        self.convertButton.grid(row=1, column=1)
        self.buttonConvertBack.grid(row=4, column=1)#Packs buttons into a grid

    def convertBack(self):#Exit to main screen
        self.mileEntry.grid_forget()
        self.kiloLabel.grid_forget()
        self.convertButton.grid_forget()
        self.buttonConvertBack.grid_forget()
        self.label.grid_forget()#Removes all components

        

        self.startGUI()

    def exitButtonPressed(self):#Close program
        exit()

    def buttonClearPressed(self):#Clear text editor
        self.textbox.delete("1.0", tk.END)

    def buttonTitle_clicked(self):#Set window title to text editor's contents
        self.title(self.textbox.get("1.0", tk.END))
        self.textbox.delete("1.0", tk.END)

    def buttonReset_clicked(self):#Exit to start
        self.textbox.pack_forget()
        self.exitButton.pack_forget()
        self.buttonClear.pack_forget()
        self.buttonTitle.pack_forget()
        self.buttonReset.pack_forget()#Removes all components

        self.startGUI()
        
    def mile_to_kilo(self):#Mile to km function
        try:
            self.mile = self.mileEntry.get()
            self.kilo = float(self.mile) * 1.60934#Formula for miles to km
            self.kiloLabel.configure(text=str(self.kilo) + " Kilometers")
        except ValueError:
            self.kiloLabel.configure(text="Please enter a valid number")

    def login(self):#Login screen
        self.registerButton.pack_forget()
        self.loginButton.pack_forget()#Removes all components

        self.loginConfirm = ttk.Button(self, text="Login")
        self.loginConfirm["command"] = self.loginAttempt#Login button

        self.username = tk.Entry(self)
        self.password = tk.Entry(self)#Text fields

        self.loginB = ttk.Button(text="Back")
        self.loginB["command"] = self.loginBack#Back button

        self.username.pack(side=tk.TOP)
        self.password.pack(side=tk.TOP)
        self.loginConfirm.pack(side=tk.TOP)
        self.loginB.pack()
        
        self.username.insert(0, "Username")
        self.password.insert(0, "Password")#Adds username and password to the text fields

    def loginAttempt(self):#Login function
        self.usernameTry = self.username.get()
        self.passwordTry = self.password.get()#Get text fields
        try:
            for line in open(self.completeName, "r").readlines():#Open file guiData.txt
                login_info = line.split()
                if len(login_info) == 0:
                    continue
                if self.usernameTry == login_info[0] and self.passwordTry == login_info[1]:#Checks if username and passwords match
                    self.loggedIn = True
                    self.loggedInTo = self.usernameTry
            if self.loggedIn == True:
                showinfo(message="Succefully logged in.")

                self.loginConfirm.pack_forget()
                self.username.pack_forget()
                self.password.pack_forget()
                self.loginB.pack_forget()#Removes all components

                self.startGUI()
            else:
                showinfo(message="Incorrect username or password.")
        except FileNotFoundError:#No file found
            showinfo(message="No data file found (looking for 'guiData.txt'). File should be at '" + self.completeName + "'.")

    def loginBack(self):#Exit to non-logged in start
        self.username.pack_forget()
        self.password.pack_forget()
        self.loginConfirm.pack_forget()
        self.loginB.pack_forget()#Removes all components

        self.startGUI_NL()

    def register(self):#Register screen
        self.registerButton.pack_forget()
        self.loginButton.pack_forget()#Removes all components

        self.registerConfirm = ttk.Button(self, text="Register")
        self.registerConfirm["command"] = self.registerAttempt#Register button

        self.username = tk.Entry(self)
        self.password = tk.Entry(self)#Text fields

        self.registerB = ttk.Button(text="Back")
        self.registerB["command"] = self.registerBack#Back button
        
        self.username.pack(side=tk.TOP)
        self.password.pack(side=tk.TOP)
        self.registerConfirm.pack(side=tk.TOP)
        self.registerB.pack()

        self.username.insert(0, "Username")
        self.password.insert(0, "Password")#Adds username and password to the text fields
        

    def registerBack(self):#Exit to non-logged in start
        self.username.pack_forget()
        self.password.pack_forget()
        self.registerConfirm.pack_forget()
        self.registerB.pack_forget()#Removes all components

        self.startGUI_NL()
        
    def registerAttempt(self):#Register function
        self.usernameTest = 0

        registerUser = self.username.get()#Get username/password fields
        registerPass = self.password.get()

        registerUser = self.removeBadChar(registerUser)#Remove bad characters
        registerPass = self.removeBadChar(registerPass)

        if registerPass == "" or registerUser == "":
            return False
        
        try:
            for line in open(self.completeName,"r").readlines():#Opens guiData.txt (read only)
                self.registerTry = line.split()
                if len(self.registerTry) == 0:
                    continue#Checks if nothing is there
                if registerUser == self.registerTry[0]:
                    self.usernameTest = True#Checks username match
                else:
                    continue
            if self.usernameTest == 0:#Checks if any matching names exist
                self.protectedNames()

                for i in range(0, len(self.blacklistNames), 1):#Checks if username is blacklisted
                    if registerUser.lower() == self.blacklistNames[i]:
                        self.usernameTest = True
                if self.usernameTest == True:
                    showinfo(message="Username blocked")
                else:
                    file = open(self.completeName, "a")
                    file.write(registerUser + " " + registerPass + "\n")#Writes username and password to data file
                    print(file)
                    file.close()

                    showinfo(message="Username " + registerUser + " registered.")
                    self.loggedIn = True
                    self.loggedInTo = registerUser

                    self.username.pack_forget()
                    self.password.pack_forget()
                    self.registerConfirm.pack_forget()
                    self.registerB.pack_forget()

                    self.startGUI()
            else:
                showinfo(message="Username taken.")
        except FileNotFoundError:
            with open(self.completeName, "w") as file:#If there is no file, it will make one
                file.write(registerUser + " " + registerPass + "\n")#Writes username and password to data file
                file.close()
            showinfo(message="Username " + registerUser + " registered.")
            self.loggedIn = True
            self.loggedInTo = registerUser
            self.username.pack_forget()
            self.password.pack_forget()
            self.registerConfirm.pack_forget()
            self.registerB.pack_forget()
            self.startGUI()

    def removeBadChar(self, x):#Replace bad characters
        x = x.replace(" ", "")
        x = x.replace(".", "")
        x = x.replace("\\", "")
        return x

    def startGUI(self):#Opens logged in start
        self.buttonText = ttk.Button(self, text="Open Text Editor")#Text editor button
        self.buttonText["command"] = self.textEditButtonPressed

        self.buttonConvert = ttk.Button(self, text="Open Miles to kilometers")#Miles to km button
        self.buttonConvert["command"] = self.convertButtonPressed

        self.logoutButton = ttk.Button(self, text="Logout")#Log out button
        self.logoutButton["command"] = self.logout

        self.buttonText.pack(side=tk.TOP)
        self.buttonConvert.pack(side=tk.TOP)
        self.logoutButton.pack(side=tk.TOP)

    def startGUI_NL(self):#Opens logged out start
        self.loginButton = ttk.Button(self, text="Login")#Login button
        self.loginButton["command"] = self.login

        self.registerButton = ttk.Button(self, text="Register")#Register button
        self.registerButton["command"] = self.register

        self.registerButton.pack(side=tk.TOP)
        self.loginButton.pack(side=tk.TOP)

    def logout(self):
        self.buttonText.pack_forget()
        self.buttonConvert.pack_forget()
        self.logoutButton.pack_forget()

        self.loggedIn = False#Removes login details
        self.loggedInTo = ""

        self.startGUI_NL()#Opens logged out start

        showinfo(message="You have been successfully logged out.")

if __name__ == "__main__":
    app = App()
    app.mainloop()

def startUp():
    if __name__ == "__main__":
        app = App()
        app.mainloop()