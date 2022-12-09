import sys
from pathlib import Path
from json import load
from tkinter import Text, ttk
from googletrans import Translator
from ttkthemes import ThemedTk

# Import tradicional
# from tools import local_path

# Import hackeado
# tools = __import__('tools')
# local_path = tools.local_path

# Importlib
from importlib import import_module
tools = import_module('tools')
local_path = tools.local_path

base_path = local_path()


translator = Translator()
janela = ThemedTk(theme='arc')
janela.title('Duno Translator!')
frame_geral = ttk.Frame()


with open(base_path / Path('langs.json')) as f:
    values = load(f)


def traduzir(evento=None):  # NOQA
    texto = entrada.get('1.0', 'end')
    src = combo_entrada.get()
    dest = combo_saida.get()
    resultado = translator.translate(text=texto, src=src, dest=dest)

    saida.configure(state='normal')
    saida.delete('1.0', 'end')
    saida.insert('1.0', resultado.text)
    saida.configure(state='disabled')


# Entradas
frame_entrada = ttk.Frame(frame_geral)

label_entrada = ttk.Label(frame_entrada, text='Entrada', font=(None, 20))
combo_entrada = ttk.Combobox(frame_entrada, values=values, font=(None, 20))
combo_entrada.set('pt')

label_entrada.grid(row=0, column=0, padx=10, pady=10)
combo_entrada.grid(row=0, column=1, padx=10, pady=10)
frame_entrada.pack()

entrada = Text(frame_geral, height=10, width=50, font=(None, 15))
entrada.pack(padx=10, fill='both', expand=1)

# Saidas
frame_saida = ttk.Frame(frame_geral)

label_saida = ttk.Label(frame_saida, text='Saida', font=(None, 20))
combo_saida = ttk.Combobox(frame_saida, values=values, font=(None, 20))
combo_saida.set('en')

label_saida.grid(row=0, column=0, padx=10, pady=10)
combo_saida.grid(row=0, column=1, padx=10, pady=10)
frame_saida.pack()

saida = Text(
    frame_geral, height=10, width=50, font=(None, 15), state='disabled'
)
saida.pack(padx=10, pady=10, fill='both', expand=1)


botão = ttk.Button(frame_geral, text='Traduzir!', command=traduzir)

botão.pack(fill='both', padx=10, pady=10)

janela.bind('<Return>', traduzir)
frame_geral.pack()

janela.mainloop()
