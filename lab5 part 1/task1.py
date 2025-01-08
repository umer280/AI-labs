#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Step 1: Prepare the Data
data = {
    'Gender': ['male', 'male', 'male', 'male', 'female', 'female', 'female', 'female'],
    'Height': [6.00, 5.92, 5.58, 5.92, 5.00, 5.50, 5.42, 5.75],
    'Weight': [180, 190, 170, 165, 100, 150, 130, 150],
    'Foot Size': [12, 11, 12, 10, 6, 8, 7, 9]
}

df = pd.DataFrame(data)

# Step 2: Split the Data into Features and Target
X = df[['Height', 'Weight', 'Foot Size']]
y = df['Gender']

# Step 3: Create and Train the Decision Tree Classifier
clf = DecisionTreeClassifier()
clf.fit(X, y)  # Train on the entire dataset

# Step 4: Take New Entry from the User
def get_user_input():
    print("Please enter the following details:")
    height = float(input("Height (in feet): "))
    weight = float(input("Weight (in pounds): "))
    foot_size = float(input("Foot Size (in inches): "))
    return [height, weight, foot_size]

# Get the new entry from the user
new_entry = get_user_input()

# Step 5: Make Prediction for the New Entry
prediction = clf.predict([new_entry])
print(f"Predicted Gender: {prediction[0]}")


# In[ ]:




