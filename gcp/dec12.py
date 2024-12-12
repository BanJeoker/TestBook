import pandas as pd
import numpy as np
from sklearn.metrics import mean_absolute_error
from lightgbm import LGBMRegressor

# Sample DataFrame
data = {
    'date': pd.date_range(start='2024-01-01', periods=100, freq='D'),
    'feature': np.random.rand(100),
    'target': np.random.rand(100) * 100
}
df = pd.DataFrame(data)

# Ensure the 'date' column is in datetime format
df['date'] = pd.to_datetime(df['date'])

# Define the initial test range
test_start = '2024-03-01'
test_end = '2024-03-10'

# Convert test range to datetime
test_start = pd.to_datetime(test_start)
test_end = pd.to_datetime(test_end)

# Prepare to store errors
errors = []

while test_start <= test_end:
    # Train data: all data before the test range
    train_data = df[df['date'] < test_start]
    
    # Test data: data within the test range
    test_data = df[(df['date'] >= test_start) & (df['date'] <= test_end)]
    
    # Exit the loop if there's no test data left
    if test_data.empty:
        break

    # Extract features and target
    X_train, y_train = train_data[['feature']], train_data['target']
    X_test, y_test = test_data[['feature']], test_data['target']

    # Train LightGBM model
    model = LGBMRegressor()
    model.fit(X_train, y_train)
    
    # Make predictions
    y_pred = model.predict(X_test)
    
    # Calculate mean absolute error
    mae = mean_absolute_error(y_test, y_pred)
    errors.append(mae)
    
    # Print the results for this iteration
    print(f"Test range: {test_start.date()} to {test_end.date()}, MAE: {mae}")
    
    # Expand the training range by reducing the test range by one day
    test_start += pd.Timedelta(days=1)

# Print progression of errors
print("Error progression:", errors)
