import dpkt
import sys
import time
def main():
	request = {}    #map of ip and number of requests sent
	response = {}   #map of ip and number of responses it got
	t1 = time.time()
	f = open(sys.argv[1],'rb')
	pcap = dpkt.pcap.Reader(f)
	
	for ts, buf in pcap:
		try :
			eth = dpkt.ethernet.Ethernet(buf)
			if eth.type != dpkt.ethernet.ETH_TYPE_IP:
				continue
			ip = eth.data
			if ip.p != dpkt.ip.IP_PROTO_TCP:
				continue
			tcp = ip.data
			if (tcp.flags & dpkt.tcp.TH_SYN) and not (tcp.flags & dpkt.tcp.TH_ACK):
				request[ip.src] = request.get(ip.src,0) + 1

			elif ((tcp.flags & dpkt.tcp.TH_SYN) and (tcp.flags & dpkt.tcp.TH_ACK)):
				response[ip.dst] = response.get(ip.dst,0) + 1
		except dpkt.dpkt.NeedData:
			continue

	
	keys = list(request.keys())	
	for key in keys:
		if request[key] > 3 * response.get(key,0):
			print(str(key[0])+"."+str(key[1])+"."+str(key[2])+"."+str(key[3]))


if __name__ == '__main__':
    
    main()
