import matplotlib.pyplot as plt

k = 5
x = [a for a in range(15)]
y = [max(0,b-k) for b in range (15)]
plt.xlabel(r'$S_t$')
plt.ylabel("Payoff")
plt.plot(x,y)
plt.show()