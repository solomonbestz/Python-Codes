import qrcode

image = qrcode.make("Approved")

image.save("approve.png")