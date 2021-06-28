#!/usr/bin/python3
def xor(b1,b2):
	return bytes.fromhex("".join([hex(i[0]^i[1])[2:].zfill(2) for i in zip(b1,b2)]))

iv=bytes.fromhex("df9c7ca127ba361226924163da5ca413")
ct=bytes.fromhex("48ae022891990e789b9e94009c70e90d")
#org_p="admin=False;expi"
tar_p="\x00"*6+"True;"+"\x00"*5
tar_p = bytes(tar_p, "ascii")
mask="\x00"*6+"False"+"\x00"*5
mask= bytes(mask, "ascii")
input_iv=xor(xor(iv, mask), tar_p)
print("input iv = %s"%input_iv.hex())
print("input ciphertext = 48ae022891990e789b9e94009c70e90d3f798c5b02844f5fbe132bcba1c20b9c")
