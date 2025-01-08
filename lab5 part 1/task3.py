#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from sklearn.tree import DecisionTreeClassifier

# Step 1: Prepare the Dataset using NumPy
# Data from Table 1
data = np.array([
    ['male', 6.00, 180, 12],
    ['male', 5.92, 190, 11],
    ['male', 5.58, 170, 12],
    ['male', 5.92, 165, 10],
    ['female', 5.00, 100, 6],
    ['female', 5.50, 150, 8],
    ['female', 5.42, 130, 7],
    ['female', 5.75, 150, 9]
])

# Separate features (Height, Weight, Foot Size) and target (Gender)
X = data[:, 1:].astype(float)  # Features (Height, Weight, Foot Size)
y = data[:, 0]  # Target (Gender)

# Step 2: Train the Decision Tree Classifier
clf = DecisionTreeClassifier()
clf.fit(X, y)  # Train the model on the entire dataset

# Step 3: Take New Entry from the User
def get_user_input():
    print("Please enter the following details:")
    height = float(input("Height (in feet): "))
    weight = float(input("Weight (in pounds): "))
    foot_size = float(input("Foot Size (in inches): "))
    return np.array([height, weight, foot_size])

# Get the new entry from the user
new_entry = get_user_input()

# Step 4: Predict the Gender for the New Entry
predicted_gender = clf.predict([new_entry])
print(f"Predicted Gender: {predicted_gender[0]}")

# Step 5: Add the New Entry to the Dataset
# Append the new entry to the existing dataset
new_entry_with_gender = np.append(predicted_gender, new_entry)
data = np.vstack([data, new_entry_with_gender])

# Step 6: Display the Updated Dataset
print("\nUpdated Dataset with the New Entry:")
print(data)


# In[ ]:




