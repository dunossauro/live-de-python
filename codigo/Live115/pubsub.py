# http://www.code2succeed.com/pub-sub/
# https://www.oreilly.com/library/view/learning-javascript-design/9781449334840/ch09s05.html
# https://en.wikipedia.org/wiki/Publish%E2%80%93subscribe_pattern#Message_filtering
from typing import Dict, Set, List

class Publicador:
    def __init__(self, topico, pub_sub):
        self.topico = topico
        self.mensagens = []
        self.pub = pub_sub

    def publicar(self, mensagem):
        msg = {'topico': self.topico, 'mensagem': mensagem}
        self.pub.receber_mensagem(msg)

class Inscrito:
    def __init__(self, nome):
        self.nome = nome

    def atualizar(self, topico, mensagem):
        print(f"|{topico}|\t{self.nome} recebeu: '{mensagem}'")

class PubSub:
    def __init__(self):
        self.inscritos_por_topico: Dict[str, Set] = {}
        self.fila_de_mensagens: List[Dict[str, str]] = []

    def adicionar_inscrito(self, topico, inscrito):
        if topico in self.inscritos_por_topico:
            self.inscritos_por_topico[topico].add(inscrito)
        else:
            self.inscritos_por_topico[topico] = {inscrito}

    def receber_mensagem(self, mensagem: Dict[str, str]):
        """{'topico': xpto, 'mensagem': xpto}"""
        self.fila_de_mensagens.append(mensagem)

    def _enviar_mensagens_por_topico(self, topico, mensagem):
        for incrito in self.inscritos_por_topico[topico]:
            incrito.atualizar(topico, mensagem)

    def broadcast(self):
        for msg in self.fila_de_mensagens:
            self._enviar_mensagens_por_topico(msg['topico'], msg['mensagem'])

        self.fila_de_mensagens = []


eduardo = Inscrito('Eduardo')
maria = Inscrito('Maria')
jose = Inscrito('José')

bus = PubSub()

blog_1 = Publicador('Blog do zé', bus)
blog_2 = Publicador('PSF', bus)

bus.adicionar_inscrito('PSF', eduardo)
bus.adicionar_inscrito('Blog do zé', eduardo)
bus.adicionar_inscrito('PSF', maria)
bus.adicionar_inscrito('Blog do zé', jose)

blog_1.publicar('Zé foi a feira hoje')
blog_2.publicar('Zé, membro da PSF foi a feira hoje.')


bus.broadcast()
