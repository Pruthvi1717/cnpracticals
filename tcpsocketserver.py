import socket


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP socket


host = 'localhost'  
port = 80  


server_socket.bind((host, port))
print(f"Server started on port {port}...")


server_socket.listen(5)
print("Server is listening for connections...")

while True:
   
    client_socket, client_address = server_socket.accept()
    print(f"Got connection from {client_address}")

    
    client_socket.sendall(b"Thank you for connecting\n")

    
    client_socket.close()

    
    break
