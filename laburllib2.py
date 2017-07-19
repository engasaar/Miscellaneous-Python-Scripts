import urllib2
import ast
x='http://ip-api.com/json/'
site='hotmail.com'
#site=raw_input("please enter your site:")
url=x+site
print url
response=urllib2.urlopen(url)
h=response.read()
ls1=h.split(',')

for x in range(len(ls1)):
    ls1[x]=ls1[x].split(":")
      
print ls1[2][1]
print ls1[4][1]
print ls1[8][1]
#print ls[2] + ls[4] +ls[8]

#dict=ast.literal_eval(h)

#print "the country is: "+dict['country'] + '\nthe service provider is: ' + dict['isp'] + '\nthe ip address is: ' + dict['query']


