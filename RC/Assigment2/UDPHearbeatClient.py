import time
from socket import *

# Set the server's IP address and port
serverIP = '127.0.0.1'
serverPort = 12000

# Create a UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Set the timeout to 1 second
clientSocket.settimeout(1)

# Initialize variables for tracking sequence numbers
sequence_number = 1

# Send the Heartbeat packets to the server
while True:
    # Get the current timestamp
    timestamp = time.time()

    # Prepare the Heartbeat packet
    message = f'Heartbeat {sequence_number} {timestamp}'

    try:
        # Send the Heartbeat packet to the server
        clientSocket.sendto(message.encode(), (serverIP, serverPort))

        # Receive the server's response
        response, serverAddress = clientSocket.recvfrom(1024)

        # Print the server's response (time difference)
        print(f'Response from server: Time difference: {response.decode()}')

        # Increment the sequence number
        sequence_number += 1

        # Sleep for 1 second before sending the next Heartbeat packet
        time.sleep(1)

    except timeout:
        # If the server does not respond within 1 second, print an error message
        print('Server did not respond')

# Close the socket
clientSocket.close()