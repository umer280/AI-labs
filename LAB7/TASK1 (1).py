#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

# Dictionary of student scores
data = {
    'Student': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Math': [85, 90, None, 78, 88],
    'Science': [92, None, 85, 80, None],
    'English': [78, 85, 90, None, 82]
}

# Create DataFrame
df = pd.DataFrame(data)

# Forward fill missing values
df_filled = df.ffill()

print("Original DataFrame:")
print(df)
print("\nDataFrame after Forward Fill:")
print(df_filled)


# In[2]:


from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error

# Example dataset
data = {
    'Math': [85, 90, 78, 88, 92, 80, 85, 78, 82, 95],
    'Science': [92, 85, 80, 88, 90, 78, 85, 82, 88, 92],
    'English': [78, 85, 90, 82, 88, 85, 80, 78, 85, 90],
    'Performance': [88, 92, 85, 90, 95, 82, 88, 85, 90, 96]
}

# Create DataFrame
df = pd.DataFrame(data)

# Features (X) and Target (y)
X = df[['Math', 'Science', 'English']]
y = df['Performance']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Decision Tree Regressor
model = DecisionTreeRegressor(random_state=42)
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")


# In[ ]:





# In[ ]:





# In[ ]:





# In[5]:


import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Example dataset
data = {
    'CreditScore': [700, 650, 800, 600, 750],
    'Income': [50000, 45000, 60000, 40000, 55000],
    'LoanAmount': [20000, 25000, 15000, 30000, 22000],
    'Risk': ['Low', 'High', 'Low', 'High', 'Low']
}

# Create DataFrame
df = pd.DataFrame(data)

# Features (X) and Target (y)
X = df[['CreditScore', 'Income', 'LoanAmount']].values  # Convert to NumPy array
y = df['Risk'].values  # Convert to NumPy array

# Train a KNN Classifier
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)

# Predict and evaluate
y_pred = model.predict(X)
accuracy = accuracy_score(y, y_pred)
print(f"Accuracy: {accuracy}")


# In[6]:


from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Example dataset
data = {
    'Email': [
        'Win a free iPhone now!',
        'Hi, can we schedule a meeting?',
        'Claim your prize today!',
        'Reminder: Project deadline tomorrow'
    ],
    'Label': ['spam', 'not spam', 'spam', 'not spam']
}

# Create DataFrame
df = pd.DataFrame(data)

# Convert text to features
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['Email'])
y = df['Label']

# Train a Naïve Bayes Classifier
model = MultinomialNB()
model.fit(X, y)

# Predict and evaluate
y_pred = model.predict(X)
accuracy = accuracy_score(y, y_pred)
print(f"Accuracy: {accuracy}")


# In[7]:


from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Example dataset
data = {
    'Symptom1': [1, 0, 1, 0, 1],
    'Symptom2': [0, 1, 0, 1, 0],
    'Symptom3': [1, 1, 0, 0, 1],
    'Disease': ['A', 'B', 'A', 'B', 'A']
}

# Create DataFrame
df = pd.DataFrame(data)

# Features (X) and Target (y)
X = df[['Symptom1', 'Symptom2', 'Symptom3']]
y = df['Disease']

# Train a Decision Tree Classifier
model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)

# Predict and evaluate
y_pred = model.predict(X)
accuracy = accuracy_score(y, y_pred)
print(f"Accuracy: {accuracy}")


# In[8]:


from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Example dataset
data = {
    'Size': [1200, 1500, 1800, 2000, 2200],
    'Rooms': [2, 3, 4, 3, 4],
    'Location': [1, 2, 3, 2, 1],
    'Price': [250000, 300000, 350000, 400000, 450000]
}

# Create DataFrame
df = pd.DataFrame(data)

# Features (X) and Target (y)
X = df[['Size', 'Rooms', 'Location']]
y = df['Price']

# Train a Linear Regression model
model = LinearRegression()
model.fit(X, y)

# Predict and evaluate
y_pred = model.predict(X)
mse = mean_squared_error(y, y_pred)
print(f"Mean Squared Error: {mse}")


# In[ ]:




