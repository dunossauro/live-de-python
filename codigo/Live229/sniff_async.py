from scapy.sendrecv import AsyncSniffer
from time import sleep


s = AsyncSniffer(
    filter='udp and port 68', iface='wlp2s0'
)
s.start()

s.stop()
print(s.results)
