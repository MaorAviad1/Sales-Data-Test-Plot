import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Data Cleaning
# Remove dollar signs and commas from the 'Sum of sales Since Jan 2020', 'Price', and 'Profit per Unit' columns, and convert them to float
data['Sum of sales Since Jan 2020'] = data['Sum of sales Since Jan 2020'].replace('[\$,]', '', regex=True).astype(float)
data['Price'] = data['Price'].replace('[\$,]', '', regex=True).astype(float)
data['Profit per Unit'] = data['Profit per Unit'].replace('[\$,]', '', regex=True).astype(float)

# Remove percent sign from 'Return %' and convert it to float
data['Return %'] = data['Return %'].replace('[\%,]', '', regex=True).astype(float)

# Create a summary inventory column
data['Total Inventory'] = data['FBA Inventory'] + data['FBM Inventory'] + data['3pl Inventory'] + data['Warehouse Inventory']

# Remove dollar signs and commas from 'Profit - last 12 months' and convert it to float
data['Profit - last 12 months'] = data['Profit - last 12 months'].replace('[\$,]', '', regex=True).astype(float)

# Analyze data

# 1. Look at the sales distribution among the products.
plt.figure(figsize=(12, 6))
sns.histplot(data=data, x="Sum of sales Since Jan 2020", bins=30, color='skyblue')
plt.title('Sales Distribution Among the Products')
plt.xlabel('Sales Since Jan 2020')
plt.ylabel('Count')
plt.show()

# 2. Compare the profit per unit of each product.
top_profit_products = data.nlargest(10, 'Profit per Unit')
plt.figure(figsize=(12, 6))
sns.barplot(data=top_profit_products, x='Product Name', y='Profit per Unit', palette='viridis')
plt.title('Top 10 Products by Profit per Unit')
plt.xlabel('Product Name')
plt.ylabel('Profit per Unit')
plt.xticks(rotation=45)
plt.show()

# 3. Visualize the inventory distribution across different types (FBA, FBM, 3pl, Warehouse).
inventory_types = ['FBA Inventory', 'FBM Inventory', '3pl Inventory', 'Warehouse Inventory']
inventory_sum = [data[type].sum() for type in inventory_types]

plt.figure(figsize=(12, 6))
plt.bar(inventory_types, inventory_sum, color=['#5cb85c','#5bc0de','#d9534f','#f0ad4e'])
plt.title('Inventory Distribution Across Different Types')
plt.xlabel('Inventory Type')
plt.ylabel('Total Inventory')
plt.show()

# 4. Perform an analysis on the relationship between price and sales.
plt.figure(figsize=(12, 6))
sns.scatterplot(data=data, x='Price', y='Sum of sales Since Jan 2020', color='purple')
plt.title('Relationship Between Price and Sales')
plt.xlabel('Price')
plt.ylabel('Sales Since Jan 2020')
plt.show()

# 5. Investigate how profit has changed over the last 12 months for each product.
# For this, we need the data for each month in the last 12 months, but we only have the total profit for the last 12 months.
# Hence, we are unable to create a graph showing how profit has changed over the last 12 months for each product with the current data.

# Replace "#DIV/0!" with NaN
data.replace("#DIV/0!", np.nan, inplace=True)

# Convert 'Price', 'Profit per Unit', 'Sum of sales Since Jan 2020', 'Profit - last 12 months' to float again
data['Sum of sales Since Jan 2020'] = data['Sum of sales Since Jan 2020'].astype(float)
data['Price'] = data['Price'].astype(float)
data['Profit per Unit'] = data['Profit per Unit'].astype(float)
data['Profit - last 12 months'] = data['Profit - last 12 months'].astype(float)

# Analyze data

# 1. Look at the sales distribution among the products.
plt.figure(figsize=(12, 6))
sns.histplot(data=data, x="Sum of sales Since Jan 2020", bins=30, color='skyblue')
plt.title('Sales Distribution Among the Products')
plt.xlabel('Sales Since Jan 2020')
plt.ylabel('Count')
plt.show()

