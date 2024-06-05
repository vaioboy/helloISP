'''
Color Space Convertion
'''

import numpy as np

class CSC:
    'csc'

    def __init__(self, img, mode):
        self.img = img
        self.mode = mode

    def do_rgb2yuv(self, rgb):
        'rgb to yuv'
        r = rgb[0]
        g = rgb[1]
        b = rgb[2]
        yuv = np.empty(3,'u1')

        yuv[0] = 0.299*r+0.587*g+0.114*b
        yuv[1] = -0.16874*r-0.33126*g+0.5*b+128
        yuv[2] = 0.5*r-0.41869*g-0.08131*b+128

        return yuv

    def execute(self):
        'execute'

        img_h = self.img.shape[0]
        img_w = self.img.shape[1]

        for y in range(img_h):
            for x in range(img_w):
                if self.mode == 'rgb2yuv':
                    self.img[y,x] = self.do_rgb2yuv(self.img[y,x])

        return self.img
