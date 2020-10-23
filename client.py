
import socket

# definicao do ip da porta
UDP_IP = '127.0.0.1'
UDP_PORT = 12000

# criacao do socket
clientSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# recebo do usuario o calculo aritmetico
calculo = input('Digite a operacao aritmetica ')

# envio para o servidor a operacao artimetica codificada
clientSocket.sendto(calculo.encode('utf-8'),(UDP_IP,UDP_PORT))

# recebo a resposta do servidor, decodifica e exibo na tela
resposta,serveraddress = clientSocket.recvfrom(4096)
print('Sua Resposta  '+ str(resposta.decode()))

# termino a conexao do client
clientSocket.close()


