Programmatically analyze trace data to detect suspicious behavior.

Port scanning is a technique used to find network hosts that have services listening on one or more
target ports. It can be used offensively to locate vulnerable systems in preparation for an attack, or
defensively for research or network administration. In one port scan technique, known as a SYN
scan, the scanner sends TCP SYN packets (the first packet in the TCP handshake) and watches for
hosts that respond with SYN+ACK packets (the second handshake step).

Since most hosts are not prepared to receive connections on any given port, typically, during a port
scan, a much smaller number of hosts will respond with SYN+ACK packets than originally received
SYN packets. By observing this effect in a packet trace, you can identify source addresses that may
be attempting a port scan.
