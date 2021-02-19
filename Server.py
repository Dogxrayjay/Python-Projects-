# My server application

import socket
import time
import sys

HOST = "127.0.0.1"
PORT = 5454
BUFFER = 1024

password = 'password'

print("Waiting for client to connect")
# Create a TCP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
# Wait for connection
s.listen(1)
# If there is a connection, accept it
conn, addr = s.accept()
# AF_INET refers to the address family ipv4.
# The SOCK_STREAM means connection oriented TCP protocol.
tries = 0
filename = 'some_text_file.txt'
while True:
    # wait for data to be received through the connection
    data = conn.recvfrom(BUFFER)
    # Check if the data sent by the client(password) is correct

    if data[0].decode() == password:
        conn.send("Authenticated".encode())
        # Open the file to send in binary
        file = open(filename,'rb')
        line = file.read(1024)
        while line:
            conn.send(line)
            line = file.read(1024)

    else:
        tries += 1
        if tries == 3:
            conn.send("You have reached the limit of unsuccessful tries. Server shutting down".encode())
            conn.close()
            break
        else:
            conn.send("Wrong password".encode())
    time.sleep(1)

# It creates the file but it doesn't write
