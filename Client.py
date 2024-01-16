from socket import *
import sys


clientSocket = socket(AF_INET, SOCK_STREAM)

# Connect to the proxy server
print('Connecting to proxy server...')
clientSocket.connect(('10.0.0.2', 23052)) 

try:
   # Send HTTP request to the proxy server
   message = 'GET /HelloWorld.html HTTP/1.1\r\nHost: 10.0.0.1:23050\r\n\r\n'.encode() # Replace '/HelloWorld.html' with the relative path to your HTML file
   clientSocket.send(message)

   # Receive response from the proxy server
   responseMessage = clientSocket.recv(1024)
   print(responseMessage.decode())
finally:
   # Close the connection
   clientSocket.close()
   sys.exit()
