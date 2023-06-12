from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage
import facerecognition as fr

import imagecapture as ic
from PIL import Image, ImageTk
import os

def b1opendb():
    from subprocess import Popen
    try:
        print("Opening The Database Please Wait..")
        p= Popen("Book1.csv", shell=True)
        print("Database Opened Succesfully..")
    except :
        print("Problem In Opening The Database !! ")

def b2facereconginiton():
    x=fr.face()
    return x

def b3databaseentry():
    # db.image()
    # exec(open('db.py').read())
    os.system('python db.py')


def imageentry():
    ic.imageupload()
   
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "build" / "assets" / "frame0"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()
window.geometry("1211x620")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=620,
    width=1211,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(605.0, 310.0, image=image_image_1)

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
def btn3():
    x=fr.face()
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda:b1opendb() ,
    relief="flat"
)
button_1.place(x=605.0, y=169.0, width=494.3037109375, height=93.54046630859375)

button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda:imageentry(),
    relief="flat"
)
button_2.place(x=606.014404296875, y=388.0, width=494.3037109375, height=93.5404052734375)

button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: b2facereconginiton(),
    relief="flat"
)
button_3.place(x=606.014404296875, y=275.0, width=494.30279541015625, height=93.54046630859375)

button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda:b3databaseentry(),
    relief="flat"
)
button_4.place(x=605.0, y=501.0, width=500.0291748046875, height=93.8927001953125)

window.resizable(True,True)
window.mainloop()
