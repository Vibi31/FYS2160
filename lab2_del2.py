import matplotlib.pyplot as plt
import numpy as np


V = np.linspace(0.4, 50, 1000)
T = 0.5
#plt.axhline(y=-5.25, color='r', linestyle='-')
#T= 1, 0.9, 0.8, 0.7, 0.6, 0.5
P = (8*T/(3*V-1)) - (3/(V**2))
G = (-8/3)*T*np.log(3*V-1)-3/V + P*V

"""
plt.plot(V, G)
plt.xlabel('V')
plt.ylabel('G')
plt.show()


plt.plot(P, G)
plt.xlabel('P')
plt.ylabel('G')
plt.show()

plt.plot(P, V)
plt.xlabel('P')
plt.ylabel('V')
plt.show()
"""

#plotting regression:
data = np.array([
    [0.95, 0.81],
    [0.9, 0.647],
    [0.8, 0.383],
    [0.7, 0.198],
    [0.6, 0.087],
    [0.5, 0.028],])
x, y = data.T
#plt.scatter(x,y)
#plt.title('P vs T')

func = np.polyfit(x, np.log(y), 3)
x = np.linspace(0.5, 0.95, 100)
#plt.plot(x, np.exp(func[0]*x**3 + x**2*func[1] + x*func[2] + func[3]))
#plt.xlabel('T')
#plt.ylabel('P')
#plt.show()


#saving the y points 
y = np.exp(func[0]*x**3 + x**2*func[1] + x*func[2] + func[3])
y_grad = np.gradient(y)
#plt.plot(x, y_grad)
#plt.show()



#data for t vs dV
data_tv = np.array([
    [0.95, 1.05],
    [0.9, 1.75],
    [0.8, 3.62],
    [0.7, 7.29],
    [0.6, 16.2],
    [0.5, 41.9],])
x1, y1 = data_tv.T   
func1 = np.polyfit(x1, np.log(y1), 3)
plt.plot(x, np.exp(func1[0]*x**3 + x**2*func1[1] + x*func1[2] + func1[3]))

plt.scatter(x1,y1)
plt.title('dV vs T')
plt.show()

H = y_grad*x*np.exp(func1[0]*x**3 + x**2*func1[1] + x*func1[2] + func1[3])

plt.plot(x, H/x )
plt.title('relation')
plt.ylabel('H/x')
plt.xlabel('x')
plt.show()

