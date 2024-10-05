import pandas as pd
import numpy as np
from faker import Faker

fake = Faker()

num_transactions=10000
    # Generate synthetic data
data = {
        'TransactionID': range(1, num_transactions + 1),
        'Location': [fake.city() for _ in range(num_transactions)],
        'TransactionAmount': np.random.uniform(1, 1000, num_transactions),
        'MerchantType': [fake.company() if np.random.rand() > 0.9 else 'Unusual Merchant' for _ in range(num_transactions)],
        'Timestamp': [fake.date_time_this_year() for _ in range(num_transactions)]
    }

    # Create DataFrame
df = pd.DataFrame(data)
print(df.head())

