from socket import *
import sys

serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepare a server socket
# Fill in start
serverSocket.bind(('10.0.0.1', 23050)) # Bind the server to port 8888
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

    filename = path[1:]
    print(filename)
    print(f"Open this link in the browser: http://{hostName}:{hostPort}/{filename}")
    f = open(filename)
    outputdata = f.read()
    # Send one HTTP header line into socket
    # Fill in start
    connectionSocket.sendall(
        'HTTP/1.1 200 OK\nContent-Type: text/html\n\n'.encode())
    # Fill in end
    # Send the content of the requested file to the client
    connectionSocket.sendall(outputdata.encode())
    connectionSocket.close()
 except IOError:
    # Send response message for file not found
    # Fill in start
    connectionSocket.sendall('HTTP/1.1 404 File Not Found\n\n'.encode())
    # Fill in end
    connectionSocket.close()

serverSocket.close()
sys.exit() # Terminate the program after sending the corresponding data
