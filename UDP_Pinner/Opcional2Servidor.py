import socket
import time

# Crea un socket UDP
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Asigna la dirección IP y el número de puerto al socket
serverSocket.bind(('localhost', 12001))

last_sequence_number = None

while True:
 print('Esperando Heartbeat...') # Imprime un mensaje cada vez que espera un Heartbeat
 message, address = serverSocket.recvfrom(1024)
 print(f'Recibido Heartbeat de {address}') # Imprime un mensaje cada vez que recibe un Heartbeat
 sequence_number = int(message.split()[1])
 if last_sequence_number is not None and sequence_number != last_sequence_number + 1:
     print(f'Perdido el paquete {last_sequence_number + 1}')
 last_sequence_number = sequence_number

serverSocket.close()
