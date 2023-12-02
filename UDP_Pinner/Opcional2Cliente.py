import socket
import time

# Crea un socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Define la dirección del servidor y el puerto
server_address = ('localhost', 12001)

# Establece un tiempo de espera de 1 segundo en el socket
sock.settimeout(1)

sequence_number = 0

while True:
 print(f'Enviando Heartbeat {sequence_number}') # Imprime un mensaje cada vez que envía un Heartbeat
 message = f'Heartbeat {sequence_number} {time.time()}'
 sent = sock.sendto(message.encode(), server_address)
 sequence_number += 1
 time.sleep(1) # Espera 1 segundo antes de enviar el siguiente Heartbeat

sock.close()
