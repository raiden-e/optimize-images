#!/usr/bin/env python
# requires Pillow==7.1.2 webp-converter==4.0.1
import argparse
import json
import os
import pprint
import sys

from PIL import Image

pp = pprint.PrettyPrinter()

# VAULT_ADDR =  os.environ.get('VAULT_ADDR', 'http://localhost:8200')

def parse_args():
    parser = argparse.ArgumentParser(
        description='Converts and deploys a markdown post to Confluence')
    help = {
        "dir":                  f'The path to your Git repository (default: {os.getcwd()}))',
    }
    parser.add_argument(
        '--dir',
        dest='dir',
        default=os.getcwd(),
        help=help["dir"]
    )
    return parser.parse_args()

def crawlDirectories(inputPath):
    for dirpath, dirnames, files in os.walk(inputPath):
        pp.pprint(f'Found directory: {dirpath}')
        for file_name in files:
            file, ext = os.path.splitext(dirpath+os.sep+file_name)
            pp.pprint(ext)
            if ext in [".png", ".jpg", ".jpeg"]:
                convertImage(dirpath+os.sep+file_name)


def convertImage(infile):
    file, ext = os.path.splitext(infile)
    pp.pprint(file)
    im = Image.open(infile).convert("RGB")
    im.save(file + ".webp", "WEBP", quality=100)
    os.remove(infile)


def main():
    args = parse_args()
    pp.pprint("Starting")
    crawlDirectories(args.dir)


if __name__ == '__main__':
    main()
