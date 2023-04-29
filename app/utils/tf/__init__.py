import numpy as np
from . import tf2lib as tl
from . import module
from PIL import Image, ImageDraw, ImageFilter
import io
from .base64_pil_converter import pil_to_base64, base64_to_pil

TF_IMAGE_SIZE = 256


def convert_image(base64data: str, model: str, convert_direction: str, percent_crop):
    # 画像を読み込んでリサイズ
    img = base64_to_pil(base64data)

    resized_width = round(TF_IMAGE_SIZE * 100 / percent_crop["width"])
    resized_height = round(TF_IMAGE_SIZE * 100 / percent_crop["height"])

    pil_image_resized = img.resize((resized_width, resized_height))

    orig_image_array = np.array(pil_image_resized)

    # 切り取り
    h0 = round(orig_image_array.shape[0] * percent_crop["y"] / 100)
    h1 = h0+TF_IMAGE_SIZE
    v0 = round(orig_image_array.shape[1] * percent_crop["x"] / 100)
    v1 = v0+TF_IMAGE_SIZE
    cropped_image_array = orig_image_array[h0:h1, v0:v1, :]

    # model
    G_A2B = module.ResnetGenerator(input_shape=(TF_IMAGE_SIZE, TF_IMAGE_SIZE, 3))
    G_B2A = module.ResnetGenerator(input_shape=(TF_IMAGE_SIZE, TF_IMAGE_SIZE, 3))

    # resotre
    tl.Checkpoint(dict(G_A2B=G_A2B, G_B2A=G_B2A), f'constants/checkpoints/{model}').restore()

    # prepare image
    A = cropped_image_array.reshape([1, TF_IMAGE_SIZE, TF_IMAGE_SIZE, 3])

    # convert
    if (convert_direction == 'a2b'):
        converted = G_A2B(A, training=False)
    else:
        converted = G_B2A(A, training=False)

    # re-process
    converted_array = converted[0].numpy() * 127.5 + 127.5
    converted_array = np.concatenate([converted_array], axis=1).astype(np.uint8)

    ### append images
    orig_image = Image.fromarray(orig_image_array)
    converted_image = Image.fromarray(converted_array)

    mask_im = Image.new("L", converted_image.size, 0)
    draw = ImageDraw.Draw(mask_im)
    draw.ellipse((0, 0, TF_IMAGE_SIZE, TF_IMAGE_SIZE), fill=255)

    mask_im = mask_im.filter(ImageFilter.GaussianBlur(5))
    orig_image.paste(converted_image, (v0, h0), mask_im)
    ###

    return [
        pil_to_base64(orig_image, format="jpeg"),
        pil_to_base64(converted_image, format="jpeg")
    ]
