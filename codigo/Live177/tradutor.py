"""
1 - Um campo de texto Para ser traduzido
1 - Um campo de texto para o que foi traduzido
1 - Selecionar a linguagem de entrada
1 - Selecionar a linguagem de saida
1 - Botão para traduzir
"""

from tkinter import Tk, ttk, Text, Button
from googletrans import Translator
from ttkthemes import ThemedTk
from ttkbootstrap import Style

translator = Translator()

# Janela Tk default
# janela = Tk()

# Janela do ttkthemes
# janela = ThemedTk(theme='breeze')

# Janela do ttkbootstrap
style = Style(theme='darkly')
janela = style.master

janela.title('Duno Translator!')

frame_geral = ttk.Frame()


def traduzir(evento=None):
    texto = entrada.get('1.0', 'end')
    src = combo_entrada.get()
    dest = combo_saida.get()
    resultado = translator.translate(
        text=texto, src=src, dest=dest
    )

    saida.configure(state='normal')
    saida.delete('1.0', 'end')
    saida.insert('1.0', resultado.text)
    saida.configure(state='disabled')


values = ['pt', 'es', 'en']

# Entradas
frame_entrada = ttk.Frame(frame_geral)

label_entrada = ttk.Label(
    frame_entrada,
    text='Entrada',
    font=(None, 20)
)
combo_entrada = ttk.Combobox(
    frame_entrada,
    values=values,
    font=(None, 20)
)
combo_entrada.set('pt')

label_entrada.grid(row=0, column=0, padx=10, pady=10)
combo_entrada.grid(row=0, column=1, padx=10, pady=10)
frame_entrada.pack()

entrada = Text(
    frame_geral,
    height=10,
    width=50,
    font=(None, 15)
)
entrada.pack(padx=10, fill='both', expand='yes')

# Saidas
frame_saida = ttk.Frame(frame_geral)

label_saida = ttk.Label(
    frame_saida,
    text='Saida',
    font=(None, 20)
)
combo_saida = ttk.Combobox(
    frame_saida,
    values=values,
    font=(None, 20)
)
combo_saida.set('en')

label_saida.grid(row=0, column=0, padx=10, pady=10)
combo_saida.grid(row=0, column=1, padx=10, pady=10)
frame_saida.pack()

saida = Text(
    frame_geral,
    height=10,
    width=50,
    font=(None, 15),
    state='disabled'
)
saida.pack(padx=10, pady=10, fill='both', expand='yes')


botão = ttk.Button(
    frame_geral,
    text='Traduzir!',
    # font=(None, 20),
    command=traduzir
)

botão.pack(fill='both', padx=10, pady=10)

janela.bind('<Return>', traduzir)
frame_geral.pack()

janela.mainloop()
