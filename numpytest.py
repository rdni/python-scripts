import numpy as n
from scipy import stats
import matplotlib.pyplot as plt
dataSet = n.random.normal(5.0, 2.0, 100000)

a = n.mean(dataSet)
b = n.median(dataSet)
c = n.std(dataSet)
d = n.var(dataSet)
e = n.percentile(dataSet, 99.99)
print(a)
print(b)
print(c)
print(d)
print(e)
plt.hist(dataSet, 100)
plt.show()