#import socket module
from socket import *
import sys # In order to terminate the program
from threading import Thread

class RequestHandler(Thread):
   def __init__(self, connectionSocket, addr):
       Thread.__init__(self)
       self.connectionSocket = connectionSocket
       self.addr = addr
       self.start()

   def run(self):
       try:
           message = self.connectionSocket.recv(1024).decode() # Recibimos el mensaje del cliente
           words = message.split()
           if len(words) < 2:
               return
           filename = words[1]
           f = open(filename[1:])
           outputdata = f.read() # Leemos el contenido del archivo
           #Send one HTTP header line into socket
           self.connectionSocket.send('HTTP/1.1 200 OK\n'.encode()) # Enviamos la respuesta HTTP
           self.connectionSocket.send('Content-Type: text/html\n'.encode()) # Especificamos el tipo de contenido
           #Send the content of the requested file to the client
           for i in range(0, len(outputdata)):
               self.connectionSocket.send(outputdata[i].encode())
               self.connectionSocket.send("\r\n".encode())
           self.connectionSocket.close()
       except IOError:
           #Send response message for file not found
           self.connectionSocket.send('HTTP/1.1 404 Not Found\n'.encode()) # Enviamos el mensaje de error 404
           #Close client socket
           self.connectionSocket.close()

serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
serverSocket.bind(('127.0.0.1', 8858)) # Usamos el puerto 8858
serverSocket.listen(1)

while True:
 #Establish the connection
 print('Ready to serve...')
 connectionSocket, addr = serverSocket.accept() # Aceptamos la conexión
 RequestHandler(connectionSocket, addr)

serverSocket.close()
sys.exit() #Terminate the program after sending the corresponding data
