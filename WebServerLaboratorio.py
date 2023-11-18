WebServerLaboratorio

Laboratorio 1: Laboratorio de servidores web
En esta práctica de laboratorio, aprenderá los conceptos básicos de la programación de sockets para conexiones TCP en Python: cómo crear un socket, vincularlo a una dirección y puerto específicos, así como enviar y recibir un paquete HTTP. También aprenderás algunos conceptos básicos del formato de encabezado HTTP.
Desarrollará un servidor web que maneje una solicitud HTTP a la vez. Su servidor web debería aceptar y analizar la solicitud HTTP, obtener el archivo solicitado del sistema de archivos del servidor, crear una respuesta HTTP mensaje que consta del archivo solicitado precedido por líneas de encabezado y luego envía la respuesta directamente al cliente. Si el archivo solicitado no está presente en el servidor, el servidor debe enviar un HTTP "404 No Encontrado” mensaje de vuelta al cliente.
Código
A continuación, encontrará el código esqueleto para el servidor web. Debes completar el código esqueleto. Los lugares donde necesita completar el código están marcados con #Rellenar inicio y #Rellenar final. Cada lugar puede requerir una o más líneas de código.
Ejecutando el servidor
Coloque un archivo HTML (por ejemplo, HelloWorld.html) en el mismo directorio en el que se encuentra el servidor. Ejecute el servidor programa. Determine la dirección IP del host que ejecuta el servidor (por ejemplo, 128.238.251.26). De otro host, abra un navegador y proporcione la URL correspondiente. Por ejemplo:
http://128.238.251.26:6789/HolaMundo.html
'HelloWorld.html' es el nombre del archivo que colocó en el directorio del servidor. Tenga en cuenta también el uso del puerto, número después de los dos puntos. Debe reemplazar este número de puerto con cualquier puerto que haya utilizado en el código del servidor. En el ejemplo anterior, hemos utilizado el número de puerto 6789. El navegador debería mostrar entonces el contenido de HelloWorld.html. Si omite ":6789", el navegador asumirá el puerto 80 y obtendrá la página web desde el servidor solo si su servidor está escuchando en el puerto 80.
Luego intente obtener un archivo que no esté presente en el servidor. Debería recibir el mensaje "404 no encontrado"

Qué entregar
Entregarás el código completo del servidor junto con las capturas de pantalla del navegador de tu cliente, verificando que realmente recibe el contenido del archivo HTML del servidor.
Código Python esqueleto para el servidor web
#import socket module
from socket import *
import sys # In order to terminate the program 
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket 
#Fill in start
#Fill in end 
while True: 
#Establish the connection 
print('Ready to serve...') 
connectionSocket, addr = #Fill in start                    #Fill in end 
try: 
message = #Fill in start                               #Fill in end 
filename = message.split()[1] 
f = open(filename[1:]) 
outputdata = #Fill in start                             #Fill in end
#Send one HTTP header line into socket 
#Fill in start 
#Fill in end 
#Send the content of the requested file to the client 
for i in range(0, len(outputdata)): 
connectionSocket.send(outputdata[i].encode()) connectionSocket.send("\r\n".encode())

connectionSocket.close()
except IOError: 
#Send response message for file not found
 #Fill in start 
#Fill in end 
#Close client socket
 #Fill in start 
#Fill in end 
       serverSocket.close() 
       sys.exit()#Terminate the program after sending the corresponding data



Ejercicios
1. Actualmente, el servidor web maneja solo una solicitud HTTP a la vez. Implementar un servidor multiproceso que sea capaz de atender múltiples solicitudes simultáneamente. Usando subprocesos, primero cree un hilo principal en el que su servidor modificado escucha a los clientes en un puerto fijo. Cuando recibe una conexión TCP solicitud de un cliente, configurará la conexión TCP a través de otro puerto y prestará servicios al cliente en una solicitud en un hilo separado. Habrá una conexión TCP separada en un hilo separado para cada par solicitud/respuesta.
2. En lugar de utilizar un navegador, escriba su propio cliente HTTP para probar su servidor. Tu cliente se conectará al servidor mediante una conexión TCP, enviar una solicitud HTTP al servidor y mostrar el servidor respuesta como salida. Puede asumir que la solicitud HTTP enviada es un método GET. El cliente debe tomar argumentos de línea de comando que especifiquen la dirección IP del servidor o el nombre de host,el puerto en el que el servidor está escuchando y la ruta en la que se almacena el objeto solicitado en el servidor.
El siguiente es un formato de comando de entrada para ejecutar el cliente.
client.py servidor_host puerto_servidor nombre de archivo


