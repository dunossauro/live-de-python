from random import randint
from scapy.config import conf
from scapy.layers.inet import IP, TCP
from scapy.sendrecv import send, sr1

iface = conf.iface
sport = randint(1024, 65535)

ip = IP(src=iface.ip, dst='192.168.15.1')

syn = ip/TCP(sport=sport, dport=80, flags='S', seq=1000)
synack = sr1(syn)

ACK = TCP(
    sport=sport,
    dport=80,
    flags='A',
    seq=synack.ack+1,
    ack=synack.seq+1
)
send(ip/ACK)
