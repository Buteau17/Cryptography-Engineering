f16keyoutput = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0]
solution = [0, 0, 0, 0, 0, 0, 0, 0]

for i in range(255):
    flg = 1
    for j in range(8):
        c = 0
        for k in range(8):
            c += solution[k] * f16keyoutput[j+1+k]
        if(f16keyoutput[j] != c%2):
            flg = 0
            break
    if flg:
        print(solution)
        break
 
    cnt = 0
    while(solution[cnt]):
        solution[cnt] = 0
        cnt += 1
    solution[cnt] = 1