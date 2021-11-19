# server.py
# coding: utf-8

import socket
import json
from math import factorial

# Configuração da conexão
serverPort = 16000
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(0)

print("Servidor pronto para receber")

# Identifica e calcula o resultado da operação
def calculaOperacao(dadosJSON):
    if dadosJSON["tipo"] == "soma":
        return dadosJSON["num1"] + dadosJSON["num2"]
    
    elif dadosJSON["tipo"] == "produto":
        return dadosJSON["num1"] * dadosJSON["num2"]

    elif dadosJSON["tipo"] == "fatorial":
        if dadosJSON["num1"] >= 0:
            return factorial(dadosJSON["num1"])
    
    return None


# Loop que aguarda a conexão do cliente e processa a mensagem recebida
while True:
    try:
        connectionSocket, addr = serverSocket.accept()
        print("Conexão vinda de {}".format(addr))
        message = connectionSocket.recv(2048)
        decodedMessage = message.decode('utf-8')
        print("{} ==> {}".format(addr, decodedMessage))

        # Transforma o objeto recebito em um objeto JSON
        dadosJSON = json.loads(decodedMessage)

        # Identifica a operação e realiza os cálculos
        resposta = calculaOperacao(dadosJSON)
        resposta = str(resposta)
        # Retorna a mensagem modificada
        connectionSocket.send(resposta.encode('utf-8'))

        # Encerra a conexão com o cliente
        connectionSocket.close()
    except ConnectionResetError:
        print(f"Conexão perdida com {addr}")