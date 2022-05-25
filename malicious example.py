import os
import tkinter as tk
with open ("test.py", "w") as file:
    file.write("import os\nimport tkinter as tk\nfullscreen = tk.Tk()\nfullscreen.attributes(\"-fullscreen\", True)\nfullscreen.overrideredirect(True)\nfullscreen.mainloop()")
os.system("test.py")
fullscreen = tk.Tk()
fullscreen.attributes("-fullscreen", True)
fullscreen.overrideredirect(True)
fullscreen.mainloop()