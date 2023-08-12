from pwn import *
KEY_LEN = 50000

conn = remote('mercury.picoctf.net', 20266)
print(conn.recvline()) # Header 1
print(conn.recvline()) # Header 2

# Extracting flag
flag = conn.recvline()
print(flag)
#print("Unmodified flag length: {}".format(len(flag)))
flagLen = (len(flag) - 1) / 2 # Grabbing flag length
print("Length of flag: {}".format(flagLen))
print(conn.recvuntil(b'?')) # Receiving until user input

# Cycling back to beginning of key
# key_location is probably on 33
inpToCompleteCycle = KEY_LEN - flagLen
print(conn.send(b'A' * int(inpToCompleteCycle) + b'\r\n'))
print(conn.recvuntil(b'?'), sep='\n') # Receiving until user input

# Encrypting new message using first 32 characters of key
print(conn.send(b'A' * 32 + b'\r\n'))
print(conn.recvline())
my_cipher = conn.recvline()
print(my_cipher)
cipherLen = (len(my_cipher) - 1) / 2 # Grabbing flag length
print("Length of my_cipher: {}".format(cipherLen))
print("cipher1: {}".format(flag))
print("cipher2: {}".format(my_cipher))

print(conn.recvuntil(b'?')) # Receiving until user input
