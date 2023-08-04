#''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])

# Flag was encrypted into UTF-16, where 2 bytes are used for encoding each Chinese character
# I need to split each UTF-16 chunk into 2 UTF-8 chunks, and each of those will be a flag chr
enc = open("enc").read()

for i in range(0, len(enc)):
    hx = hex(ord(enc[i])).lstrip("0x")
    print(hx, end='')

print()
