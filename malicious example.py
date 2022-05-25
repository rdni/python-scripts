import os
import tkinter as tk
from tkinter.messagebox import showinfo
with open ("test.py", "w") as file:
    file.write("import os\nimport tkinter as tk\nfrom tkinter.messagebox import showinfo\nfullscreen = tk.Tk()\nshowinfo(message=\"I did warn you xD\")\nfullscreen.attributes(\"-fullscreen\", True)\nfullscreen.overrideredirect(True)\nfullscreen.mainloop()")
os.system("test.py")
fullscreen = tk.Tk()
showinfo(message="why?")
fullscreen.attributes("-fullscreen", True)
fullscreen.overrideredirect(True)
fullscreen.mainloop()