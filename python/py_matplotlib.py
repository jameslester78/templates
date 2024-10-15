import matplotlib.pyplot as plt

#a simple line graph

x = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5]
y = [4.8, 5.5, 3.5, 4.6, 6.5, 6.6, 2.6, 3.0]

plt.plot(x,y)
plt.xlabel('x axis description')
plt.ylabel('y axis description')
plt.title('graph title')

plt.show()

plt.clf() #clear the graph

#a simple bar graph

bar_x = [1,2,3,4,5,6,7]
bar_y = [5,7,8,9,2,5,3]

plt.bar(bar_x,bar_y,color='red')
plt.title('a bar graph')

plt.show()


