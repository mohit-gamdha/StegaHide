from PIL import Image
import binascii
img = Image.open("redImage.png")
pixels = img.load()

binary = ""

width, height = img.size
temp = 0
for i in range(30, height):
    for j in range(30, width):
        r, g, b = pixels[i, j]
        if r % 2 == 0:
            binary += '0'
        else:
            binary += '1'
        if g % 2 == 0:
            binary += '0'
        else:
            binary += '1'
        if b % 2 is 1:
            temp = 1
            break
    if temp == 1:
        break

img.close()

temp = int(binary, 2)
binary = binascii.unhexlify('%x' % temp)


hidden_msg = ''.join(chr(i) for i in binary)
print(hidden_msg)