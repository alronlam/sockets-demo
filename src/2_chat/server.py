import socket
import threading


def handle_client_receive(client_socket):
    try:
        while True:
            data = client_socket.recv(1024).decode()
            if not data:
                break  # Break the loop if no data is received (client closed the connection)

            print("Client: ", data)
    finally:
        client_socket.close()


def handle_client_send(client_socket):
    try:
        while True:
            # Get a message from the server user and send it to the client
            server_message = input("")
            client_socket.send(server_message.encode())
    finally:
        client_socket.close()


def start_server():
    ### Start a server that listens on port 12345 ###
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", 12345))
    server_socket.listen(1)
    print("Listening for messages on port 12345")

    ### Wait for a new connection ###
    client_socket, client_address = server_socket.accept()
    print(f"{client_address} has connected!")

    # Start two threads for each client: one for receiving, one for sending
    threading.Thread(target=handle_client_receive, args=(client_socket,)).start()
    threading.Thread(target=handle_client_send, args=(client_socket,)).start()

    while True:
        pass


if __name__ == "__main__":
    start_server()
