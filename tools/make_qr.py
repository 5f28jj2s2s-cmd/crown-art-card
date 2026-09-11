"""Generate a static URL QR locally. Install: python3 -m pip install 'qrcode[pil]'"""
import argparse
from pathlib import Path
from urllib.parse import urlparse
import qrcode
import qrcode.image.svg
from PIL import Image, ImageDraw, ImageFont

parser = argparse.ArgumentParser(description='Create Crown Art URL QR files. No QR service required.')
parser.add_argument('url', help='Full live HTTPS page URL, including repository path and trailing slash')
parser.add_argument('--placeholder', action='store_true', help='Label the image as a placeholder')
args = parser.parse_args()
if urlparse(args.url).scheme != 'https' or not urlparse(args.url).netloc:
    parser.error('Enter a complete https:// URL.')
out = Path(__file__).resolve().parents[1] / 'qr'
out.mkdir(exist_ok=True)
stem = 'PLACEHOLDER-DO-NOT-PRINT' if args.placeholder else 'crown-art-live'
qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=16, border=4)
qr.add_data(args.url)
qr.make(fit=True)
raw = qr.make_image(fill_color='black', back_color='white').convert('RGB')
font = ImageFont.load_default(size=22)
label = 'PLACEHOLDER — DO NOT PRINT' if args.placeholder else 'CROWN ART • SAVE CONTACT'
canvas = Image.new('RGB', (raw.width, raw.height + 100), 'white')
canvas.paste(raw, (0, 0))
draw = ImageDraw.Draw(canvas)
draw.text((raw.width / 2, raw.height + 10), label, fill='black', font=font, anchor='mt')
# A smaller URL label preserves the QR's four-module white quiet zone.
draw.text((raw.width / 2, raw.height + 49), args.url, fill='black', font=ImageFont.load_default(size=14), anchor='mt')
canvas.save(out / f'{stem}.png')
qr.make_image(image_factory=qrcode.image.svg.SvgPathImage).save(out / f'{stem}.svg')
(out / 'destination.txt').write_text(('PLACEHOLDER — replace before use\n' if args.placeholder else 'LIVE QR DESTINATION\n') + args.url + '\n')
print(f'Created {stem}.png and {stem}.svg in {out}')
