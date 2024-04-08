import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# url =  "http://py4e-data.dr-chuck.net/comments_42.xml"
url = "http://py4e-data.dr-chuck.net/comments_1918788.xml"
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
tree = ET.fromstring(data)

counts = tree.findall('.//count')

sum = 0
for i in range(len(counts)):
    num = counts[i].text
    sum += int(num)

print(sum)