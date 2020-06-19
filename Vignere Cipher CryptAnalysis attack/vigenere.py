#!/usr/bin/python3

import sys
from collections import Counter

#taken from Wikipedia
letter_freqs = {
    'A': 0.08167,
    'B': 0.01492,
    'C': 0.02782,
    'D': 0.04253,
    'E': 0.12702,
    'F': 0.02228,
    'G': 0.02015,
    'H': 0.06094,
    'I': 0.06966,
    'J': 0.00153,
    'K': 0.00772,
    'L': 0.04025,
    'M': 0.02406,
    'N': 0.06749,
    'O': 0.07507,
    'P': 0.01929,
    'Q': 0.00095,
    'R': 0.05987,
    'S': 0.06327,
    'T': 0.09056,
    'U': 0.02758,
    'V': 0.00978,
    'W': 0.02361,
    'X': 0.00150,
    'Y': 0.01974,
    'Z': 0.00074
}

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def pop_var_english_text():
    freq = list(letter_freqs.values())
    mean = sum(freq)/26
    var = 0
    for i in freq:
        var = var + (i-mean)**2
    var=var/26
    return var

def pop_var(s):
    """Calculate the population variance of letter frequencies in given string."""
    freqs = Counter(s)
    mean = sum(float(v)/len(s) for v in freqs.values())/len(freqs)  
    return sum((float(freqs[c])/len(s)-mean)**2 for c in freqs)/len(freqs)

d = {}
def freq_var_mean_keylen(cipher,keylength):
    for i in range(0,len(cipher)):
        index = i%keylength
        a = d.get(index,[])
        a.append(cipher[i])
        d[index] = a
    mean = []
    for key in list(d.keys()):
        mean.append(pop_var("".join(d[key])))
    return sum(mean)/len(mean)


def originalText(cipher_text, key): 
    orig_text = [] 
    for i in range(len(cipher_text)): 
        x = (ord(cipher_text[i]) -
            ord(key[0]) + 26) % 26
        x += ord('A') 
        orig_text.append(chr(x)) 
    return("" . join(orig_text))

def findchar(sequence):
    alphabets = list(letter_freqs.keys())
    alphabets.sort()
    english_freq_values = []
    for i in alphabets:
        english_freq_values.append(letter_freqs[i])
    chisquare = []    
    for alphabet in alphabets:
        decrypted_seq = originalText(sequence,alphabet)
        decrypted_seq_freq = []
        for i in alphabets:
            decrypted_seq_freq.append(decrypted_seq.count(i)/len(sequence))
        chivalue = 0.0
        for i in range(0,len(english_freq_values)):
            chivalue += ((decrypted_seq_freq[i]-english_freq_values[i])**2/english_freq_values[i])
        chisquare.append(chivalue)
    return chisquare.index(min(chisquare))

        


if __name__ == "__main__":
    # Read ciphertext from stdin
    # Ignore line breaks and spaces, convert to all upper case
    #cipher = sys.stdin.read().replace("\n", "").replace(" ", "").upper() 
    cipher = sys.argv[1].replace("\n", "").replace(" ", "").upper()
    #################################################################
    # Your code to determine the key and decrypt the ciphertext here
    key_length_mean = []
    for i in range(2,14):
        key_length_mean.append(freq_var_mean_keylen(cipher,i))
    keylength = key_length_mean.index(max(key_length_mean))+2
    key1 = ""
    for i in range(0,keylength):
        sequence = []
        for j in range(0,len(cipher)):
            if j%keylength==i:
                sequence.append(cipher[j])
        key1 = key1 + chr(ord('A')+findchar(sequence))
    print(key1)    


