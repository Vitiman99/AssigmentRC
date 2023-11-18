UDPLaboratorio

Codigo del Servidor

# UDPPingerServer.py
# We will need the following module to generate randomized lost packets
import random
from socket import *
# Create a UDP socket 
# Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.bind(('', 12000))
while True:
# Generate random number in the range of 0 to 10
rand = random.randint(0, 10) 
# Receive the client packet along with the address it is coming from 
message, address = serverSocket.recvfrom(1024)
# Capitalize the message from the client
message = message.upper()
# If rand is less is than 4, we consider the packet lost and do not respond
if rand < 4:
continue
# Otherwise, the server responds 
serverSocket.sendto(message, address)
Ejercicios
1.Actualmente, el programa calcula el tiempo de ida y vuelta para cada paquete y lo imprime individualmente. Modifique esto para que corresponda a la forma en que funciona el programa de ping estándar. Deberá informar el RTT mínimo, máximo y promedio al final de todos los pings del cliente. Además, calcule la tasa de pérdida de paquetes (en porcentaje).
import random
from socket import *

# Create a UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Assign IP address and port number to socket
serverSocket.bind(('', 12000))

# Initialize variables for tracking RTT and packet loss
rtt_list = []  # List to store RTT values
lost_packets = 0  # Counter for lost packets
total_packets = 0  # Counter for total packets

while True:
    # Generate random number in the range of 0 to 10
    rand = random.randint(0, 10)

    # Receive the client packet along with the address it is coming from
    message, address = serverSocket.recvfrom(1024)

    # Capitalize the message from the client
    message = message.upper()

    # Calculate RTT if the packet is not lost
    if rand >= 4:
        response_time = time.time() - float(message.decode('utf-8'))
        rtt_list.append(response_time)
        total_packets += 1
    else:
        lost_packets += 1

    # Send the response back to the client
    serverSocket.sendto(message, address)

# Calculate minimum, maximum, average RTT, and packet loss rate
if rtt_list:
    minimum_rtt = min(rtt_list)
    maximum_rtt = max(rtt_list)
    average_rtt = sum(rtt_list) / len(rtt_list)
    packet_loss_rate = (lost_packets / total_packets) * 100

    # Print the RTT statistics and packet loss rate
    print("Minimum RTT:", minimum_rtt, "seconds")
    print("Maximum RTT:", maximum_rtt, "seconds")
    print("Average RTT:", average_rtt, "seconds")
    print("Packet Loss Rate:", packet_loss_rate, "%")


2.Otra aplicación similar a UDP Ping sería UDP Heartbeat. Heartbeat se puede utilizar para verificar si una aplicación está en funcionamiento e informar la pérdida de paquetes unidireccional. El cliente envía un número de secuencia y una marca de tiempo actual en el paquete UDP al servidor, que está escuchando el latido del corazón (es decir, los paquetes UDP) del cliente. Al recibir los paquetes, el servidor calcula la diferencia de tiempo e informa los paquetes perdidos. Si faltan los paquetes de latido durante un período de tiempo específico, podemos suponer que la aplicación cliente se ha detenido.
Implemente UDP Heartbeat (tanto cliente como servidor). Deberá modificar el UDPPingerServer.py proporcionado y su cliente de ping UDP.


Código del servidor de UDP Heartbeat
Python
import random
from socket import *

# Create a UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Assign IP address and port number to socket
serverSocket.bind(('', 12000))

# Initialize variables for tracking heartbeats
heartbeat_list = []  # List to store heartbeats
lost_heartbeats = 0  # Counter for lost heartbeats

# Set the heartbeat timeout
heartbeat_timeout = 10  # seconds

while True:
    # Receive the client heartbeat
    message, address = serverSocket.recvfrom(1024)

    # Extract the sequence number and timestamp from the heartbeat
    sequence_number = int(message.decode('utf-8').split(' ')[0])
    timestamp = float(message.decode('utf-8').split(' ')[1])

    # Add the heartbeat to the list
    heartbeat_list.append({'sequence_number': sequence_number, 'timestamp': timestamp})

    # Calculate the difference in time between the current heartbeat and the previous heartbeat
    if len(heartbeat_list) > 1:
        previous_timestamp = heartbeat_list[-2]['timestamp']
        difference_in_time = timestamp - previous_timestamp

        # If the difference in time is greater than the heartbeat timeout, then the heartbeat is lost
        if difference_in_time > heartbeat_timeout:
            lost_heartbeats += 1

    # Print the heartbeat statistics
    print("Heartbeats received:", len(heartbeat_list))
    print("Heartbeats lost:", lost_heartbeats)

Código del cliente de UDP Heartbeat
Python
import time
from socket import *

# Create a UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Set the heartbeat interval
heartbeat_interval = 1  # seconds

while True:
    # Generate a random sequence number
    sequence_number = random.randint(1, 1000)

    # Get the current timestamp
    timestamp = time.time()

    # Create the heartbeat message
    message = "{} {}".format(sequence_number, timestamp)

    # Send the heartbeat message to the server
    clientSocket.sendto(message.encode('utf-8'), ('localhost', 12000))

    # Sleep for the heartbeat interval
    time.sleep(heartbeat_interval)
Este código funciona de la siguiente manera:
•	El servidor crea un socket UDP y lo vincula a un puerto específico.
•	El cliente crea un socket UDP y establece el intervalo de latidos.
•	El servidor entra en un bucle infinito, esperando paquetes UDP del cliente.
•	Cuando el servidor recibe un paquete UDP, extrae el número de secuencia y la marca de tiempo del paquete.
•	El servidor agrega el latido al final de una lista.
•	Si el servidor no recibe un latido del cliente durante el intervalo de latidos, el servidor marca el latido como perdido.
•	El cliente genera un número de secuencia aleatorio y obtiene la marca de tiempo actual.
•	El cliente crea un mensaje de latido con el número de secuencia y la marca de tiempo.
•	El cliente envía el mensaje de latido al servidor.
•	El cliente duerme durante el intervalo de latidos.
Para probar el código, ejecute el servidor primero y luego el cliente. El servidor imprimirá las estadísticas de latidos, que incluyen la cantidad de latidos recibidos y la cantidad de latidos perdidos.
Por ejemplo, si el servidor y el cliente están en la misma máquina y el intervalo de latidos se establece en 1 segundo, el servidor imprimirá lo siguiente:
Heartbeats received: 10
Heartbeats lost: 0
Si el servidor y el cliente están en máquinas diferentes, es posible que vea algunos latidos perdidos. La cantidad de latidos perdidos dependerá de la latencia de la red entre las dos máquinas.
