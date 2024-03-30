#create qr code with customize design
import qrcode as q

from PIL import Image
qr=q.QRCode(version=1, error_correction=q.constants.ERROR_CORRECT_H, box_size=15, border=5)
qr.add_data("https://www.facebook.com/mlrmamun.khan.1/")
qr.make(fit=True)
img=qr.make_image(fill_color='red', back_color='white')
img.save("Facebook_Mamun khan.png")