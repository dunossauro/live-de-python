from scapy.layers.inet import IP, ICMP
from scapy.layers.l2 import Ether
from scapy.sendrecv import srp1

pacote = Ether()
pacote /= IP(dst='192.168.15.1')
pacote /= ICMP()
pacote.show()

resultado = srp1(pacote)

resultado.show()
