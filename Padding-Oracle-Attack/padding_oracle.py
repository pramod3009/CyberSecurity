#!/usr/bin/python3

import requests
import sys


def split_blocks(data):
    lenght = len(data)
    blocks = []
    for i in range(lenght//16):
        blocks.append(data[i*16:(i+1)*16])
    return blocks

def byte_xor(ba1, ba2):
    return bytearray([_a ^ _b for _a, _b in zip(ba1, ba2)])

def find_last_block_bytes(block, all_blocks, index,oracle_url):
    plaintext_bytes = bytearray([0 for _ in range(16)])
    flag = 0
    expected_padding = bytearray([0 for i in range(16)])
    c_prime = byte_xor(byte_xor(expected_padding, plaintext_bytes), block)
    i = 0
    for byte in range(0,256):
        c_prime[15 - i] = byte
        cipher_temp = ""
        for k  in all_blocks[:index]:
            cipher_temp+=str(k.hex())
        cipher_temp += str(c_prime.hex()) + str((all_blocks[index+1]).hex())
        r = requests.get("%s?message=%s" % (oracle_url, bytes.fromhex(cipher_temp).hex()))
        r.raise_for_status()
        obj = r.json()
        if obj['status'] == 'invalid_mac':
            plaintext_bytes[15-i] = (byte ^ (i+1) ^ block[15-i])
            flag = 1
            break
    to_set = 1
    if not flag:
        plaintext_bytes[15] = 1
    else:
        to_set = plaintext_bytes[15]
        for i in range(0,to_set):
            plaintext_bytes[15-i] = plaintext_bytes[15]
    
    for i in range(to_set,16):
        expected_padding = bytearray([0 for _ in range(16-i)] + [(i+1) for _ in range(i)])
        c_prime = byte_xor(byte_xor(expected_padding, plaintext_bytes), block)
        for byte in range(0,256):
            c_prime[15 - i] = byte
            cipher_temp = ""
            for k  in all_blocks[:index]:
                cipher_temp+=str(k.hex())
            cipher_temp += str(c_prime.hex()) + str((all_blocks[index+1]).hex())
            r = requests.get("%s?message=%s" % (oracle_url, bytes.fromhex(cipher_temp).hex()))
            r.raise_for_status()
            obj = r.json()
            if obj['status'] == 'invalid_mac':
                plaintext_bytes[15-i] = (byte ^ (i+1) ^ block[15-i])
                break
    
    return plaintext_bytes,to_set    







def find_bytes(block, all_blocks, index,oracle_url):

    plaintext_bytes = bytearray([0 for _ in range(16)])
    
    for i in range(16):
        expected_padding = bytearray([0 for _ in range(16-i)] + [(i+1) for _ in range(i)])
        c_prime = byte_xor(byte_xor(expected_padding, plaintext_bytes), block)
        for byte in range(0,256):
            c_prime[15 - i] = byte
            cipher_temp = ""
            for k  in all_blocks[:index]:
                cipher_temp+=str(k.hex())
            cipher_temp += str(c_prime.hex()) + str((all_blocks[index+1]).hex())
             
            r = requests.get("%s?message=%s" % (oracle_url, bytes.fromhex(cipher_temp).hex()))
            r.raise_for_status()
            obj = r.json()
            print(obj)
            if obj['status'] == 'invalid_mac':
                plaintext_bytes[15-i] = (byte ^ (i+1) ^ block[15-i])
                break
    
    return plaintext_bytes 
            
        
    
def find_plaintext(ciphertext,oracle_url):
    ciphertext = bytearray.fromhex(ciphertext)
    blocks = split_blocks(ciphertext)
    plaintext = bytearray()
    
    for i in range(0,len(blocks)-2):
        temp = find_bytes(blocks[i], blocks, i,oracle_url)
        plaintext =  plaintext + temp 
        print(plaintext)
    temp,to_set =  find_last_block_bytes(blocks[len(blocks)-2],blocks,len(blocks)-2,oracle_url) 
    plaintext =  plaintext + temp   
    print(plaintext[:-(to_set+32)])


if __name__ == '__main__':
    
    if len(sys.argv) < 3:
       print("usage: %s ORACLE_URL CIPHERTEXT_HEX" % (sys.argv[0]), file=sys.stderr)
       sys.exit(-1)
    oracle_url = sys.argv[1]
    ciphertext = sys.argv[2]

    
    find_plaintext(ciphertext,oracle_url)
   












