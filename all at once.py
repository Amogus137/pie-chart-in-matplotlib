import matplotlib.pyplot as plt
import numpy as np

x = ([35,25,25,15])

mylabels = ["apples", "bananas", "qovun", "qulupnay"]
mycolors = ["black", "hotpink", "blue", "red"] 
myexplode = [0.2 , 0, 0, 0]

plt.pie(x, labels = mylabels, colors = mycolors, explode = myexplode, shadow = True, startangle = 90)
plt.legend(title = "4 fruits:")
plt.show()


