import qrcode
import datetime

time = datetime.datetime.now()

saved_data = qrcode

url = "https://catx0rr.github.io/info"

qr = qrcode.QRCode(
                   version=1, 
		   error_correction=qrcode.constants.ERROR_CORRECT_L,
                   box_size=10, 
                   border=4)

qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill='black', back_color='white')
img.save("qrcode" + time.strftime("%d-%m-%y_%H%M%S") + ".png")
