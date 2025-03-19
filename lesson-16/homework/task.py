import pandas as pd

# Flights parquet file
flights_df = pd.read_parquet('data/flights/')
flights_df.to_csv('data/flights.csv', index=False)
print("\nFirst five rows of Flights dataset:")
print(flights_df.head())

# unique_destinations = flights_df['dest'].nunique()
# print("\nNumber of unique destinations:", unique_destinations)

# missing_values = flights_df.isnull().sum()
# print("\nMissing values in Flights dataset:")
# print(missing_values)

# numerical_columns = flights_df.select_dtypes(include=['float64', 'int64']).columns
# for col in numerical_columns:
#     if flights_df[col].isnull().any():
#         flights_df[col].fillna(flights_df[col].mean(), inplace=True)
# print("\nMissing values filled with column mean.")