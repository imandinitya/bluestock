import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "sqlite:///bluestock_mf.db"
)

fund_df = pd.read_csv(
    "data/processed/01_fund_master_clean.csv"
)

nav_df = pd.read_csv(
    "data/processed/02_nav_history_clean.csv"
)

perf_df = pd.read_csv(
    "data/processed/07_scheme_performance_clean.csv"
)

txn_df = pd.read_csv(
    "data/processed/08_investor_transactions_clean.csv"
)

aum_df = pd.read_csv(
    "data/processed/03_aum_by_fund_house_clean.csv"
)
portfolio_df = pd.read_csv(
    "data/processed/09_portfolio_holdings_clean.csv"
)

benchmark_df = pd.read_csv(
    "data/processed/10_benchmark_indices_clean.csv"
) 
fund_df.to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False
)

nav_df.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

txn_df.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

perf_df.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

aum_df.to_sql(
    "fact_aum",
    engine,
    if_exists="replace",
    index=False
)

portfolio_df.to_sql(
    "portfolio_holdings",
    engine,
    if_exists="replace",
    index=False
)

benchmark_df.to_sql(
    "benchmark_indices",
    engine,
    if_exists="replace",
    index=False
)

print("Database loaded successfully!")