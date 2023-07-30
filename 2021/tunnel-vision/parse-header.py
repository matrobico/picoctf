# Opens file in read mode as bytes
file = open("tunn3l_v1s10n_corrected_v2.bmp", "rb")
fbytes = file.read()

# Bitmap File Header (14 bytes, not optional)
# Contains metadata about image
#bmpFileHeader = fbytes[:13]
bmpId = fbytes[:2]
bmpSize = int.from_bytes(fbytes[2:6], byteorder="little")
# The 4 bytes here are reserved and are application dependant (6:10)
bmpOffset = int.from_bytes(fbytes[10:14], byteorder="little")

#print("ID: " + str(bmpId))
print("ID: {}".format(str(bmpId)))
print("Size of BMP File: " + str(bmpSize))
print("Image Data Offset: {} => Hex: {}".format(str(bmpOffset), str(hex(bmpOffset))))
print("Offset bytes: {}".format(fbytes[10:14]))

# DIB Header (X bytes in this case, not optional)
# Instructs how to display image on screen
#DIB = fbytes[14:53]
dibSize = int.from_bytes(fbytes[14:18], byteorder="little")
bmpWidth = int.from_bytes(fbytes[18:22], byteorder="little")
bmpHeight = int.from_bytes(fbytes[22:26], byteorder="little")
colorPlanes = int.from_bytes(fbytes[26:28], byteorder="little")
bitsPerPixel = int.from_bytes(fbytes[28:30], byteorder="little")
compressionMethod = fbytes[30:34]
imageSize = int.from_bytes(fbytes[34:38], byteorder="little")
horRes = int.from_bytes(fbytes[38:42], byteorder="little")
verRes = int.from_bytes(fbytes[42:46], byteorder="little")
numColors = int.from_bytes(fbytes[46:50], byteorder="little")
numImportantColors = int.from_bytes(fbytes[50:54], byteorder="little")

print("DIB Size: " + str(dibSize))
print("DIB Size bytes: {}".format(fbytes[14:18]))
print("BM Width: " + str(bmpWidth))
print("BM Height: " + str(bmpHeight))
print("Color Planes: " + str(colorPlanes))
print("Bits Per Pixel: " + str(bitsPerPixel))
print("Compression Method: " + str(compressionMethod))
print("Image Size: " + str(imageSize))
print("Horizontal Resolution: " + str(horRes))
print("Vertical Resolution: " + str(verRes))
print("Number of Colors: " + str(numColors))
print("Number of Important Colors: " + str(numImportantColors))

# No "Extra Bit Masks"

# Color Table (mandatory for color depths <= 8 bits)

# Gap1 (artifact of the file offset to pixel array in the bmp file header)

# Pixel Array (not optional)
# Pixel array must begin at address that is multiple of 4 bytes

# Gap2

# ICC Color Profile
