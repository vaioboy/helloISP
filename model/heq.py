'''
Histogram Equalization
'''

import numpy as np

class HEQ:
    'heq'

    def __init__(self, img):
        self.img = img

    def do_hist(self):
        'histogram count'
        img_h = self.img.shape[0]
        img_w = self.img.shape[1]

        hcnt = np.zeros(256,'u4')

        for y in range(img_h):
            for x in range(img_w):
                hcnt[self.img[y,x]] = hcnt[self.img[y,x]]+1

        return hcnt

    def do_hmap(self, hcnt):
        'histogram map'
        img_h = self.img.shape[0]
        img_w = self.img.shape[1]

        hacc = np.empty(256,'u4')

        for i in range(256):
            if i==0:
                hacc[i] = hcnt[0]
            else:
                hacc[i] = hacc[i-1]+hcnt[i]

        hmap = np.empty(256,'u1')

        for i in range(256):
            hmap[i] = hacc[i]*255/(img_h*img_w)

        return hmap

    def execute(self):
        'execute'
        img_h = self.img.shape[0]
        img_w = self.img.shape[1]

        hcnt = self.do_hist()
        hmap = self.do_hmap(hcnt)

        for y in range(img_h):
            for x in range(img_w):
                self.img[y,x] = hmap[self.img[y,x]]

        return self.img
