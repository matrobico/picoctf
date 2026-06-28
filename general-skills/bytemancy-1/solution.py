from pwn import *

host="foggy-cliff.picoctf.net"
port=50804

r = remote(host,port)

r.recvuntil(b'==> ')

r.interactive()
