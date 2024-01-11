import time
from socket import *

# Set the server's IP address and port
serverIP = '127.0.0.1'
serverPort = 12000

# Create a UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)
# Set timeout to 1 second
clientSocket.settimeout(1)

# Send 10 pings to the server
for sequence_number in range(1, 11):
    # Get the current time
    start_time = time.time()

    # Prepare the ping message
    message = f'Ping {sequence_number} {start_time}'

    try:
        # Send the ping message to the server
        clientSocket.sendto(message.encode(), (serverIP, serverPort))

        # Receive the server's response
        response, serverAddress = clientSocket.recvfrom(1024)
        # Get the current time again to calculate RTT
        end_time = time.time()
        # Calculate the round trip time (RTT) in seconds
        rtt = end_time - start_time

        # Print the server's response and the RTT
        print(f'Response from server: {response.decode()}')
        print(f'Round trip time (RTT): {rtt} seconds')
    except timeout:
        # Print "Request timed out" if no response received within 1 second
        print('Request timed out')

# Close the socket
clientSocket.close()

#first run UDPPingerServer.py then this to run the client: python Assigment2/Client.py
