#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Step 1: Import Libraries and Load Data
import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

# Load the dataset
df = pd.read_excel('Online_Retail.xlsx')

# Display the first few rows of the dataset
print("Step 1: First few rows of the dataset")
print(df.head())

# Step 2: Data Cleanup
# Remove spaces from descriptions
df['Description'] = df['Description'].str.strip()

# Drop rows without invoice numbers
df.dropna(axis=0, subset=['InvoiceNo'], inplace=True)

# Convert InvoiceNo to string and remove credit transactions
df['InvoiceNo'] = df['InvoiceNo'].astype('str')
df = df[~df['InvoiceNo'].str.contains('C')]

# Display the cleaned dataframe
print("\nStep 2: Cleaned dataframe")
print(df)

# Step 3: Consolidate Items into Transactions
# Consolidate items into transactions for France
basket = (df[df['Country'] == "France"]
          .groupby(['InvoiceNo', 'Description'])['Quantity']
          .sum().unstack().reset_index().fillna(0)
          .set_index('InvoiceNo'))

# Display the basket
print("\nStep 3: Consolidated transactions for France")
print(basket)

# Step 4: Encode the Data
# Encode the units
def encode_units(x):
    if x <= 0:
        return 0
    if x >= 1:
        return 1

# Apply the encoding function
basket_sets = basket.applymap(encode_units)

# Drop the POSTAGE column (if it exists)
basket_sets.drop('POSTAGE', inplace=True, axis=1)

# Display the encoded basket
print("\nStep 4: Encoded basket")
print(basket_sets)

# Step 5: Generate Frequent Itemsets and Association Rules
# Generate frequent itemsets with a minimum support of 5%
frequent_itemsets = apriori(basket_sets, min_support=0.05, use_colnames=True)

# Generate association rules
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)

# Display the frequent itemsets
print("\nStep 5: Frequent itemsets with support >= 5%")
print(frequent_itemsets)

# Display the association rules
print("\nAssociation rules")
print(rules.head())

