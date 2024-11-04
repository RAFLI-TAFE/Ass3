# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 20:05:12 2024

@author: Rafli (20115423)
Part C: Client_site_messaging
"""

import socket  # Import the socket library
import sys

def client_site(client_socket, initial_message):
    # Send the initial message to the server
    client_socket.sendall(initial_message.encode('utf-8'))
    print("Sent message to server:", initial_message)

    # Keep the conversation going until someone says 'exit'
    while True:
        response = client_socket.recv(1024).decode('utf-8')  # Get a reply from the server
        if response.lower() == 'exit':  # If server says 'exit', stop
            print("Server ended the connection.")
            break

        print(f"Server replies: {response}")  # Print server's reply

        # You could implement more logic here for additional messages, if needed

    client_socket.close()  # Close the client connection
    print("Client is disconnected.")

def play():
    # Create a new TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 1234))  # Connect to the server at localhost and port 1234
    print("Client is connected to the server at localhost:1234.")

    # Get the message from command-line arguments or use a default message
    initial_message = sys.argv[1] if len(sys.argv) > 1 else "Hello from client!"  # Default message
    client_site(client_socket, initial_message)  # Call the client_site function

# Run the main function
if __name__ == "__main__":
    play()
