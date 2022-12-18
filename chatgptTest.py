import logging
import tkinter as tk

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Vector(x, y)

    def __mul__(self, other):
        x = self.x * other.x
        y = self.y * other.y
        return Vector(x, y)

    def __truediv__(self, other):
        x = self.x / other.x
        y = self.y / other.y
        return Vector(x, y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __call__(self, x, y):
        self.x = x
        self.y = y

class Logger:
    def __init__(self):
        logging.basicConfig(filename="vectors.log", level=logging.INFO)

    def log(self, message):
        logging.info(message)

logger = Logger()

root = tk.Tk()

def create_vector():
    x = x_entry.get()
    y = y_entry.get()
    v = Vector(x, y)
    logger.log(f"Created vector: {v}")
    result_label["text"] = f"Vector created: {v}"

def call_add_method():
    x1 = x1_entry.get()
    y1 = y1_entry.get()
    x2 = x2_entry.get()
    y2 = y2_entry.get()
    v1 = Vector(x1, y1)
    v2 = Vector(x2, y2)
    v3 = v1 + v2
    logger.log(f"{v1} + {v2} = {v3}")
    result_label["text"] = f"{v1} + {v2} = {v3}"

def call_sub_method():
    x1 = x1_entry.get()
    y1 = y1_entry.get()
    x2 = x2_entry.get()
    y2 = y2_entry.get()
    v1 = Vector(x1, y1)
    v2 = Vector(x2, y2)
    v3 = v1 - v2
    logger.log(f"{v1} - {v2} = {v3}")
    result_label["text"] = f"{v1}
