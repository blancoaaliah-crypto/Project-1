FIN 439 Project 1 — Submission Manifest

Company: Ulta Beauty (ULTA)
Course: FIN 439 — AI-Augmented Finance
Project: Corporate Finance Application

1. Project Overview

This project evaluates whether a buy-side investment committee should initiate a position in Ulta Beauty. It includes financial forecasting, discounted cash flow valuation, scenario analysis, sensitivity testing, and investment recommendations.

2. Python Files

project1_ulta.py — Main Python model containing the five-year financial forecast, DCF valuation, scenario analysis, and sensitivity testing.

verify_project.py — Independent validation script that checks financial calculations, accounting relationships, and valuation sensitivity.

changed_input_after_lock.py — Tests the effect of reducing annual revenue growth from 5% to 4%.

3. Documentation

README.md — Explains the project's purpose, assumptions, methodology, limitations, and instructions for running the code.

locked_changed_input_record.md — Documents the AI-off prediction, changed input, actual results, and effect on the investment recommendation.

MANIFEST.md — Identifies and explains the project deliverables.

4. Financial Outputs

The main Python model generates the following files in the outputs/ folder:

results.json — Valuation results, assumptions, scenarios, and validation information.

three_statements.csv — Five-year projected financial statements.

wacc_growth_grid.csv — Valuation sensitivity to WACC and terminal growth.

validation_results.json — Automated validation results.

executive_summary.md — Summary of the model's valuation results.

5. Video Presentations

Video 1 — Research Evolution
https://youtu.be/6-V590gw30k

Explains how the research developed from Edition A to Edition B and how additional financial analysis influenced the investment recommendation.

Video 2 — Codebase Walkthrough
https://youtu.be/W9n583YVGWY

Demonstrates the Python financial model, validation tests, and changed-input sensitivity analysis.

Video 3 — Investment Committee Presentation
https://youtu.be/BxLCRPOUgcs

Presents the final investment recommendation, valuation scenarios, risks, limitations, and conditions for reconsidering the investment.

Each presentation has a corresponding transcript.

6. Investment Recommendation

The model estimates the following values per share:

Scenario

Estimated Value

Downside

$286.39

Base

$393.71

Upside

$463.74

At the October 16, 2026 reference price of $592.94, the provisional recommendation is do not initiate a position.

7. Limitations

The financial model uses FY2025 historical financial information and simplified assumptions concerning working capital, depreciation, leases, and future growth.

Some independent validation and comparable-company checks remain pending. The model's results should be refreshed and verified before making a final investment decision.
