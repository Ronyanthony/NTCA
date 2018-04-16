

#fetch data from NTCA for internationals game schedule 

import urllib.request
import urllib.parse
import re
#import numpy as np 

#html = []

#x = urllib.request.urlopen('https://cricclubs.com/NTCA/teamSchedule.do?teamId=1636&clubId=343')
#print (x.read())
url = '
'
values = {
            'teamId':'1636',
            'clubId':'343'
         }

data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url, data)
resp = urllib.request.urlopen(req)
respData = resp.read()

#print (respData)

league = re.findall (r'<li>(.*?)</li>',str(respData))
#html = league


    #print(html[i])


print (league)




