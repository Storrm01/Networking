from socket import *

myIP = '10.111.121.31'
myPort = 49100
serverAddr = (myIP, myPort)

# Create a socket to listen
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Bind this socket to a port
serverSocket.bind(serverAddr)
#just for info
# print(serverSocket)

clientList = set() # empty to start


# keep receiving
while(True) :
    # receive some message
    received, clientAddr = serverSocket.recvfrom(2048)

    # Decode and Display the message received
    decoded = received.decode()
    print(decoded)
    clientList.add(clientAddr)
    # if decoded == 'exit':
    #     break

    # Return a message to the client
        # message and the clientAddr
        # hint: use the sendto() method
    for client in clientList: # broadcasting to everyone
        print(client)
        # sendto(received, client)
    msg = input("Please enter a message to send: ")
    print()
    encoded = msg.encode()
    serverSocket.sendto(encoded, clientAddr)