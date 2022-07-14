#!/usr/bin/env python

# https://stackoverflow.com/questions/10133856/how-to-add-an-image-in-tkinter
# and
# https://www.codershubb.com/create-an-application-for-image-slide-show-using-python/
import sys
import glob
import hashlib
from tkinter import Tk, Button, CENTER, StringVar, Label, filedialog
from PIL import ImageTk, Image



YES_COUNTER = 0
NO_COUNTER = 0
TOTAL_IMAGES = 0


IMAGES = []
CURRENT_IMAGE_ELEMENT = None
CURRENT_IMAGE = None

root = Tk()
root.geometry("550x300+300+150")
root.resizable(width=True, height=True)

counting  = StringVar()

def namesparent(parent):
    tempnames = []
    for child in parent.winfo_children():
        tempnames.append(child.winfo_name())
    return tempnames

def removebyname(parent, name):
    for child in parent.winfo_children():
        if child.winfo_name() == name:
            child.destroy()

def get_by_name(parent, name):
    for child in parent.winfo_children():
        if child.winfo_name() == name:
            return child
    return None

def openfn():
    filename = filedialog.askopenfilename(title='open')
    return filename

def open_dir():
    global IMAGES, TOTAL_IMAGES
    dirname = filedialog.askdirectory()
    for filename in glob.glob(f"{dirname}/*.jpg"):
        img = Image.open(filename)
        IMAGES.append(img.copy())

        img.close()
    TOTAL_IMAGES = len(IMAGES)
    IMAGES = iter(IMAGES)

    next_image()


def next_image():
    global IMAGES
    global CURRENT_IMAGE_ELEMENT
    global CURRENT_IMAGE
    removebyname(root, "theimage")

    try:
        CURRENT_IMAGE = next(IMAGES)
    except:
        print("All IMAGES done time to FO")
        sys.exit()

    CURRENT_IMAGE_ELEMENT = ImageTk.PhotoImage(CURRENT_IMAGE)
    panel = Label(root, image=CURRENT_IMAGE_ELEMENT, name="theimage")
    panel.image = CURRENT_IMAGE_ELEMENT
    panel.pack()

    counting.set(f"{YES_COUNTER + NO_COUNTER + 1} of {TOTAL_IMAGES}")


def saveyes():
    global YES_COUNTER

    if CURRENT_IMAGE_ELEMENT:
        newname = hashlib.md5(CURRENT_IMAGE.tobytes()).hexdigest()
        CURRENT_IMAGE_ELEMENT._PhotoImage__photo.write(f"./results/yes/{newname}.jpg")
        YES_COUNTER += 1
        next_image()


def saveno():
    global NO_COUNTER

    if CURRENT_IMAGE_ELEMENT:
        newname = hashlib.md5(CURRENT_IMAGE.tobytes()).hexdigest()
        CURRENT_IMAGE_ELEMENT._PhotoImage__photo.write(f"./results/no/{newname}.jpg")
        NO_COUNTER += 1
        next_image()

def key(event):
    kp = repr(event.char)
    if kp == "'y'":
        saveyes()
    elif kp == "'n'":
        saveno()

root.bind("<Key>", key)
Button(root, text='open directory', command=open_dir).pack()
Button(root, text='Yes', command=saveyes).place(relx=0.6, rely=0.9, anchor=CENTER)
Button(root, text='No', command=saveno).place(relx=0.4, rely=0.9, anchor=CENTER)
Label(root, textvariable=counting ,name="countlabel").place(relx=0.5, rely=0.9, anchor=CENTER)

root.mainloop()
