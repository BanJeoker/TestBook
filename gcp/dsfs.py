import lightgbm as lgb
import numpy as np
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Assuming 'df' is your DataFrame and 'target' is the target column
# Save the 'id' and 'date' columns for later use
df_id_date = df[['id', 'date']]

# Drop the 'id' and 'date' columns from the DataFrame for training
X = df.drop(columns=['target', 'id', 'date'])  # Replace 'target' with your target column name
y = df['target']  # Replace 'target' with your target column name

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalize the data (scaling)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Create and train the LightGBM regressor model
lgb_reg = lgb.LGBMRegressor(objective='regression', random_state=42)
lgb_reg.fit(X_train_scaled, y_train)

# Make predictions
y_pred = lgb_reg.predict(X_test_scaled)

# Calculate MAE
mae = mean_absolute_error(y_test, y_pred)

# Print MAE
print(f"LightGBM Regression MAE: {mae:.4f}")

# Add back 'id' and 'date' columns to the test data for plotting
test_data = X_test.copy()
test_data['id'] = df_id_date.loc[X_test.index, 'id']
test_data['date'] = df_id_date.loc[X_test.index, 'date']

# Sort the test data by 'date'
test_data_sorted = test_data.sort_values(by='date')

# Plot something based on sorted 'date'
plt.plot(test_data_sorted['date'], y_pred[test_data_sorted.index])  # Example plot
plt.title('Predictions Sorted by Date')
plt.xlabel('Date')
plt.ylabel('Prediction')
plt.show()
