import  sys, urllib, urllib.parse
from pymd5 import md5, padding
url = sys.argv[1]
before_token = url[:url.find("=")+1]
token = url[url.find("=")+1:url.find("&")]
msg = url[url.find("&")+1:]
msg_length = len(msg) + 8
bits = (msg_length + len(padding(msg_length *8)))*8
h = md5(state=bytes.fromhex(token), count=bits)
x = "&command=UnlockSafes"
h.update(x)
new_token = h.hexdigest()
new_url = before_token + new_token + "&" + msg + urllib.parse.quote(padding(msg_length*8)) + x
print(new_url)

