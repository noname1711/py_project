import qrcode

image = qrcode.make('https://docs.google.com/presentation/d/1lnHPBas8rudA5fVuSGKjVfVNKg9Oa90_8V1W4NLo9C0/edit?usp=drive_link')


image.save('qr1.png')