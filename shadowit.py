import os.path
import subprocess
import argparse

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


def build_command():
    cmd = '''{exe} {input} \
-bordercolor {borderColor} -border {borderSize} \
( +clone -background {color} -shadow {opacity}x{size}{xOffset:+d}{yOffset:+d} ) \
-reverse -background {imageBgColor} -layers merge +repage \
{output}'''.format(**params)
    return cmd

def execute(cmd):
    subprocess.call(cmd)

def parse_args():
    parser = argparse.ArgumentParser(description='Apply shadows to images')
    parser.add_argument('input', metavar='INPUT', help="input file name")
    parser.add_argument('-o', '--output', metavar='FILE', help='output file name (default: \'<input>-shadowed\')')
    parser.add_argument('--exe', help='path to ImageMagick \'convert\' executable.')
    parser.add_argument('--opacity', type=int, help='opacity of shadow (default: 65)')
    parser.add_argument('--color', help='color of shadow (default: #555555)')
    parser.add_argument('--size', type=int, help='size of shadow (default: 9)')
    parser.add_argument('-x', '--xOffset', metavar='X', type=int, help='x offset of shadow (default: 0)')
    parser.add_argument('-y', '--yOffset', metavar='Y', type=int, help='y offset of shadow (default: 0)')
    parser.add_argument('--borderColor', metavar='COLOR', help='color of image\'s border (default: none)')
    parser.add_argument('--borderSize', metavar='SIZE', type=int, help='size of image\'s border in pixels (default: 0)')
    parser.add_argument('--imageBgColor', metavar='COLOR', help='Background color of the output image (default: none)')
    args = vars(parser.parse_args())
    return args

def replace_params(params, args):
    for i in args: 
        if args[i] != None:
            params[i] = args[i]

def get_default_params():
    params = {
        'exe': EXECUTABLE,
        'opacity': SHADOW_OPACITY,
        'color': SHADOW_COLOR,
        'size': SHADOW_SIZE,
        'xOffset': SHADOW_X_OFFSET,
        'yOffset': SHADOW_Y_OFFSET,
        'borderColor': BORDER_COLOR,
        'borderSize': BORDER_SIZE,
        'imageBgColor': IMAGE_BG_COLOR,
        'input': INPUT_IMAGE,
        'output': OUTPUT_IMAGE
    }
    return params

if __name__ == '__main__':
    args = parse_args()
    params = get_default_params()
    replace_params(params, args)
    cmd = build_command()
    execute(cmd)
