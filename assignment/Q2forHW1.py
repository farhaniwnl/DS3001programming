#part1

import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0,1,50)
y = np.log(x)
z = np.exp(x)
plt.xlabel('x')
plt.ylabel('y')
plt.title("Natural Log and Exponential Functions")
plt.scatter(x,y, label = "Natural Log")
plt.scatter(x,z, label = "Exponential")
plt.legend(loc = 'lower right')

plt.show()

#part2
g = np.linspace(-6.5,6.5,100)
p = np.sin(g)
q = np.cos(g)
plt.xlabel("x")
plt.ylabel("y")
plt.scatter(g,p,label = "Sine Function")
plt.plot(g,q,label = "Cosine Function")
plt.legend(loc = 'lower left')
plt.title("Sine and Cosine Functions")
plt.show()