from socket import *

host = "localhost"  #Setting IP address for Server
port = 10000         #Setting port for Server
address = (host, port) #Address
buf_size = 1024        #buffer-size
tcp_ser_sock = socket(AF_INET, SOCK_STREAM)       #Creat a socket object
tcp_ser_sock.bind(address)   #Binding the address to localhost
tcp_ser_sock.listen()        #Open listening 

print("Waitting for connecting.....")
tcp_cli_sock, cli_address = tcp_ser_sock.accept()
print("From:", cli_address, "...")          #Print tip

while True:
    data = tcp_cli_sock.recv(buf-size)   #Receving data from client
    if not data:                  #Check
        break
    data = data.decode('utf-8')    #Decoding data from receving
    tcp_cli_sock.send(("I'm walle you sended:" + data).encode('utf-8'))  #Response to client
    
tcp_cli_sock.close()  #Close client
tcp_ser_sock.close()  #Close Server
        
