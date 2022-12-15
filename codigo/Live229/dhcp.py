from scapy.config import conf
from scapy.arch.common import get_if_raw_hwaddr
from scapy.layers.inet import IP, UDP
from scapy.layers.dhcp import BOOTP, DHCP
from scapy.layers.l2 import Ether
from scapy.sendrecv import sendp, AsyncSniffer
from scapy.volatile import RandInt

meu_mac = get_if_raw_hwaddr(conf.iface)[1]


def dhcp_discover():
    pacote = Ether(src=conf.iface.mac)
    pacote /= IP(src='0.0.0.0', dst='255.255.255.255')
    pacote /= UDP(sport=68, dport=67)
    pacote /= BOOTP(chaddr=meu_mac, xid=RandInt())
    pacote /= DHCP(
        options=[
            ('message-type', 'discover'),
            'end'
        ]
    )

    sendp(pacote, iface='wlp2s0')

def dhcp_request(requested, server_ip):
    pacote = Ether(src=conf.iface.mac)
    pacote /= IP(src='0.0.0.0', dst='255.255.255.255')
    pacote /= UDP(sport=68, dport=67)
    pacote /= BOOTP(chaddr=meu_mac, xid=RandInt())
    pacote /= DHCP(
        options=[
            ('message-type', 'request'),
            ('server_id', server_ip),
            ('requested_addr', requested),
            'end'
        ]
    )

    sendp(pacote, iface='wlp2s0')


from time import sleep

s = AsyncSniffer(filter='udp and port 68')
s.start()
sleep(0.5)
dhcp_discover()
sleep(2)
s.stop()

offer = s.results[1]

ip_server = offer[1].src
ip_oferecido = offer.yiaddr


s = AsyncSniffer(filter='udp and port 68')
s.start()
sleep(0.5)
dhcp_request(ip_oferecido, ip_server)
sleep(2)
s.stop()


s.results.summary()
