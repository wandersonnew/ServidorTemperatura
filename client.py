import socket
import pickle5 as pickle
from send_email import sendEmail

host = '127.0.0.1'
port = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

while True:
    dados = pickle.loads(client_socket.recv(1024))
    # print(f"Recebido: {dados}")
    temp = dados[1].replace('C', '').replace(',', '.').strip()
    if float(temp) > 28:
        sendEmail()