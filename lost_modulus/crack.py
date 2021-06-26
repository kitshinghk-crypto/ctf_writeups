c=0x5c61636499a82088bf4388203a93e67bf046f8c49f62857681ec9aaaa40b4772933e0abc83e938c84ff8e67e5ad85bd6eca167585b0cc03eb1333b1b1462d9d7c25f44e53bcb568f0f05219c0147f7dc3cbad45dec2f34f03bcadcbba866dd0c566035c8122d68255ada7d18954ad604965
p=c^(1/3)
p_hex=hex(p)
pt=""
for i in range(2, len(p_hex)): 
    pt=pt+chr(int(p_hex[i:i+2],16))
pt_ex = "" 
for i in range(0,len(pt),2): 
    pt_ex = pt_ex + pt[i] 
print(pt_ex)
