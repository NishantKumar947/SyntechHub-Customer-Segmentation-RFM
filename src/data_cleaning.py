import pandas as pd
import numpy as np
import os

def load_and_clean_data(input_path, output_path):
    print("\n=========================================")
    print("--- STEP 1: DATA LOADING & CLEANING SHURU ---")
    print("=========================================")
    
    # 1. Check karna ki raw file hai ya nahi
    if not os.path.exists(input_path):
        print(f"Error: Raw file '{input_path}' nahi mili!")
        return None

    print(f"Loading raw data from: {input_path} ...")
    df = pd.read_csv(input_path, encoding='ISO-8859-1')
    print(f"Original Data Shape: {df.shape[0]} Rows, {df.shape[1]} Columns")
    
    # 2. Missing Customer ID hatana
    print("Missing CustomerID wali rows ko filter kiya ja raha hai...")
    df = df.dropna(subset=['CustomerID'])
    
    # 3. Data Types thik karna
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    df['CustomerID'] = df['CustomerID'].astype(int) # ID ko float se int me convert karna
    
    # 4. Returns aur Cancellations handle karna (Sirf positive entries rakhna)
    print("Negative quantities aur prices (returns) ko hataya ja raha hai...")
    clean_df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)].copy()
    
    # 5. Total Amount calculate karna
    clean_df['TotalAmount'] = clean_df['Quantity'] * clean_df['UnitPrice']
    
    print(f"Cleaning complete! Cleaned Data Shape: {clean_df.shape[0]} Rows")
    
    # 6. Processed folder me permanently save karna
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    clean_df.to_csv(output_path, index=False)
    print(f"[SAVED] Cleaned data permanently saved at: {output_path}")
    
    return clean_df

if __name__ == "__main__":
    # Script ko akele test karne ke liye paths
    RAW_PATH = os.path.join('data', 'raw', 'data.csv')
    PROCESSED_PATH = os.path.join('data', 'processed', 'cleaned_transactions.csv')
    
    load_and_clean_data(RAW_PATH, PROCESSED_PATH)