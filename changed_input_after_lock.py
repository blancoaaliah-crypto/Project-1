"""Run after recording the required AI-off prediction."""

from dataclasses import replace
from project1_ulta import BASE, model, dcf

old = model(BASE)

new_assumptions = replace(
    BASE,
    sales_growth=0.04
)

new = model(new_assumptions)

print("CHANGED INPUT: Revenue growth 5% to 4%")
print("USD millions except per share")

for label, key in [
    ("FY2030 revenue", "revenue"),
    ("FY2030 operating income", "ebit"),
    ("FY2030 FCFF", "fcff")
]:
    print(
        label,
        "Old:", round(old[-1][key], 3),
        "New:", round(new[-1][key], 3)
    )

print(
    "DCF value/share:",
    "Old:", round(dcf(old, BASE)["value_per_share"], 2),
    "New:", round(dcf(new, new_assumptions)["value_per_share"], 2)
)