import matplotlib.pyplot as plt
x = range(1,21)
plt.xlabel('1st X')
plt.ylabel('1st Y')
plt.plot(x,x,'r') # against 1st x, 1st y
plt.axis([0,50,0,25])
plt.twinx()
plt.ylabel('2nd Y')
plt.plot(x,x,'g') # against 1st x, 2nd y
plt.axis([0,50,0,20])
plt.twiny()
plt.xlabel('2nd X')
plt.plot(x,x,'b') # against 2nd x, 2nd y
plt.axis([0,10,0,20])
plt.show()
