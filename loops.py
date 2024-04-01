if __name__ == '__main__':
    records = list()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([score, name])
    records.sort()
    
    count = 0
    second_lowest = records[0][0]
    for i in range(1, len(records)):
        if second_lowest != records[i][0] and count < 1:
            second_lowest = records[i][0]
            count += 1
    
    size = len(records)                                           
    names = list()
    
    for i in range(size):
        for j in range(2):
            if records[i][j] == second_lowest:
                # print(records[i][j])
                names.append(records[i][1])
    
    names.sort()
    
    for name in range(len(names)):
        print(names[name])
    print(records)
