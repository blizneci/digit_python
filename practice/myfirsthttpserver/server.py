import socket

# Создаем сервер, который прослушивает указанный адрес и порт
server = socket.create_server(("127.0.0.1", 8000))
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Ограничение на количество одновременных запросов
server.listen(10)
try:
    while True:
        client_socket, address = server.accept()
        # Декодируем полученные данные
        received_data = client_socket.recv(1024).decode('utf-8')

        print("Получили данные по сокету", received_data)

        # 1-й элемент данных хранит путь до указанного адреса в запросе
        path = received_data.split()[1]
        # Формируем HTTP ответ
        if path == '/quit':
            response = "HTTP/1.1 200 OK\nContent-Type: text/html; charset=utf-8\n\n"\
                f"Введена команда для остановки сервера:<br />Path: {path}<br />Сервер будет остановлен."
            raise KeyboardInterrupt
        else:
            response = "HTTP/1.1 200 OK\nContent-Type: text/html; charset=utf-8\n\n"\
                f"Привет!<br />Path: {path}"
        # Посылаем сформированный ответ в кодировке utf-8
        client_socket.send(response.encode("utf-8"))
        # Закрываем сокет для возможного дальнейшего использования
        client_socket.shutdown(socket.SHUT_RDWR)
except KeyboardInterrupt:
    # Если в терминале прервано выполнение операции, то возникает исключение
    # сервер будет остановлен
    client_socket.send(response.encode("utf-8"))
    server.shutdown(socket.SHUT_RDWR)
    server.close()