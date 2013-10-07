import xmlrpclib, sys

host, port = "", 5022
server = xmlrpclib.ServerProxy("http://%s:%d" % (host, port))
#server = xmlrpclib.ServerProxy('http://localhost:9000')
print server.test()
server.color2black('bassetts.jpg')
server.detectedges('bassetts.jpg')
server.brighten('bassetts.jpg')