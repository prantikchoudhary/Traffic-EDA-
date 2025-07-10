# Available Intersections
# 1. Dorchester Road and Huron Church Road
# 2. Totten Street and Huron Church Road
# 3. Malden Road and Huron Church Road

# Importing libraries
import pandas as pd

# Construct the String for the API call
intersection=input("Enter Intersection #:")
date=input("Enter Date(YYYY-MM-DD):")

url="https://opendata.citywindsor.ca/api/traffic?date="+str(date)+"&intersectionId="+str(intersection)+"&start_time=00:00&end_time=23:59"
print(url)

df=pd.read_json(url)
# pulls the data from the url and stores it as a dafatframe using Pandas library

print(df)

# Use Normalize to flatten the JSON attribute to Tabular form
from pandas import json_normalize  # Import directly from pandas instead of pandas.io.json
# Alternatively, you could use: import pandas as pd (if you haven't already)
# and then use pd.json_normalize()

df = json_normalize(df['traffic'])
print(df)

df.vehicleType.unique() # To check how many unique vehicles are present 
df.timeStamp.dtypes
df['timeStamp']=pd.to_datetime(df['timeStamp']) # converting the timestamps to ISO timestamps
df.head(3)
print(df)

print(df.qty.sum()) # Prints the total traffic for the day

df.groupby('vehicleType')['qty'].sum().sort_values(ascending=False) # Prints the quantity of each vehicle 

# Load matplotlib library
import matplotlib.pyplot as plt

# Bar Plot for sum of all types of vehicles
df.groupby('vehicleType')['qty'].sum().plot(kind='bar')

# Per Minute Traffic
df.plot(kind='line',x='timeStamp',y='qty',color='orange')
plt.ylabel('Number of Vehicles')
plt.xlabel('Date and Time')
plt.show()

# Per 4h Trafffic
df.groupby(pd.Grouper(key='timeStamp',axis=0, freq='4h', sort=True)).sum().plot(kind='line')
plt.show()

# Create a 4 hour list of the type of vehicles that passes in those 4 hours
type_by_hour=df.groupby([pd.Grouper(key='timeStamp',freq='4h'), 'vehicleType']).qty.sum()
print(type_by_hour)

# Dropping the column 'isDaylightSavingsTime' since its not required in our Correlation Analysis
df=df.drop(columns=['isDaylightSavingsTime'])

print(df)

# Creating the column based on larger vehicle and updating the dataframe
df['is_large_vehicle'] = df['vehicleType'].isin(['Articulated Truck', 'SingleUnitTruck', 'Bus'])

# Group by timestamp
# For hourly aggregation
hourly_data = df.groupby([pd.Grouper(key='timeStamp', freq='h')])['qty'].sum().reset_index(name='total_traffic')

# Group by large vehicle count 
# For hourly aggregation
large_vehicle_count = df[df['is_large_vehicle']].groupby(pd.Grouper(key='timeStamp', freq='h'))['qty'].sum().reset_index(name='large_vehicle_count')

# Merge the above two datasets
merged_data = pd.merge(hourly_data, large_vehicle_count, on='timeStamp', how='left')
merged_data['large_vehicle_count'] = merged_data['large_vehicle_count'].fillna(0)

# Calculate percentage of large vehicles
merged_data['large_vehicle_percentage'] = (merged_data['large_vehicle_count'] / merged_data['total_traffic']) * 100

# Calculating the coefficient of correlation
correlation = merged_data['large_vehicle_count'].corr(merged_data['total_traffic'])
print(f"Correlation between large vehicle count and total traffic: {correlation:.4f}")

# Creating the Visualizations
# Importing the required libraries
import matplotlib.pyplot as plt
import seaborn as sns

# Creating the ScatterPlot
plt.figure(figsize=(10, 6))
sns.scatterplot(x='large_vehicle_count', y='total_traffic', data=merged_data)
plt.title('Relationship between Large Vehicles and Total Traffic')
plt.xlabel('Number of Large Vehicles (Trucks & Buses)')
plt.ylabel('Total Traffic Volume')
plt.grid(True, alpha=0.3)

# Adding a TrendLine
sns.regplot(x='large_vehicle_count', y='total_traffic', data=merged_data, scatter=False, color='red')
plt.tight_layout()
plt.show()

# Plot total traffic
ax1 = plt.subplot(211)
plt.plot(merged_data['timeStamp'], merged_data['total_traffic'], label='Total Traffic')
plt.ylabel('Vehicle Count')
plt.legend()
plt.grid(True, alpha=0.3)

# Plot large vehicle count
ax2 = plt.subplot(212, sharex=ax1)
plt.plot(merged_data['timeStamp'], merged_data['large_vehicle_count'], color='green', label='Large Vehicles')
plt.xlabel('Time')
plt.ylabel('Vehicle Count')
plt.legend()
plt.grid(True, alpha=0.3)











