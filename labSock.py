from socket import *
url='ip-api.com'
request = b"GET /json/hotmail.com HTTP/1.1\n\n"
s=socket(AF_INET,SOCK_STREAM)
#ip=gethostbyname(url)
#port=80
#print ip
s.connect(('ip-api.com',80))
s.send(request)
h = s.recv(10000)

print h
'''
x='http://ip-api.com/json/'
site='hotmail.com'
#site=raw_input("please enter your site:")
url=x+site
print url
response=urllib2.urlopen(url)
h=response.read()
'''
ls1=h.split(',')

for x in range(len(ls1)):
    ls1[x]=ls1[x].split(":")
  
    
print ls1[3][1]
print ls1[5][1]
print ls1[9][1]

#print ls[2] + ls[4] +ls[8]

#dict=ast.literal_eval(h)

#print "the country is: "+dict['country'] + '\nthe service provider is: ' + dict['isp'] + '\nthe ip address is: ' + dict['query']


