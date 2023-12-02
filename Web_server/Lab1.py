# import socket module
from socket import *
import sys  # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)
# Prepare a sever socket
serverSocket.bind(('127.0.0.1', 8858))  # Usamos el puerto 8858
serverSocket.listen(1)

while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()  # Aceptamos la conexión
    try:
        message = connectionSocket.recv(1024).decode()  # Recibimos el mensaje del cliente
        words = message.split()
        if len(words) < 2:
            continue
        filename = words[1]
        f = open(filename[1:])
        outputdata = f.read()  # Leemos el contenido del archivo
        # Send one HTTP header line into socket
        connectionSocket.send('HTTP/1.1 200 OK\n'.encode())  # Enviamos la respuesta HTTP
        connectionSocket.send('Content-Type: text/html\n'.encode())  # Especificamos el tipo de contenido
        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
            connectionSocket.send("\r\n".encode())

        connectionSocket.close()
    except IOError:
        # Send response message for file not found
        connectionSocket.send('HTTP/1.1 404 Not Found\n'.encode())  # Enviamos el mensaje de error 404
        # Close client socket
        connectionSocket.close()

serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding data
