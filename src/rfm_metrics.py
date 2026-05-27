import pandas as pd
import numpy as np
import datetime as dt
import os

def calculate_rfm_metrics(input_path, output_path):
    print("\n=========================================")
    print("--- STEP 2: RFM METRICS CALCULATION ---")
    print("=========================================")
    
    # 1. Cleaned data load karna
    if not os.path.exists(input_path):
        print(f"Error: Cleaned file '{input_path}' nahi mili! Pehle Step 1 chalayein.")
        return None

    print(f"Loading cleaned data from: {input_path} ...")
    df = pd.read_csv(input_path)
    
    # Date column ko wapas datetime format me convert karna (CSV me string ban jata hai)
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    
    # 2. Snapshot Date set karna (Latest date + 1 din)
    snapshot_date = df['InvoiceDate'].max() + dt.timedelta(days=1)
    print(f"Analysis Snapshot Date: {snapshot_date.date()}")
    
    # 3. Groupby CustomerID aur R, F, M nikalna
    print("Har customer ke liye metrics calculate ho rahe hain...")
    rfm = df.groupby('CustomerID').agg({
        'InvoiceDate': lambda x: (snapshot_date - x.max()).days, # Recency
        'InvoiceNo': 'nunique',                                  # Frequency
        'TotalAmount': 'sum'                                     # Monetary
    })
    
    # Columns rename karna
    rfm.rename(columns={
        'InvoiceDate': 'Recency',
        'InvoiceNo': 'Frequency',
        'TotalAmount': 'Monetary'
    }, inplace=True)
    
    print(f"Metrics ready! Total Unique Customers: {rfm.shape[0]}")
    
    # 4. Permanently save karna processed folder me
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    rfm.to_csv(output_path) # Index (CustomerID) ke saath save hoga
    print(f"[SAVED] RFM Metrics permanently saved at: {output_path}")
    
    return rfm

if __name__ == "__main__":
    # Script ko akele test karne ke liye paths
    CLEANED_DATA_PATH = os.path.join('data', 'processed', 'cleaned_transactions.csv')
    RFM_METRICS_PATH = os.path.join('data', 'processed', 'rfm_metrics.csv')
    
    calculate_rfm_metrics(CLEANED_DATA_PATH, RFM_METRICS_PATH)