#import qrcode as qr
#img=qr.make("https://www.youtube.com")
#img.save("qrcode.png")

 #--------------------------------------------

import qrcode
from PIL import Image #pip install PIL
qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CONNECTION_H,
                 box_size-10, border=4)

qr.add_data("http://www.youtube.com")
qr.make(fit=True)
img=qr.make_image(fill_color="red", back_color="blue")
img.save("qrcode.png")


