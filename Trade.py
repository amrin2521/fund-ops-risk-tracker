
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Simulate synthetic data
np.random.seed(0)
n = 100
trade_ids = [f'TRD{1000+i}' for i in range(n)]
trade_dates = pd.date_range(start="2025-05-01", periods=n, freq='D')
settlement_delays = np.random.choice([0, 1, 2, 3], size=n, p=[0.3, 0.4, 0.2, 0.1])
settlement_dates = trade_dates + pd.to_timedelta(settlement_delays, unit='D')
amounts = np.random.uniform(1000, 50000, size=n).round(2)
statuses = np.random.choice(['Settled', 'Pending', 'Failed'], size=n, p=[0.7, 0.2, 0.1])

df = pd.DataFrame({
    'Trade_ID': trade_ids,
    'Trade_Date': trade_dates,
    'Settlement_Date': settlement_dates,
    'Amount_USD': amounts,
    'Status': statuses,
    'Settlement_Delay': settlement_delays
})

# Summary
summary = df.groupby('Status').agg(
    Trade_Count=('Trade_ID', 'count'),
    Total_Amount=('Amount_USD', 'sum'),
    Avg_Delay=('Settlement_Delay', 'mean')
).reset_index()

# Visualizations
sns.countplot(data=df, x='Status')
plt.title('Trade Status Distribution')
plt.tight_layout()
plt.savefig("trade_status_count.png")

sns.histplot(df[df['Status'] == 'Settled']['Settlement_Delay'], bins=5)
plt.title('Settlement Delay for Settled Trades')
plt.xlabel('Days')
plt.ylabel('Number of Trades')
plt.tight_layout()
plt.savefig("settlement_delay_hist.png")

# Export CSVs
df.to_csv("trade_settlement_dashboard_data.csv", index=False)
summary.to_csv("settlement_dashboard_summary.csv", index=False)
