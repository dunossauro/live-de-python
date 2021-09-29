from tkinter import Tk, Label, Button


def fui_clicado():
    print('Fui clicado')
    botão.config(text='Fui clicado!')


janela = Tk()

texto = Label(
    text='Olar bbezes!',
    font=('Arial', 50)
)
texto.pack()

texto2 = Label(text='Live de Python')
texto2.pack()

botão = Button(
    text='Clica ni mim!',
    font=('Arial', 50),
    command=fui_clicado
)

botão.pack()


def muda_label(evento):
    print('apertei 1')
    texto.config(text='Apertei 1?')


janela.bind('1', muda_label)

janela.mainloop()
