
import matplotlib.pyplot as plt
import matplotlib.image as mpimg 

file_name = input("Type in an image file name: ")

img = mpimg.imread(file_name)
plt.imshow(img)
plt.title('Choose a point to center image around: ')
pt = plt.ginput(1)

plt.axis('off')
plt.show()
