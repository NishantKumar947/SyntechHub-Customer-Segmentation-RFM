import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def create_visualizations(input_path, output_dir):
    print("\n=========================================")
    print("--- STEP 6: VISUALIZATION & DASHBOARD ---")
    print("=========================================")
    
    if not os.path.exists(input_path):
        print(f"Error: Scored file '{input_path}' nahi mili! Pehle Step 3 chalayein.")
        return
        
    # Data load karna
    rfm = pd.read_csv(input_path)
    os.makedirs(output_dir, exist_ok=True)
    
    # Styling set karna
    sns.set_theme(style="whitegrid")
    
    # ----------------------------------------------------
    # CHART 1: Bar Plot - Customer Distribution
    # ----------------------------------------------------
    plt.figure(figsize=(10, 6))
    segment_counts = rfm['Segment'].value_counts()
    
    sns.barplot(x=segment_counts.index, y=segment_counts.values, palette='viridis', hue=segment_counts.index, legend=False)
    plt.title('Customer Distribution Across Segments', fontsize=16, fontweight='bold')
    plt.xlabel('Customer Segment', fontsize=12)
    plt.ylabel('Number of Customers', fontsize=12)
    plt.xticks(rotation=15)
    
    # Bars ke upar numbers likhna
    for i, v in enumerate(segment_counts.values):
        plt.text(i, v + 15, str(v), ha='center', fontweight='bold')
        
    chart1_path = os.path.join(output_dir, 'customer_distribution.png')
    plt.tight_layout()
    plt.savefig(chart1_path, dpi=300)
    plt.close()
    print(f"[SAVED] Bar Chart save ho gaya: {chart1_path}")
    
    # ----------------------------------------------------
    # CHART 2: Pie Chart - Total Revenue per Segment
    # ----------------------------------------------------
    plt.figure(figsize=(8, 8))
    segment_revenue = rfm.groupby('Segment')['Monetary'].sum()
    
    plt.pie(segment_revenue.values, labels=segment_revenue.index, autopct='%1.1f%%', 
            startangle=140, colors=sns.color_palette('pastel'), 
            wedgeprops={'edgecolor': 'black', 'linewidth': 1, 'antialiased': True})
    
    plt.title('Total Revenue Contribution by Segment', fontsize=16, fontweight='bold')
    
    chart2_path = os.path.join(output_dir, 'revenue_contribution.png')
    plt.tight_layout()
    plt.savefig(chart2_path, dpi=300)
    plt.close()
    print(f"[SAVED] Pie Chart save ho gaya: {chart2_path}")
    
    print("\n--- ALL VISUALIZATIONS COMPLETED SUCCESSFULLY ---")

if __name__ == "__main__":
    SCORED_DATA_PATH = os.path.join('data', 'processed', 'rfm_scored_data.csv')
    REPORTS_DIR = 'reports'
    
    create_visualizations(SCORED_DATA_PATH, REPORTS_DIR)