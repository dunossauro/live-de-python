from gettext import ngettext


n_mensagens = 2

print(
    ngettext(
        'Você tem %(mensagens)d nova mensagem',
        'Você tem %(mensagens)d novas mensagens',
        n_mensagens
    ) % {'mensagens': n_mensagens}
)

"""
Russo:

Singular: Todo número terminado em 1 é singular, mas ele não pode terminar com 11
   EX: 1, 21, 41, 101, ...
   CEX: 11, 111, 1011
   Regra: v = 0 and i % 10 = 1 and i % 100 != 11

Pauca:
  Regra: v = 0 and i % 10 = 2..4 and i % 100 != 12..14

Geral:
  Regra: v = 0 and i % 10 = 0 or v = 0 and i % 10 = 5..9 or v = 0 and i % 100 = 11..14
"""
