import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

def generate_subscription_data():
    num_customers = 250 # Increased for better visuals
    data_rows = []
    
    plans = {
        'Basic Supplement Stack': 49.99,
        'Premium Performance Bundle': 99.99,
        'Ultimate Athlete Suite': 149.99
    }
    
    sources = ['Facebook Ads', 'Google Search', 'Influencer/KOL', 'Direct/Organic']

    for i in range(num_customers):
        email = f"user_{i}@example.com"
        plan = random.choice(list(plans.keys()))
        monthly_price = plans[plan]
        source = random.choice(sources)
        
        # Months active (1 to 12)
        months_active = random.randint(1, 12)
        
        # Realistic Churn Logic: Influencers have high churn, Google has low churn
        if source == 'Influencer/KOL':
            status = random.choices(['Active', 'Cancelled'], weights=[0.4, 0.6])[0]
        elif source == 'Google Search':
            status = random.choices(['Active', 'Cancelled'], weights=[0.9, 0.1])[0]
        else:
            status = random.choices(['Active', 'Cancelled'], weights=[0.7, 0.3])[0]
        
        total_spent = months_active * monthly_price
        
        data_rows.append({
            'Customer_Email': email,
            'Plan': plan,
            'Monthly_Rate': monthly_price,
            'Months_Active': months_active,
            'Status': status,
            'Source': source,
            'Total_LTV': round(total_spent, 2),
            'Signup_Date': (datetime.now() - timedelta(days=months_active*30)).strftime('%Y-%m-%d')
        })

    df = pd.DataFrame(data_rows)
    df.to_csv('subscription_data.csv', index=False)
    print("✅ Created 'subscription_data.csv' successfully.")

if __name__ == "__main__":
    generate_subscription_data()