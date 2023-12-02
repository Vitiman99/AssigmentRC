import socket
import time

# Crea un socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Define la dirección del servidor y el puerto
server_address = ('localhost', 12000)

# Establece un tiempo de espera de 1 segundo en el socket
sock.settimeout(1)

for i in range(1, 11):
  message = f'Ping {i} {time.time()}'
  sent = sock.sendto(message.encode(), server_address)

  try:
      data, server = sock.recvfrom(4096)
      print(f'Received: {data.decode()}')
      rtt = time.time() - float(message.split()[1])
      print(f'Round trip time: {rtt}')
  except socket.timeout:
      print('Request timed out')
  except ConnectionResetError:
      print('El servidor no respondió')

sock.close()
