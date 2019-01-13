#
# Installing matplotlib is required to run this script
#

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
img=mpimg.imread('images/emmanuel-macron.png')
imgplot = plt.imshow(img)
plt.show()