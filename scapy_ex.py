from scapy.all import sniff, TCP, IP, UDP, ICMP, DNS, DNSQR


IFACE = "lo"
BPF = "tcp"

def on_packet(pkt):
    if IP not in pkt:
        return
    src = pkt[IP].src
    dst = pkt[IP].dst
        # print(f"TCP {src}:{pkt[TCP].sport} -> {dst}:{pkt[TCP].dport}")
    if TCP in pkt:
        print(f"TCP  {src}:{pkt[TCP].sport} -> {dst}:{pkt[TCP].dport}")
    elif UDP in pkt:
        if DNS in pkt and DNSQR in pkt and pkt[DNS].qd:
            qname = pkt[DNS].qd.qname.decode(errors="ignore")
            print(f"DNS  {src}:{pkt[UDP].sport} -> {dst}:{pkt[UDP].dport}  q={qname}")
        else:
            print(f"UDP  {src}:{pkt[UDP].sport} -> {dst}:{pkt[UDP].dport}")
    elif ICMP in pkt:
        print(f"ICMP {src} -> {dst} type={pkt[ICMP].type} code={pkt[ICMP].code}")

sniff(filter=BPF, prn=on_packet, store=False, iface=IFACE)