# 2. Compare the profit per unit of each product.
top_profit_products = data.nlargest(10, 'Profit per Unit')
plt.figure(figsize=(12, 6))
sns.barplot(data=top_profit_products, x='Product Name', y='Profit per Unit', palette='viridis')
plt.title('Top 10 Products by Profit per Unit')
plt.xlabel('Product Name')
plt.ylabel('Profit per Unit')
plt.xticks(rotation=45)
plt.show()

# 3. Visualize the inventory distribution across different types (FBA, FBM, 3pl, Warehouse).
inventory_types = ['FBA Inventory', 'FBM Inventory', '3pl Inventory', 'Warehouse Inventory']
inventory_sum = [data[type].sum() for type in inventory_types]

plt.figure(figsize=(12, 6))
plt.bar(inventory_types, inventory_sum, color=['#5cb85c','#5bc0de','#d9534f','#f0ad4e'])
plt.title('Inventory Distribution Across Different Types')
plt.xlabel('Inventory Type')
plt.ylabel('Total Inventory')
plt.show()

# 4. Perform an analysis on the relationship between price and sales.
plt.figure(figsize=(12, 6))
sns.scatterplot(data=data, x='Price', y='Sum of sales Since Jan 2020', color='purple')
plt.title('Relationship Between Price and Sales')
plt.xlabel('Price')
plt.ylabel('Sales Since Jan 2020')
plt.show()

# 5. Investigate how profit has changed over the last 12 months for each product.
# For this, we need the data for each month in the last 12 months, but we only have the total profit for the last 12 months.
# Hence, we are unable to create a graph showing how profit has changed over the last 12 months for each product with the current data.


# Convert 'Price', 'Profit per Unit', 'Sum of sales Since Jan 2020', 'Profit - last 12 months' to float again
data['Sum of sales Since Jan 2020'] = data['Sum of sales Since Jan 2020'].replace('[\$,]', '', regex=True).astype(float)
data['Price'] = data['Price'].replace('[\$,]', '', regex=True).astype(float)
data['Profit per Unit'] = data['Profit per Unit'].replace('[\$,]', '', regex=True).astype(float)
data['Profit - last 12 months'] = data['Profit - last 12 months'].replace('[\$,]', '', regex=True).astype(float)

# Analyze data

# 1. Look at the sales distribution among the products.
plt.figure(figsize=(12, 6))
sns.histplot(data=data, x="Sum of sales Since Jan 2020", bins=30, color='skyblue')
plt.title('Sales Distribution Among the Products')
plt.xlabel('Sales Since Jan 2020')
plt.ylabel('Count')
plt.show()

# 2. Compare the profit per unit of each product.
top_profit_products = data.nlargest(10, 'Profit per Unit')
plt.figure(figsize=(12, 6))
sns.barplot(data=top_profit_products, x='Product Name', y='Profit per Unit', palette='viridis')
plt.title('Top 10 Products by Profit per Unit')
plt.xlabel('Product Name')
plt.ylabel('Profit per Unit')
plt.xticks(rotation=45)
plt.show()

# 3. Visualize the inventory distribution across different types (FBA, FBM, 3pl, Warehouse).
inventory_types = ['FBA Inventory', 'FBM Inventory', '3pl Inventory', 'Warehouse Inventory']
inventory_sum = [data[type].sum() for type in inventory_types]

plt.figure(figsize=(12, 6))
plt.bar(inventory_types, inventory_sum, color=['#5cb85c','#5bc0de','#d9534f','#f0ad4e'])
plt.title('Inventory Distribution Across Different Types')
plt.xlabel('Inventory Type')
plt.ylabel('Total Inventory')
plt.show()

# 4. Perform an analysis on the relationship between price and sales.
plt.figure(figsize=(12, 6))
sns.scatterplot(data=data, x='Price', y='Sum of sales Since Jan 2020', color='purple')
plt.title('Relationship Between Price and Sales')
plt.xlabel('Price')
plt.ylabel('Sales Since Jan 2020')
plt.show()

# 5. Investigate how profit has changed over the last 12 months for each product.
# For this, we need the data for each month in the last 12 months, but we only have the total profit for the last 12 months.
# Hence, we are unable to create a graph showing how profit has changed over the last 12 months for each product with the current data.
