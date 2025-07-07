import numpy as np
import random

# Set parameters
n = 10  # Number of data points in the dataset
window_size = 10  # Size of the rolling window
low = 100  # Lower bound of random number generation
high = 300  # Upper bound of random number generation

# Initialize empty lists for the data, rolling averages, and rolling standard deviations
data = []
rolling_avg = []
rolling_std = []

# Generate initial data point
data.append(random.randint(low, high))

# Calculate rolling averages and standard deviations
for i in range(1, n):
    # Add a new number within bounds of rolling_avg ± 1.5 * rolling_std
    if i >= window_size:
        window = data[
            i - window_size: i
        ]  # Get the previous window of size 'window_size'
        current_avg = np.mean(window)  # Calculate rolling average
        current_std = np.std(window)  # Calculate rolling standard deviation

        # Ensure the new number is within the bounds
        lower_bound = current_avg - 1.5 * current_std
        upper_bound = current_avg + 1.5 * current_std

        # Generate a number that stays within these bounds and is an integer
        new_value = random.randint(
            int(np.floor(lower_bound)), int(np.floor(upper_bound))
        )
    else:
        new_value = random.randint(
            low, high
        )  # For initial values before the window is filled

    data.append(new_value)
    rolling_avg.append(
        np.mean(data[max(0, i - window_size): i + 1])
    )  # Update rolling avg
    rolling_std.append(
        np.std(data[max(0, i - window_size): i + 1])
    )  # Update rolling std

# Print the generated dataset
print("Generated Data:", data)

# print("Rolling Standard Deviation:", rolling_std)
