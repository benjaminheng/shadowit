import os.path
import subprocess

EXECUTABLE_DIR = 'D:\Applications\ImageMagick-6.9.2-Q16'
EXECUTABLE = 'convert'

SHADOW_OPACITY = 65     # percent
SHADOW_COLOR = '#555555'
SHADOW_SIZE = 9
SHADOW_X_OFFSET = 0     # pixels
SHADOW_Y_OFFSET = 10    # pixels

BORDER_COLOR = 'none'
BORDER_SIZE = 0         # pixels

IMAGE_BG_COLOR = 'none'

INPUT_IMAGE = 'sample.png'
OUTPUT_IMAGE = 'output.png'

executablePath = os.path.join(EXECUTABLE_DIR, EXECUTABLE)

params = {
        'executable': executablePath,
        'shadowOpacity': SHADOW_OPACITY,
        'shadowColor': SHADOW_COLOR,
        'shadowSize': SHADOW_SIZE,
        'shadowX': SHADOW_X_OFFSET,
        'shadowY': SHADOW_Y_OFFSET,
        'borderColor': BORDER_COLOR,
        'borderSize': BORDER_SIZE,
        'imageBgColor': IMAGE_BG_COLOR,
        'inputImage': INPUT_IMAGE,
        'outputImage': OUTPUT_IMAGE
    }

def build_command():
    cmd = '''{executable} {inputImage} \
-bordercolor {borderColor} -border {borderSize} \
( +clone -background {shadowColor} \
-shadow {shadowOpacity}x{shadowSize}{shadowX:+d}{shadowY:+d} ) \
-reverse -background {imageBgColor} -layers merge +repage \
{outputImage}'''.format(**params)
    return cmd

def execute(cmd):
    subprocess.call(cmd)

cmd = build_command()
execute(cmd)
