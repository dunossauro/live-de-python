class Pizza:
    pedaços = 8

    @classmethod
    def mudar_tamanho(cls, pedaços):
        cls.pedaços = pedaços


class Mussarela(Pizza):
    ...

class Calabresa(Pizza):
    ...

class MeioAMeio(Mussarela, Calabresa):
    ...
