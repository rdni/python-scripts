import tkinter as tk
import threading
import time
from interactions import *
import asyncio

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.configure(bg="light blue")
        self.title("Tkinter Interface")
        self.geometry("300x150")
        self.create_widgets()

    def create_widgets(self):
        self.main_button = tk.Button(self, text="Open Menu", command=self.open_menu, bg="light grey")
        self.main_button.pack(pady=10)

        self.close_button = tk.Button(self, text="Close Main Menu", command=self.exit, bg="light grey")
        self.close_button.pack(pady=10)

    def open_menu(self):
        self.top = tk.Toplevel(self)
        self.top.configure(bg="light blue")
        self.top.title("Menu")

        self.text = tk.Entry(self.top, width=50, bg="light grey")
        self.text.pack(padx=10, pady=10)
        
        say_hello_button = tk.Button(self.top, text="OK", command=self.hello, bg="light grey")
        say_hello_button.pack(padx=10, pady=10)

        cancel_button = tk.Button(self.top, text="Execute", command=self.close_all, bg="light grey")
        cancel_button.pack(padx=10, pady=10)



    def close_all(self):
        self.top.destroy()
        self.destroy()

    def hello(self):
        text = self.text.get()
        
        asyncio.create_task(client.test(text=text))

    def exit(self):
        self.destroy()

def run_tkinter(*args):
    print(args)
    global app
    app = MainWindow()
    app.mainloop()


class BotClient(Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @listen()
    async def on_ready(self):
        print("Ready!")

    @listen()
    async def on_message_create(self, event):
        message: Message = event.message
        if message.content == "test":
            await message.delete()
            run_tkinter(self)
    
    async def test(self, text="test"):
        await self.get_channel(920712406110441477).send(text)
        app = MainWindow()
        app.mainloop()


if __name__ == "__main__":
    global client
    client = BotClient(token="MTA1Mzc2Njc2NjUxNTQ1Mzk5NA.GtSjlZ.K0BB6XuVkMZ9VZ2-wk2-zTu8vuvPA9QBi3P0yE", intents=Intents.ALL)
    client.start()