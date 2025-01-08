#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Step 1: Prepare the Initial Dataset
data = {
    'Gender': ['male', 'male', 'male', 'male', 'female', 'female', 'female', 'female'],
    'Height': [6.00, 5.92, 5.58, 5.92, 5.00, 5.50, 5.42, 5.75],
    'Weight': [180, 190, 170, 165, 100, 150, 130, 150],
    'Foot Size': [12, 11, 12, 10, 6, 8, 7, 9]
}

df = pd.DataFrame(data)

# Step 2: Take New Entry from the User
def get_user_input():
    print("Please enter the following details:")
    height = float(input("Height (in feet): "))
    weight = float(input("Weight (in pounds): "))
    foot_size = float(input("Foot Size (in inches): "))
    return [height, weight, foot_size]

# Get the new entry from the user
new_entry = get_user_input()

# Step 3: Add the New Entry to the Dataset (with unknown gender for now)
# We'll add the new entry with a placeholder gender (e.g., 'unknown')
df.loc[len(df)] = ['unknown'] + new_entry

# Step 4: Split the Data into Features and Target
X = df[['Height', 'Weight', 'Foot Size']]
y = df['Gender']

# Step 5: Train the Decision Tree on the Updated Dataset
clf = DecisionTreeClassifier()
clf.fit(X[:-1], y[:-1])  # Train on all rows except the last one (new entry)

# Step 6: Predict the Gender for the New Entry
predicted_gender = clf.predict([new_entry])
print(f"Predicted Gender for the new entry: {predicted_gender[0]}")

# Step 7: Update the Dataset with the Predicted Gender
df.at[len(df) - 1, 'Gender'] = predicted_gender[0]

# Step 8: Display the Updated Dataset
print("\nUpdated Dataset with the New Entry:")
print(df)


# In[ ]:




