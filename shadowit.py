import os.path
import subprocess
import argparse

# Default params
EXECUTABLE = 'convert'
SHADOW_OPACITY = 100     # percent
SHADOW_COLOR = '#444444'
SHADOW_SIZE = 22
SHADOW_X_OFFSET = 0     # pixels
SHADOW_Y_OFFSET = 20    # pixels
IMAGE_BG_COLOR = 'none'
INPUT_IMAGE = ''
OUTPUT_IMAGE = 'output.png'


def build_command(params):
    cmd = '''{exe} {input} -bordercolor none -border {borderSize} \
( +clone -background {color} -shadow {opacity}x{size}{xOffset:+d}{yOffset:+d} ) \
-reverse -background {imageBgColor} -layers merge +repage \
{output}'''.format(**params)
    return cmd

def execute(cmd):
    subprocess.call(cmd)

def parse_args():
    parser = argparse.ArgumentParser(description='Apply shadows to images')
    parser.add_argument('input', metavar='INPUT', help="input file name")
    parser.add_argument('-o', '--output', metavar='FILE', help='output file name (default: \'output.png\')')
    parser.add_argument('--exe', help='path to ImageMagick \'convert\' executable.')
    parser.add_argument('--opacity', type=int, help='opacity of shadow (default: %s)' % SHADOW_OPACITY)
    parser.add_argument('--color', help='color of shadow (default: %s)' % SHADOW_COLOR)
    parser.add_argument('--size', type=int, help='size of shadow (default: %d)' % SHADOW_SIZE)
    parser.add_argument('-x', '--xOffset', metavar='X', type=int, help='x offset of shadow (default: %d)' % SHADOW_X_OFFSET)
    parser.add_argument('-y', '--yOffset', metavar='Y', type=int, help='y offset of shadow (default: %d)' % SHADOW_Y_OFFSET)
    parser.add_argument('--imageBgColor', metavar='COLOR', help='Background color of the output image (default: %s)' % IMAGE_BG_COLOR)
    args = vars(parser.parse_args())
    return args

def build_params(params, args):
    for i in args: 
        if args[i] != None:
            params[i] = args[i]
    params['borderSize'] = compute_border_size(params['size'], params['xOffset'], params['yOffset'])

def compute_border_size(size, x, y):
    larger = x if x >= y else y
    return (2 * size) - larger

def get_default_params():
    params = {
        'exe': EXECUTABLE,
        'opacity': SHADOW_OPACITY,
        'color': SHADOW_COLOR,
        'size': SHADOW_SIZE,
        'xOffset': SHADOW_X_OFFSET,
        'yOffset': SHADOW_Y_OFFSET,
        'imageBgColor': IMAGE_BG_COLOR,
        'input': INPUT_IMAGE,
        'output': OUTPUT_IMAGE
    }
    return params

if __name__ == '__main__':
    args = parse_args()
    params = get_default_params()
    build_params(params, args)
    cmd = build_command(params)
    execute(cmd)
