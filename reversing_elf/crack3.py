#!/usr/bin/python3

#The encoded password ends with "==", so (length of original password)%3=1
#len(encoded_pw) = 64, so number of round = 16
def update_str(input_str, index, char):
    str_list=list(input_str);
    str_list[index]=char
    return ''.join(str_list)

org_pw="@"*46
encoded_pw="ZjByX3kwdXJfNWVjMG5kX2xlNTVvbl91bmJhc2U2NF80bGxfN2gzXzdoMW5nNQ=="
text="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
encoded_pw_ind=[text.find(i) for i in list(encoded_pw)];

epw_len=len(encoded_pw)
round_num=epw_len/4;
i=45
j=60
#first round
for char_guess in range(32,128):
    if ((char_guess&3)*16 == encoded_pw_ind[61] and char_guess>>2 == encoded_pw_ind[60] ):
        org_pw = update_str(org_pw, i, chr(char_guess))
#other rounds
i=i-3
j=j-4
while (i>=0):
    print("i=%d, j=%d"%(i,j))
    for char_guess_0 in range(32,128):
        for char_guess_1 in range(32,128):
            for char_guess_2 in range(32,128):
                if (char_guess_0 >> 2 != encoded_pw_ind[j]):
                    continue
                if (char_guess_2 & 0x3f != encoded_pw_ind[j+3]):
                    continue
                if (((char_guess_1 >> 4) | ((char_guess_0 & 3) <<4)) != encoded_pw_ind[j+1]):
                    continue
                if (((char_guess_2>>6)|((char_guess_1 & 0x0f)*4))!=encoded_pw_ind[j+2]):
                    continue
                org_pw = update_str(org_pw, i,   chr(char_guess_0)) 
                org_pw = update_str(org_pw, i+1, chr(char_guess_1))
                org_pw = update_str(org_pw, i+2, chr(char_guess_2))
    i=i-3
    j=j-4
print(org_pw)
