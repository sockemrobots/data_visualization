import matplotlib.pyplot as plt 

from random_walk import RandomWalk

#keep making points as long as the program is active 
while True:
    rw = RandomWalk(50000)
    rw.fill_walk()

    #set the size of the plotting window 
    plt.figure(figsize=(10, 6))
    
    plt.scatter(rw.x_values, rw.y_values, s=15)
    plt.show()

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=1)

    #emphasize the first and last points 
    plt.scatter(0, 0, c= 'green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    #remove the axes
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    keep_running = raw_input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break 

