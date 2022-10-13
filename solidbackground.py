from PIL import Image
import os
import argparse

# python solidbackground.py -c "#35F68A" -r "1920x1080" -o "./test.png"

def create_background(color, resolution, output):
    w, h = (int(_) for _ in resolution.split('x'))
    img = Image.new('RGB', (w, h), color)
    img.save(output)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('-c', '--colorhex', required=True, type=str, help='RGB hex value of desired color')
    ap.add_argument('-r', '--resolution', required=True, type=str, help='image resolution; ex) 1920x1080')
    ap.add_argument('-o', '--outputfile', required=True, type=str, help='filepath to save image to')
    args = ap.parse_args()

    c = args.colorhex.lower()
    if len(c) != 7 or not c[1:].isalnum() or any(d not in '0123456789abcdef' for d in c[1:]):
        print('invalid color hex')
        return
    
    r = args.resolution
    if 'x' not in r or any(not n.isnumeric() for n in r.split('x')):
        print('invalid resolution')
        return
    
    o = args.outputfile
    o = os.path.expanduser(o)
    try:
        with open(o, 'w') as temp:
            pass
    except OSError:
        print('invalid file path')
        return

    create_background(c, r, o)

if __name__ == '__main__':
    main()