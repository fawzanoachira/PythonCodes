def length(inp: list):
    for i in range(len(inp)):
        if(inp[i]%2==0):
            inp = inp.pop(i)
        else:
            for j in range(len(inp)):
                for k in range(len(inp)):
                    if(inp[k]==inp[j]):
                       inp = inp.pop(k)
    return len(inp)


inp = input()
inp = inp.split()
n = len(inp)
    
print(length(inp))                                            