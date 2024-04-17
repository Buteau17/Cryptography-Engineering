
def binary_to_text(binary):
    return ''.join(chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8))

key = [0, 0, 0, 0, 0, 0, 0, 1]
plaintext = 'ATNYCUWEARESTRIVINGTOBEAGREATUNIVERSITYTHATTRANSCENDSDISCIPLINARYDIVIDESTOSOLVETHEINCREASINGLYCOMPLEXPROBLEMSTHATTHEWORLDFACESWEWILLCONTINUETOBEGUIDEDBYTHEIDEATHATWECANACHIEVESOMETHINGMUCHGREATERTOGETHERTHANWECANINDIVIDUALLYAFTERALLTHATWASTHEIDEATHATLEDTOTHECREATIONOFOURUNIVERSITYINTHEFIRSTPLACE'
c = ''
group = []
for i in range(len(plaintext)):
    ch = bin(ord(plaintext[i]))
    m = [0]
    t = ''
    for j in range(2, 9):
        m.append(int(ch[j]))
    for j in range(8):
        c = c + str(key[j] ^ m[j])
        t = t + str(key[j] ^ m[j])
    group.append(t)
    tmp = key[0]
    for j in range(7):
        key[j] = key[j+1]
    key[7] = 0
    if tmp:
        key[3] = 1 ^ key[3]
        key[4] = 1 ^ key[4]
        key[5] = 1 ^ key[5]
        key[7] = 1 ^ key[7]
print(f'Cipher text: {c}')
 
key = [0, 0, 0, 0, 0, 0, 0, 1]
text = ''
for i in group:
    t = ''
    for j in range(8):
        t = t + str(int(key[j]) ^ int(i[j]))
    tmp = key[0]
    for j in range(7):
        key[j] = key[j+1]
    key[7] = 0
    if tmp:
        key[3] = 1 ^ key[3]
        key[4] = 1 ^ key[4]
        key[5] = 1 ^ key[5]
        key[7] = 1 ^ key[7]
    t = chr(int(t, 2))
    text += t
    
print(f'\nDecrypted text: {text}')