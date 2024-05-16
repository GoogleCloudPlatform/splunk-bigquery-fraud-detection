# Copyright 2024 Google LLC

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     https://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pandas as pd
import numpy as np
import random

# Set random seed for reproducibility
random.seed(42)

# Define parameters
start_date = '2023-04-01'
end_date = '2023-05-31'
time_interval = '15min'  # Fixed time interval for transactions
num_users = 10
locations = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia', 'Phoenix', 'San Antonio', 'San Diego', 'Dallas', 'San Jose']
fraud_rate = 0.01
fraud_pattern_interval = '36000min'  # Interval for fraudulent transactions

# Generate user data
user_ids = range(1, num_users + 1)
user_names = [f'User_{i}' for i in user_ids]

# Generate transaction data
dates = pd.date_range(start_date, end_date, freq=time_interval)
transactions = []

for date in dates:
    for user_id, user_name in zip(user_ids, user_names):
        # Generate random number of transactions for each user
        num_transactions = random.randint(0, 1)

        for _ in range(num_transactions):
            # Generate random transaction amount
            amount = random.uniform(10, 1000)

            # Generate random action (withdrawal or credit)
            action = random.choice(['withdrawal', 'credit'])

            # Generate random location
            location = random.choice(locations)

            # Determine if transaction is fraudulent based on pattern
            is_fraud = (date.minute % int(fraud_pattern_interval.rstrip('min'))) == 0

            transactions.append({
                'timestamp': date,
                'amount': amount,
                'action': action,
                'location': location,
                'User_ID': user_id,
                'user_name': user_name,
                'is_fraud': is_fraud
            })

# Create DataFrame from transaction data
df = pd.DataFrame(transactions)

# Save DataFrame to CSV file
df.to_csv('timeseries_data.csv', index=False)
