#Web Server With Python
import socket
HOST, PORT = '', 8888
listening_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listening_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

listening_socket.bind((HOST, PORT))
listening_socket.listen(1)

while True:
    client_connection, client_address = listening_socket.accept()
    request_data = client_connection.recv(1024)
    print(request_data.decode('utf-8'))
    http_response = b"""

HTTP/1.1 200 OK

This is a server response
"""
    client_connection.sendall(http_response)
    client_connection.close()

