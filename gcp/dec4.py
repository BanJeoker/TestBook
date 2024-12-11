import plotly.graph_objects as go

# Assuming 'y_test_sorted' is your sorted y_test, and 'y_pred' is the predicted values
# Calculate the difference between y_test and y_pred
difference = y_test_sorted - y_pred

# If you want to plot against the 'date' column from your sorted test_data
# Assuming 'test_data_sorted' has the 'date' column

# Create the figure using Plotly
fig = go.Figure()

# Add the y_test line to the plot
fig.add_trace(go.Scatter(x=test_data_sorted['date'], y=y_test_sorted, mode='lines', name='y_test', line=dict(color='blue')))

# Add the difference line to the plot
fig.add_trace(go.Scatter(x=test_data_sorted['date'], y=difference, mode='lines', name='Difference (y_test - y_pred)', line=dict(color='red')))

# Update layout for the figure (add titles, labels, etc.)
fig.update_layout(
    title='y_test and Difference Between y_test and y_pred',
    xaxis_title='Date',
    yaxis_title='Value',
    template='plotly_dark',  # Optional: use a dark template for aesthetics
    autosize=True,
    showlegend=True
)

# Display the plot
fig.show()



plt.gca().xaxis.set_major_locator(ticker.MaxNLocator(nbins=20))  # Adjust 'nbins' for more ticks

import matplotlib.pyplot as plt

# Assuming 'y_test_sorted' is your sorted y_test, and 'y_pred' is the predicted values
# Calculate the difference between y_test and y_pred
difference = y_test_sorted - y_pred

# If you want to plot against the 'date' column from your sorted test_data
# Assuming 'test_data_sorted' has the 'date' column
plt.plot(test_data_sorted['date'], y_test_sorted, label='y_test', color='blue')
plt.plot(test_data_sorted['date'], difference, label='Difference (y_test - y_pred)', color='red')

# Add labels and title
plt.title('y_test and Difference Between y_test and y_pred')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()



lgb.plot_importance(lgb_reg, importance_type='split', max_num_features=10, title='Feature Importance')
plt.show()


import lightgbm as lgb
import numpy as np
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Assuming 'df' is your DataFrame and 'target' is the target column
# Prepare the features (X) and target (y)
X = df.drop(columns=['target'])  # Replace 'target' with your target column name
y = df['target']                 # Replace 'target' with your target column name

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








import matplotlib.pyplot as plt

# Assuming you've already trained 'lr' and 'lasso' and made predictions (as in the previous code)
# Make predictions on the test set
lr_preds = lr.predict(X_test_scaled)
lasso_preds = lasso.predict(X_test_scaled)

# Plot for Linear Regression
plt.figure(figsize=(12, 6))

# Linear Regression
plt.subplot(1, 2, 1)
plt.scatter(y_test, lr_preds, color='blue', alpha=0.5)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', linestyle='--')  # line for perfect predictions
plt.title('True vs Predicted - Linear Regression')
plt.xlabel('True Values')
plt.ylabel('Predicted Values')

# LASSO Regression
plt.subplot(1, 2, 2)
plt.scatter(y_test, lasso_preds, color='green', alpha=0.5)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', linestyle='--')  # line for perfect predictions
plt.title('True vs Predicted - LASSO Regression')
plt.xlabel('True Values')
plt.ylabel('Predicted Values')

# Show the plots
plt.tight_layout()
plt.show()




import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, Lasso
from sklearn.metrics import mean_absolute_error

# Step 1: Load and shuffle the data
df = ...  # Your prepared DataFrame
df = df.sample(frac=1, random_state=42).reset_index(drop=True)  # Shuffle the rows

# Step 2: Train-test split
X = df.drop(columns=['target'])  # Replace 'target' with your target column name
y = df['target']                 # Replace 'target' with your target column name
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Normalize the data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Step 4: Perform regression and predictions
# Linear Regression
lr = LinearRegression()
lr.fit(X_train_scaled, y_train)
lr_preds = lr.predict(X_test_scaled)

# LASSO Regression
lasso = Lasso(alpha=0.1)  # You can adjust alpha if needed
lasso.fit(X_train_scaled, y_train)
lasso_preds = lasso.predict(X_test_scaled)

# Step 5: Compare using MAE
lr_mae = mean_absolute_error(y_test, lr_preds)
lasso_mae = mean_absolute_error(y_test, lasso_preds)

# Output results
print(f"Linear Regression MAE: {lr_mae:.4f}")
print(f"LASSO Regression MAE: {lasso_mae:.4f}")


import matplotlib.pyplot as plt
import numpy as np

# Assuming you've already trained your models (lr and lasso from previous code)
# Get feature names
feature_names = X.columns

# Get coefficients from Linear Regression and LASSO
lr_coefficients = lr.coef_
lasso_coefficients = lasso.coef_

# Plot feature importance
plt.figure(figsize=(12, 6))

