import random
import matplotlib.pyplot as plt
import numpy as np

# Code for the NumPy array which stores [x, y] as coordinates
coordinates = np.empty((0, 2))

def append_coordinate(coords, x, y):
    return np.append(coords, np.array([[x, y]]), axis=0)

# Calculating the Function
def CalculateValueOfPi(n):
    insideCircle = 0
    outsideCircle = 0
    global coordinates  # Declare the use of the global variable
    for i in range(n):    
        x = random.random()
        y = random.random()

        # Distance of (x, y) from origin
        dist = (x**2 + y**2)**0.5
        if dist <= 1:
            insideCircle += 1
        else:
            outsideCircle += 1
        
        # Update the coordinates array with new points
        coordinates = append_coordinate(coordinates, x, y)

    return (insideCircle / (outsideCircle + insideCircle)) * 4

n = int(input("Enter number of iterations to perform on this randomised calculation: "))
answer = CalculateValueOfPi(n)

# Matplotlib code
radius = 1

theta = np.linspace(0, np.pi/2, 100)
x_circle = radius * np.cos(theta)
y_circle = radius * np.sin(theta)

square_x = [0, radius, radius, 0, 0]
square_y = [0, 0, radius, radius, 0]

plt.plot(x_circle, y_circle, label='Quarter Circle', color = "red")
plt.plot(square_x, square_y, label='Square', color = "yellow")

plt.axis('equal')
plt.grid(True)
 
x_scatter = coordinates[:, 0]
y_scatter = coordinates[:, 1]

plt.scatter(x_scatter, y_scatter, s = 10) #s makes the points thinner

plt.text(1.0,0.2, f"The calculated value of pi is: {answer:.5f}", fontsize=12, color='red')

plt.title(f'Calculating the value of pi based on random points (n = {n}) falling.')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.legend()
plt.show()
