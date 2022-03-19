from src.spaxel import *
import numpy as np


def encode_image(image, text, chars_per_pixel=3, image_type='RGB'):
    encoded_image = np.copy(image)
    max_text_length = int(chars_per_pixel * (image.shape[0] / 2) * (image.shape[1] / 2))
    if len(text) > max_text_length:
        print('Warning: the provided text is too long to fit in this image! It will get cropped at %i text length' % (
            max_text_length))
    elif len(text) < max_text_length:
        print('Repeating text %.2f times to fill image space' % (float(max_text_length) / float(len(text))))
        text *= (max_text_length // len(text) + 1)
    else:
        print("Wow, perfect text length for this image! :)")
    text_index = 0
    for i in range(image.shape[0] // 2):
        if (100 * i / (image.shape[0] // 2)) % 10 == 0:
            print("%i " % (100 * i / (image.shape[0] // 2)) + "%")
        for j in range(image.shape[1] // 2):
            pixels = [[2 * i, 2 * j], [2 * i, 2 * j + 1], [2 * i + 1, 2 * j], [2 * i + 1, 2 * j + 1]]
            colors = [image[pixel[0], pixel[1], :] for pixel in pixels]
            spaxel = Spaxel(pixels, colors, image_type=image_type)
            spaxel_text = text[text_index:text_index + chars_per_pixel]
            text_index += chars_per_pixel

            spaxel.encode(spaxel_text)
            spaxel.save_to_image(encoded_image)
    return encoded_image


def decode_image(image, image_type='RGB'):
    decoded_text = ''
    for i in range(image.shape[0] // 2):
        if (100 * i / (image.shape[0] // 2)) % 10 == 0:
            print("%i " % (100 * i / (image.shape[0] // 2)) + "%")
        for j in range(image.shape[1] // 2):
            pixels = [[2 * i, 2 * j], [2 * i, 2 * j + 1], [2 * i + 1, 2 * j], [2 * i + 1, 2 * j + 1]]
            colors = [image[pixel[0], pixel[1], :] for pixel in pixels]
            spaxel = Spaxel(pixels, colors, image_type=image_type)
            decoded_text += spaxel.decode()
    return decoded_text
