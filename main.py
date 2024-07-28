from PIL import Image, ImageDraw, ImageFont
from bidi.algorithm import get_display
import arabic_reshaper
import qrcode


def create_dard(type_card, name, father_name, date_print, QR_code, path_poto, save_file_name):
    t = type_card
    if t == "1":
        file_name = "assets/library card 1.png"
    elif t == "2":
        file_name = "assets/library card 2.png"
    img = Image.open(file_name)
    font = ImageFont.truetype("assets/B-NAZANIN.ttf", size=40, encoding="unic")
    draw = ImageDraw.Draw(img)

    text = name
    text2 = father_name
    date = date_print.split("/")
    year = date[0]
    month = date[1]
    day = date[2]

    reshaped_text = arabic_reshaper.reshape(text)
    bidi_text = get_display(reshaped_text)

    reshaped_text2 = arabic_reshaper.reshape(text2)
    bidi_text2 = get_display(reshaped_text2)

    reshaped_text3 = arabic_reshaper.reshape(year)
    bidi_text3 = get_display(reshaped_text3)

    reshaped_text4 = arabic_reshaper.reshape(month)
    bidi_text4 = get_display(reshaped_text4)

    reshaped_text5 = arabic_reshaper.reshape(day)
    bidi_text5 = get_display(reshaped_text5)

    draw.text((730, 230), bidi_text, (50, 50, 50), font=font, anchor="rt")
    draw.text((730, 300), bidi_text2, (50, 50, 50), font=font, anchor="rt")
    draw.text((440, 390), bidi_text3, (50, 50, 50), font=font)
    draw.text((580, 390), bidi_text4, (50, 50, 50), font=font)
    draw.text((690, 390), bidi_text5, (50, 50, 50), font=font)

    qr = qrcode.make(QR_code)
    qr.save('qr.png')

    img_qr = Image.open("qr.png")
    img_qr=img_qr.resize((150, 150))

    picture = Image.open(path_poto)
    picture = picture.resize((150, 225))

    img.paste(img_qr, (99, 350))
    img.paste(picture, (99, 140))
    img.save("./export-img/"+save_file_name+".png")





create_dard(
    input("Enter type of card\n"),
    input("Enter your name\n"),
    input("Enter your father name\n"),
    input("Enter date of today\n"),
    input("Enter your code\n"),
    input("Enter your path photo\n"),
    input("Enter file name\n")
)