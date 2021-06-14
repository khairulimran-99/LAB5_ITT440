import socket
import sys

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 8888

serverSocket.bind(('',port))

serverSocket.listen(5)
print("Waiting Client....")

while True:
        connection, addr = serverSocket.accept()
        print("Connected to client")

        fileName = connection.recv(1024)
        file = open(fileName, "wb")

        msg = "Connected to: " +  addr[0] + "\n **Thank You** \n"
        connection.send(msg.encode("utf-8"))

        receive = connection.recv(1024)
        while receive:
                file.write(receive)
                rData = connection.recv(1024)

        file.close()
        print("File stored succesfully")

        connection.close()
        print("Server close connection")

        break
