# Fund Ops Risk Tracker

This project is a simulation of a trade settlement workflow. It models how operations teams track trades, monitor settlement delays, and generate summaries of overall processing health. I built this to get hands-on experience with data in a finance operations context—like the kind of work done at BNP Paribas, Citi, or other institutional banks.

Using Python, I created synthetic trade data, performed analysis, and visualized key metrics.

---

## 📁 What's in this project

| File | Description |
|------|-------------|
| `Trade.py` | Script that generates, processes, and visualizes trade data |
| `trade_settlement_dashboard_data.csv` | Mock trade data with timestamps, status, and delays |
| `settlement_dashboard_summary.csv` | Summary: total trades, amount settled, avg delays |
| `trade_status_count.png` | Bar chart of number of trades by status |
| `settlement_delay_hist.png` | Histogram showing trade settlement delays |

---

## Why I built this

I wanted to create a small-scale simulation of post-trade processing — the kind of thing fund servicing or operations analysts work on. This project helped me think through:
- How to structure transactional data
- How to summarize key risk indicators (like delays and failures)
- How to visualize operational health for reporting

---

## 🚀 How to run

1. Clone or download this repo:
   ```bash
   git clone https://github.com/<your-username>/fund-ops-risk-tracker.git
   cd fund-ops-risk-tracker

🔍 Real-World Context
In large banks, trade operations teams reconcile thousands of trades per day. They check whether trades settled, track any delays, and investigate failed transactions. This project mimics that on a smaller scale—focusing on data structure, analysis, and reporting, just like those used in real middle/back-office operations.

📈 What I Learned
How to simulate financial operations data using Python
How to use pandas and matplotlib for reporting KPIs
How to create visual summaries that highlight operational risks
How trade status and settlement delays affect downstream processes

➕ Next Steps
Some things I’d like to build on:
Add time-based tracking (e.g., trades across multiple days)
Create an interactive dashboard using Streamlit
Simulate trade matching and reconciliation between buy/sell sides

