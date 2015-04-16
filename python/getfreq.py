from BeautifulSoup import BeautifulSoup
import urllib2
from collections import Counter
import json

def paginate(page):
  urljson ="http://127.0.0.1:8000/articles/?user_id=339&page="+str(page)
  #urljson ="http://readbug.develapps.es/articles/?user_id=339&page="+str(page)
  
  print urljson
  headersk={"Authorization" : " Bearer 5432423","Content-Type": "application/json"}
  request = urllib2.Request(urljson, headers=headersk)
  contents = urllib2.urlopen(request).read()
  soup = BeautifulSoup(contents)
  newDictionary=json.loads(str(soup))
  res=[]
  for i in  newDictionary['results']:
    res.append(i['article_id'])
  print res
  return res

stream=[]
for i in range(20):
  page=paginate(i)
  for y in page:
    stream.append(y)

print len(stream)
print Counter(stream).most_common()
