#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pylab as pl
import numpy as np
import matplotlib.pyplot as plt


# In[3]:


x = np.linspace(-2, 4, 50)
y = np.sin(x)
pl.plot(x, y)


# In[4]:


x = np.linspace(-5, 8, 100)
y = np.sin(x)
pl.plot(x, y)


# In[5]:


pl.plot(x, y)
pl.xlim(-2, 6)
pl.ylim(-0.75, 0.75)


# In[7]:


pl.plot(x, y)

pl.xlabel('this is x!')
pl.ylabel('this is y!')
pl.title('My First Plot')


# In[9]:


y = np.sin(2 * np.pi *x)
pl.plot(x, y)
pl.title(r'$\sin(2 \pi x)$')


# In[10]:


pl.plot(x, y, '-r') #solid red line ('r' comes from RGB color scheme)
pl.xlim(-2, 10)
pl.ylim(-0.75, 0.75)

pl.xlabel('this is x!')
pl.ylabel('this is y!')
pl.title('My Plot')


# In[11]:


pl.plot(x, y, '-c')


# In[12]:


get_ipython().run_line_magic('pinfo', 'pl.plot')


# In[13]:


x = np.linspace(0, 20, 1000)
y1 = np.sin(x)
y2 = np.cos(x)

pl.plot(x, y1, '-b', label = 'sine')
pl.plot(x, y2, '--r', label = 'cosine')
pl.legend(loc = 'upper right')
pl.ylim(-1.5, 2.0)


# In[16]:


x1 = np.linspace(0, 10, 20)
y1 = np.sin(x1)

x2 = np.linspace(0, 10, 1000)
y2 = np.sin(x2)


# In[20]:


pl.plot(x1, y1, 'go', label = 'sampled')
pl.plot(x2, y2, 'k:', label = 'continuous')
pl.legend()

pl.ylim(-1.5, 2.0)


# In[21]:


"""
Other options for the color characters are:

 'r' = red
 'g' = green
 'b' = blue
 'c' = cyan
 'm' = magenta
 'y' = yellow
 'k' = black
 'w' = white
 
 Options for line styles are

 '-' = solid
 '--' = dashed
 ':' = dotted
 '-.' = dot-dashed
 '.' = points
 'o' = filled circles
 '^' = filled triangles
"""


# In[ ]:




