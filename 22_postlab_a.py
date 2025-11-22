
import pandas as pd
import numpy as np
data = {
    'TransactionID': [1001, 1002, 1003, 1004, 1005],
    'ProductCategory': ['Electronics', 'Books', 'Apparel', 'Books', 'Electronics'],
    'Price': [499.99, 12.50, 75.00, 22.95, 1200.00],
    'UnitsSold': [5, 20, np.nan, 8, 3],  # Introduced a missing value here
    'OrderDate': ['2023-10-01', '2023-10-02', '2023-10-01', '2023-10-03', '2023-10-04'],
    'IsDiscounted': [True, False, True, False, True]
}

df = pd.DataFrame(data)

print("--- DataFrame Head with Missing Value (Row Index 2) ---")
print(df.head())
print("\n" + "="*50 + "\n")
print("--- Column Data Types ---")
print(df.dtypes)
print("\n" + "="*50 + "\n")

