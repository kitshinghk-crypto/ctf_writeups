#!/usr/bin/python3

ciphertext="134af6e1297bc4a96f6a87fe046684e8047084ee046d84c5282dd7ef292dc9"
ciphertext_list = []
for i in range(0,len(ciphertext),2):
    c=ciphertext[i:i+2]
    ciphertext_list.append(int(c, 16))
key=[]
key.append(ciphertext_list[0] ^ ord("H"))
key.append(ciphertext_list[1] ^ ord("T"))
key.append(ciphertext_list[2] ^ ord("B"))
key.append(ciphertext_list[3] ^ ord("{"))

for k, i in enumerate(ciphertext_list):
    c=chr(ciphertext_list[k] ^ key[k%len(key)])
    print(c,end="")
print("")
