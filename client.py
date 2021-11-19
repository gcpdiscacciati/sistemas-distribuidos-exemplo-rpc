# client.py
# coding: utf-8

from rpc import OperacoesMatematicas

RPC_SERVER = "127.0.0.1"

RPC_PORT = 16000

# Instancia a classe
op = OperacoesMatematicas(RPC_SERVER, RPC_PORT)

soma = op.soma(2, 3.5)
produto = op.produto(6.2, 2)
fatorial = op.fatorial(5)
 

print(f"Soma de 2 e 3.5: {soma}") # Exibe 5
print(f"Produto de 6.2 e 2: {produto}") # Exibe 5
print(f"Fatorial de 5: {fatorial}") # Exibe 5