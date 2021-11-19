# sistemas-distribuidos-exemplo-rpc

Exemplo de RPC. O arquivo `client.py` instancia uma classe contida no arquivo `rpc.py`, obtendo acesso às operações matemáticas disponíveis. A conexão com o servidor se dá no arquivo `rpc.py`. O processamento e os cálculos são realizados no servidor, que retorna o resultado para o cliente mantendo a conexão via socket transparente.

## Como usar
Em um ambiente configurado com o Python 3, execute o servidor, e em seguida execute o cliente
#### `python server.py`
#### `python client.py`

### Importante verificar o IP do servidor no arquivo `client.py` e alterá-lo se necessário.
