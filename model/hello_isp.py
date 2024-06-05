'''
hello ISP top
'''

import numpy as np
import matplotlib.pyplot as plt

from dpc import DPC
from dms import DMS
from csc import CSC
from gac import GAC
from heq import HEQ

IMG_W = 1920
IMG_H = 1080
PATTERN = 'rggb'

img_raw = np.fromfile('../image/test.RAW', dtype='u2')
img_raw = img_raw.reshape([IMG_H,IMG_W])
print(50*'-' + '\nRead image done...\n')

dpc = DPC(img_raw, 20, 0)
img_dpc = dpc.execute()
print(50*'-' + '\nDPC done...\n')

#img_r = img_raw[::2, ::2]
#img_gr = img_raw[::2, 1::2]
#img_gb = img_raw[1::2, ::2]
#img_b = img_raw[1::2, 1::2]
#
#plt.imshow(img_r, cmap='gray')
#plt.show()

dms = DMS(img_dpc, 'rggb')
img_rgb = dms.execute()
print(50*'-'+'\nDemosaicing done...\n')

gac = GAC(img_rgb)
img_rgb = gac.execute()
print(50*'-'+'\nGamma done...\n')

plt.imshow(img_rgb)
plt.show()

#csc = CSC(img_rgb, 'rgb2yuv')
#img_yuv = csc.execute()
#print(50*'-'+'\nCSC done...\n')
#
#img_y = img_yuv[:,:,0]
#heq = HEQ(img_y)
#img_y = heq.execute()
#
#plt.imshow(img_y, 'gray')
#plt.show()
