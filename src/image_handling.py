import matplotlib.pyplot as plt


def load_image(filename):
    image = plt.imread(filename)
    if filename.endswith('png'):
        image_type = 'RGBA'
    else:
        image_type = 'RGB'
    return image, image_type


def show_image(image):
    plt.imshow(image)
    plt.show()


def save_image(image, filename):
    plt.imsave(filename, image, vmin=0, vmax=1)#, pil_kwargs={'compress_level': 0})
