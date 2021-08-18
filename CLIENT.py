import socket
import sys

s = socket.socket()
s.connect(("localhost",9999)) #connecting to the port
f = open ("newtext.txt", "rb")  #opening the file
l = f.read(1024) # reading the file
while (l):
    s.send(l) #sending the file via socket
    l = f.read(1024)

print('Done sending')
s.close() #closing the connection