1. 
import os
import sys
from socket import *

def handle_client(connectionSocket):
    #Receive the request
    request = connectionSocket.recv(1024).decode()

    #Extract the filename from the request
    filename = request.split()[1]

    #Check if the file exists
    if not os.path.exists(filename):
        #Send error message
        response = 'HTTP/1.1 404 Not Found\n\n'
        connectionSocket.sendall(response.encode())
        connectionSocket.close()
        return

    #Open the requested file
    f = open(filename, 'rb')

    #Send the response
    response = 'HTTP/1.1 200 OK\n'
    response += 'Content-Type: text/html\n\n'
    response += f.read()

    connectionSocket.sendall(response.encode())

    f.close()
    connectionSocket.close()

def main():
    #Prepare a sever socket
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('', 80)) # Listen on all interfaces on port 80
    serverSocket.listen(5) # Allow 5 pending connections

    while True:
        #Establish the connection
        print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()

        #Create a new thread to handle the request
        thread = threading.Thread(target=handle_client, args=(connectionSocket,))
        thread.start()

if __name__ == '__main__':
    main()
Usa el código con precaución. Más información
content_copy
Este código funciona de la siguiente manera:
•	En la línea 1, el código importa el módulo threading.
•	En la línea 2, el código importa el módulo os.
•	En la línea 3, el código importa el módulo sys.
•	En la línea 12, el código crea una función llamada handle_client() que se encargará de manejar las solicitudes de los clientes.
•	En la línea 22, el código crea un bucle infinito que se utiliza para aceptar solicitudes de clientes de forma indefinida.
•	En la línea 24, el código acepta una conexión TCP de un cliente.
•	En la línea 26, el código crea un nuevo hilo para manejar la solicitud del cliente.
•	En la línea 27, el código inicia el nuevo hilo.
Cuando un cliente se conecta al servidor, el servidor crea un nuevo hilo para manejar la solicitud del cliente. El nuevo hilo se encarga de:
•	Recibir la solicitud del cliente.
•	Extraer el nombre del archivo solicitado de la solicitud.
•	Verificar si el archivo solicitado existe.
•	Si el archivo solicitado existe, abrirlo y enviarlo al cliente.
•	Cerrar la conexión con el cliente.
Este enfoque permite que el servidor maneje múltiples solicitudes simultáneamente. Cada solicitud es manejada por un hilo separado, lo que significa que el servidor puede atender múltiples solicitudes sin bloquearse.
Para probar el servidor, puede ejecutar el siguiente comando en un terminal:
python server.py
Luego, puede abrir un navegador y acceder a un archivo en el servidor. Por ejemplo, si tiene un archivo llamado index.html en el directorio del servidor, puede acceder al archivo escribiendo la siguiente URL en la barra de direcciones del navegador:
http://localhost:80/index.html
Si el archivo existe, el navegador debería mostrar el contenido del archivo.


2.import socket

def main():
    #Get the arguments from the command line
    host = sys.argv[1]
    port = int(sys.argv[2])
    filename = sys.argv[3]

    #Create a TCP socket
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Connect to the server
    clientSocket.connect((host, port))

    #Send the request
    request = 'GET /{} HTTP/1.1\n\n'.format(filename)
    clientSocket.send(request.encode())

    #Receive the response
    response = clientSocket.recv(1024)

    #Print the response
    print(response.decode())

if __name__ == '__main__':
    main()
Usa el código con precaución. Más información
content_copy
Este código funciona de la siguiente manera:
•	En la línea 2, el código importa el módulo socket.
•	En la línea 6, el código obtiene los argumentos de línea de comando.
•	En la línea 9, el código crea un socket TCP.
•	En la línea 11, el código se conecta al servidor.
•	En la línea 13, el código envía la solicitud al servidor.
•	En la línea 15, el código recibe la respuesta del servidor.
•	En la línea 17, el código imprime la respuesta del servidor.
Para probar el cliente, puede ejecutar el siguiente comando en un terminal:
python client.py localhost 80 index.html
Este comando se conectará al servidor web multiproceso que se está ejecutando en la dirección IP localhost en el puerto 80 y solicitará el archivo index.html. Si el archivo existe, el cliente debería imprimir el contenido del archivo en la salida del terminal.
Aquí hay un ejemplo de la salida del cliente:
HTTP/1.1 200 OK
Content-Type: text/html

<!DOCTYPE html>
<html lang="en">
<head>
<title>Hello, world!</title>
</head>
<body>
<h1>Hello, world!</h1>
</body>
</html>

