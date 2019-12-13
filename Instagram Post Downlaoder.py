# ================MODULES==================
from tkinter import *
from tkinter.filedialog import askdirectory
import subprocess
import os
import win32clipboard
import requests
from bs4 import BeautifulSoup
# ================CONFIGURATIONS==================
root = Tk()
root.title("Insta Downloader V1.0")
root.geometry('600x250')
color = "gray88"
root.configure(bg=color)
root.resizable(width=False, height=False)
# ================VARIABLES==================
path = os.path.dirname(os.path.realpath(__file__))

# ================FUNCTIONS==================
def save_to():
    global path
    path=askdirectory()
    path = path.replace("/", "\\")
def open_current_dir():
    global path
    subprocess.Popen(f'explorer {path}')
def clear():
    link_ent.delete("0", END)
def paste():
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    link_ent.delete("0", END)
    link_ent.insert("0", data)
def download():
    link = link_ent.get()
    response = requests.get(link)
    html = response.text
    soup = BeautifulSoup(html, 'lxml')
    photo_url = soup.find("meta", property="og:image")['content']
    photo_name = photo_url[-25:-6]
    requests_url = requests.get(photo_url)
    save_path = path + "\\" + photo_name
    f = open(save_path + '.jpg', 'ab')
    f.write(requests_url.content)
    f.close()
# ================FRAMES==================
f1 = Frame(root, width=600, height=40, bg=color)
f1.pack(side=TOP)

f2 = Frame(root, width=600, height=100, bg=color)
f2.pack(side=TOP)

f3 = Frame(root, width=600, height=110, bg=color)
f3.pack(side=TOP)
# ================LABLES==================
welcome_label = Label(f1, bg=color, text="Instagram Downloader By: Reza Sarvani", font=("arial", 20, "bold"))
welcome_label.pack(side=TOP)

link_label = Label(f2, bg=color, text="Post Link:", font=("arial", 14, "bold") )
link_label.place(x=30,y=30)

# ================ENTRY==================
link_ent = Entry(f2, bd=10, width=35, bg="gray88")
link_ent.place(x=170,y=26)

# ================BUTTONS==================
download_btn = Button(f2, text="Download", font=("arial", 14, "bold"), bg=color, command=download)
download_btn.place(x=440, y=26)

paste_btn = Button(f2, text="Paste", font=("arial", 11, "bold"), bg=color, command=paste)
paste_btn.place(x=440, y=65)

clear_btn = Button(f2, text="Clear", font=("arial", 11, "bold"), bg=color, command=clear)
clear_btn.place(x=499, y=65)

save_to_btn = Button(f3, text="Save To...", font=("arial", 18, "bold"), bg=color, command=save_to)
save_to_btn.place(x=50, y=30)

open_current_dir_btn = Button(f3, text="Open Download Directory", font=("arial", 18, "bold"), bg=color, command=open_current_dir)
open_current_dir_btn.place(x=210, y=30)


root.mainloop()