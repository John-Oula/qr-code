import qrcode

def qr_code_generator():

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_Q,
        box_size=10,
        border=4,
    )
    qr.add_data('https://www.antratechstudios.com?s=qr')
    qr.make(fit=True)

    image = qr.make_image(fill_color="black", back_color="white")
    image.save('qr-code.png')

if __name__ == '__main__':
    qr_code_generator()