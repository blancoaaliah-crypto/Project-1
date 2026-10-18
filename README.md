# FIN 439 Project 1 — Ulta Beauty (ULTA)

## Project overview

This project analyzes Ulta Beauty from the perspective of a buy-side investment committee that currently holds no position.

The purpose is to evaluate whether the fund should initiate a position, place the security on watch, or decline to initiate based on a defensible valuation range.

The model builds on Ulta Beauty work completed in FIN 439 Labs 6, 8, 10, and 11.

## Company and investment context

- Company: Ulta Beauty Inc.
- Ticker: ULTA
- Security: Common stock
- Decision user: Buy-side investment committee
- Investment horizon: 12–24 months
- Historical base: FY2025, ended January 31, 2026
- Projection years: FY2026E–FY2030E
- Currency: USD
- Financial statement units: USD millions
- Share basis: 44.991 million weighted-average diluted shares
- Existing position: None

The October 16, 2026 market-price observation is used for comparison, but the financial forecast remains based on earlier FY2025 statements. The model therefore requires a valuation-date refresh before a final investment decision.

## How to run

Python 3.9 or newer is recommended. No external libraries are necessary.

In the VS Code terminal:

python3 project1_ulta.py

Run the additional validation:

python3 verify_project.py

## Financial model

The Python application produces:

1. Five-year projected income statement
2. Five-year projected balance sheet
3. Five-year projected cash flow statement
4. Free cash flow to the firm
5. Enterprise-value DCF
6. Enterprise-to-equity bridge
7. Low/base/high scenario valuations
8. WACC and terminal growth sensitivity
9. Reverse DCF
10. Comparable-company valuation when verified inputs are available

## Key assumptions

The base case uses:

- Annual sales growth: 5%
- Gross margin: FY2025 ratio
- SG&A: FY2025 ratio of SG&A to gross profit
- Inventory days: FY2025 year-end calculation
- Capital expenditures: $435 million annually
- WACC: 9.1%
- Terminal growth: 2.5%
- Diluted shares: 44.991 million

These are modeling judgments, not official Ulta guidance.

## FCFF formula

FCFF = EBIT × (1 - Tax Rate)
       + Depreciation and Amortization
       - Capital Expenditures
       - Change in Operating Working Capital

The model currently uses inventory changes as the working-capital approximation.

## DCF formula

Enterprise Value = PV of Five-Year FCFF + PV of Terminal Value

Terminal Value = Final-Year FCFF × (1 + g) / (WACC - g)

Equity Value = Enterprise Value + Cash - Interest-Bearing Debt

Value Per Share = Equity Value / Diluted Shares

## Validation

Automated tests include:

- Historical income statement reconciliation
- Historical balance sheet reconciliation
- Forecast balance sheet balancing
- Cash flow and balance sheet cash reconciliation
- WACC directional sensitivity
- Terminal growth directional sensitivity
- Revenue and SG&A directional sensitivity
- Synthetic DCF known-answer calculation
- Deliberate cash-error detection

The professor's specific training-case results and the locked human-authored changed-input record remain separate requirements.

## Model limitations

The model simplifies several financial relationships:

- Other working-capital accounts remain unchanged.
- Lease assets and liabilities are held flat.
- Depreciation and amortization is approximated using historical D&A relative to PP&E.
- Share repurchases and future dilution are excluded.
- The WACC remains a working estimate from an earlier lab.
- The valuation bridge uses FY2025 cash and debt.
- Forward peer multiples require independent verification.
- The current financial basis does not fully incorporate later FY2026 information.

A balanced financial model does not automatically prove that its forecasts are economically accurate.

## Source

Ulta Beauty FY2025 Form 10-K, filed March 26, 2026.

https://www.sec.gov/Archives/edgar/data/1403568/000110465926035243/ulta-20260131x10k.htm

## Submission limitations

This is a working research application, not a final signed committee recommendation.

The student must independently verify relevant financial evidence, complete the required AI-off test and partner challenge records, run the model in a fresh environment, and record the three required presentations.