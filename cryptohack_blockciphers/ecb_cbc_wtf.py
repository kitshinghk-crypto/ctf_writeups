#!/usr/bin/python3
def unhex(b):
	return bytes.fromhex(b)

def xor(b1,b2):
	return bytes.fromhex("".join([hex(i[0]^i[1])[2:].zfill(2) for i in zip(b1,b2)]))

c1=unhex("bda62cc8b6c2ac2ea16dbd0fb9b8681c")
c2=unhex("d18d5eebb32ab6f07402c99adde095bc")
c3=unhex("85a910b058f50aa397a9ad2d8f68a54d")
d_c1=unhex("945632b799a6e95d3681d43d08d2c6f6")
d_c2=unhex("ded455b8c2add71dc20fe23accdb0329")
d_c3=unhex("8eb928db824ee9c1435de8bbfcc1b4c1")

p2=xor(c1, d_c2)
p3=xor(d_c3, c2)

print(p2)
print(p3)
