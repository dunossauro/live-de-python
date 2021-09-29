from tkinter import Tk, ttk, Button

janela = Tk()
estilo = ttk.Style()
estilo.configure(
    'TButton',
    font=('Arial', 50),
)


b1 = Button(text='Live de Python', bg='black',)
b2 = ttk.Button(text='Live de Python')

b1.pack()
b2.pack(
    padx=50, pady=50
)

# print(b1.winfo_class())
# print(b2.winfo_class())

janela.mainloop()
