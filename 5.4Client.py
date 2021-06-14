import socket
import os

host = "192.168.56.103"

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 8888

serverSocket.connect((host,port))

send = input("File to send: ")
print("Name: " + send)

file = open(send, "rb")
sendData = file.read(1024)

serverSocket.send(send.encode("utf-8"))

while sendData:
	print("eceive from server \n", serverSocket.recv(1024).decode("utf-8"))
	serverSocket.send(sendData)
	sendData  = file.read(1024)

serverSocket.close()
