#!/usr/bin/python3
import json
import string
import http.client

print_string = string.printable
host="aes.cryptohack.org"
request_url = "/ecb_oracle/encrypt/"
connection = http.client.HTTPSConnection(host)

def getCipherText(plaintext):
	url = request_url + plaintext + "/"
	connection.request('GET',url)
	response = connection.getresponse()
	result = response.read().decode()
	result = json.loads(result)["ciphertext"]
	return result

cts =[]
for i in range(1,16):
	pt= hex(ord("a"))[2:]*i
	ct = getCipherText(pt)
	ct = ct[:32]
	cts.append(ct)

pt= hex(ord("a"))[2:]*16
ct = getCipherText(pt)
ct = ct[32:64]
cts.append(ct)

flag=""
for i in range(15,-1,-1):
	for byte in print_string:
		pt = hex(ord("a"))[2:]*i + flag + hex(ord(byte))[2:].zfill(2)
		ct = getCipherText(pt)
		ct = ct[:32]
		if ct in cts:
			flag = flag + hex(ord(byte))[2:].zfill(2)
			print(bytes.fromhex(flag))
			break

cts =[]
for i in range(1,16):
	pt= hex(ord("a"))[2:]*i
	ct = getCipherText(pt)
	ct = ct[32:64]
	cts.append(ct)

flag2=""
for i in range(15,-1,-1):
	for byte in print_string:
		pt = hex(ord("a"))[2:]*i + flag + flag2 + hex(ord(byte))[2:].zfill(2)
		ct = getCipherText(pt)
		ct = ct[32:64]
		if ct in cts:
			flag2 = flag2 + hex(ord(byte))[2:].zfill(2)
			print(bytes.fromhex(flag2))
			break

print(bytes.fromhex(flag+flag2))
