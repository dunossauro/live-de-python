from sys import exit
from scapy.sendrecv import sniff


def xpto(s):
    return s


try:
    sniff(
        filter='udp',
        prn=xpto,
        iface='wlp2s0'
    )
except KeyboardInterrupt:
    exit(0)
