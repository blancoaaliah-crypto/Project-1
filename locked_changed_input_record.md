Project 1 — Locked Changed-Input Record

Company: Ulta Beauty (ULTA)
Course: FIN 439 — AI-Augmented Finance
Model: Five-Year FCFF DCF and Three-Statement Forecast

1. Changed Input

Item

Value

Original revenue growth

5.0%

New revenue growth

4.0%

Change

−1 percentage point

Forecast period

FY2026–FY2030

WACC

9.1%

Terminal growth

2.5%

2. Prediction

Student prediction: The model will fail the changed-input test because lowering revenue growth may create problems with the model's calculations. I also expect the valuation to decrease.

AI-off prediction timestamp: Not independently verified.

Precommit evidence: Not provided.

3. Actual Test Results

Execution status: COMPLETED

The Python changed-input test executed successfully.

Metric

Original 5%

New 4%

Change

FY2030 revenue

$15,816.728M

$15,077.760M

−$738.968M

FY2030 operating income

$1,956.529M

$1,865.119M

−$91.410M

FY2030 FCFF

$1,293.899M

$1,255.303M

−$38.596M

DCF value/share

$393.71

$384.14

−$9.57

4. Expected vs. Actual Results

The predicted model failure did not occur. The Python program successfully calculated the changed-input scenario.

However, the expectation that a lower revenue growth assumption would decrease valuation was correct.

Revenue, operating income, FCFF, and intrinsic value all decreased after the growth assumption changed from 5% to 4%.

5. Failure Diagnosis

Test status: PASS — directional response

No Python error occurred during execution.

The model did not fail because lowering revenue growth is a valid input change. The financial statements and valuation calculations continued to produce results.

The original prediction confused a negative valuation impact with a technical model failure.

6. Investment Recommendation Effect

Original recommendation: Provisional do not initiate.

Recommendation after test: Provisional do not initiate.

The estimated value decreased from $393.71 to $384.14 per diluted share.

The recommendation remains unchanged because both estimated values are below the referenced market price of $592.94.

The changed-input test reinforces the model's sensitivity to slower sales growth, but does not independently establish that the investment is overvalued.

7. Validation Conclusion

The changed-input test successfully demonstrated that reducing annual revenue growth from 5% to 4% decreases projected revenue, operating income, FCFF, and estimated equity value per share.

Actual test execution: Completed in the provided Python environment.

Directional validation: PASS.

Original prediction of technical failure: Not supported by actual results.

Independent AI-off prediction and timestamp verification: I predicted that decreasing annual revenue growth from 5% to 4% would cause the model to fail because the change could affect the financial calculations. I also expected the valuation to decrease. October 17, 2026, 1:30 PM

Final conclusion: The model responded in the expected financial direction, and the provisional investment recommendation did not change.