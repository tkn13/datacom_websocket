from socket import *

serverName = 'localhost'
serverPort = 12000

# Create a TCP socket (SOCK_STREAM)
clientSocket = socket(AF_INET, SOCK_STREAM)

# Establish connection to the server
clientSocket.connect((serverName, serverPort))

# Get user input and send the message
message = input("Input lowercase sentence:")
clientSocket.send(message.encode())

# Receive the modified message from the server
modifiedMessage = clientSocket.recv(2048)
print(modifiedMessage.decode())

# Close the socket
clientSocket.close()
