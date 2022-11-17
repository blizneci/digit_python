import socket
from time import sleep


server = socket.create_server(("127.0.0.1", 8000))
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.listen(10)
try:
    while True:
        client_socket, address = server.accept()
        received_data = client_socket.recv(1024).decode('utf-8')

        print("Получили данные по сокету :", received_data)

        path = received_data.split(" ")[1]
        if "quit" in path:
            response = f"HTTP/1.1 200 OK\nContent-Type: text/html; charset=utf-8\n\n" \
                f"Server will be closed<br />\nPath: {path}"
        else:
            response = f"HTTP/1.1 200 OK\nContent-Type: text/html; charset=utf-8\n\n" \
                f"Helloooo!<br />path: {path}"
        client_socket.send(response.encode('utf-8'))
        client_socket.shutdown(socket.SHUT_RDWR)
        if "quit" in path:
            raise KeyboardInterrupt
except KeyboardInterrupt:
    server.shutdown(socket.SHUT_RDWR)
    server.close()