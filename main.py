from src.image_handling import *
from src.image_encoding import *


if __name__ == '__main__':
    test_image, image_type = load_image('figs/githubsmall.png')
    with open('sampletext_full.txt', 'r') as file:
        sample_text = file.read()
    encoded_image = encode_image(test_image, sample_text, image_type=image_type)
    decoded_text = decode_image(encoded_image, image_type=image_type)
    save_image(encoded_image, 'figs/encoded_github.png')
    loaded_image, image_type = load_image('figs/encoded_github.png')
    decoded_text = decode_image(loaded_image, image_type=image_type)
    print(decoded_text)
