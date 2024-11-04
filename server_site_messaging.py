# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 11:50:23 2024

@author: Rafli (20115423)
Part C: Server_site_messaging
"""

import socket  # Import the socket library

def handle_client(connection, client_address):
    print(f"Connected to client at {client_address}")

    while True:
        try:
            message = connection.recv(1024).decode('utf-8')  # Get a message from the client
            
            if message.lower() == 'exit':  # If client says 'exit', stop
                print("Client disconnected.")
                break
            
            print(f"Client says: {message}")  # Print the client's message
            
            response = input("Reply to client (or type 'exit' to end): ")  # Send a response back to the client
            connection.sendall(response.encode('utf-8'))
            
            if response.lower() == 'exit':  # If server says 'exit', stop
                print("Server is ending the conversation.")
                break
        except Exception as e:
            print(f"An error occurred: {e}")
            break

    connection.close()  # Close the client connection
    print("Connection closed.")

def server_site():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:  # Use 'with' for automatic closure
        try:
            server_socket.bind(('localhost', 1234))  # Bind to localhost and port 1234
            server_socket.listen(1)  # Listen for incoming connections
            print("Server is now waiting for a connection on port 1234...")

            while True:
                connection, client_address = server_socket.accept()  # Accept a connection
                handle_client(connection, client_address)  # Handle client in a separate function
        except Exception as e:
            print(f"An error occurred while starting the server: {e}")

def play():
    # Start the server
    print("Starting the server...")
    server_site()

# Run the main function
if __name__ == "__main__":
    play()
