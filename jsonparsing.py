import urllib.request, urllib.parse, urllib.error
import json, ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url1 =  "http://py4e-data.dr-chuck.net/comments_1918789.json"
uh1 = urllib.request.urlopen(url1, context=ctx)

data1 = uh1.read()

info = json.loads(data1)

sum = 0
for item in range(len(info['comments'])):

    num = info["comments"][item]['count']
    sum += num

print(sum)