def get_encoding(character, color_step=1., base=6):
    char_ascii = ord(character)
    if char_ascii > (base ** 3) - 1:
        raise IOError("Character unicode value too large - use ASCII characters")
    first_digit = char_ascii // base ** 2
    second_digit = (char_ascii - first_digit * base ** 2) // base
    third_digit = char_ascii - first_digit * base ** 2 - second_digit * base
    first_digit += (- base // 2)
    second_digit += (- base // 2)
    third_digit += (- base // 2)
    return [color_step*first_digit, color_step*second_digit, color_step*third_digit]


def get_decoded_letter(encoded_letter, base=6, color_step=1.):
    first_digit = round(encoded_letter[0]/color_step) + base // 2
    second_digit = round(encoded_letter[1]/color_step) + base // 2
    third_digit = round(encoded_letter[2]/color_step) + base // 2
    ascii_number = round(third_digit + second_digit * base + first_digit * base ** 2)
    return chr(ascii_number)
