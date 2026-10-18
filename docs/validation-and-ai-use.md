
# FIN 439 Project 1 — Validation and AI Use

**Company:** Ulta Beauty, Inc. (ULTA)  
**Project:** Corporate Finance Application  
**Analysis:** Five-Year Financial Forecast and Discounted Cash Flow Valuation

## Model and Validation Approach

I developed a five-year financial projection for Ulta Beauty covering FY2026 through FY2030 using FY2025 reported financial information.

The model connects the income statement, balance sheet, and cash flow statement and calculates free cash flow to the firm (FCFF), enterprise value, equity value, and estimated value per diluted share.

I also developed downside, base, and upside valuation scenarios and performed sensitivity testing on important financial assumptions.

### Base Assumptions

- Annual revenue growth: 5%
- WACC: 9.1%
- Terminal growth: 2.5%
- Annual capital expenditures: $435 million
- Diluted shares: 44.991 million

These represent my financial-model assumptions rather than official Ulta management forecasts.

## Validation Tests and Results

I used Python to evaluate the accuracy and consistency of the calculations.

### Historical Financial Reconciliation

I verified that revenue less cost of sales equals gross profit. I also checked the operating income calculation and confirmed that historical assets equal liabilities plus equity.

### Projected Financial Statements

The model generated five years of projected financial statements. I checked that projected balance sheets balanced and ending cash reconciled with the related cash flow calculations.

### Discounted Cash Flow Validation

I used a synthetic known-answer calculation to test the DCF formula.

The example assumed:

- Annual FCFF of $100 million
- WACC of 10%
- Terminal growth of 0%
- Cash and debt of $0
- 10 million shares

The expected enterprise value was $1,000 million, producing an estimated equity value of $100 per share.

This known-answer test confirmed the DCF calculation under the specified assumptions.

### Sensitivity Testing

I evaluated how changing financial assumptions affected estimated equity value.

The model confirmed that:

- Increasing WACC decreased estimated value.
- Increasing terminal growth increased estimated value.
- Increasing revenue growth increased estimated value.
- Increasing SG&A expense reduced estimated value.

These results followed the expected financial relationships under the tested assumptions.

### Error Detection

I introduced a deliberate $1 million error into the projected cash balance.

The independent cash-flow reconciliation detected the inconsistency.

This demonstrated that the model could identify a particular accounting error rather than simply producing financial outputs without checking them.

## DCF Scenario Results

| Scenario | Estimated Intrinsic Value/Share |
|---|---:|
| Downside | $286.39 |
| Base | $393.71 |
| Upside | $463.74 |

The October 16, 2026 reference stock price was $592.94.

Because the model used FY2025 financial information, the comparison with the later stock price requires attention to the difference in dates.

## Locked Changed-Input Record

**Company:** Ulta Beauty, Inc.  
**Date:** October 17, 2026  
**Prediction time:** 1:30 PM EDT  
**Changed input:** Annual revenue growth  
**Original value:** 5.0%  
**New value:** 4.0%  
**Forecast period:** FY2026–FY2030

### My Prediction

I predicted that changing annual revenue growth from 5% to 4% would cause the model to **FAIL** because lowering revenue growth might affect the financial calculations.

I also predicted that the company's estimated valuation would decrease.

### Test Procedure

I compared the original base-case financial forecast with a lower-growth case using the Python script `changed_input_after_lock.py`.

The remaining model assumptions were held constant.

I compared projected FY2030 revenue, operating income, free cash flow to the firm, and DCF value per diluted share.

### Actual Results

| Financial Measure | 5% Growth | 4% Growth |
|---|---:|---:|
| FY2030 revenue | $15,816.73M | $15,077.76M |
| FY2030 operating income | $1,956.53M | $1,865.12M |
| FY2030 FCFF | $1,293.90M | $1,255.30M |
| DCF value/share | $393.71 | $384.14 |

**Actual execution result: PASS**

The model successfully calculated the changed-input scenario without experiencing a technical error.

My prediction about the direction of the valuation was correct: reducing revenue growth decreased the estimated value by $9.57 per share.

However, my prediction that the program would fail was incorrect.

The model was able to adjust to the lower revenue assumption while maintaining its financial calculations.

### Investment Decision Effect

The lower-growth scenario reduced estimated intrinsic value, but it did not change my provisional investment recommendation.

Both the original $393.71 valuation and the revised $384.14 valuation were below the reference market price of $592.94.

Therefore, my recommendation remains to not initiate at that reference price.

This test demonstrated that revenue growth is an important valuation assumption and that changes in expected sales performance can materially affect estimated equity value.

## Historical Data and Methodology

I used Ulta Beauty's FY2025 Form 10-K, filed March 26, 2026, along with earlier FIN 439 lab work as the foundation for the financial model.

The enterprise-to-equity bridge uses reported cash, interest-bearing debt, and historical diluted shares.

The model includes simplifying assumptions related to working capital, operating leases, depreciation, and future share-count changes.

These assumptions are important when interpreting the results.

## Comparable-Company Analysis

I evaluated Sally Beauty Holdings (SBH) and Bath & Body Works (BBWI) as potential comparable companies.

Both companies have exposure to the beauty and personal-care industries, although their business models and operating economics differ from Ulta.

The Python project includes calculations for EV/EBITDA and P/E valuation approaches.

I considered differences in fiscal periods, valuation multiple definitions, and lease treatment when interpreting the comparable-company analysis.

## AI-Use Disclosure

I used **Codex/ChatGPT** during October 2026 to assist with this FIN 439 Project 1.

I used these tools for:

- Developing and debugging Python code
- Building and organizing financial modeling functions
- Troubleshooting errors
- Checking financial calculations and valuation outputs
- Developing validation and sensitivity tests
- Organizing research and supporting documentation
- Drafting and revising written analysis

I used Ulta's financial filings and my previous FIN 439 coursework as the financial-data foundation for the project.

My financial assumptions, changed-input prediction, interpretation of results, and investment recommendation are described throughout the project.

One important modeling consideration was recognizing that financial statements can balance mathematically even when their forecast assumptions are uncertain.

I therefore treated my valuation estimates as scenarios rather than precise predictions of future stock prices.

## Investment Conclusion

The three DCF scenarios produced estimated intrinsic values between $286.39 and $463.74 per diluted share.

These estimated values were below the October 16, 2026 reference market price of $592.94.

Based on the model assumptions, my provisional recommendation is do not initiate a position at that reference price.

I would reconsider the recommendation if more current financial information supported stronger long-term cash flows or if Ulta's share price provided an adequate margin of safety.

## Primary Source

Ulta Beauty FY2025 Form 10-K  
Fiscal year ended January 31, 2026  
Filed March 26, 2026

https://www.sec.gov/Archives/edgar/data/1403568/000110465926035243/ulta-20260131x10k.htm
