import qrcode

def generate_qr_code(data, file_name, foreground_color='black', background_color='white', box_size=10):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=box_size,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color=foreground_color, back_color=background_color)

    # Resize image to improve appearance
    img = img.resize((len(data) * box_size * 4, len(data) * box_size * 4), Image.ANTIALIAS)

    img.save(file_name)

# Example usage
generate_qr_code(data='https://www.example.com', file_name='example_qr_code.png', foreground_color='#FF5733', background_color='#000000', box_size=20)
print("QR code generated successfully!")