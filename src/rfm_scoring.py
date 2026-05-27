import pandas as pd
import numpy as np
import os

def segment_and_score(input_path, output_data_path, output_summary_path):
    print("\n=========================================")
    print("--- STEP 3 & 4: SCORING & SEGMENTATION ---")
    print("=========================================")
    
    if not os.path.exists(input_path):
        print(f"Error: Metrics file '{input_path}' nahi mili! Pehle Step 2 chalayein.")
        return None

    print(f"Loading RFM Metrics from: {input_path} ...")
    rfm = pd.read_csv(input_path, index_col='CustomerID')
    
    # 1. Quantiles ke basis par 1 se 5 tak scoring karna
    print("Customers ko 1-5 ke scale par rank kiya ja raha hai...")
    rfm['R_Score'] = pd.qcut(rfm['Recency'], q=5, labels=[5, 4, 3, 2, 1])
    rfm['F_Score'] = pd.qcut(rfm['Frequency'].rank(method='first'), q=5, labels=[1, 2, 3, 4, 5])
    rfm['M_Score'] = pd.qcut(rfm['Monetary'], q=5, labels=[1, 2, 3, 4, 5])
    
    # Total Score nikalna (Teeno ko jod kar)
    rfm['RFM_Score'] = rfm[['R_Score', 'F_Score', 'M_Score']].sum(axis=1)
    
    # 2. Segment Names Assign Karna
    print("Scores ke basis par groups (Segments) banaye ja rahe hain...")
    def score_to_segment(score):
        if score >= 13:
            return 'Champions'
        elif score >= 10:
            return 'Loyal Customers'
        elif score >= 7:
            return 'Promising / New'
        elif score >= 5:
            return 'At Risk'
        else:
            return 'Lost Customers'
            
    rfm['Segment'] = rfm['RFM_Score'].apply(score_to_segment)
    
    # 3. Final Scored Data Save Karna
    rfm.to_csv(output_data_path)
    print(f"[SAVED] Scored & Segmented data saved at: {output_data_path}")
    
    # 4. STEP 5: Segment Analysis (Summary Report)
    print("\n--- STEP 5: GENERATING SEGMENT SUMMARY REPORT ---")
    summary = rfm.groupby('Segment').agg({
        'Recency': 'mean',
        'Frequency': 'mean',
        'Monetary': 'mean',
        'RFM_Score': 'count'
    }).rename(columns={'RFM_Score': 'Customer_Count'}).sort_values(by='Monetary', ascending=False)
    
    summary = summary.round(2)
    summary.to_csv(output_summary_path)
    print(f"[SAVED] Segment summary report saved at: {output_summary_path}")
    
    print("\nSegments ka Quick Behavioral Summary:")
    print(summary)
    
    return rfm

if __name__ == "__main__":
    # Test karne ke liye paths
    METRICS_PATH = os.path.join('data', 'processed', 'rfm_metrics.csv')
    SCORED_PATH = os.path.join('data', 'processed', 'rfm_scored_data.csv')
    SUMMARY_PATH = os.path.join('data', 'processed', 'segment_summary_report.csv')
    
    segment_and_score(METRICS_PATH, SCORED_PATH, SUMMARY_PATH)