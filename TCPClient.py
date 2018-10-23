# chapter 2
# TCP socket
# client

from socket import *
# serverName = 'hostname' 											# pass either IP address, of server, or hostname
serverName = '192.168.0.123'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM) 			# using IPV4, and TCP socket
clientSocket.connect((serverName, serverPort))			# initiate TCP connection
sentence = input('Input lowercase sentence')
clientSocket.send(sentence.encode()) 					# unlike UDP, does not take explicit packet and destination address
modifiedSentence = clientSocket.recv(1024)
print('From Server: ', modifiedSentence.decode())
clientSocket.close()