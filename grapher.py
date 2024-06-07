# import matplotlib as plt
import matplotlib.pyplot as plt

from dataParser import dataParser
import numpy as np



dataValues = dataParser(cheese)

xValues = list(range(1,len(dataValues) + 1,1))
yValues = dataValues

print(xValues)
print(yValues)

plt.plot(xValues,yValues)
plt.xlabel('date')
plt.ylabel('intrest')
plt.title('trends')
plt.show()