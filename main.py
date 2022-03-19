from src.image_handling import *
from src.image_encoding import *

if __name__ == '__main__':
    # encode
    test_image, image_type = load_image('figures/githubsmall.png')
    with open('test/sample_texts/cantico1.txt', 'r') as file:
        sample_text = file.read()
    encoded_image = encode_image(test_image, sample_text, image_type=image_type)
    save_image(encoded_image, 'figures/encoded_github.png')

    # decode
    loaded_image, image_type = load_image('figures/encoded_github.png')
    decoded_text = decode_image(loaded_image, image_type=image_type)
    print(decoded_text)
