from pwn import *
KEY_LEN = 50000

conn = remote('mercury.picoctf.net', 20266)
print(conn.recvline()) # Header 1
print(conn.recvline()) # Header 2

# Extracting flag
flag = conn.recvline()
print(flag)
flag = unhex(flag)
#print("Unmodified flag length: {}".format(len(flag)))
#TODO: Figure out error here
flagLen = (len(flag) - 1) / 2 # Grabbing flag length
#flagLen = len(flag) - 1
#print("Length of flag: {}".format(flagLen))
print(conn.recvuntil(b'?')) # Receiving until user input

# Cycling back to beginning of key
# key_location is probably on 33
inpToCompleteCycle = KEY_LEN - flagLen
print(conn.send(b'A' * int(inpToCompleteCycle) + b'\r\n'))
#print(conn.recvuntil(b'?'), sep='\n') # Receiving until user input
conn.sendlineafter("What data would you like to encrypt? ", flag)
#print(conn.send(flag))
print(conn.recvline())

"""
# Encrypting new message using first 32 characters of key
print(conn.send(b'A' * 32 + b'\r\n'))
print(conn.recvline())
# Receiving my message encrypted with same key portion used to encrypt flag
my_cipher = conn.recvline()
print(my_cipher)
cipherLen = (len(my_cipher) - 1) / 2 # Grabbing flag length
print("Length of my_cipher: {}".format(cipherLen))
print("cipher1: {}".format(flag))           # Encrypted flag
print("cipher2: {}".format(my_cipher))      # Encrypted message

# TODO: Separate flag and my_cipher into lists, where every
#       element is is composed of 2 characters (representing 1 byte)
split_flag = [str(flag[i:i+2], 'UTF-8') for i in range(0, len(flag), 2)]
split_my_cipher = [str(my_cipher[i:i+2], 'UTF-8') for i in range(0, len(my_cipher), 2)]
print("split cipher1: {}".format(split_flag))
print("split cipher2: {}".format(split_my_cipher))
# c1 xor c2 = m1 xor m2 -> m1,m2
decoded_message = []
for i in range(0, len(split_flag)-1):
    decoded_message.append(chr(int(split_flag[i], 16) ^ int(split_my_cipher[i], 16)))
print("Decoded message: {}".format(decoded_message))

# ERROR: The lists were joined, so when I go through and XOR everything here, I'm
# XORing the wrong "things" together, rather than a byte at a time.
# i.e. (5 XOR 2, instead of 5b XOR 23)
"""

"""
result = list(map(lambda c1, c2: "{}".format(c1 ^ c2), flag, my_cipher))
print("C1 XOR C2 not joined: {}".format(result))
print("C1 XOR C2 joined: \n{}\n".format("".join(result)))
"""
"""
for i in range (0, len(result)):
    print("Result Character: {}".format(chr(int(result[i]))))
"""

print(conn.recvuntil(b'?')) # Receiving until user input
