# rpc.py
# coding: utf-8

import socket
import json

# Conecta ao servidor, envia os dados e recebe a resposta da operação
def connect(self, dados):
        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            clientSocket.connect((self.ip, self.port))
            dados = json.dumps(dados)
            clientSocket.send(dados.encode('utf-8'))
            modifiedMessage = clientSocket.recv(1024).decode('utf-8')
            return modifiedMessage
        except Exception as e:
            print(e)
            return None

class OperacoesMatematicas:
    
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def soma(self, a, b):
        dados = {
                    "tipo" : "soma",
                    "num1" : a,
                    "num2" : b    
                }
        return connect(self, dados)
    
    def produto(self, a, b):
        dados = {
                    "tipo" : "produto",
                    "num1" : a,
                    "num2" : b    
                }
        return connect(self, dados)

    def fatorial(self, num):
        dados = {
                    "tipo" : "fatorial",
                    "num1" : num,
                    "num2" : None   
                }
        return connect(self, dados)

    
