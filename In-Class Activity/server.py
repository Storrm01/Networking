from socket import *

myIP = '127.0.0.1'
myPort = 13000
myAddr = (myIP, myPort)

# Create a socket to listen
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Bind this socket to a port
serverSocket.bind(myAddr)

# keep receiving
while(True) :
    # receive some message
    received, clientAddr = serverSocket.recvfrom(2048)

    # Decode and Display the message received
    decoded = received.decode()
    print(decoded)
    if decoded == 'exit':
        break

    # Return a message to the client
        # message and the clientAddr
        # hint: use the sendto() method