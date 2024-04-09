import urllib.request, urllib.error, urllib.parse

f = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

print(type(f))
for line in f:
    print(line.decode())