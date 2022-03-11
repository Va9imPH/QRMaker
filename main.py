import qrcode

adress = input("Input link: ")
filename = input("Input file name: ")

def get_qrcode(url=adress, name=filename):
    qr = qrcode.make(data=url)
    qr.save(stream=f'{name}.png')

    return f"QR code was created with name {name}.png"

def main():
    print(get_qrcode(url=adress, name=filename))

if __name__ == "__main__":
    main()