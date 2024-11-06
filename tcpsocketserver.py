import socket

# Create TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Host and port setup
host = 'localhost'  # Can also use '' for all available interfaces
port = 8080  # Use a higher port to avoid permission issues with port 80

# Bind the socket to the address and port
try:
    server_socket.bind((host, port))
    print(f"Server started on {host}:{port}...")
except Exception as e:
    print(f"Failed to bind server to port {port}: {e}")
    exit()

# Start listening for incoming connections
server_socket.listen(5)
print("Server is listening for connections...")

while True:
    try:
        # Accept a new connection from a client
        client_socket, client_address = server_socket.accept()
        print(f"Got connection from {client_address}")
        
        # Send a message to the client
        client_socket.sendall(b"Thank you for connecting\n")
        
        # Close the connection with the client after sending the message
        client_socket.close()
    except Exception as e:
        print(f"Error handling client: {e}")
