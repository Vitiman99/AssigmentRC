import time
from socket import *

# Set the server's IP address and port
serverIP = '127.0.0.1'
serverPort = 12000

# Create a UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)
# Set timeout to 1 second
clientSocket.settimeout(1)

# Initialize variables for RTT calculations
min_rtt = float('inf')
max_rtt = 0
total_rtt = 0
packets_sent = 0
packets_received = 0

# Send 10 pings to the server
for sequence_number in range(1, 11):
    # Get the current time
    start_time = time.time()

    # Prepare the ping message
    message = f'Ping {sequence_number} {start_time}'

    try:
        # Send the ping message to the server
        clientSocket.sendto(message.encode(), (serverIP, serverPort))
        packets_sent += 1

        # Receive the server's response
        response, serverAddress = clientSocket.recvfrom(1024)
        # Get the current time again to calculate RTT
        end_time = time.time()
        # Calculate the round trip time (RTT) in seconds
        rtt = end_time - start_time

        # Update min and max RTT
        min_rtt = min(min_rtt, rtt)
        max_rtt = max(max_rtt, rtt)

        # Calculate total RTT for average calculation
        total_rtt += rtt
        packets_received += 1

        # Print the server's response and the RTT
        print(f'Response from server: {response.decode()}')
        print(f'Round trip time (RTT): {rtt} seconds')
    except timeout:
        # Print "Request timed out" if no response received within 1 second
        print('Request timed out')

# Calculate average RTT
average_rtt = total_rtt / packets_received if packets_received > 0 else 0

# Calculate packet loss rate
packet_loss_rate = (packets_sent - packets_received) / packets_sent * 100 if packets_sent > 0 else 0

# Print statistics
print(f'\nPing statistics:')
print(f'  Packets sent: {packets_sent}')
print(f'  Packets received: {packets_received}')
print(f'  Packet loss rate: {packet_loss_rate}%')
print(f'  Minimum RTT: {min_rtt} seconds')
print(f'  Maximum RTT: {max_rtt} seconds')
print(f'  Average RTT: {average_rtt} seconds')

# Close the socket
clientSocket.close()

#first run UDPPingerServer.py then this to run the client: python Assigment2/ClientStatistics.py