# Iterative Socket Server, Single-Threaded Server

# Import Libraries
import socket
import subprocess
import time
import sys

# Run Commands
def run_command(command):
    if command == "Date and Time":
        result = time.ctime()
    elif command == "Uptime":
        result = subprocess.check_output("uptime", shell=True).decode()
    elif command == "Memory Use":
        result = subprocess.check_output("free -m", shell=True).decode()
    elif command == "Netstat":
        result = subprocess.check_output("netstat - tulnp | head -n 6", shell=True).decode()
    elif command == "Current Users":
        result = subprocess.check_output("who", shell=True).decode()
    elif command == "Running Processes":
        result = subprocess.check_output("ps aux | head -n 6", shell=True).decode()
    elif command == "Exit Program":
        print("Connection closed.")
        sys.exit()
    else:
        result = "Invalid command."
    return result

# Setup Server
def create_server(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind(('139.62.210.155', port))
        server_socket.listen(1)
        print(f"Server is listening on port {port}")

        # Accept Connections
        while True:
            conn, addr = server_socket.accept()
            print(f"Connected by {addr}")

            # Accept Commands
            with conn:
                command = conn.recv(1024).decode()
                print(f"Command received from {addr}: {command}")

                # Server Exit Check
                if command == "goodbye_world":
                    conn.sendall("Shutting down the server.".encode())
                    print("Server shutdown command received. Closing server.")
                    sys.exit()
                
                # Handle Commands
                result = run_command(command)
                conn.sendall(result.encode())
                print(f"Result sent to client {addr}: {command}")

# Ask User for Port Number and Create Server
port = int(input("Enter port number to listen on: "))
create_server(port)
