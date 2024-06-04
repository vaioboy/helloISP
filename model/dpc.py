'''
Defect Pixel Correction
'''

import numpy as np

class DPC:
    'DPC'
    def __init__(self, img, thres, mode):
        self.img = img
        self.thres = thres
        self.mode = mode

    def detect(self, arr, thres):
        'detect'
        res = False

        res =   abs(arr[0]-arr[1])>thres and \
                abs(arr[0]-arr[2])>thres and \
                abs(arr[0]-arr[3])>thres and \
                abs(arr[0]-arr[4])>thres and \
                abs(arr[0]-arr[5])>thres and \
                abs(arr[0]-arr[6])>thres and \
                abs(arr[0]-arr[7])>thres and \
                abs(arr[0]-arr[8])>thres

        return res

    def mean_s(self, arr):
        'mean simple'
        res =  (arr[1]+arr[2]+arr[3]+arr[4]+
                arr[5]+arr[6]+arr[7]+arr[8])/8

        return res

    def mean_d(self, arr):
        'mean dirction'
        dh = abs(arr[4]+arr[5]-arr[0])
        dv = abs(arr[2]+arr[7]-arr[0])
        dl = abs(arr[1]+arr[8]-arr[0])
        dr = abs(arr[3]+arr[6]-arr[0])

        if min(dh,dv,dl,dr) == dh:
            res = (arr[4]+arr[5])/2
        elif min(dh,dv,dl,dr) == dv:
            res = (arr[2]+arr[7])/2
        elif min(dh,dv,dl,dr) == dl:
            res = (arr[1]+arr[8])/2
        else:
            res = (arr[3]+arr[6])/2

        return res

    def execute(self):
        'execute'
        img_pad = np.pad(self.img,(2,2))

        img_h = self.img.shape[0]
        img_w = self.img.shape[1]

        arr = np.empty(9, np.uint16)

        for y in range(img_h):
            for x in range(img_w):
                arr[0] = img_pad[y+2,x+2]
                arr[1] = img_pad[y+0,x+0]
                arr[2] = img_pad[y+0,x+2]
                arr[3] = img_pad[y+0,x+4]
                arr[4] = img_pad[y+2,x+0]
                arr[5] = img_pad[y+2,x+4]
                arr[6] = img_pad[y+4,x+0]
                arr[7] = img_pad[y+4,x+2]
                arr[8] = img_pad[y+4,x+4]

                arr = arr.astype(int)

                if self.detect(arr, self.thres):
                    if self.mode == 0:
                        pix = self.mean_s(arr)
                    else:
                        pix = self.mean_d(arr)

                    self.img[y,x] = pix.astype('u2')

        return self.img
