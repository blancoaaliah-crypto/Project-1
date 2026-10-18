
# FIN 439 Project 1 — Ulta Research and Assumptions

## Research objective

Evaluate Ulta Beauty common stock for a hypothetical buy-side investment committee. The fund holds no existing position.

The decision is whether to initiate, watch/defer, or do not initiate.

## Historical evidence

Source: Ulta Beauty FY2025 10-K, filed March 26, 2026.

Fiscal year ended January 31, 2026.

https://www.sec.gov/Archives/edgar/data/1403568/000110465926035243/ulta-20260131x10k.htm

All monetary amounts are USD millions.

| Item | FY2025 |
|---|---:|
| Net sales | 12,392.820 |
| Cost of sales | 7,547.596 |
| Gross profit | 4,845.224 |
| SG&A | 3,296.411 |
| Pre-opening expenses | 15.821 |
| Operating income | 1,532.992 |
| Net income | 1,153.479 |
| Depreciation and amortization | 300.772 |
| Capital expenditures | 434.829 |
| Cash | 424.243 |
| Inventory | 2,181.127 |
| PP&E | 1,434.062 |
| Total assets | 6,999.294 |
| Interest-bearing debt | 62.287 |
| Diluted weighted-average shares | 44.991 million |

These are historical model inputs rather than projections.

## Historical reconciliation

Gross Profit = Revenue - Cost of Sales

4,845.224 = 12,392.820 - 7,547.596

Operating Income = Gross Profit - SG&A - Pre-opening

1,532.992 = 4,845.224 - 3,296.411 - 15.821

Balance sheet:

Assets = Liabilities + Equity

6,999.294 = 4,195.843 + 2,803.451

The calculations reconcile the entered historical totals, but do not replace a full independent filing review.

## Data contamination and normalization

The normalized base currently retains reported FY2025 operating results.

Possible sources of contamination include:

- Nonrecurring charges
- Changes in product mix
- Store openings and closures
- Inventory fluctuations
- Acquisition-related effects
- Depreciation and amortization classification
- Changes in share repurchases
- Stock-based compensation
- Lease accounting
- Differences between FY2025 and later reporting periods

No adjustment should be described as an independently confirmed normalization without evidence.

The code currently uses reported FY2025 operating results as its baseline. Any discovered material one-time item requires an explicit adjustment and bridge to reported figures.

## Forecast assumptions

### Revenue growth

Base assumption: 5% annually.

Basis: Lab 10 modeling assumption.

Challenge: Consumer spending, comparable sales, competitive intensity, online sales, and new-store expansion could produce a different growth path.

Evidence that would change it: Updated quarterly filings and management guidance.

### Gross margin

Base assumption: Historical FY2025 gross margin of approximately 39.1%.

Challenge: Promotional intensity, product mix, shrinkage, freight, and tariffs may affect profitability.

Evidence that would change it: Updated margin trends and management commentary.

### SG&A

Base assumption: Approximately 68.03% of gross profit.

Challenge: Marketing, payroll, technology investments, and operating leverage could change costs.

Evidence that would change it: Quarterly SG&A growth and company investment plans.

### Inventory days

Base assumption: Approximately 105.5 days.

Challenge: Year-end inventory is seasonal and may not represent average annual turnover.

Evidence that would change it: Quarterly inventory turnover and same-store sales performance.

### Capital expenditures

Base assumption: $435 million per year.

Challenge: Store expansion, technology, distribution, and automation spending may change.

Evidence that would change it: Updated capital-expenditure guidance and cash-flow statements.

### Depreciation and amortization

The model uses total FY2025 D&A as a percentage of opening PP&E.

Challenge: Total D&A includes amortization that does not necessarily correspond to PP&E depreciation.

This assumption is a simplified approximation and requires independent evaluation.

### Tax rate

Base assumption: FY2025 income taxes divided by pretax income before affiliate.

Challenge: Effective tax rates may vary with tax legislation, credits, and geographic income.

### WACC

Base assumption: 9.1%.

Basis: Earlier Lab 6 modeling exercise.

Challenge: Changes in Treasury rates, equity risk premium, beta, debt costs, and capital structure.

The assumption must be refreshed with contemporaneous market evidence for a final valuation.

### Terminal growth

Base assumption: 2.5%.

Challenge: Long-run growth must remain economically sustainable.

Terminal value should be tested under alternative growth and discount-rate assumptions.

## Valuation conventions

The model uses enterprise-value FCFF rather than FCFE.

FCFF is determined from after-tax operating income plus depreciation and amortization, less capital expenditures and changes in inventory.

Enterprise value is converted to equity value using opening cash and interest-bearing debt.

Operating leases are excluded from the debt bridge in the simplified model. This must be consistently reflected in comparable-company calculations.

## Comparable companies

Initial candidates from Lab 8:

- Sally Beauty Holdings (SBH)
- Bath & Body Works (BBWI)

These are imperfect peers because of differences in assortment, scale, distribution, and customer economics.

Both EV/EBITDA and P/E are included in the code framework. The current project requires verified contemporaneous peer inputs before reporting completed comparable valuations.

## Market comparison

Reference closing price: $592.94 on October 16, 2026.

Source: MarketWatch.

The market observation is later than the historical financial-model basis.

Therefore, comparing the two is informative as an initial screen but not an apples-to-apples valuation-date comparison.

## Research interpretation

A valuation range is preferable to a single definitive estimate because the result depends on uncertain operating margins, growth, capital reinvestment, discount rates, and terminal assumptions.

Any difference between DCF and relative valuation should be explained economically instead of resolved by simply averaging methods.