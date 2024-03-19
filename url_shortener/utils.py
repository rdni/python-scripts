import sqlite3
import regex
from os import getcwd
from os.path import join
import random

def safe(sql: str) -> bool:
    return sql.isalnum()

def isurl(text: str) -> bool:
    return regex.match(r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)", text)

def make_short_url(len: int) -> str:
    short_code = random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', k=len)
    
    database = sqlite3.connect(join(getcwd(), "database.db"))
    cur = database.cursor()
    cur.execute(f"SELECT * FROM urls WHERE short_url=\"{short_code}\"")
    
    result = cur.fetchone()
    
    if result is not None:
        database.close()
        return make_short_url(len)
    
    database.close()
    
    return "".join(short_code)