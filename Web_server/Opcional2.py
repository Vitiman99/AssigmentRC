import sys
from socket import *

serverName = sys.argv[1]
serverPort = int(sys.argv[2])
filename = sys.argv[3]

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

request = 'GET /' + filename + ' HTTP/1.0\r\n\r\n'
clientSocket.send(request.encode())

response = clientSocket.recv(1024).decode()
print(response)

clientSocket.close()
