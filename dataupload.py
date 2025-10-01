import os
import tkinter as tk
import time
from random import shuffle
from tkinter import messagebox
from PIL import ImageTk, Image
import tkinter as tk
import time
from random import shuffle
import PIL.Image
from tkinter import *
from tkinter import messagebox, filedialog
import cv2 as cv
import matplotlib.pyplot as plt
import cvlib as cv
import tk as tk
from PIL import Image
import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog
import cv2
import matplotlib.pyplot as plt
import cvlib as cv
import tk as tk
import tkinter as tk
from ultralytics.models.yolo import model
from ultralytics import YOLO
from cvlib.object_detection import draw_bbox
from PIL import Image, ImageTk

veheast = 0
vehwest = 0
vehnorth = 0
vehsouth = 0


class ViewData:
    def __init__(self):
        def act():
            global veheast
            global objectInfo

            x = 0
            f_types = [('Jpg Files', '*.jpg')]
            filename1 = filedialog.askopenfilename(filetypes=f_types)
            im=cv2.imread(filename1)
            model = YOLO('yolov8n.pt')

            results =model.predict(filename1)
            result = results[0]
            veheast=(len(result.boxes))
            print(veheast)

            s1="Vehicle Count is ",str(len(result.boxes))
            messagebox.showinfo("Success" ,s1)

            plt.imshow(im)
            plt.show()

        def act1():
            global vehwest
            f_types = [('Jpg Files', '*.jpg')]
            filename1 = filedialog.askopenfilename(filetypes=f_types)
            im = cv2.imread(filename1)
            model = YOLO('yolov8n.pt')

            results =model.predict(filename1)
            result = results[0]
            vehwest=(len(result.boxes))
            print(vehwest)

            s1="Vehicle Count is ",str(len(result.boxes))
            messagebox.showinfo("Success" ,s1)
            plt.imshow(im)
            plt.show()
        def act2():
            global vehnorth
            f_types = [('Jpg Files', '*.jpg')]
            filename1 = filedialog.askopenfilename(filetypes=f_types)
            im = cv2.imread(filename1)
            model = YOLO('yolov8n.pt')

            results = model.predict(filename1)
            result = results[0]
            vehnorth = (len(result.boxes))
            print(vehnorth)

            s1 = "Vehicle Count is ", str(len(result.boxes))
            messagebox.showinfo("Success", s1)
            plt.imshow(im)
            plt.show()

        def act3():
            global vehsouth
            f_types = [('Jpg Files', '*.jpg')]
            filename1 = filedialog.askopenfilename(filetypes=f_types)
            im = cv2.imread(filename1)
            model = YOLO('yolov8n.pt')

            results = model.predict(filename1)
            result = results[0]
            vehsouth = (len(result.boxes))
            print(vehsouth)
            plt.imshow(im)
            plt.show()

            s1 = "Vehicle Count is ", str(len(result.boxes))
            messagebox.showinfo("Success", s1)

            if len(result.boxes) > 0:
                print(len(result.boxes), "is a positive number.")

            root = tk.Toplevel()
            root.title("Traffic Time Saver1")
            root.geometry('900x800')
            root['background'] = 'white'
            image1 = PIL.Image.open("2.png")
            img = image1.resize((900, 800))
            test = ImageTk.PhotoImage(img)

            label1 = tk.Label(root, image=test)
            label1.image = test

            # Position image
            label1.place(x=0, y=0)

            # image1 = Image.open("3.png")
            test = ImageTk.PhotoImage(img)

            label1 = tk.Label(root, image=test)
            label1.image = test
            btn1 = tk.Button(root, text="North")
            btn1.place(relx=0.43, rely=0.30)

            btn2 = tk.Button(root, text="South")
            btn2.place(relx=0.43, rely=0.60)

            btn3 = tk.Button(root, text="East ")
            btn3.place(relx=0.57, rely=0.45)

            btn4 = tk.Button(root, text="West ")
            btn4.place(relx=0.30, rely=0.45)

            colors = ["red", "yellow", "green"]
            while True:
                shuffle(colors)
                for i in range(0, 20):
                    btn1.config(background='green')
                    btn2.config(background='red')
                    btn3.config(background='red')
                    btn4.config(background='red')
                    btn1.update()
                    print(veheast)
                    time.sleep(veheast)
                    btn1.config(background='red')

                    btn2.config(background='green')
                    btn2.update()
                    print(vehwest)
                    time.sleep(vehwest)
                    btn2.config(background='red')

                    btn3.config(background='green')
                    btn3.update()
                    print(vehnorth)
                    time.sleep(vehnorth)
                    btn3.config(background='red')

                    btn4.config(background='green')
                    btn4.update()
                    print(vehsouth)
                    time.sleep(vehsouth)
                    btn4.config(background='red')
            # exec(open("demo.py").read())

        winadmin = Tk()
        winadmin.title("Traffic Time Saver")
        winadmin.geometry('900x800')
        winadmin['background'] = 'white'
        # image1 = PIL.Image.open(file='D:\\2.jpg')
        image1 = PIL.Image.open("2.png")
        img = image1.resize((900, 800))
        test = ImageTk.PhotoImage(img)

        label1 = tk.Label(winadmin, image=test)
        label1.image = test

        # Position image
        label1.place(x=0, y=0)

        # image1 = Image.open("3.png")
        test = ImageTk.PhotoImage(img)

        label1 = tk.Label(winadmin, image=test)
        label1.image = test

        Button(winadmin, text=" Upload North Traffic Image   ", font='Verdana 10 bold', bg="#c6eb8a",
               command=act).place(
            x=240,
            y=200)

        Button(winadmin, text=" Upload South Traffic Image   ", font='Verdana 10 bold', bg="#c6eb8a",
               command=act1).place(
            x=250,
            y=400)

        Button(winadmin, text=" Upload East Traffic Image   ", font='Verdana 10 bold', bg="#c6eb8a",
               command=act2).place(
            x=480,
            y=300)

        Button(winadmin, text=" Upload West Traffic Image   ", font='Verdana 10 bold', bg="#c6eb8a",
               command=act3).place(
            x=5,
            y=300)

        winadmin.mainloop()
