import socket
import sys

if __name__ == "__main__":

    host = "localhost"
    port = 8000

    try:
        ### Open a new socket at port 5000 ###
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Server listening at port {port}")

        ### Wait for a new connection ###
        client_socket, client_address = server_socket.accept()
        print(f"{client_address} has connected!")

        ### Keep receiving and printing messages ###
        while True:
            data = client_socket.recv(1024).decode("utf-8")
            if data:
                print("Client: ", data)
            else:
                print("Client disconnected. Waiting for new connection...")
                client_socket, client_address = server_socket.accept()
                print(f"{client_address} has connected!")

    finally:
        print("Closing the server socket")
        server_socket.close()
