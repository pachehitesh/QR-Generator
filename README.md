# QR-Generator


**QR Code Generator Function Description:**

This Python function, `generate_qr_code`, allows users to quickly and easily generate QR codes for specified data. The function utilizes the `qrcode` library to create QR codes with customizable foreground and background colors, box size, and error correction level.

**Parameters:**
- `data`: The input data to be encoded into the QR code.
- `file_name`: The filename/path where the generated QR code image will be saved.
- `foreground_color`: The color of the QR code's foreground elements (default is black).
- `background_color`: The color of the QR code's background (default is white).
- `box_size`: The size of each individual box (pixel) in the QR code (default is 10 pixels).

**Functionality:**
1. The function initializes a QRCode object from the `qrcode` library, setting parameters such as version, error correction level, box size, and border.
2. It adds the provided data to the QRCode object and generates the QR code image.
3. The function then applies the specified foreground and background colors to the QR code image.
4. Optionally, the function resizes the image to improve its appearance.
5. Finally, the function saves the generated QR code image with the provided filename.

**Example Usage:**
```python
generate_qr_code(data='https://www.example.com', 
                 file_name='example_qr_code.png', 
                 foreground_color='#FF5733', 
                 background_color='#000000', 
                 box_size=20)
```

**Note:** Ensure you have the `qrcode` library installed (`pip install qrcode`) before using this function.

---

