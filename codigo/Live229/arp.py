'''
Who has 192.168.15.1
'''

from scapy.layers.l2 import Ether, ARP
from scapy.sendrecv import srp1

MAC = 'dc:8b:28:14:21:e3'
BROADCAST = 'ff:ff:ff:ff:ff:ff'

frame = Ether(src=MAC, dst=BROADCAST)
pacote = ARP(pdst='192.168.15.1')

pacote_final = frame / pacote
pacote_final.show()

resposta = srp1(pacote_final)
resposta.show()
