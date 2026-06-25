-- 1. Top 5 Funds by AUM

SELECT
    scheme_name,
    aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;


-- 2. Average NAV per Month

SELECT
    strftime('%Y-%m', date) AS month,
    AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY month
ORDER BY month;


-- 3. SIP Transactions Count

SELECT
    transaction_type,
    COUNT(*) AS transaction_count
FROM fact_transactions
GROUP BY transaction_type;


-- 4. Transactions by State

SELECT
    state,
    COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;


-- 5. Funds with Expense Ratio Less Than 1%

SELECT
    scheme_name,
    expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;


-- 6. Top 5 Performing Funds (1-Year Return)

SELECT
    scheme_name,
    return_1yr_pct
FROM fact_performance
ORDER BY return_1yr_pct DESC
LIMIT 5;


-- 7. Average Expense Ratio by Fund House

SELECT
    fund_house,
    AVG(expense_ratio_pct) AS avg_expense_ratio
FROM fact_performance
GROUP BY fund_house
ORDER BY avg_expense_ratio;


-- 8. Transaction Amount by Payment Mode

SELECT
    payment_mode,
    SUM(amount_inr) AS total_amount
FROM fact_transactions
GROUP BY payment_mode
ORDER BY total_amount DESC;


-- 9. Portfolio Allocation by Sector

SELECT
    sector,
    SUM(weight_pct) AS total_weight
FROM portfolio_holdings
GROUP BY sector
ORDER BY total_weight DESC;


-- 10. Benchmark Index Average Close Value

SELECT
    index_name,
    AVG(close_value) AS avg_close
FROM benchmark_indices
GROUP BY index_name;