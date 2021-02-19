# My Client application
import socket
import sys

HOST = "localhost"
PORT = 5454
BUFFER = 1024
# Create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect to the socket
s.connect((HOST, PORT))
count = 0
source_file_name = 'client_file.txt'
while True:
    # Ask the user to enter the password
    MESSAGE = input('Enter the password:').encode()
    count += 1
    print("Sending Data to Server")
    # Send this to the server
    s.sendto(MESSAGE, (HOST, PORT))
    # Wait for a response from the server
    data = s.recv(BUFFER).decode()
    print(data)
    if 'Authenticated' in data:
        # Open a file to write
        file = open(source_file_name, 'wb')
        # Keep writing the data until the
        while True:
            line = s.recv(1024)
            while line:
                file.write(line)
                line = s.recv(1024)
            break
        file.close()
        s.close()

    if "unsuccessful" in data:
        break
    time.sleep(1)
