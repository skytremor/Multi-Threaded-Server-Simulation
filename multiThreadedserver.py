#import socket module
from socket import *
import sys
import threading

#--------------------------------------------------------------
#--------------------Variable Declaration----------------------
port        = 4017
server      = '127.0.0.1'
#--------------------------------------------------------------
#-----------------Socket creation and binding------------------

#Creates a new socket using the given address family, socket type and protocol number. 
#If socket creation fails, output error message and exit process.
try :
    serverSocket = socket(AF_INET, SOCK_STREAM)
    print 'Socket was sucessfully created.'
except socket.error, msg :
    print 'Failed to create socket. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
 
 
#Binds socket to localhost and port
#If binding fails, output error message and exit procces.
try:
    serverSocket.bind((server, port))
    serverSocket.listen(1)
except socket.error , msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
     
print 'Socket binding complete.'
#--------------------------------------------------------------
def receiverThread():
    while True:
        #Establish the connection
        print 'Ready to serve...'
        connectionSocket, addr = serverSocket.accept()#Fill in start  #Fill in end
        try:
            message = connectionSocket.recv(1024)#Fill in start #Fill in end
            filename = message.split()[1]
            f = open(filename[1:])
            outputdata = f.read()#Fill in start #Fill in end
            connectionSocket.send('\nHTTP/1.x 200 OK\n')
            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i])
            connectionSocket.close()
        except IOError:
            connectionSocket.send('\n404 File Not Found\n') 
            connectionSocket.close()


receiver = threading.Thread(target=receiverThread)    #Listener Thread

receiver.start()                            #Start listener thread
            
serverSocket.close()