import matplotlib.pyplot as plt
import numpy as np

x = ([35,25,25,15])

mylabels = ["apples", "bananas", "qovun", "qulupnay"]
myexplode = [0.2 , 0, 0, 0]

plt.pie(x, labels = mylabels,explode = myexplode, shadow = True) #1 shadow
plt.show()


