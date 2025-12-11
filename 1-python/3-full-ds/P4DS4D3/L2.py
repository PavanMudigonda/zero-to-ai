import matplotlib.image as img
import matplotlib.pyplot as plt

image = img.imread('MySamplePlot.png')
print(image)

print(image.shape)
print(image.dtype)
plt.show()