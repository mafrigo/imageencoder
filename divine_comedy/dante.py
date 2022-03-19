from src.image_handling import *
from src.image_encoding import *
from unidecode import unidecode


def remove_non_ascii(text):
    return unidecode(text)


def encrypt_divine_comedy():
    test_image, image_type = load_image('divine_comedy/dante.png')
    with open('divine_comedy/divinacommedia.txt', 'r', encoding="utf8") as file:
        sample_text = file.read()
        sample_text = remove_non_ascii(sample_text)
    encoded_image = encode_image(test_image, sample_text, image_type=image_type)
    save_image(encoded_image, 'divine_comedy/dante-encrypted.png')


def decrypt_divine_comedy():
    loaded_image, image_type = load_image('divine_comedy/dante-encrypted.png')
    decoded_text = decode_image(loaded_image, image_type=image_type)
    print(decoded_text[50:110])
    print(decoded_text[534520:534563])


# encrypt_divine_comedy()
decrypt_divine_comedy()
