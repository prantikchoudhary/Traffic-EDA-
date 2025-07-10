# Time Series Analysis of ongoing traffic between 3 junctions in Windsor (Correlation of larger vehicles and traffic congestion)

API Used : /api/traffic at **https://opendata.citywindsor.ca/swagger/index.html
**

 Available Intersections
 1. Dorchester Road and Huron Church Road
 2. Totten Street and Huron Church Road
 3. Malden Road and Huron Church Road

### 🔶 Step 1.1 | API Calling 

![Screen Shot 2025-07-08 at 10 48 33 PM](https://github.com/user-attachments/assets/3c9573b3-f8a8-49be-9dc2-d67df243ddca)

### The API call returns a dataframe in JSON format (Flattening the JSON output into a tabular form for increased readability)


![Screen Shot 2025-07-08 at 10 50 20 PM](https://github.com/user-attachments/assets/64599dbd-69c5-404d-92a6-d621acd511b0)

### 🔶 Step 1.2 | Performing EDA

![Screen Shot 2025-07-08 at 10 53 08 PM](https://github.com/user-attachments/assets/5b35301f-12df-487e-a61e-845a3c8a040f)

# Charting 

### 🔶 Step 2.1 | Bar Graph for Total Vehicles


![Screen Shot 2025-07-08 at 10 54 57 PM](https://github.com/user-attachments/assets/10748d69-1da4-4af7-9310-22d07da4adff)

### 🔶 Step 2.2 | Per Minute Traffic 
![Screen Shot 2025-07-08 at 10 55 52 PM](https://github.com/user-attachments/assets/0335d77f-98be-488f-92d7-448f609f5d49)

### 🔶 Step 2.3 | Per 4-Hour Traffic 


![Screen Shot 2025-07-08 at 10 56 29 PM](https://github.com/user-attachments/assets/ca2bf282-7c53-4ee7-8379-77eb40554ef2)

### 🔶 Step 2.4 | Cleaning the Dataframe before Correlation Analysis


![Screen Shot 2025-07-08 at 10 58 45 PM](https://github.com/user-attachments/assets/fd7f897b-46b7-4ea1-a703-49e14b93c2f0)


# Finding the Correlation between large vehicle count and Traffic concussion


![Screen Shot 2025-07-08 at 11 00 32 PM](https://github.com/user-attachments/assets/01306214-7787-4379-bfc9-979f23b0fcf1)

The correlation value of 0.4265 shows there is only a 42% correlation between the count of larger vehicles to the total traffic congestion.

# Visualizing

### 🔶 Step 3.1 | Scatter Plot


![Screen Shot 2025-07-08 at 11 02 39 PM](https://github.com/user-attachments/assets/d0f5ce3e-1bd1-499f-b09e-3b2da9be0017)

#### Key Insights :
1. Weak or No Strong Linear Correlation (points are widely scattered).
2. Several points to the left (where large vehicle count is low) have very high traffic volumes.
3. Traffic congestion is much more affected by (small vehicle count, signals and road conditions) than large vehicles.

### 🔶 Step 3.2 | Trendline


![Screen Shot 2025-07-08 at 11 03 18 PM](https://github.com/user-attachments/assets/2450945a-703f-449a-90a3-4470f48342af)

#### Key Insights :
1. Slightly positive linear relationship - red line slopes upward, where there are more large vehicles in an hour the traffic tends to be higher as well.
2. Wide Confidence Interval (shaded pink region) - Means the regression model is not much certain about its prediction for total traffic at different counts of larger vehicles.
3. Trendline shows a statistical relationship and not causation.

### 🔶 Step 3.3 | Line Graph for Total Traffic Count and Large Vehicle Count


![Screen Shot 2025-07-08 at 11 03 53 PM](https://github.com/user-attachments/assets/3726ae06-2a8e-4eaf-b438-7c2adf2ee98c)

#### Key Insights :
1. Total traffic’s rush hour peaks don’t always correspond to peaks in large vehicle count.
2. The two lines do not move together very closely. This visual observation matches your earlier findings (low correlation coefficient, weak linear relationship, wide scatter and confidence bands).

# Conclusion

1. On average, more large vehicles being present slightly coincides with more traffic, but it does not account for all the variation in total traffic.
2. While you could use the line to predict total traffic from large vehicle count, the wide shaded region suggests predictions will be imprecise.
3. Practical Implication - Traffic management or congestion mitigation strategies should not focus exclusively on regulating large vehicle counts, since total volume is influenced by other factors as well.