# Linear Regression Feature Importance
plt.subplot(1, 2, 1)
plt.barh(feature_names, np.abs(lr_coefficients))
plt.title('Feature Importance - Linear Regression')
plt.xlabel('Coefficient Magnitude')
plt.ylabel('Features')

# LASSO Regression Feature Importance
plt.subplot(1, 2, 2)
plt.barh(feature_names, np.abs(lasso_coefficients))
plt.title('Feature Importance - LASSO Regression')
plt.xlabel('Coefficient Magnitude')
plt.ylabel('Features')

# Adjust layout and show plot
plt.tight_layout()
plt.show()


import pandas as pd

# Sample DataFrame
data = {
    'id': [1, 1, 1, 2, 2],
    'date1': ['2020-01-01', '2020-01-03', '2020-01-05', '2020-01-01', '2020-01-04']
}
df = pd.DataFrame(data)

# Convert 'date1' to datetime
df['date1'] = pd.to_datetime(df['date1'])

# Calculate the difference in days within each group
df['diff_days'] = df.groupby('id')['date1'].diff().fillna(pd.Timedelta(days=-1)).dt.days

print(df)



mask = np.triu(np.ones_like(corr_matrix, dtype=bool))

# Flatten the matrix and filter by high correlation values
high_corr = corr_matrix.where(mask).stack().reset_index(name='correlation')

# Filter out correlations less than a threshold, e.g., 0.8
high_corr = high_corr[high_corr['correlation'] > 0.8]

# Sort by correlation in descending order
high_corr_sorted = high_corr.sort_values(by='correlation', ascending=False)

# Print the high correlation pairs
print(high_corr_sorted)


import pandas as pd
import numpy as np

# Sample DataFrame
data = {
    'A': [1, 2, 3, 4, 5],
    'B': [5, 4, 3, 2, 1],
    'C': [1, 3, 2, 5, 4],
    'D': [10, 20, 30, 40, 50]
}
df = pd.DataFrame(data)

# Compute the correlation matrix
corr_matrix = df.corr()

# Set the threshold for high correlation
threshold = 0.8

# Create an empty list to store columns to drop
to_drop = []

# Iterate over the correlation matrix
for column in corr_matrix.columns:
    # Get the correlations for the current column
    corr_values = corr_matrix[column]
    
    # Find columns that are highly correlated (greater than the threshold)
    # and are not the same column (diagonal elements)
    high_corr_columns = corr_values[(corr_values > threshold) & (corr_values < 1)].index
    
    for col in high_corr_columns:
        # If the column hasn't already been marked for removal, mark it
        if col not in to_drop:
            to_drop.append(col)

# Drop the highly correlated columns
df_cleaned = df.drop(columns=to_drop)

print("DataFrame after removing highly correlated columns:")
print(df_cleaned)

import xgboost as xgb
import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Assuming 'df' is your DataFrame and 'target' is the target column
# Prepare the features (X) and target (y)
X = df.drop(columns=['target'])  # Replace 'target' with your target column name
y = df['target']                 # Replace 'target' with your target column name

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalize the data (scaling)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Create and train the XGBoost regressor model
xg_reg = xgb.XGBRegressor(objective='reg:squarederror', random_state=42)
xg_reg.fit(X_train_scaled, y_train)

# Make predictions
y_pred = xg_reg.predict(X_test_scaled)

# Calculate RMSE
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

# Print RMSE
print(f"XGBoost Regression RMSE: {rmse:.4f}")


import xgboost as xgb
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Assuming 'df' is your DataFrame and 'target' is the target column
# Prepare the features (X) and target (y)
X = df.drop(columns=['target'])  # Replace 'target' with your target column name
y = df['target']                 # Replace 'target' with your target column name

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalize the data (scaling)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Create and train the XGBoost regressor model
xg_reg = xgb.XGBRegressor(objective='reg:squarederror', random_state=42)
xg_reg.fit(X_train_scaled, y_train)

# Plot feature importance
xgb.plot_importance(xg_reg, importance_type='weight', max_num_features=10, title="Feature Importance (Weight)")
plt.show()

# Alternatively, get feature importance as scores
importance_scores = xg_reg.get_booster().get_score(importance_type='weight')

# Display feature importance
print("Feature Importance Scores:")
print(importance_scores)



In XGBoost, the F-score (also called feature score or frequency score) is a measure of feature importance that indicates how many times a feature was used in a decision tree split, i.e., how many times a feature contributed to reducing the loss function. The F-score is calculated as the number of times a feature is used in the decision trees built by the model.

How the F-score is calculated:
The F-score is calculated by counting the number of times a feature is used in a split (a node in the tree) across all trees in the model.
It reflects the contribution of each feature to the model's predictive performance.
Higher F-scores indicate that a feature has been used more frequently and is more important in the model.
Importance Types in XGBoost:
XGBoost provides several ways to measure feature importance, and F-score is one of them. The most commonly used importance types are:

Weight (or F-score): The number of times a feature is used in a split.
Gain: The average gain of a feature when it is used in a split.
Cover: The average coverage (the number of samples affected) of a feature when it is used in a split.
