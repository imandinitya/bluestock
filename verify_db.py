import sqlite3

conn = sqlite3.connect("bluestock_mf.db")

cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM dim_fund")
print("dim_fund:", cursor.fetchone()[0])

cursor.execute("SELECT COUNT(*) FROM fact_nav")
print("fact_nav:", cursor.fetchone()[0])

cursor.execute("SELECT COUNT(*) FROM fact_transactions")
print("fact_transactions:", cursor.fetchone()[0])

cursor.execute("SELECT COUNT(*) FROM fact_performance")
print("fact_performance:", cursor.fetchone()[0])

cursor.execute("SELECT COUNT(*) FROM fact_aum")
print("fact_aum:", cursor.fetchone()[0])

cursor.execute(
    "SELECT COUNT(*) FROM portfolio_holdings"
)
print(
    "portfolio_holdings:",
    cursor.fetchone()[0]
)

cursor.execute(
    "SELECT COUNT(*) FROM benchmark_indices"
)
print(
    "benchmark_indices:",
    cursor.fetchone()[0]
)
conn.close()