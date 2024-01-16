from socket import *
import sys

serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepare a server socket
# Fill in start
serverSocket.bind(('10.0.0.2', 23052)) # Bind the server to port 8888
serverSocket.listen(1) # Listen for incoming connections
# Fill in end

while True:
 # Establish the connection
 print('Ready to serve...')
 connectionSocket, addr = serverSocket.accept() # Accept incoming connection
 try:
     message = connectionSocket.recv(1024).decode() # Receive HTTP request
     lines = message.split('\n')
     method, path, version = lines[0].split()
     headers = {}
     for line in lines[1:]:
         if ':' in line:
             name, value = line.split(': ')
             headers[name] = value

     host = headers['Host']
     hostPort = int(host.split(':')[1])
     hostName = host.split(':')[0]
     print(hostName)
     print(hostPort)
     webServerSocket = socket(AF_INET, SOCK_STREAM)
     webServerSocket.connect((hostName, hostPort))
     webServerSocket.send(message.encode())

     responseMessage = b''
     while True:
         part = webServerSocket.recv(4096)
         if not part:
             break
         responseMessage += part

     connectionSocket.send(responseMessage)

     connectionSocket.close()
     webServerSocket.close()
 except IOError:
     # Send response message for file not found
     # Fill in start
     connectionSocket.sendall('HTTP/1.1 500 Internal Server Error\n\n'.encode())
     # Fill in end
     connectionSocket.close()

serverSocket.close()
sys.exit() # Terminate the program after sending the corresponding data
