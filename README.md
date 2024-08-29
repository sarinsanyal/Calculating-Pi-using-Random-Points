# Calculating-Pi-using-Random-Points.
This Project attempts to calculate the value of Pi (as accurately as possible) by using random points that fall on a quarter circle and a square.

I first encountered this question on a YouTube video posted by Jonathan Ma. The question was absurd (at first) but pretty captivating.

"Given a random() function, that generates any number between 0 and 1 (both inclusive), calculate the value of Pi."
It is absurd.

But, the problem becomes pretty easy, once we know where to apply this random function. And how. 

We can plot a square on the First Quadrant of an R2 area with a side length = 1. Then, we draw a quarter circle which has the same radius as the side.

Now, when we plot random points inside the space of (1.0, 1.0) and origin. IF the point has a distance from the origin inside the quarter circle (i.e. less than 1) we can surely add it to an inside counter.
ELSE, it goes to an outside counter.

We iterate this thing as many times as the user inputs, and then with a large number of points the sum of all these points becomes almost equal to the area od the respective spaces. Divide the area suitably, and then we have the value of Pi.

Pretty interesting isn't it?

