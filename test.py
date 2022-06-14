from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np


def openImage():
    filetypes = (
        ('Images', '*.png;*.jpeg;*.jpg'),
        ('?', '*.lol')
    )
    filename = filedialog.askopenfilename(filetypes=filetypes, title='Выберите изображение')

    if filename:
        image = Image.open(filename)
        customWidget(image)

def saveImage(image):
    filetypes = (
        ('PNG', '*.png;'),
        ('JPG', '*.jpg'),
        ('JPEG', '*.jpeg'),
        ('?', '*.lol')
    )
    file = filedialog.asksaveasfilename(title='Сохранить картинку', defaultextension=filetypes, filetypes=filetypes, initialfile='Out')
    if file:
        image.save(file)


def customWidget(image: Image):
    for widget in frame1.winfo_children():
        widget.destroy()
    for widget in frame2.winfo_children():
        widget.destroy()

    b1 = Button(frame1, command=lambda: imageCoding(image), text='Закодировать', width=15, font=('Arial', 24))
    b2 = Button(frame1, command=lambda: imageDecoding(image), text='Раскодировать', width=15, font=('Arial', 24))

    _image = image.resize((256, 256))
    _image = ImageTk.PhotoImage(_image)
    panel = Label(frame2, image=_image)
    panel.image = _image
    save = Button(frame2, command=lambda: saveImage(image), text='Сохранить', width=15, font=('Arial', 24))

    frame1.pack(pady=10)
    b1.pack(side=LEFT)
    b2.pack(side=RIGHT)
    frame2.pack(pady=20)
    panel.pack()
    save.pack()


def imageCoding(image: Image):
    image = np.array(image)
    newImage = np.array(image)

    for i in range(3):
        x = 0
        y = 0
        z = 0
        image = np.array(newImage)
        for _x in range(image.shape[0]):
            for _y in range(image.shape[1]):
                for _z in range(image.shape[2]):
                    if (y == image.shape[1]):
                        y = 0
                        x += 1
                        if (x == image.shape[0]):
                            x = 0
                            z += 1

                    newImage[x, y, z] = image[_x, _y, _z]

                    y += 1

    if (image.shape[2] == 4):
        mode = 'RGBA'
    else:
        mode = 'RGB'
    image = Image.fromarray(newImage, mode=mode)

    customWidget(image)

def imageDecoding(image: Image):
    image = np.array(image)
    newImage = np.array(image)

    for i in range(3):
        x = 0
        y = 0
        z = 0
        image = np.array(newImage)
        for _x in range(image.shape[0]):
            for _y in range(image.shape[1]):
                for _z in range(image.shape[2]):
                    if (y == image.shape[1]):
                        y = 0
                        x += 1
                        if (x == image.shape[0]):
                            x = 0
                            z += 1

                    newImage[_x, _y, _z] = image[x, y, z]

                    y += 1

    if (image.shape[2] == 4):
        mode = 'RGBA'
    else:
        mode = 'RGB'
    image = Image.fromarray(newImage, mode=mode)

    customWidget(image)


if __name__ == '__main__':
    root = Tk()
    root.title('Dev by Larinenok')
    root.geometry('600x600')
    root.resizable(width=False, height=False)

    frame1 = Frame(root)
    frame2 = Frame(root)

    l = Label(text='Выберите изображение:', font=('Arial', 24))
    b = Button(command=openImage, text='Выбрать',  width=15, font=('Arial', 24))

    l.pack()
    b.pack()

    root.mainloop()