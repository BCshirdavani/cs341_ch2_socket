# chapter 2
# UDP socket
# client

from socket import *
# serverName = 'hostname' 											# pass either IP address, of server, or hostname
serverName = '192.168.0.123'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM) 							# creates client socket, IPv4, UDP
message = input('Input lowercase sentence:') 						# get user input
clientSocket.sendto(message.encode(), (serverName, serverPort))		# convert message string to byte, and send
modifiedMessage, serverAddress = clientSocket.recvfrom(2048) 		# packet back from server put into var, also source address of server into var..buffer size = 2048
print(modifiedMessage.decode())										# display string of message
clientSocket.close()
