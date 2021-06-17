#!/usr/bin/python3
def process_ind(i):
    if (i>3):
        p=2
        while i>p:
            if (i%p ==0):
                return 0
            p=p+1
    return 1

def process_secret(secret):
    secret_len = len(secret)
    i=0;
    while (i<secret_len):
        is_xor_i = process_ind(i)
        if (is_xor_i==0):
            secret[i]=secret[i] ^ 0x37
        else:
            secret[i]=secret[i] ^ i
        i=i+1
    return secret

secret=[0x41, 0x6c, 0x61, 0x6e, 0x20, 0x54, 0x75, 0x72, 0x69, 0x6e, 0x67, 0x20, 0x57, 0x61, 0x73, 0x20, 0x61, 0x20, 0x47, 0x65, 0x6e, 0x69,0x75, 0x73, 0x65]
print("".join([chr(i) for i in secret]))
p_secret = process_secret(secret)
print("".join([chr(i) for i in p_secret]))

