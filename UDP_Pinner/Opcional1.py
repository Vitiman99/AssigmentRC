import socket
import time

# Crea un socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Define la dirección del servidor y el puerto
server_address = ('localhost', 12000)

# Establece un tiempo de espera de 1 segundo en el socket
sock.settimeout(1)

rtts = []
packet_loss = 0

for i in range(1, 11):
 message = f'Ping {i} {time.time()}'
 sent = sock.sendto(message.encode(), server_address)

 try:
     data, server = sock.recvfrom(4096)
     print(f'Received: {data.decode()}')
     rtt = time.time() - float(message.split()[1])
     rtts.append(rtt)
 except socket.timeout:
     print('Request timed out')
     packet_loss += 1
 except ConnectionResetError:
     print('El servidor no respondió')
     packet_loss += 1

min_rtt = min(rtts) if rtts else None
max_rtt = max(rtts) if rtts else None
avg_rtt = sum(rtts) / len(rtts) if rtts else None

packet_loss_rate = (packet_loss / 10) * 100 if rtts else None

print(f'Min RTT: {min_rtt}')
print(f'Max RTT: {max_rtt}')
print(f'Avg RTT: {avg_rtt}')
print(f'Packet loss rate: {packet_loss_rate}%')

sock.close()
