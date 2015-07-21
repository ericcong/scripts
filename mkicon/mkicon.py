""" Generate a round png icon with text on it

Usage:
    mkicon <text> <background color in hex> <text color in hex>

Returns:
    A 514*514 png file called "icon.png" in the current directory,
    with a circle of 512*512 and text on it.

"""

from PIL import Image, ImageDraw, ImageFont
import sys

if len(sys.argv) > 2:
    background_color = sys.argv[2]
else: 
    background_color = "000000"

if len(sys.argv) > 3:
    text_color = sys.argv[3]
else:
    text_color = "FFFFFF"

title = sys.argv[1]
length = len(title)

image = Image.new('RGBA', (514, 514))
draw = ImageDraw.Draw(image)
draw.ellipse((1, 1, 513, 513),
        fill='#'+background_color)

font = ImageFont.truetype(
        filename="/System/Library/Fonts/Menlo.ttc",
        size=600/length,
        index=1)

draw.text((78, 257.199 - 336.4656/length), title,
        font=font,
        fill='#'+text_color)

image.save("icon.png", 'PNG')