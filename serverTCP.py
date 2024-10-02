from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)

# Bind the server to the port
serverSocket.bind(('', serverPort))

# Listen for incoming connections (queue up to 1 connection request)
serverSocket.listen(1)
print('The server is ready to receive')

while True:
    # Accept a connection from a client
    connectionSocket, clientAddress = serverSocket.accept()
    
    # Receive the message from the client
    message = connectionSocket.recv(2048)
    modifiedMessage = (message.decode()).upper()
    
    # Send the modified message back to the client
    connectionSocket.send(modifiedMessage.encode())
    
    # Close the connection to the client
    connectionSocket.close()
