import base64
import ssl
from socket import *

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = 'smtp.gmail.com'

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, 587))

recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
   print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
   print('250 reply not received from server.')

# Send STARTTLS command and print server response.
starttlsCommand = 'STARTTLS\r\n'
clientSocket.send(starttlsCommand.encode())
recv2 = clientSocket.recv(1024).decode()
print(recv2)
if recv2[:3] != '220':
   print('220 reply not received from server.')

# Start TLS encryption
clientSocket = ssl.wrap_socket(clientSocket)

# Send HELO command again after TLS handshake and print server response.
clientSocket.send(heloCommand.encode())
recv3 = clientSocket.recv(1024).decode()
print(recv3)
if recv3[:3] != '250':
   print('250 reply not received from server.')

# Send AUTH LOGIN command and print server response.
authCommand = 'AUTH LOGIN\r\n'
clientSocket.send(authCommand.encode())
recv4 = clientSocket.recv(1024).decode()
print(recv4)
if recv4[:3] != '334':
   print('334 reply not received from server.')

# Send username and print server response.
username = 'manumartinez0309@gmail.com'
usernameCommand = base64.b64encode(username.encode()).decode() + '\r\n'
clientSocket.send(usernameCommand.encode())
recv5 = clientSocket.recv(1024).decode()
print(recv5)
if recv5[:3] != '334':
   print('334 reply not received from server.')

# Send password and print server response.
password = 'ojhn kqsh pzek tgqn' # Replace with your app password
passwordCommand = base64.b64encode(password.encode()).decode() + '\r\n'
clientSocket.send(passwordCommand.encode())
recv6 = clientSocket.recv(1024).decode()
print(recv6)
if recv6[:3] != '235':
   print('235 reply not received from server.')

# Send MAIL FROM command and print server response.
mailFromCommand = 'MAIL FROM: <manumartinez0309@gmail.com>\r\n'
clientSocket.send(mailFromCommand.encode())
recv7 = clientSocket.recv(1024).decode()
print(recv7)
if recv7[:3] != '250':
   print('250 reply not received from server.')

# Send RCPT TO command and print server response.
rcptToCommand = 'RCPT TO: <victormsire@gmail.com>\r\n'
clientSocket.send(rcptToCommand.encode())
recv8 = clientSocket.recv(1024).decode()
print(recv8)
if recv8[:3] != '250':
   print('250 reply not received from server.')

# Send DATA command and print server response.
dataCommand = 'DATA\r\n'
clientSocket.send(dataCommand.encode())
recv9 = clientSocket.recv(1024).decode()
print(recv9)
if recv9[:3] != '354':
   print('354 reply not received from server.')

# Send message data.
clientSocket.send(msg.encode())

# Message ends with a single period.
clientSocket.send(endmsg.encode())
recv10 = clientSocket.recv(1024).decode()
print(recv10)
if recv10[:3] != '250':
   print('250 reply not received from server.')

# Send QUIT command and get server response.
quitCommand = 'QUIT\r\n'
clientSocket.send(quitCommand.encode())
recv11 = clientSocket.recv(1024).decode()
print(recv11)
if recv11[:3] != '221':
   print('221 reply not received from server.')

# Close the socket.
clientSocket.close()
