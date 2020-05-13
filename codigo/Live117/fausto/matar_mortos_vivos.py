from abc import ABC, abstractmethod


class MatadorDeMortosVivos(ABC):
    def matar(self, morto_vivo):

        self.antes_da_cabeca()  # Hook
        self.arrancar_cabeca(morto_vivo)
        self.depois_da_cabeca()  # Hook

        self.antes_do_coracao()  # Hook
        self.esmagar_coracao(morto_vivo)
        self.depois_do_coracao() # Hook


    @abstractmethod
    def arrancar_cabeca(self, morto_vivo):
        ...

    @abstractmethod
    def esmagar_coracao(self, morto_vivo):
        ...

    def antes_da_cabeca(self):
        ...

    def depois_da_cabeca(self):
        ...

    def antes_do_coracao(self):
        ...

    def depois_do_coracao(self):
        ...
