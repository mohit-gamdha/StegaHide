from PIL import Image

img = Image.open("redImage.png")
pixels = img.load()

text = "armaan paaji IT"

binary = ""

for ch in text:
    temp = f'{ord(ch):08b}'
    for b in temp:
        binary += b

length_binary = len(binary)
pos = 0
width, height = img.size
for i in range(30, height):
    for j in range(30, width):
        r, g, b = pixels[i, j]
        if binary[pos] == '1':
            if r % 2 == 0:
                r += 1
        else:
            if r % 2 == 1:
                r -= 1
        pos += 1
        if binary[pos] == '1':
            if g % 2 is 0:
                g += 1
        else:
            if g % 2 == 1:
                g -= 1
        pos += 1

        if pos >= length_binary:
            if b % 2 == 0:
                b += 1
            pixels[i, j] = (r, g, b)
            break
        else:
            if b % 2 == 1:
                b -= 1
            pixels[i, j] = (r, g, b)
    if pos >= length_binary:
        break

img.save("redImage.png")
img.close()