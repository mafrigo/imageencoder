from src.image_handling import *
from src.image_encoding import *
from src.text_handling import *

if __name__ == '__main__':
    # encode
    test_image, image_type = load_image('test/sample_figures/githubsmall.png')
    sample_text = read_file('test/sample_texts/cantico1.txt')
    encoded_image = encode_image(test_image, sample_text, image_type=image_type)
    save_image(encoded_image, 'test/sample_figures/encoded_github.png')

    # decode
    loaded_image, image_type = load_image('test/sample_figures/encoded_github.png')
    decoded_text = decode_image(loaded_image, image_type=image_type)
    write_file('test/sample_texts/decoded_text.txt', decoded_text)
    print(decoded_text)
