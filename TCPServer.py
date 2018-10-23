# chapter 2
# TCP socket
# server

from socket import * 
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('',serverPort))							# associate server with port #, serverSocket = welcoming socket
serverSocket.listen(1)										# listen for client
print('The server is ready to receive')

while True:
	connectionSocket, addr = serverSocket.accept()			# create connection socket for client, completing handshake
	sentence = connectionSocket.recv(1024).decode()
	print('received: ', sentence)			
	capitalizedSentence = sentence.upper()
	connectionSocket.send(capitalizedSentence.encode())
	connectionSocket.close()