#!/usr/bin/env python
# coding: utf-8

# #1. Import the NUMPY package under the name np.

# In[1]:


import numpy as np


# #2. Print the NUMPY version and the configuration.

# In[2]:


print(np.__version__)


# #3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# # Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?

# In[3]:


a=np.random.random((2,3,5))
b=np.random.randint(1, size=10)
c=np.random.rand(3,2)
print(a)
print(b)
print(c)


# #4. Print a.

# In[4]:


print(a)


# #5. Create a 5x2x3 3-dimensional array with all values equaling 1.
# #Assign the array to variable "b"

# In[5]:


b=np.full((5, 2, 3),1)


# #6. Print b.

# In[6]:


print(b)


# #7. Do a and b have the same size? How do you prove that in Python code?

# In[7]:


a.shape == b.shape


# In[8]:


#They don't have the same size as their dimensions are different.


# #8. Are you able to add a and b? Why or why not?

# In[9]:


a+b


# In[10]:


#It is not possible as they have difference dimmensions


# #9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".

# In[11]:


print(a)
c = b.reshape(2,3,5)


# #10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?

# In[12]:


d=a+c #Because they have the same dimensions now


# #11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.

# In[13]:


print(a)


# In[14]:


print(d)


# In[15]:


# The d array has all the values of a plus 1


# #12. Multiply a and c. Assign the result to e.

# In[16]:


e= a*c
print(e)


# #13. Does e equal to a? Why or why not?

# In[17]:


e.shape == a.shape #because they have the same dimension 


# #14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"

# In[21]:


d_max =d.max()
d_min =d.min()
d_mean = d.mean()
print(d_max)
print(d_min)
print(d_mean)


# #15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.

# In[27]:


f=np.empty([2,3,5])
print(f)


# #16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
# If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
# If a value equals to d_mean, assign 50 to the corresponding value in f.
# Assign 0 to the corresponding value(s) in f for d_min in d.
# Assign 100 to the corresponding value(s) in f for d_max in d.
# In the end, f should have only the following values: 0, 25, 50, 75, and 100.
# Note: you don't have to use Numpy in this question.

# In[28]:


for x in range(2):
        for z in range(3):
                for y in range (5):
                        if d[x,z,y]> d_min and d[x,z,y] < d_mean:
                                f [x,z,y]= 25
                        elif d[x,z,y] > d_mean and d[x,z,y] < d_max:
                                f[x,z,y] =75
                        elif d[x,z,y]==d_min:
                                f[x,z,y]=0
                        elif d[x,z,y]==d_max:
                                f[x,z,y]= 100
                        elif d[x,z,y]==d_mean:
                                f [x,z,y]=50 
   


# #17. Print d and f. Do you have your expected f?
# For instance, if your d is:
# 
# array([[[1.85836099, 1.67064465, 1.62576044, 1.40243961, 1.88454931],
#         [1.75354326, 1.69403643, 1.36729252, 1.61415071, 1.12104981],
#         [1.72201435, 1.1862918 , 1.87078449, 1.7726778 , 1.88180042]],
# 
#        [[1.44747908, 1.31673383, 1.02000951, 1.52218947, 1.97066381],
#         [1.79129243, 1.74983003, 1.96028037, 1.85166831, 1.65450881],
#         [1.18068344, 1.9587381 , 1.00656599, 1.93402165, 1.73514584]]])
# 
# Your f should be:
# array([[[ 75.,  75.,  75.,  25.,  75.],
#         [ 75.,  75.,  25.,  25.,  25.],
#         [ 75.,  25.,  75.,  75.,  75.]],
# 
#        [[ 25.,  25.,  25.,  25., 100.],
#         [ 75.,  75.,  75.,  75.,  75.],
#         [ 25.,  75.,   0.,  75.,  75.]]])

# In[29]:


print(d)
print(f)


# #18. Bonus question: instead of using numbers (i.e. 0, 25, 50, 75, and 100), how to use string values
# ("A", "B", "C", "D", and "E") to label the array elements? You are expecting the result to be:
# array([[[ 'D',  'D',  'D',  'B',  'D'],
#         [ 'D',  'D',  'B',  'B',  'B'],
#         [ 'D',  'B',  'D',  'D',  'D']],
# 
#        [[ 'B',  'B',  'B',  'B',  'E'],
#         [ 'D',  'D',  'D',  'D',  'D'],
#         [ 'B',  'D',   'A',  'D', 'D']]])
# Again, you don't need Numpy in this question.

# In[43]:


g = f.tolist()
for x in range(2):
        for z in range(3):
                for y in range (5):
                        if d[x,z,y]> d_min and d[x,z,y] < d_mean:
                                g [x][z][y] = 'A'
                        elif d[x,z,y] > d_mean and d[x,z,y] < d_max:
                                g[x][z][y]  = 'B'
                        elif d[x,z,y]==d_min:
                                g[x][z][y] = 'C'
                        elif d[x,z,y]==d_max:
                                g[x][z][y] = 'D'
                        elif d[x,z,y]==d_mean:
                                g[x][z][y] ='E' 
                                


# In[46]:


h=np.array(g)


# In[47]:


print(h)


# In[ ]:




