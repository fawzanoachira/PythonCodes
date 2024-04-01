import re

with open("regex_sum_1918784.txt", "r+") as f:
    numbers = []
    for file in f:
        strings = re.findall("[0-9]+",file)
        if(len(strings)!=0):
            numbers.append(strings)

sum = 0
for i in range(len(numbers)):
    for j in range(len(numbers[i])):
        sum += int(numbers[i][j])
print(sum)