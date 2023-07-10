import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('mercury.picoctf.net', 22902))

data = clientsocket.recv(1024)
data = data.split(b'\n')

for i in range(0,len(data)):
	if data[i] != b'':
		data[i] = chr(int(bytes.decode(data[i])))
	else:
		data.pop(i)

solution=""
print(solution.join(data))
