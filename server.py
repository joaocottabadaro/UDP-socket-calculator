
import socket


UDP_IP = '127.0.0.1'
UDP_PORT = 12000

# criacao e inicializacao do servidor
serverSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serverSocket.bind((UDP_IP,UDP_PORT ))

print('Servidor Inicializado')
# loop para continuar recebendo requisicoes de usuarios
while 1:
   
    try:
        # recebo um objeto socket e o endereco da conexao 
        calculo,clientAddress = serverSocket.recvfrom(1024)
        # resolve e decodifico a operacao aritmetica
        resposta = eval(calculo.decode())

        # envio de volta a resolucao codificada
        serverSocket.sendto(str(resposta).encode(), clientAddress)
    except:
        break

# desligo o servidor caso ocorra erro
serverSocket.close()

