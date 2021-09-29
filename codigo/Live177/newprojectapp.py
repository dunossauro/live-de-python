import os
import tkinter as tk
import tkinter.ttk as ttk
import pygubu

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
PROJECT_UI = os.path.join(PROJECT_PATH, "newproject")

class NewprojectApp:
    def __init__(self, master=None):
        # build ui
        self.frame_1 = ttk.Frame(master)
        self.button_1 = ttk.Button(self.frame_1)
        self.button_1.configure(text='button_1')
        self.button_1.grid(column='0', row='0')
        self.button_2 = ttk.Button(self.frame_1)
        self.button_2.configure(text='button_2')
        self.button_2.grid(column='0', row='1')
        self.label_1 = ttk.Label(self.frame_1)
        self.label_1.configure(text='Eduardo é legal')
        self.label_1.grid(column='0', row='2')
        self.combobox_1 = ttk.Combobox(self.frame_1)
        self.combobox_1.grid(column='0', row='3')
        self.entry_1 = ttk.Entry(self.frame_1)
        _text_ = '''entry_1'''
        self.entry_1.delete('0', 'end')
        self.entry_1.insert('0', _text_)
        self.entry_1.grid(column='0', row='4')
        self.label_2 = ttk.Label(self.frame_1)
        self.label_2.configure(text='label_2')
        self.label_2.grid(column='0', row='5')
        self.menubutton_1 = ttk.Menubutton(self.frame_1)
        self.menubutton_1.configure(text='menubutton_1')
        self.menubutton_1.grid(column='0', row='6')
        self.message_1 = tk.Message(self.frame_1)
        self.message_1.configure(text='message_1')
        self.message_1.grid(column='0', row='7')
        self.__tkvar = tk.StringVar(value='')
        __values = []
        self.optionmenu_1 = tk.OptionMenu(self.frame_1, self.__tkvar, None, *__values, command=None)
        self.optionmenu_1.grid(column='0', row='8')
        self.progressbar_1 = ttk.Progressbar(self.frame_1)
        self.progressbar_1.configure(orient='horizontal')
        self.progressbar_1.grid(column='0', row='9')
        self.radiobutton_1 = ttk.Radiobutton(self.frame_1)
        self.radiobutton_1.configure(text='radiobutton_1')
        self.radiobutton_1.grid(column='0', row='10')
        self.scrollbar_1 = ttk.Scrollbar(self.frame_1)
        self.scrollbar_1.configure(orient='horizontal')
        self.scrollbar_1.grid(column='0', row='11')
        self.spinbox_1 = ttk.Spinbox(self.frame_1)
        _text_ = '''spinbox_1'''
        self.spinbox_1.delete('0', 'end')
        self.spinbox_1.insert('0', _text_)
        self.spinbox_1.grid(column='0', row='12')
        self.sizegrip_1 = ttk.Sizegrip(self.frame_1)
        self.sizegrip_1.grid(column='0', row='13')
        self.sizegrip_2 = ttk.Sizegrip(self.frame_1)
        self.sizegrip_2.grid(column='0', row='14')
        self.scrollbar_2 = ttk.Scrollbar(self.frame_1)
        self.scrollbar_2.configure(orient='horizontal')
        self.scrollbar_2.grid(column='0', row='15')
        self.progressbar_2 = ttk.Progressbar(self.frame_1)
        self.progressbar_2.configure(orient='horizontal')
        self.progressbar_2.grid(column='0', row='16')
        __values = []
        self.optionmenu_2 = tk.OptionMenu(self.frame_1, self.__tkvar, None, *__values, command=None)
        self.optionmenu_2.grid(column='0', row='17')
        self.label_3 = ttk.Label(self.frame_1)
        self.label_3.configure(text='label_3')
        self.label_3.grid(column='0', row='18')
        self.checkbutton_1 = ttk.Checkbutton(self.frame_1)
        self.checkbutton_1.configure(text='checkbutton_1')
        self.checkbutton_1.grid(column='0', row='19')
        self.button_3 = ttk.Button(self.frame_1)
        self.button_3.configure(text='button_3')
        self.button_3.grid(column='0', row='20')
        self.menubutton_2 = ttk.Menubutton(self.frame_1)
        self.menu_1 = tk.Menu(self.menubutton_2)
        self.menubutton_2.configure(text='menubutton_2')
        self.menubutton_2.grid(column='0', row='21')
        self.frame_1.configure(height='200', width='200')
        self.frame_1.grid(column='0', row='0')

        # Main widget
        self.mainwindow = self.frame_1
    

    def run(self):
        self.mainwindow.mainloop()


if __name__ == '__main__':
    root = tk.Tk()
    app = NewprojectApp(root)
    app.run()

