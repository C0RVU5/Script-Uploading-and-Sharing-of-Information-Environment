#--------------------//SERVER//-----------------------#
import socket, threading, os, sys
from time import sleep
def Main():
    host = '127.0.0.1'
    port = 5444
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host,port))
    s.listen(1)

    print "SERVER STARTED"
    c, addr = s.accept()
    print "CLIENT CONNECTED IP:<" + str(addr) + ">"
    sleep(10)


    usrres = c.recv(2048).strip()
    if usrres == "1":
	       serverret(sock, name)
    elif usrres == "2":
	       serversub(sock, name)
    else:
	       print("ERR...")
               Main()

#================================ progress of socket client + server comms dont think it works beyond here
def serversub(sock, name):
    s.send("ENTER FILENAME")
    filename = c.recv(1024)

    if os.path.isfile(filename) == True:
        s.send("FILE NAME ALREADY EXISTS")
        sub(sock,name)

    elif os.path.isfile(filename) == False:
        s.send("SUBMITTING: +"(filename))
        print("SERVER SUBMITTING FILE: " +(filename))
        f = open(filename, 'wb')
        data = s.recv(1024)
        totalRecv = len(data)
        f.write(data)
        while totalRecv < filesize:
            data = s.recv(1024)
            totalRecv += len(data)
            f.write(data)
            print "{0:.2f}".format((totalRecv/float(filesize))*100)+ "%"
	else:
	    print "Download Complete!"
    elif filename == "fileserver.py":
        s.send("ACCESS TO FILE IS DENIED")

    else:
        s.send("ERR...\nSERVER RESTARTING")
        print("SERVER RESTARTING")
        Main()





#sendfile
def serverret(name, sock):
    sock.send("ENTER FILENAME")
    filename = sock.recv(1024)
    if os.path.isfile(filename) == True:
        sock.send("EXISTS " + str(os.path.getsize(filename)))
	sock.send("1.DOWNLOAD\n2.CANCEL")
        userResponse = s.recv(1024)
        if userResponse == '1':
            with open(filename, 'rb') as f:
                bytesToSend = f.read(1024)
                sock.send(bytesToSend)
                while bytesToSend != "":
                    bytesToSend = f.read(1024)
                    sock.send(bytesToSend)
                sock.send("DOWNLOAD COMPLETE")

        elif userResponse == "2":
            Main()

        else:
            sock.send("ERR...\nSERVER RESTARTING")
            print("SERVER RESTARTING")
            Main()
    elif os.path.isfile(filename) == False:
        sock.send("FILE DOES NOT EXIST")
        ret(sock, name)
    else:
        print("ERR...")
        Main()

Main()
