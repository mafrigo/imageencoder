import numpy as np


class Spaxel:
    spaxel_ID = 0
    contained_pixels = [[]]
    encoded_characters = None
    original_colors = [[]]
    encoded_colors = [[]]
    pixels_per_side = 2
    image_type = 'RGB'

    def __init__(self, contained_pixels, original_colors, image_type='RGB', pixels_per_side=2):
        self.contained_pixels = contained_pixels
        self.pixels_per_side = pixels_per_side
        self.original_colors = original_colors
        self.image_type = image_type

    def encode(self, characters_to_be_encoded):
        from src.encoding import get_encoding
        self.encoded_characters = characters_to_be_encoded
        average_color = np.mean(self.original_colors, axis=0)
        if self.image_type == 'RGB':
            average_color = np.clip(average_color, 3, 252)
            color_step = 1.
        if self.image_type == 'RGBA':
            average_color = list(np.clip(average_color[:3], 0.03, 0.97)) + [average_color[3]]
            color_step = 0.01
        self.encoded_colors = np.array([average_color] * 4)
        for i in range(3):  #loop over R G B
            character = characters_to_be_encoded[i]
            encoded_character = get_encoding(character, color_step)+[0.]
            self.encoded_colors[:,i] += np.array(encoded_character)

    def decode(self):
        from src.encoding import get_decoded_letter
        control_color=np.array(self.original_colors)[3,:]
        sequence=''
        if self.image_type == 'RGB':
            color_step = 1.
        if self.image_type == 'RGBA':
            color_step = 0.01
        for i in range(3):  #loop over R G B
            encoded_letter = np.array(self.original_colors)[0:3,i]-control_color[i]
            sequence += get_decoded_letter(encoded_letter, color_step=color_step)
        return sequence

    def save_to_image(self, image):
        for i in range(len(self.contained_pixels)):
            pixel = self.contained_pixels[i]
            image[pixel[0], pixel[1], :] = self.encoded_colors[i]
