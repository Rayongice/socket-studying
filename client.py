from socket import *

host = "localhost" #Server IP address
port = 10000       #Server port
address = (host, port) #address

buf_size = 1024    #buffer-size

tcp_cli_sock = socket(AF_INET, SOCKET_STREAM) #Using TCP to connect with socket
tcp_cli_sock.connect(address)                 #To connect Server

while True:
    data = input("> ")       #Get info from user
    if not data:             #Check
        break                #Break
    tcp_cli_sock.send(data.encode('utf-8'))   #Sending message
    
 data = tcp_cli_sock.recv(buf_size)          #Receving message from Server
 if not data:                      #Check
     break                         #Break
 print(data.decode('utf-8'))        #Decoding message from Server
 tcp_cli_sock.close()               #Close connecting
