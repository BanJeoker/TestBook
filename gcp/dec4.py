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
