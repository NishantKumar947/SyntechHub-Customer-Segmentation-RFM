import os
import sys

# src folder ke modules ko import karne ke liye path check karna
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from data_cleaning import load_and_clean_data
from rfm_metrics import calculate_rfm_metrics
from rfm_scoring import segment_and_score
from visualization import create_visualizations

def run_pipeline():
    print("==========================================================")
    print("     SYNTECHHUB: CUSTOMER SEGMENTATION PIPELINE SHURU     ")
    print("==========================================================")
    
    # Sabhi paths ko yahan define karna
    RAW_DATA_PATH = os.path.join('data', 'raw', 'data.csv')
    CLEANED_DATA_PATH = os.path.join('data', 'processed', 'cleaned_transactions.csv')
    RFM_METRICS_PATH = os.path.join('data', 'processed', 'rfm_metrics.csv')
    RFM_SCORED_PATH = os.path.join('data', 'processed', 'rfm_scored_data.csv')
    SUMMARY_REPORT_PATH = os.path.join('data', 'processed', 'segment_summary_report.csv')
    REPORTS_DIR = 'reports'
    
    # PIPELINE EXECUTION
    # 1. Data Cleaning
    clean_df = load_and_clean_data(RAW_DATA_PATH, CLEANED_DATA_PATH)
    if clean_df is None:
        print("Pipeline failed at Step 1: Data Cleaning.")
        return
        
    # 2. RFM Metrics Calculation
    rfm_df = calculate_rfm_metrics(CLEANED_DATA_PATH, RFM_METRICS_PATH)
    if rfm_df is None:
        print("Pipeline failed at Step 2: RFM Metrics Calculation.")
        return
        
    # 3. Scoring & Segmentation (Step 3, 4 & 5)
    scored_df = segment_and_score(RFM_METRICS_PATH, RFM_SCORED_PATH, SUMMARY_REPORT_PATH)
    if scored_df is None:
        print("Pipeline failed at Step 3: Scoring & Segmentation.")
        return
        
    # 4. Visualizations (Step 6)
    create_visualizations(RFM_SCORED_PATH, REPORTS_DIR)
    
    print("\n==========================================================")
    print("   [SUCCESS] PIPELINE EXECUTED SUCCESSFULLY! ALL OUTPUTS READY.")
    print("==========================================================")

if __name__ == "__main__":
    run_pipeline()