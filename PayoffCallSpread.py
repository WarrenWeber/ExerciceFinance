import matplotlib.pyplot as plt

k1 = 2
k2 = 6
x2 = [a for a in range(15)]
y2 = [max(0,b-k1) - max(0,b-k2) for b in range (15)]
plt.xlabel(r'$S_t$')
plt.ylabel("Payoff")
plt.plot(x2,y2)
plt.show()