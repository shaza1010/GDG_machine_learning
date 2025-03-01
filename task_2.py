import pandas as pd
import numpy as np

# Load the data from the user to a DataFrame
file_name = input("What's the name of the file?(csv files only) ")
df = pd.read_csv(file_name, index_col="TransactionID")
print("Data loading ...")

print(f"Data loaded!")

# Calculate the total revenue, average sale, highest sale, lowest sale, best selling product
transaction_price = df["UnitPrice"] * df["Quantity"]

total_revenue = np.sum(transaction_price)
average_sale = np.mean(transaction_price)
highest_sale = np.max(transaction_price)
lowest_sale = np.min(transaction_price)

highest_selling_product = df.loc[transaction_price.idxmax(), 'Product']
lowest_selling_product = df.loc[transaction_price.idxmin(), 'Product']
best_selling_product = df.groupby("Product")["Quantity"].sum().idxmax()

# Display the Retail Sales Report
print("\nRetail Sales Report")
print("----------------------------\n")
print(f"Total transactions: {len(df)}")
print(f"Total Revenue: ${total_revenue:,}")
print(f"Average Sale: ${average_sale:,}")
print(f"Highest Sale: ${highest_sale:,} (Product: {highest_selling_product})")
print(f"Lowest Sale: ${lowest_sale:,} (Product: {lowest_selling_product})")
print(f"Best-Selling Product: {best_selling_product}")

print("----------------------------------------- \n")
