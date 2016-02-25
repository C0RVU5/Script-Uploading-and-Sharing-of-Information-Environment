#--------------------//CLIENT//-----------------------#
import socket, os, sys
from time import sleep
def Main():
    print("CLIENT STARTED")
    print("SUSIE(Script Uploading and Sharing of Information Environment)")
    print("Open data project written in Python2 by -C0RVUS-")
    host = '127.0.0.1'
    port = 5444
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    s.send("Still connected")

    usrres = raw_input("1.RETRIEVE FILE\n2.SUBMIT FILE\n> ")
    s.send(usrres)

    if usrres == "1":
        clientret()
    elif usrres == "2":
        clientsub()
    else:
        print("ERR..")
        print("RESTARTING CLIENT")
        Main()



#================================================================
    #while True:
        #output = s.recv(1024)
        #print(output)
    #else:
        # Main()
#================================================================

def clientsub():
    recev = (c.recv(1024))
    print(recev)
    send = raw_input("> ")
    s.send(send)
    recev = (c.recv(1024))
    print(recev)

#================================================================
def clientret():
    recev = (c.recv(1024))
    print(recev)
    send = raw_input("> ")
    s.send(send)
    recev = (c.recv(1024))
    print(recev)


Main()
