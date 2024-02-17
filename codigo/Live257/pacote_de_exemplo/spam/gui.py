from tkinter import Tk, Label, filedialog

from PIL import Image, ImageTk

window = Tk()
window.title('Spam!')
window.geometry('500x300')


path = filedialog.askopenfilename(filetypes=[('Image File', '.jpg')])

image = Image.open(path)
image = image.resize((500, 300))
photo = ImageTk.PhotoImage(image)


label = Label(window, image=photo)
label.pack()


def app():
    window.mainloop()
