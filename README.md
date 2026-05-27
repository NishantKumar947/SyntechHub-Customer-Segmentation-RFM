# SyntechHub-Customer-Segmentation-RFM
Customer Segmentation pipeline using RFM Analysis with Python and Tableau dashboard.

This repository contains a professional, end-to-end data analytics pipeline to segment retail customers based on their buying behavior using **RFM (Recency, Frequency, Monetary) Analysis**. 

## 📁 Project Structure
```text
SyntechHub_RFM_Project/
│
├── data/
│   ├── raw/                  # Raw dataset downloaded from UCI Repository
│   └── processed/            # Cleaned data, RFM metrics, and summary reports
│
├── src/
│   ├── __init__.py           # Makes src a python package
│   ├── data_cleaning.py      # Step 1: Handles missing IDs and negative returns
│   ├── rfm_metrics.py        # Step 2: Calculates Recency, Frequency, and Monetary values
│   ├── rfm_scoring.py        # Step 3, 4, 5: Quantile scoring, segmentation, and summary reports
│   └── visualization.py      # Step 6: Generates analytical charts
│
├── reports/                  # Contains final output charts (Bar chart & Pie chart)
├── download_data.py          # Script to automatically download benchmark dataset
├── requirements.txt          # Required Python libraries
└── main.py                   # Main orchestrator to run the complete pipeline


🚀 How to Run the Project
Clone the repository:

Bash
git clone <your-github-repo-link>
cd SyntechHub_RFM_Project
Install requirements:

Bash
pip install -r requirements.txt
Download the Dataset:

Bash
python download_data.py
Run the Complete Pipeline:

Bash
python main.py
📊 Business Insights Generated
Champions: Recent shoppers, high frequency, and maximum spenders. (Target with Loyalty programs & early access).

Loyal Customers: Regular buyers with solid spending. (Target with upsell offers).

At Risk: Customers who haven't visited recently. (Target with reactivation/win-back emails).
