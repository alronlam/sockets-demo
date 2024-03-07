import socket
import threading


def handle_server_receive(server_socket):
    try:
        while True:
            data = server_socket.recv(1024).decode()
            if not data:
                break  # Break the loop if no data is received (server closed the connection)

            print("Server: ", data)
    finally:
        server_socket.close()


def handle_server_send(server_socket):
    try:
        while True:
            # Get a message from the client user and send it to the server
            client_message = input("")
            server_socket.send(client_message.encode())
    finally:
        server_socket.close()


def start_client():
    server_address = (
        "localhost",
        12345,
    )  # Replace <SERVER_IP> with the server's IP address
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(server_address)

    # Start two threads for the client: one for receiving, one for sending
    threading.Thread(target=handle_server_receive, args=(client_socket,)).start()
    threading.Thread(target=handle_server_send, args=(client_socket,)).start()

    # Main thread can perform other tasks or handle additional logic
    try:
        while True:
            pass  # You can add additional logic here if needed

    finally:
        client_socket.close()


if __name__ == "__main__":
    start_client()
