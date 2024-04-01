name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
counts = dict()

for line in handle:
    if line.startswith("From"):
        line = line.split()
        #print(words)
        line = line[1]
        counts[line]=counts.get(line,0) + 1
#print(counts)

bigcount =None
bigword =None

for l,m in counts.items():
    if bigcount == None or m > bigcount:
        bigword=l
        bigcount=m
print(bigword,bigcount)