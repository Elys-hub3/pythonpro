import socket
import threading

#definir l'adresse ip
trach_ip = "0.0.0.0" #adresse local du receveur
#definir le port
trach_port = 8080 #port >1000

#définir la variable serveur pour créer la connection
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#lier l'adresse ip avec le port
server.bind((trach_ip, trach_port))#corriger trach par bind
#ecouter
server.listen(5)
print("listening on %s:%d" %(trach_ip, trach_port))

#creer une fonction
def manage_client(client_socket):
	while True:
		request = client_socket.recv(1024)
		print("Received : %s" % (request))
		client_socket.send('ACCEPTED!')


while True:
	client, addr = server.accept()
	print("server is running, accept connection from %s:%d" %(addr[0], addr[1]))
	manage_client = threading.Thread(target=manage_client, args=(client,))
	manage_client.start()
