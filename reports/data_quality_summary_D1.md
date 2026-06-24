## Day One Data Quality Overview
## Dataset Overview
Out of ten supplied CSV files along with five active NAV sources, every one made it into Pandas without issue. Examination followed, looking at structure, variable kinds, glimpses of actual entries, gaps in data, and repeated rows each checked thoroughly.

## Key Findings
1. Fund Master (01_fund_master.csv)
Contains 40 mutual fund schemes and 15 attributes.
Starts with details like AMFI code, then lists the managing firm behind each investment plan. Followed by its broad group type, along with a more specific division within that class. Each entry shows the standard used for performance comparison. Cost factor appears next, stated as a percentage tied to management expenses. A named individual oversees the fund's decisions. Ends with how much uncertainty is linked to the investment level.
Checking revealed complete data. Nothing absent found during review.
Checking completed - no matching entries identified.
2. NAV History (02_nav_history.csv)
With 46,000 past net asset value entries logged for every plan included.
Each entry includes an AMFI identifier alongside a specific day plus its corresponding net asset value.
Checking confirmed all entries present. Data complete across fields.
Checking showed no repeated entries. One-of-a-kind results came up each time.
Though appearing as text, the date entries must become proper timestamps when tidied up. Conversion happens mid-process, shifting format from character sequence to time object. A transformation step handles this shift carefully, ensuring values reflect actual moments. String-based dates turn into structured points on a timeline through parsing routines. Only after reformatting do they act like real calendar marks inside datasets.
3. AUM by Fund House
Contains 90 records of fund house AUM information.
Checking confirmed no gaps in data. Still, every entry appears just once. Nothing repeated. All spots filled without extras showing up.
Date column requires datetime conversion.
4. Monthly SIP Inflows
Contains 48 monthly observations.
Detected 12 missing values in the yoy_growth_pct column.
Some entries are blank - probably because data needed for annual comparisons wasn’t accessible during those periods.
Checking completed - no matching entries identified.
5. Category Inflows (05_category_inflows.csv)
A total of 144 entries appear, spread through different types of mutual funds.
Checking confirmed no gaps in data. Still, every entry appears just once.
6. Industry Folio Count
Contains 21 observations of industry-wide folio statistics.
Checking confirmed all entries present. Every record appears only once.
7. Scheme Performance (07_scheme_performance.csv)
Forty performance entries exist at the scheme level.
Performance data covers risk-adjusted returns like alpha and beta. One finds the Sharpe and Sortino ratios included here. Asset size appears as total AUM reported. Costs show up through the expense ratio figure. Historical rankings offer context alongside these numbers. Ratings reflect evaluations from recognized sources. Metrics reappear across time periods for consistency.
Checking confirmed all entries present. Every record appears once only.
8. Investor Transactions (08_investor_transactions.csv)
Contains 32,778 transaction records.
Investor age and background appear alongside how deals are structured. Transaction specifics show up with methods used to pay. Payment choices link directly to verification steps completed. Status of identity checks ties back to who invested.
Checking confirmed every entry present, none repeated. Data appears complete without gaps or double entries.
Midway through data prep, the transaction date field must shift into datetime format. Processing this step early avoids mismatched time readings later on. Converting at this stage supports smoother merges downstream. A wrong type here breaks sequence tracking across records.
9. Portfolio Holdings (09_portfolio_holdings.csv)
Contains 322 portfolio holding records.
Stock-level allocation forms part of the data, along with details on sectors. Information about market value is included, while the portfolio's date appears alongside. Each element contributes without overlap, ensuring clarity through separation. Timing and composition remain visible at a glance.
Checking confirmed all entries present. Every record appears only once.
10. Benchmark Indices (10_benchmark_indices.csv)
Contains 8,050 benchmark index observations.
The listing shows the index title alongside its final traded price.
Checking confirmed all entries present. Every record appears only once.
Date column requires datetime conversion.
Live NAV Data
Live NAV data retrieved from MFAPI
HDFC Top 100 Direct
SBI Bluechip
ICICI Bluechip
Nippon Large Cap
Axis Bluechip
Kotak Bluechip
Each dataset ended up stored properly in CSV format, with every file holding the complete information required
Historical NAV values
No missing values
No duplicate records
Fund Master Exploration
Categories Identified
Equity
Debt
Other scheme categories available in the dataset
Available Attributes
Fund House
Scheme Name
Category
Sub Category
Benchmark
Expense Ratio
Fund Manager
Risk Category
SEBI Category Code
Risk Categories
Low
Moderate
Very High
AMFI Code Validation
Checking took place across:
01_fund_master.csv
02_nav_history.csv
## Results:
Some funds lack an official identifier number - zero cases found so far
Every scheme listed in the fund master data comes with matching NAV history entries. Though some might expect gaps, each one shows full alignment. Where a scheme exists, its daily values appear without exception. Not a single entry lacks this paired record. Matching details follow wherever a fund is found. Full coverage appears across every case observed.
## Overall Assessment
High-quality data appear throughout these collections
One check showed no repeated entries found.
A few gaps appear - just twelve entries are absent from the year-on-year SIP growth data.
Consistent schema across datasets.
Complete AMFI code coverage between master and NAV history datasets.
Although the dataset works for initial processing, it fits better once refined on Day 2. Following cleanup, structural adjustments prepare it for storage. Once shaped correctly, insertion into a SQLite system becomes straightforward. After formatting steps finish, the information flows smoothly into the database setup.