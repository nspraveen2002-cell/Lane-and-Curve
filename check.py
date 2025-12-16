# -*- coding: utf-8 -*-
import os
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter import filedialog as fd


name="video.mp4"
pos=name.index(".")
name1=name[:pos]
ext1=name[pos:]
print(name1+"_output"+ext1)

def select_file():
    filetypes = ( ('video files', '*.mp4'),       ('All files', '*.*')    )
    filename = fd.askopenfilename(   title='Open a file',     initialdir='/',        filetypes=filetypes)
    showinfo(         title='Selected File',        message=filename  )
    return filename
