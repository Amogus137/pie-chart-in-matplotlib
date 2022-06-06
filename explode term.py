import matplotlib.pyplot as plt
import numpy as np

x = ([35,25,25,15])

mylabels = ["apples", "bananas", "qovun", "qulupnay"] #1 explode uses with labels
myexplode = [0.2 , 0, 0, 0]

plt.pie(x, labels = mylabels, explode = myexplode) #2
plt.show()


