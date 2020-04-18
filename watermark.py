#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont
import json


class Watermark(object):
    DEFAULT_JSON='./default.json'

    def __init__(self, json_path=DEFAULT_JSON):
        self.load_config_from_json(json_path)

    def load_config_from_json(self, json_path=DEFAULT_JSON):
        with open(json_path, 'r') as f:
            config = json.load(f)
            self.text        = config['text']
            self.font        = config['font']
            self.fontsize    = config['fontsize']
            self.input       = config['input']
            self.output      = config['output']
            self.fill        = tuple(config['fill'])
            self.pos         = config['pos']
            self.wordspacing = config['wordspacing']
    
    def draw(self):
        try:
            font = ImageFont.truetype(self.font, self.fontsize)
        except:
            font = ImageFont.load_default()
        img = Image.open(self.input)
        draw = ImageDraw.Draw(img)
        posx = self.pos[0]
        for char in self.text:
            draw.text((posx, self.pos[1]), char, fill=self.fill, font=font)
            posx += self.wordspacing
        img.save(self.output)

if __name__ == "__main__":
    watermark = Watermark()
    watermark.draw()
