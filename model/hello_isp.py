'''
hello ISP top
'''

import numpy as np
import matplotlib.pyplot as plt

from dpc import DPC
from dms import DMS

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

plt.imshow(img_rgb)
plt.show()
