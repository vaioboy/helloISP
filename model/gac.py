'''
Gamma Correction
'''

import numpy as np

class GAC:
    'gac'
    def __init__(self,img):
        self.img = img

    def do_gamma(self):
        'calculate gamma LUT'
        ori = np.arange(256,dtype='uint8')

        lut = np.empty(256,'u1')
        lut = ori*(1**(1/2.2))

        return lut

    def execute(self):
        'execute'
        img_h = self.img.shape[0]
        img_w = self.img.shape[1]

        lut = self.do_gamma()

        for y in range(img_h):
            for x in range(img_w):
                self.img[y,x] = lut[self.img[y,x]]

        return self.img
