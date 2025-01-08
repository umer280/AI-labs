#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
from sklearn.linear_model import LinearRegression

# Step 1: Prepare the Dataset
areas = np.array([2600, 3000, 3200, 3600, 4000]).reshape(-1, 1)
prices = np.array([550000, 565000, 610000, 680000, 725000])

# Step 2: Create and Train the Linear Regression Model
model = LinearRegression()
model.fit(areas, prices)

# Step 3: Predict Prices for Areas in the Dataset
predicted_prices = model.predict(areas)

# Step 4: Display the Results
for area, price in zip(areas, predicted_prices):
    print(f"Area: {area[0]} sqr ft, Predicted Price: ${price:.2f}")


# In[ ]:




