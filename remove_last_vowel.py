arr = ["a","e","i","o","u","A","E","I","O","U"]

inp = input()
n = len(arr)
while(n>0):
    for i in range(n):
        for j in range(n):
            if inp[len(inp)-1] == arr[j]:
                inp = inp[:-1]
    n = n - 1
print(inp)