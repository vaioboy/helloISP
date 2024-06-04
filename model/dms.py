'''
Demosaicing
'''

import numpy as np

class DMS:
    'DMS'
    def __init__(self, img, pattern):
        self.img = img
        self.pattern = pattern

    def do_rggb(self, mat_raw):
        'for rggb'
        mat_rgb = np.empty((2,2,3),'u2')

        mat_rgb[0,0,0] = mat_raw[1,1]
        mat_rgb[0,0,1] = (mat_raw[0,1]+mat_raw[2,1]+mat_raw[1,0]+mat_raw[1,2])/4
        mat_rgb[0,0,2] = (mat_raw[0,0]+mat_raw[0,2]+mat_raw[2,0]+mat_raw[2,2])/4

        mat_rgb[0,1,0] = (mat_raw[1,1]+mat_raw[1,3])/2
        mat_rgb[0,1,1] = mat_raw[1,2]
        mat_rgb[0,1,2] = (mat_raw[0,2]+mat_raw[2,2])/2

        mat_rgb[1,0,0] = (mat_raw[1,1]+mat_raw[3,1])/2
        mat_rgb[1,0,1] = mat_raw[1,2]
        mat_rgb[1,0,2] = (mat_raw[2,0]+mat_raw[2,2])/2

        mat_rgb[1,1,0] = (mat_raw[1,1]+mat_raw[3,1]+mat_raw[3,1]+mat_raw[3,3])/4
        mat_rgb[1,1,1] = (mat_raw[1,2]+mat_raw[3,2]+mat_raw[2,1]+mat_raw[2,3])/4
        mat_rgb[1,1,2] = mat_raw[2,2]

        mat_rgb = (mat_rgb/4).astype('u1')

        return mat_rgb

    def execute(self):
        'execute'
        img_pad = np.pad(self.img,(1,1))

        img_h = self.img.shape[0]
        img_w = self.img.shape[1]

        img_rgb = np.empty((img_h,img_w,3),'u1')

        for y in range(int(img_h/2)):
            for x in range(int(img_w/2)):
                mat_raw = np.empty((4,4),'u2')
                mat_rgb = np.empty((2,2,3),'u1')

                mat_raw = img_pad[2*y:2*y+4,2*x:2*x+4]

                if self.pattern == 'rggb':
                    mat_rgb = self.do_rggb(mat_raw)

                img_rgb[2*y:2*y+2,2*x:2*x+2] = mat_rgb

        return img_rgb
