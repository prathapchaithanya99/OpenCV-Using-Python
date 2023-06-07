#!/usr/bin/env python
# coding: utf-8

# In[1]:


#pylint:disable=no-member

import cv2 as cv 


# In[2]:


# Read in an image
img = cv.imread('Desktop/PRATHAP_PHOTO.jpg')
cv.imshow('Prathap', img)

#Output
cv.waitKey(0)


# In[3]:


# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#Output
cv.waitKey(0)


# In[4]:


# Blur 
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

#Output
cv.waitKey(0)


# In[5]:


# Edge Cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

#Output
cv.waitKey(0)


# In[7]:


# Dilating the image
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('Dilated', dilated)

#Output
cv.waitKey(0)


# In[8]:


# Eroding
eroded = cv.erode(dilated, (7,7), iterations=3)
cv.imshow('Eroded', eroded)

#Output
cv.waitKey(0)


# In[9]:


# Resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

#Output
cv.waitKey(0)


# In[ ]:




