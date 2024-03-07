import socket

if __name__ == "__main__":

    host = "localhost"
    port = 8000

    ### Connect to server socket ###
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.connect((host, port))

    ### Keep sending messages ###
    while True:
        client_message = input("Client: ")
        server_socket.send(client_message.encode())
