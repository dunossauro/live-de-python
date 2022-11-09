"""Console."""
from rich.console import Console

c = Console()

# t = '[red on yellow reverse] Textão da massa! [/]'

# # c.print(t)
# # c.log(t)
# # c.out(t)

# # c.print_json('["a", [1, 2, 3, 4]]')


# c.rule('Boas vindas ao meu terminal :snake:')

# c.print(
#     'Esse é o meu textão. Ele é MERMO!',
#     justify='center',
#     style='red on white'
# )

# c.rule('Esse é meu LOG!')

# c.log(
#     'Esse é o meu textão. Ele é MERMO!',
#     justify='right',
#     style='white on red'
# )

# c.input('Qual [red on blue b]foi[/]?')

# # c.print(
# #     'Esse é o meu textão. Ele é MERMO!',
# #     justify='left',
# #     style='blink'
# # )


# from rich.prompt import Prompt

# p = Prompt()
# p.ask('Qual foi?')

# name = p.ask("Enter your name", choices=["Paul", "Jessica", "Duncan"], default="Paul")

from time import sleep

with c.status('Esperando...', spinner='moon'):
    sleep(5)

