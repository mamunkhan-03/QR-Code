import qrcode as qr
img=qr.make("https://www.facebook.com/mlrmamun.khan.1/")
img.save("Facebook_Mamun.png")
qr.make(fit=True)
img=qr.make_image(fill_color='red', back_color='white')
