import time
from socket import *

# Create a UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.bind(('', 12000))

# Set the timeout to 5 seconds
serverSocket.settimeout(5)

# Initialize variables for tracking sequence numbers and packet loss
expected_sequence_number = 1
packets_lost = 0

while True:
    try:
        # Receive the client packet along with the address it is coming from
        message, address = serverSocket.recvfrom(1024)

        # Split the message to extract the sequence number and timestamp
        message_parts = message.decode().split()
        sequence_number = int(message_parts[1])
        timestamp = float(message_parts[2])

        # Calculate the time difference
        time_difference = time.time() - timestamp

        # Check if the received sequence number is as expected
        if sequence_number == expected_sequence_number:
            print(f'Received heartbeat from client {address[0]}')
            expected_sequence_number += 1
        else:
            # Report any lost packets
            packets_lost += sequence_number - expected_sequence_number
            expected_sequence_number = sequence_number + 1

        # Send the time difference back to the client
        serverSocket.sendto(str(time_difference).encode(), address)

    except timeout:
        # If no heartbeat received for the specified period of time, assume the client application has stopped
        print('Client application has stopped')

# Print the packet loss rate
packet_loss_rate = (packets_lost / expected_sequence_number) * 100
print(f'Packet loss rate: {packet_loss_rate}%')

# Close the socket
serverSocket.close()