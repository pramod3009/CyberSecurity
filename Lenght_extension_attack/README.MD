Lenght extension on MD5 hash. 
Input : url with commands and a token.
Output: re-generated URL with new token and an extra command added as an extension.

python3 len_ext_attack.py "https://project1.ecen4133.org/1234/lengthextension/api?token=d9eef8e8f748680bfd7567aa0e30369c&command=SprinklersPowerOn"

https://project1.ecen4133.org/1234/lengthextension/api?token=2fba66865ae4a14ea47a2ed815a23b91&command=SprinklersPowerOn%80%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%08%01%00%00%00%00%00%00&command=UnlockSafes
