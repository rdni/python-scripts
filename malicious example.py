import os
import tkinter as tk
from tkinter.messagebox import showinfo
for i in range (0, 5, 1):
    fileName = "test" + str(i) + ".py"
    with open (fileName, "w") as file:
        file.write("import os\nimport tkinter as tk\nfrom tkinter.messagebox import showinfo\nfullscreen = tk.Tk()\nshowinfo(message=\"I did warn you xD\")\nfullscreen.attributes(\"-fullscreen\", True)\nfullscreen.overrideredirect(True)\nwhile True:\n\tfullscreen.attributes(\"-fullscreen\", True)\n\tfullscreen.overrideredirect(True)\nfullscreen.mainloop()")
    os.system(fileName)
fullscreen = tk.Tk()
showinfo(message="why?")
fullscreen.attributes("-fullscreen", True)
fullscreen.overrideredirect(True)
fullscreen.mainloop()