from pwn import *

host=
port=

r = remote(host,port)

r.recvuntil(b'')
