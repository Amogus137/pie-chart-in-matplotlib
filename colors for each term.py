import matplotlib.pyplot as plt
import numpy as np

x = ([35,25,25,15])

mylabels = ["apples", "bananas", "qovun", "qulupnay"]
mycolors = ["black", "hotpink", "blue", "red"] # colors for each terms

plt.pie(x, labels = mylabels, colors = mycolors)
plt.legend(title = "4 fruits:")
plt.show()


