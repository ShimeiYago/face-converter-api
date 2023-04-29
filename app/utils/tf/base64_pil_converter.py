from io import BytesIO
import base64
from PIL import Image

def pil_to_base64(img, format="jpeg"):
    buffer = BytesIO()
    img.save(buffer, format)
    img_str = base64.b64encode(buffer.getvalue()).decode("ascii")

    return img_str


def base64_to_pil(img_str):
    # if "base64," in img_str:
    #     # DARA URI の場合、data:[<mediatype>][;base64], を除く
    #     img_str = img_str.split(",")[1]
    img_raw = base64.b64decode(img_str)
    img = Image.open(BytesIO(img_raw))

    return img
