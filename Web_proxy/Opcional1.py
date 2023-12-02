from socket import *
import sys

if len(sys.argv) <= 1:
   print('Usage : "python ProxyServer.py server_ip"\n[server_ip : It is the IP Address Of Proxy Server')
   sys.exit(2)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
server_ip = '0.0.0.0'
server_port = 12345
tcpSerSock.bind((server_ip, server_port))
tcpSerSock.listen(5)

while 1:
   print('Ready to serve...')
   tcpCliSock, addr = tcpSerSock.accept()
   print('Received a connection from:', addr)
   message = tcpCliSock.recv(1024).decode()
   print(message)
   filename = message.split()[1].partition("/")[2]
   filetouse = "/" + filename
   fileExist = "false"
   try:
       f = open(filetouse[1:], "r")
       outputdata = f.readlines()
       fileExist = "true"
       tcpCliSock.send("HTTP/1.0 200 OK\r\n")
       tcpCliSock.send("Content-Type:text/html\r\n")
       for i in range(len(outputdata)):
           tcpCliSock.send(outputdata[i])
       print('Read from cache')
   except IOError:
       if fileExist == "false":
           c = socket(AF_INET, SOCK_STREAM)
           hostn = filename.replace("www.","",1)
           print(hostn)
           try:
               c.connect((hostn, 80))
               fileobj = c.makefile('r', 0)
               fileobj.write("GET "+"http://" + filename + " HTTP/1.0\n\n")
               h = fileobj.readline()
               h = fileobj.readline()
               while h != '\r\n':
                  h = fileobj.readline()
               h = fileobj.readline()
               while h != '\r\n':
                  tcpCliSock.send(h)
                  h = fileobj.readline()
               tmpFile = open("./" + filename,"wb")
               tmpFile.write(fileobj.read())
               tmpFile.close()
           except Exception as e:
               print("Illegal request", e)
               tcpCliSock.send("HTTP/1.0 404 ERROR\r\n")
               tcpCliSock.send("Content-Type:text/html\r\n")
               tcpCliSock.send("\r\n")
               tcpCliSock.send("<HTML><TITLE>Not Found</TITLE></HTML>")
       else:
           tcpCliSock.send("HTTP/1.0 404 ERROR\r\n")
           tcpCliSock.send("Content-Type:text/html\r\n")
           tcpCliSock.send("\r\n")
           tcpCliSock.send("<HTML><TITLE>Not Found</TITLE></HTML>")
   tcpCliSock.close()

# python Opcional1.py 192.168.1.1