'''
Play
'''

import numpy as np
import matplotlib.pyplot as plt

axis_x = np.arange(0,1,0.0039)
axis_y = axis_x**(1/2.2)

plt.plot(axis_x*256,axis_y*256,)
plt.title('Gamma')
plt.legend(["gamma=2.2"])
plt.xlabel('Actual luminance')
plt.ylabel('Corrected value')
plt.grid(True)
plt.xlim(0,255)
plt.ylim(0,255)
plt.xticks(np.arange(0,256,32))
plt.yticks(np.arange(0,256,32))
plt.show()
