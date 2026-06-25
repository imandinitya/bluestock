import pandas as pd
import os

# Create processed folder
os.makedirs("data/processed", exist_ok=True)

print("=" * 60)
print("DAY 2 - DATA CLEANING")
print("=" * 60)

# ==================================================
# 1. FUND MASTER
# ==================================================

fund_df = pd.read_csv("data/raw/01_fund_master.csv")

fund_df = fund_df.drop_duplicates()

fund_df.to_csv(
    "data/processed/01_fund_master_clean.csv",
    index=False
)

print("✓ Fund Master Cleaned")


# ==================================================
# 2. NAV HISTORY
# ==================================================

nav_df = pd.read_csv("data/raw/02_nav_history.csv")

# Convert date
nav_df["date"] = pd.to_datetime(nav_df["date"])

# Sort
nav_df = nav_df.sort_values(
    ["amfi_code", "date"]
)

# Remove duplicates
nav_df = nav_df.drop_duplicates()

# Forward fill NAV
nav_df["nav"] = (
    nav_df.groupby("amfi_code")["nav"]
    .ffill()
)

# Validate NAV > 0
nav_df = nav_df[
    nav_df["nav"] > 0
]

nav_df.to_csv(
    "data/processed/02_nav_history_clean.csv",
    index=False
)

print("✓ NAV History Cleaned")


# ==================================================
# 3. AUM BY FUND HOUSE
# ==================================================

aum_df = pd.read_csv(
    "data/raw/03_aum_by_fund_house.csv"
)

aum_df["date"] = pd.to_datetime(
    aum_df["date"]
)

aum_df = aum_df.drop_duplicates()

aum_df.to_csv(
    "data/processed/03_aum_by_fund_house_clean.csv",
    index=False
)

print("✓ AUM Data Cleaned")


# ==================================================
# 4. MONTHLY SIP INFLOWS
# ==================================================

sip_df = pd.read_csv(
    "data/raw/04_monthly_sip_inflows.csv"
)

sip_df = sip_df.drop_duplicates()

sip_df.to_csv(
    "data/processed/04_monthly_sip_inflows_clean.csv",
    index=False
)

print("✓ SIP Data Cleaned")


# ==================================================
# 5. CATEGORY INFLOWS
# ==================================================

cat_df = pd.read_csv(
    "data/raw/05_category_inflows.csv"
)

cat_df = cat_df.drop_duplicates()

cat_df.to_csv(
    "data/processed/05_category_inflows_clean.csv",
    index=False
)

print("✓ Category Inflows Cleaned")


# ==================================================
# 6. INDUSTRY FOLIO COUNT
# ==================================================

folio_df = pd.read_csv(
    "data/raw/06_industry_folio_count.csv"
)

folio_df = folio_df.drop_duplicates()

folio_df.to_csv(
    "data/processed/06_industry_folio_count_clean.csv",
    index=False
)

print("✓ Folio Count Cleaned")


# ==================================================
# 7. SCHEME PERFORMANCE
# ==================================================

perf_df = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)

return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in return_cols:
    perf_df[col] = pd.to_numeric(
        perf_df[col],
        errors="coerce"
    )

# Expense ratio validation
invalid_expense = perf_df[
    (perf_df["expense_ratio_pct"] < 0.1)
    |
    (perf_df["expense_ratio_pct"] > 2.5)
]

print(
    "Invalid Expense Ratios:",
    len(invalid_expense)
)

# Return anomalies
anomalies = perf_df[
    (perf_df["return_1yr_pct"] > 100)
    |
    (perf_df["return_1yr_pct"] < -100)
]

print(
    "Performance Anomalies:",
    len(anomalies)
)

perf_df.to_csv(
    "data/processed/07_scheme_performance_clean.csv",
    index=False
)

print("✓ Scheme Performance Cleaned")


# ==================================================
# 8. INVESTOR TRANSACTIONS
# ==================================================

txn_df = pd.read_csv(
    "data/raw/08_investor_transactions.csv"
)

txn_df["transaction_date"] = pd.to_datetime(
    txn_df["transaction_date"]
)

txn_df["transaction_type"] = (
    txn_df["transaction_type"]
    .str.strip()
    .str.title()
)

txn_df = txn_df[
    txn_df["amount_inr"] > 0
]

valid_kyc = [
    "Verified",
    "Pending",
    "Rejected"
]

invalid_kyc = txn_df[
    ~txn_df["kyc_status"]
    .isin(valid_kyc)
]

print(
    "Invalid KYC Records:",
    len(invalid_kyc)
)

txn_df.to_csv(
    "data/processed/08_investor_transactions_clean.csv",
    index=False
)

print("✓ Investor Transactions Cleaned")


# ==================================================
# 9. PORTFOLIO HOLDINGS
# ==================================================

portfolio_df = pd.read_csv(
    "data/raw/09_portfolio_holdings.csv"
)

portfolio_df = portfolio_df.drop_duplicates()

portfolio_df.to_csv(
    "data/processed/09_portfolio_holdings_clean.csv",
    index=False
)

print("✓ Portfolio Holdings Cleaned")


# ==================================================
# 10. BENCHMARK INDICES
# ==================================================

benchmark_df = pd.read_csv(
    "data/raw/10_benchmark_indices.csv"
)

benchmark_df["date"] = pd.to_datetime(
    benchmark_df["date"]
)

benchmark_df = benchmark_df.drop_duplicates()

benchmark_df.to_csv(
    "data/processed/10_benchmark_indices_clean.csv",
    index=False
)

print("✓ Benchmark Indices Cleaned")


print("\n" + "=" * 60)
print("ALL 10 DATASETS CLEANED SUCCESSFULLY")
print("=" * 60)