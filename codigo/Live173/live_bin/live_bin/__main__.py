# ---- SIMPLES
from tkinter import Tk, Label

root = Tk()
a = Label(root, text="Hello World")
a.pack()

root.mainloop()

# ---- TEMAS
# from tkinter import ttk
# from ttkthemes import ThemedTk

# window = ThemedTk(theme='yaru')

# ttk.Label(
#     window, text='Hello World'
# ).pack()

# ttk.Button(
#     window, text='Quit', command=window.destroy
# ).pack()

# window.mainloop()

# from kivy.base import EventLoop
# EventLoop.ensure_window()

# from kivy.logger import Logger, LOG_LEVELS

# Logger.setLevel(LOG_LEVELS["debug"])

# from kivy.app import App
# from kivy.uix.label import Label


# class MainApp(App):
#     def build(self):
#         return Label(text="Hello, World")


# MainApp().run()
