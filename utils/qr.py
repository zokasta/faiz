import os
import qrcode
import qrcode.image.svg


def generate_qr_svg(data, filename="qrcode.svg"):

    downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")

    if not os.path.exists(downloads_folder):
        os.makedirs(downloads_folder)

    filepath = os.path.join(downloads_folder, filename)

    factory = qrcode.image.svg.SvgImage
    qr = qrcode.QRCode(box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)

    qr_image = qr.make_image(image_factory=factory)
    qr_image.save(filepath)
    print("Check you download folder")
    return filepath

def main(args):
    if len(args) == 0:
        print("You need to provide link")
    else:
        generate_qr_svg(args[0])