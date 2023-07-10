# Opens file in read mode as bytes
file = open("tunn3l_v1s10n", "rb")
fbytes = file.read()

# Bitmap File Header
bmpFileHeader = fbytes[:13]
bmpId = bmpFileHeader[:2]
bmpSize = int.from_bytes(bmpFileHeader[2:5], byteorder="little")
# The 4 bytes here are reserved and are application dependant
bmpOffset = int.from_bytes(bmpFileHeader[10:13], byteorder="little")

print("Header: " + str(bmpId))
print("Sizse: " + str(bmpSize))
print("Offset: " + str(bmpOffset))

# DIB Header
DIB = fbytes[14:53]
bmpWidth = DIB[[14:17]
