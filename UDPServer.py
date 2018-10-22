# chapter 2
# UDP socket
# server

from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))									# assign port 12000 to server's socket
print("The server is ready to receive")
while True:
	message, clientAddress = serverSocket.recvfrom(2048) 			# packet from client to vars
	modifiedMessage = message.decode().upper()						# make upper case
	serverSocket.sendto(modifiedMessage.encode(), clientAddress)	# send back to client