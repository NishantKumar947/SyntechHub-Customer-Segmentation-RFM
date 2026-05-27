import os
import urllib.request
import pandas as pd

def download_retail_data():
    print("\n=========================================")
    print("--- STEP 0: DATA DOWNLOAD SHURU HO RAHA HAI ---")
    print("=========================================")
    
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00352/Online%20Retail.xlsx"
    raw_dir = os.path.join('data', 'raw')
    excel_path = os.path.join(raw_dir, 'Online_Retail.xlsx')
    csv_path = os.path.join(raw_dir, 'data.csv')
    
    os.makedirs(raw_dir, exist_ok=True)
    
    if not os.path.exists(csv_path):
        if not os.path.exists(excel_path):
            print("Internet se original dataset download ho raha hai (Approx 23MB)...")
            print("Kripya 1-2 minute wait karein...")
            urllib.request.urlretrieve(url, excel_path)
            print("Excel file download ho gayi!")
        
        print("Excel ko CSV me convert kiya ja raha hai fast processing ke liye...")
        df = pd.read_excel(excel_path, engine='openpyxl')
        df.to_csv(csv_path, index=False)
        print(f"Success! Dataset yahan save ho gaya: {csv_path}")
        
        if os.path.exists(excel_path):
            os.remove(excel_path)
    else:
        print(f"Dataset pehle se majood hai: {csv_path}")

if __name__ == "__main__":
    download_retail_data()