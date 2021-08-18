import socket
import sys
s = socket.socket()
s.bind(("localhost",9999)) #Creating and bining to a port on local host
s.listen(10) # Accepts up to 10 connections.
print ('Server listening....')

while True:
    sc, address = s.accept() #accepting the connections

    print(address)

    with open('received_file.txt', 'wb') as f: #creating a file
        print('file opened')
        while True:
            print('receiving data...')
            data = sc.recv(1024) #receiving the data

            if not data:
                break
            # write data to a file
            f.write(data)#writing the data into the created file
    f.close() # closing the file
    print('File recieved')

    sc.close() #closing the connection

s.close() #closing the socket