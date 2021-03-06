import random
from io import BytesIO
import os
from PIL import Image, ImageDraw, ImageFont


def get_random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def get_valid_code_img():
    img = Image.new('RGB', (260, 34), color=get_random_color())
    draw = ImageDraw.Draw(img)
    # font_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
    #  '../static/fonts/element-icons.732389d.ttf')
    font_path = '/System/Library/Fonts/NewYork.ttf'
    kumo_font = ImageFont.truetype(
        font_path, size=30)
    valid_code_str = ''
    for i in range(5):
        random_num = str(random.randint(0, 9))
        random_low_alpha = chr(random.randint(97, 122))
        random_high_alpha = chr(random.randint(65, 90))
        random_char = random.choice(
            [random_num, random_low_alpha, random_high_alpha])
        draw.text((i * 50 + 20, 5), random_char,
                  get_random_color(), font=kumo_font)

        # 保存验证码字符串
        valid_code_str += random_char

    # 噪点噪线
    width = 260
    height = 34
    for i in range(5):
        x1 = random.randint(0, width)
        x2 = random.randint(0, width)
        y1 = random.randint(0, height)
        y2 = random.randint(0, height)
        draw.line((x1, y1, x2, y2), fill=get_random_color())

    for i in range(5):
        draw.point([random.randint(0, width), random.randint(
            0, height)], fill=get_random_color())
        x = random.randint(0, width)
        y = random.randint(0, height)
        draw.arc((x, y, x + 4, y + 4), 0, 90, fill=get_random_color())

    # 保存验证码字符串到该用户的session
    # request.session['valid_code_str'] = valid_code_str

    f = BytesIO()  # 用完之后，BytesIO会自动清掉
    img.save(f, 'png')
    data = f.getvalue()

    return valid_code_str, data
