from scapy.layers.dns import DNS, DNSQR
from scapy.layers.inet import IP, UDP
from scapy.sendrecv import sr1


# Endereço Virtual!
pacote = IP(dst='192.168.15.1')
# Porta do serviço
pacote /= UDP(dport=53)
# Protocolo do serviço
pacote /= DNS(qd=DNSQR(qname='ddg.gg'))

resposta = sr1(pacote)
resposta.show()
