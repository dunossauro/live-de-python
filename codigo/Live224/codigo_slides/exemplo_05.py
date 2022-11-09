"""
Exemplo 05

Primeiros exemplos do console.
"""
from time import sleep
from rich.console import Console

c = Console(record=True)

t = 'Teste'

# Saídas !
c.print(t)
c.log(t)
c.out("Locals", locals())
sleep(1)
c.log(t, log_locals=True)
c.print_json('[false, true, null, "foo"]')

# Alinhamento e estilo
c.print(t, justify='center', style='red on white')
c.print(t, justify='left', style='bold')
c.print(t, justify='right', style='u b')

# Rules
c.rule('Boas vindas :warning:')

# Inputs
c.input('Qual seu nome [b]mesmo[/]? ')

# Status
with c.status('Esperando o lado certo da lua...', spinner='moon'):
    sleep(3)

# export

c.save_html('resultado.html')
