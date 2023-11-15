"""
File: blur.py
Name: Angela
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: the original img
    :return: blurred img
    """
    new_img = SimpleImage.blank(img.width, img.height)  # create a blank img with the same height and width

    for x in range(img.width):
        for y in range(img.height):
            # go through every pixel
            all_r, all_g, all_b, count = 0, 0, 0, 0
            for i in range(x - 1, x + 2):
                for j in range(y - 1, y + 2):
                    # go through all neighbors of (x, y)
                    if img.width > i >= 0 and img.height > j >= 0:  # check if (i, j) exists
                        img_p = img.get_pixel(i, j)
                        all_r += img_p.red
                        all_g += img_p.green
                        all_b += img_p.blue
                        count += 1

            new_img_p = new_img.get_pixel(x, y)
            new_img_p.red = all_r / count
            new_img_p.green = all_g / count
            new_img_p.blue = all_b / count

    return new_img


def main():
    """
    TODO: show the original img and the blurred img
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
