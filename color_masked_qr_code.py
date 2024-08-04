import qrcode
from PIL import Image

# Set parameters

message01 = 'Yuan Ze University'
message02 = 'https://www.yzu.edu.tw'

VERSION = 1
EC = qrcode.constants.ERROR_CORRECT_H
BOX_SIZE = 20
BORDER = 2

RED = (233, 0, 0)
GREEN = (32, 255, 32)


# Code starts

def is_black(pixel):
    return pixel == (0, 0, 0)

def is_white(pixel):
    return pixel == (255, 255, 255)

# Generate the first QR code

qr1 = qrcode.QRCode(
    version = VERSION,
    error_correction = EC,
    box_size = BOX_SIZE,
    border = BORDER
)
qr1.add_data(message01)
qr1.make(fit=True)
img1 = qr1.make_image()
img1 = img1.convert("RGB")


# Generate the second QR code

qr2 = qrcode.QRCode(
    version = VERSION,
    error_correction = EC,
    box_size = BOX_SIZE,
    border = BORDER
)
qr2.add_data(message02)
qr2.make(fit=True)
img2 = qr2.make_image()
img2 = img2.convert("RGB")


# Generate color QR code

result_image = Image.new("RGB", img1.size)

pixels1 = img1.load()
pixels2 = img2.load()
result_pixels = result_image.load()

for x in range(img1.size[0]):
    for y in range(img1.size[1]):
        
        pixel1 = pixels1[x, y]
        pixel2 = pixels2[x, y]
    
        if (is_black(pixel1) and is_white(pixel2)):
            result_pixels[x, y] = RED  # set as red
        elif (is_black(pixel2) and is_white(pixel1)):
            result_pixels[x, y] = GREEN  # set as green
        else:
            result_pixels[x, y] = pixel1 # no change

result_image.show()
