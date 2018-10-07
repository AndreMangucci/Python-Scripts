import socket
target_host = ""
target_port = 

while 1 :
    # create a socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect the client
    client.connect((target_host,target_port))

    data = input("Send some data : ")
    if data == "-exit" :
        break
    # send some data
    data = data+"!"
    client.sendall((data).encode())

    #receive some data
    response = client.recv(4096).decode('utf-8')
    print (response)