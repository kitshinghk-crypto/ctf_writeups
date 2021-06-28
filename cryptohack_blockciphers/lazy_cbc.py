#!/usr/bin/python3

def xor(b1,b2):
	return bytes.fromhex("".join([hex(i[0]^i[1])[2:].zfill(2) for i in zip(b1,b2)]))

p1=bytes.fromhex("41414141414141414141414141414141")
c1=bytes.fromhex("8de2ac514f19899efd87df3d89c237b8")
fake_cipher=c1*2
decrypt_fake_cipher="41414141414141414141414141414141d6c790e0e63978341dff2b2374f5af2c"
decrypt_fake_cipher=bytes.fromhex(decrypt_fake_cipher[32:])
iv=xor(xor(decrypt_fake_cipher, c1),p1)
print("Key=%s"%iv.hex())
print(bytes.fromhex("63727970746f7b35306d335f703330706c335f64306e375f3768316e6b5f49565f31355f316d70307237346e375f3f7d"))
