import socket
import time
import pickle5 as pickle
from temp_server import getTemp

host = '0.0.0.0'  # Ou '127.0.0.1' para conexões locais
port = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen()

print(f"Servidor ativo em {host}:{port}")

client_socket, client_address = server_socket.accept()
print(f"Conexão recebida de {client_address}")

while True:
    # mensagem = "Dados constantes do servidor"
    # client_socket.send(mensagem.encode())
    mensagem = pickle.dumps(getTemp())
    client_socket.send(mensagem)
    time.sleep(29)  # Envie dados a cada 29 segundos

# Feche a conexão com o cliente
client_socket.close()