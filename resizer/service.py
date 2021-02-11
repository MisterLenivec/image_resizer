from PIL import Image

from image_resizer.settings import MEDIA_ROOT, MEDIA_URL


def check_img_param(width, height, original_width, original_height):
    """Checking the correct of the parameters and proportions of the picture"""
    if width is None:
        height_percent = (height / float(original_height))
        width = int((float(original_width) * float(height_percent)))
    elif height is None:
        width_percent = (width / float(original_width))
        height = int((float(original_height) * float(width_percent)))

    ratio_w = width / original_width
    ratio_h = height / original_height
    if ratio_w < ratio_h:
        resize_width = width
        resize_height = round(ratio_w * original_height)
    else:
        resize_width = round(ratio_h * original_width)
        resize_height = height

    offset = (round((width - resize_width) / 2), round((height - resize_height) / 2))

    return width, height, resize_width, resize_height, offset


def get_file_name_and_format(name):
    """Checking and getting the name and format of the image"""
    img_formats = ['png', 'jpeg', 'jpg', 'svg']
    img_format = None
    name = name

    if '.' in name:
        name, img_format = name.split('.')

    if img_format is None or img_format.lower() not in img_formats:
        img_format = 'png'

    return name, img_format


def images_resize(name, width, height):
    """Create a resized copy of the image"""
    img = Image.open(f'{MEDIA_ROOT}/{name}')

    width, height, resize_width, resize_height, offset = check_img_param(
        width, height, img.size[0], img.size[1]
    )

    img = img.resize((resize_width, resize_height), Image.ANTIALIAS)
    background = Image.new('RGB', (width, height), (255, 255, 255))
    background.paste(img, offset)

    name, img_format = get_file_name_and_format(str(name))

    background.save(f'{MEDIA_ROOT}/copies/{name}-lenivacopied.{img_format}')
    background.name = f'{MEDIA_URL}copies/{name}-lenivacopied.{img_format}'
    return background
