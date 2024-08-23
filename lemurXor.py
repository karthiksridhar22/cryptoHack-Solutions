#xor rgb values of two images

from PIL import Image

img1 = Image.open('lemur_ed66878c338e662d3473f0d98eedbd0d.png')
img2 = Image.open('flag_7ae18c704272532658c10b5faad06d74.png')

pix1 = list(img1.getdata())

pix2 = list(img2.getdata())

pix3 = []

for p1, p2 in zip(pix1, pix2):
    pix3.append(tuple(p1[i] ^ p2[i] for i in range(3)))

img3 = Image.new(img1.mode, img1.size)
img3.putdata(pix3)

img3.save('result.png')
img3.show()