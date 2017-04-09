import urllib
import xml.etree.ElementTree as ET

serviceurl = raw_input('Enter location: ')
if not serviceurl: serviceurl = 'http://python-data.dr-chuck.net/comments_283746.xml'

print 'Retrieving', serviceurl
uh = urllib.urlopen(serviceurl)
data = uh.read()
info = ET.fromstring(data)

counts = info.findall('comments/comment')
results = 0
for i in counts: 
    results+=int(i.find('count').text)
print results

#TODO
#Find sum in count elements
'''
print results
'''
