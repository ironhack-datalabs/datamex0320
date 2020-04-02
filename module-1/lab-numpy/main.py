#1. Import the NUMPY package under the name np.

import numpy as np

#2. Print the NUMPY version and the configuration.

print(np.version.version)


#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?
a=np.random.rand(2,3,5)
a=np.random.random((2,3,5))



#4. Print a.
[[[0.08222657 0.6899152  0.7167361  0.20353577 0.33726667]
  [0.00738315 0.02048562 0.22148889 0.15048683 0.85248741]
  [0.99355918 0.31644372 0.25076353 0.79936183 0.80276036]]

 [[0.14433729 0.10686889 0.78151136 0.30892063 0.53684239]
  [0.49399908 0.83086821 0.94733729 0.27875296 0.58153518]
  [0.3408575  0.4660762  0.79457244 0.77847571 0.70589535]]]

#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"
b=np.ones((5,3,2))


#6. Print b.
[[[1. 1.]
  [1. 1.]
  [1. 1.]]

 [[1. 1.]
  [1. 1.]
  [1. 1.]]

 [[1. 1.]
  [1. 1.]
  [1. 1.]]

 [[1. 1.]
  [1. 1.]
  [1. 1.]]

 [[1. 1.]
  [1. 1.]
  [1. 1.]]]


#7. Do a and b have the same size? How do you prove that in Python code?

print(a.size - b.size)
0

#8. Are you able to add a and b? Why or why not?

#No, because they do not have the same structure. 
new_array = a.__add__(b)
ValueError: operands could not be broadcast together with shapes (2,3,5) (5,2,3) 


#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".
c=b.T
c.shape
(2, 3, 5)
#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?

#it does work now because they both have the same shapes
d=a.__add__(c)
print(d)

[[[1.08222657 1.6899152  1.7167361  1.20353577 1.33726667]
  [1.00738315 1.02048562 1.22148889 1.15048683 1.85248741]
  [1.99355918 1.31644372 1.25076353 1.79936183 1.80276036]]

 [[1.14433729 1.10686889 1.78151136 1.30892063 1.53684239]
  [1.49399908 1.83086821 1.94733729 1.27875296 1.58153518]
  [1.3408575  1.4660762  1.79457244 1.77847571 1.70589535]]]

#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.

#d has the same structure as a but with every value increased by 1.

[[[0.08222657 0.6899152  0.7167361  0.20353577 0.33726667]
  [0.00738315 0.02048562 0.22148889 0.15048683 0.85248741]
  [0.99355918 0.31644372 0.25076353 0.79936183 0.80276036]]

 [[0.14433729 0.10686889 0.78151136 0.30892063 0.53684239]
  [0.49399908 0.83086821 0.94733729 0.27875296 0.58153518]
  [0.3408575  0.4660762  0.79457244 0.77847571 0.70589535]]]

[[[1.08222657 1.6899152  1.7167361  1.20353577 1.33726667]
  [1.00738315 1.02048562 1.22148889 1.15048683 1.85248741]
  [1.99355918 1.31644372 1.25076353 1.79936183 1.80276036]]

 [[1.14433729 1.10686889 1.78151136 1.30892063 1.53684239]
  [1.49399908 1.83086821 1.94733729 1.27875296 1.58153518]
  [1.3408575  1.4660762  1.79457244 1.77847571 1.70589535]]]



#12. Multiply a and c. Assign the result to e.
e=np.multiply(a,c)
print(e)

#matmul wouldn't work in thsi case because we are multiplying a 3 dimension vector. 

#13. Does e equal to a? Why or why not?

#Yes, they do, because we the only thing we did was multiplying every element by 1. 



#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"
d_mean=d.mean()
d_min=d.min()
d_max=d.max()

#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.
f=np.empty((2,3,5))



"""
#16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
If a value equals to d_mean, assign 50 to the corresponding value in f.
Assign 0 to the corresponding value(s) in f for d_min in d.
Assign 100 to the corresponding value(s) in f for d_max in d.
In the end, f should have only the following values: 0, 25, 50, 75, and 100.
Note: you don't have to use Numpy in this question.
"""

for x in range(2):
    for y in range(3):
        for z in range(5):
            if d[x,y,z] > d_min and d[x,y,z] < d_mean:
                f[x,y,z]=25
            elif d[x,y,z] >d_mean and d[x,y,z] < d_max:
                f[x,y,z]=75
            elif d[x,y,z] == d_mean:
                f[x,y,z]=50
            elif d[x,y,z] == d_max:
                f[x,y,z]=100
            elif d[x,y,z]== d_min:
                f[x,y,z]==0



"""
#17. Print d and f. Do you have your expected f?
For instance, if your d is:
array([[[1.85836099, 1.67064465, 1.62576044, 1.40243961, 1.88454931],
        [1.75354326, 1.69403643, 1.36729252, 1.61415071, 1.12104981],
        [1.72201435, 1.1862918 , 1.87078449, 1.7726778 , 1.88180042]],
       [[1.44747908, 1.31673383, 1.02000951, 1.52218947, 1.97066381],
        [1.79129243, 1.74983003, 1.96028037, 1.85166831, 1.65450881],
        [1.18068344, 1.9587381 , 1.00656599, 1.93402165, 1.73514584]]])
Your f should be:
array([[[ 75.,  75.,  75.,  25.,  75.],
        [ 75.,  75.,  25.,  25.,  25.],
        [ 75.,  25.,  75.,  75.,  75.]],
       [[ 25.,  25.,  25.,  25., 100.],
        [ 75.,  75.,  75.,  75.,  75.],
        [ 25.,  75.,   0.,  75.,  75.]]])
"""

print(d)
[[[1.08222657 1.6899152  1.7167361  1.20353577 1.33726667]
  [1.00738315 1.02048562 1.22148889 1.15048683 1.85248741]
  [1.99355918 1.31644372 1.25076353 1.79936183 1.80276036]]

 [[1.14433729 1.10686889 1.78151136 1.30892063 1.53684239]
  [1.49399908 1.83086821 1.94733729 1.27875296 1.58153518]
  [1.3408575  1.4660762  1.79457244 1.77847571 1.70589535]]]

  print(f.astype(int))
[[[ 25  75  75  25  25]
  [  0  25  25  25  75]
  [100  25  25  75  75]]

 [[ 25  25  75  25  75]
  [ 75  75  75  25  75]
  [ 25  25  75  75  75]]]

"""
#18. Bonus question: instead of using numbers (i.e. 0, 25, 50, 75, and 100), how to use string values 
("A", "B", "C", "D", and "E") to label the array elements? You are expecting the result to be:
array([[[ 'D',  'D',  'D',  'B',  'D'],
        [ 'D',  'D',  'B',  'B',  'B'],
        [ 'D',  'B',  'D',  'D',  'D']],
       [[ 'B',  'B',  'B',  'B',  'E'],
        [ 'D',  'D',  'D',  'D',  'D'],
        [ 'B',  'D',   'A',  'D', 'D']]])
Again, you don't need Numpy in this question.
"""

