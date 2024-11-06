import socket

# Server info
host = 'localhost'  # Use '127.0.0.1' or 'localhost' for local connections
port = 8080  # Make sure this matches the server's port

# Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to the server
    client_socket.connect((host, port))
    print(f"Connected to server at {host}:{port}")
    
    # Receive and print the message from the server
    data = client_socket.recv(1024)
    print("Received from server:", data.decode())
    
except Exception as e:
    print(f"Error connecting to the server: {e}")
finally:
    # Close the client socket
    client_socket.close()
