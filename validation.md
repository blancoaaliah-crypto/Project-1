# FIN 439 Project 1 — Validation Record

## Purpose

Document how the Ulta financial model has been checked, where independent evidence is available, and which requirements remain incomplete.

## Automated tests

| Test | Status |
|---|---|
| Historical gross profit reconciliation | Implemented |
| Historical operating income reconciliation | Implemented |
| Historical balance sheet reconciliation | Implemented |
| Five-year balance sheet checks | Implemented |
| Cash flow-to-balance sheet tie | Implemented |
| WACC directional sensitivity | Implemented |
| Terminal growth directional sensitivity | Implemented |
| Revenue growth directional test | Implemented |
| SG&A directional test | Implemented |
| Deliberate $1 million cash error | Implemented |
| Synthetic constant-FCFF DCF | Implemented |
| SEC unit conversion check | Implemented |

The model stops with an AssertionError when a required accounting check fails.

## Synthetic known-answer example

Assume:

- Annual FCFF = $100 million
- WACC = 10%
- Terminal growth = 0%
- Cash = 0
- Debt = 0
- Shares = 10 million

Because perpetual FCFF is constant, enterprise value equals:

EV = 100 / 0.10 = $1,000 million

Equity value = $1,000 million

Value per share = $1,000 million / 10 million shares

Value per share = $100

The independent verification script checks these results.

This synthetic test is not the professor's published training-case reconciliation.

## Independent historical definition check

The verification script tests that selected SEC financial-statement amounts expressed in USD thousands have been correctly converted to USD millions.

Examples:

Cash: 424,243 / 1,000 = 424.243

Inventory: 2,181,127 / 1,000 = 2,181.127

Debt: 62,287 / 1,000 = 62.287

Total assets: 6,999,294 / 1,000 = 6,999.294

The independently reviewed filing locators and reviewer signoff still need to be documented.

## Directional tests

### WACC

Holding operating forecasts constant, increasing WACC should decrease present value.

### Terminal growth

Holding WACC and explicit-period FCFF constant, increasing terminal growth should increase terminal value.

### Revenue growth

Higher revenue growth should improve operating income and DCF value under the tested assumptions.

### SG&A

Higher SG&A relative to gross profit should reduce operating income and equity valuation.

These directional tests are implemented in the Python application.

## Highest-risk failure test

A $1 million error is deliberately added to projected cash.

The independent cash roll-forward should reject the incorrect balance.

This tests whether the program detects that accounting inconsistency.

It does not prove every forecast driver is economically correct.

## Pending validation requirements

### Professor's training-case reconciliation

Status: PENDING

Need to enter and compare the specific published training-case inputs and expected outputs.

### Locked changed-input record

Status: PENDING

The required human-authored, AI-off prediction must be completed and timestamped before running the changed-input case.

See locked_changed_input_record.md.

### Peer-policy verification

Status: PENDING

Both EV/EBITDA and P/E require verified input values, matched periods, and source dates.

### Partner challenge

Status: PENDING

Partner identity, actual challenge, response, and subsequent model changes must come from the real review.

### Clean environment cold run

Status: PENDING HUMAN EXECUTION

Record:

- Date and time:
- Operating system:
- Python version:
- Fresh folder or environment:
- Command used:
- Terminal output:
- Errors:
- Resolution:
- Final result:
- Student confirmation:

## Validation conclusion

The model contains working automated checks for accounting articulation and valuation direction.

Its main limitations are simplifying assumptions in depreciation, working capital, leases, cost of capital, and historical valuation-date alignment.

A passing automated test is necessary, but does not constitute full research approval.