import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url1 =  "http://py4e-data.dr-chuck.net/comments_42.xml"
url2 = "http://py4e-data.dr-chuck.net/comments_1918788.xml"
uh1 = urllib.request.urlopen(url1, context=ctx)
uh2 = urllib.request.urlopen(url2, context=ctx)

data1 = uh1.read()
data2 = uh2.read()
tree1 = ET.fromstring(data1)
tree2 = ET.fromstring(data2)

counts1 = tree1.findall('.//count')
counts2 = tree2.findall('.//count')

sum1 = 0
sum2 = 0

for i in range(len(counts1)):
    num = counts1[i].text
    sum1 += int(num)

for i in range(len(counts2)):
    num = counts2[i].text
    sum2 += int(num)

print(sum1)
print(sum2)