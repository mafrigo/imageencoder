from src.image_handling import *
from src.image_encoding import *
from src.text_handling import *
from unidecode import unidecode


def remove_non_ascii(text):
    return unidecode(text)


def encrypt_divine_comedy():
    test_image, image_type = load_image('divine_comedy/dante.png')
    sample_text = read_file('divine_comedy/divinacommedia.txt')
    encoded_image = encode_image(test_image, sample_text, image_type=image_type)
    save_image(encoded_image, 'divine_comedy/dante-encrypted.png')


def decrypt_divine_comedy():
    loaded_image, image_type = load_image('divine_comedy/dante-encrypted.png')
    decoded_text = decode_image(loaded_image, image_type=image_type)
    write_file('divine_comedy/divinacommedia-decrypted.txt', decoded_text)
    print(decoded_text[50:110])
    print(decoded_text[534520:534563])


# encrypt_divine_comedy()
decrypt_divine_comedy()
