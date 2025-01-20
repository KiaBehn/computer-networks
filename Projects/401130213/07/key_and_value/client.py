import socket


IP = socket.gethostbyname(socket.gethostname())
PORT = 5050


def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((IP, PORT))

    while True:
        command = input("Enter command (SET key value, GET key, DELETE key) or exit/quit to quit: ")
        if command.lower() in ['exit', 'quit']:
            break
        client_socket.sendall(command.encode('utf-8'))
        response = client_socket.recv(1024).decode('utf-8')
        print(response)

    client_socket.close()


if __name__ == '__main__':
    main()
