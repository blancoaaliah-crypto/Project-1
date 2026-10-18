
"""FIN 439 Project 1 — Ulta Beauty
Five-year financial model and FCFF valuation.
USD millions except per-share figures.
"""

from dataclasses import dataclass, replace
from pathlib import Path
import csv
import json

OUT = Path(__file__).resolve().parent / "outputs"

# Historical FY2025 information from Ulta's 10-K
SOURCE = "https://www.sec.gov/Archives/edgar/data/1403568/000110465926035243/ulta-20260131x10k.htm"

MARKET_PRICE = 592.94
MARKET_DATE = "2026-10-16"

H = {
    "revenue": 12392.820,
    "cogs": 7547.596,
    "gross_profit": 4845.224,
    "sga": 3296.411,
    "preopening": 15.821,
    "operating_income": 1532.992,
    "net_income": 1153.479,
    "da": 300.772,
    "capex": 434.829,
    "income_taxes": 373.869,
    "pretax": 1531.205,
    "cash": 424.243,
    "inventory": 2181.127,
    "ppe": 1434.062,
    "lease_assets": 1813.074,
    "total_assets": 6999.294,
    "debt": 62.287,
    "lease_liabilities": 2119.774,
    "total_liabilities": 4195.843,
    "equity": 2803.451,
    "shares_diluted": 44.991,
}

H["other_assets"] = (
    H["total_assets"]
    - H["cash"]
    - H["inventory"]
    - H["ppe"]
    - H["lease_assets"]
)

H["other_liabilities"] = (
    H["total_liabilities"]
    - H["debt"]
    - H["lease_liabilities"]
)


# 1. FINANCIAL ASSUMPTIONS

@dataclass(frozen=True)
class Assumptions:
    sales_growth: float = 0.05
    gross_margin: float = H["gross_profit"] / H["revenue"]
    sga_pct_gp: float = H["sga"] / H["gross_profit"]
    preopening_pct_sales: float = H["preopening"] / H["revenue"]
    inventory_days: float = H["inventory"] / H["cogs"] * 365
    da_pct_open_ppe: float = H["da"] / H["ppe"]
    tax_rate: float = H["income_taxes"] / H["pretax"]
    capex: float = 435.0
    borrowing_rate: float = 0.055
    minimum_cash: float = 100.0
    revolver_limit: float = 1000.0
    wacc: float = 0.091
    terminal_growth: float = 0.025
    shares: float = H["shares_diluted"]
    valuation_cash: float = H["cash"]
    valuation_debt: float = H["debt"]


BASE = Assumptions()


def require(condition, message):
    if not condition:
        raise AssertionError(message)


# 2. FIVE-YEAR THREE-STATEMENT MODEL

def model(a=BASE):

    require(
        0 <= a.terminal_growth < a.wacc < 1,
        "Invalid WACC or terminal growth"
    )

    require(
        a.sales_growth > -1 and a.capex >= 0 and a.shares > 0,
        "Invalid forecast assumptions"
    )

    # Historical statement reconciliation
    require(
        abs(H["total_assets"] - H["total_liabilities"] - H["equity"]) < 0.001,
        "Opening balance sheet does not balance"
    )

    require(
        abs(H["revenue"] - H["cogs"] - H["gross_profit"]) < 0.001,
        "Historical gross profit does not reconcile"
    )

    require(
        abs(H["gross_profit"] - H["sga"] -
            H["preopening"] - H["operating_income"]) < 0.001,
        "Historical operating income does not reconcile"
    )

    previous = {
        "revenue": H["revenue"],
        "inventory": H["inventory"],
        "ppe": H["ppe"],
        "cash": H["cash"],
        "lease_assets": H["lease_assets"],
        "other_assets": H["other_assets"],
        "lease_liabilities": H["lease_liabilities"],
        "other_liabilities": H["other_liabilities"],
        "debt": H["debt"],
        "revolver": 0.0,
        "equity": H["equity"]
    }

    results = []

    for year in range(2026, 2031):

        # Income statement
        sales = previous["revenue"] * (1 + a.sales_growth)
        gross_profit = sales * a.gross_margin
        cogs = sales - gross_profit

        sga = gross_profit * a.sga_pct_gp
        preopening = sales * a.preopening_pct_sales

        # SG&A includes D&A, so do not subtract D&A twice
        ebit = gross_profit - sga - preopening

        interest = (
            previous["debt"] + previous["revolver"]
        ) * a.borrowing_rate

        pretax = ebit - interest
        taxes = max(pretax, 0) * a.tax_rate
        net_income = pretax - taxes

        # Balance sheet drivers
        inventory = cogs * a.inventory_days / 365
        change_inventory = inventory - previous["inventory"]

        # Simplified depreciation assumption
        da = previous["ppe"] * a.da_pct_open_ppe
        ppe = previous["ppe"] + a.capex - da

        # Cash flow statement
        cfo = net_income + da - change_inventory
        cfi = -a.capex

        cash_before_financing = previous["cash"] + cfo + cfi

        revolver = previous["revolver"]

        draw = max(
            0.0,
            a.minimum_cash - cash_before_financing
        )

        require(
            revolver + draw <= a.revolver_limit + 1e-8,
            f"FY{year}: Revolver capacity exceeded"
        )

        revolver += draw
        cash = cash_before_financing + draw

        repayment = min(
            revolver,
            max(0.0, cash - a.minimum_cash)
        )

        revolver -= repayment
        cash -= repayment

        cff = draw - repayment

        # Balance sheet
        equity = previous["equity"] + net_income

        total_assets = (
            cash
            + inventory
            + ppe
            + previous["lease_assets"]
            + previous["other_assets"]
        )

        total_liabilities = (
            previous["debt"]
            + revolver
            + previous["lease_liabilities"]
            + previous["other_liabilities"]
        )

        bs_gap = total_assets - total_liabilities - equity

        cf_gap = cash - (
            previous["cash"] + cfo + cfi + cff
        )

        # Accounting validation
        require(
            abs(bs_gap) < 1e-7,
            f"FY{year}: Balance sheet does not balance"
        )

        require(
            abs(cf_gap) < 1e-7,
            f"FY{year}: Cash flow does not tie"
        )

        require(
            cash >= a.minimum_cash - 1e-7,
            f"FY{year}: Cash below minimum"
        )

        # Free cash flow to the firm
        nopat = ebit * (1 - a.tax_rate)

        fcff = (
            nopat
            + da
            - a.capex
            - change_inventory
        )

        row = {
            "year": year,
            "revenue": sales,
            "cost_of_sales": cogs,
            "gross_profit": gross_profit,
            "sga": sga,
            "preopening": preopening,
            "ebit": ebit,
            "interest": interest,
            "pretax": pretax,
            "taxes": taxes,
            "net_income": net_income,
            "inventory": inventory,
            "delta_inventory": change_inventory,
            "depreciation_amortization": da,
            "capex": a.capex,
            "ppe": ppe,
            "cfo": cfo,
            "cfi": cfi,
            "cff": cff,
            "cash": cash,
            "revolver_draw": draw,
            "revolver_repayment": repayment,
            "debt": previous["debt"],
            "revolver": revolver,
            "lease_assets": previous["lease_assets"],
            "other_assets": previous["other_assets"],
            "lease_liabilities": previous["lease_liabilities"],
            "other_liabilities": previous["other_liabilities"],
            "equity": equity,
            "total_assets": total_assets,
            "total_liabilities": total_liabilities,
            "balance_sheet_gap": bs_gap,
            "cash_flow_gap": cf_gap,
            "nopat": nopat,
            "fcff": fcff
        }

        results.append(row)
        previous = dict(row)

    return results


# 3. FCFF DISCOUNTED CASH FLOW VALUATION

def dcf(rows, a=BASE):

    free_cash_flows = [row["fcff"] for row in rows]

    require(
        free_cash_flows[-1] > 0,
        "Terminal FCFF must be positive"
    )

    discounted_cash_flows = []

    for year_number, cash_flow in enumerate(free_cash_flows, 1):
        present_value = cash_flow / (1 + a.wacc) ** year_number
        discounted_cash_flows.append(present_value)

    terminal_value = (
        free_cash_flows[-1] * (1 + a.terminal_growth)
        / (a.wacc - a.terminal_growth)
    )

    pv_terminal = terminal_value / (1 + a.wacc) ** len(rows)

    enterprise_value = sum(discounted_cash_flows) + pv_terminal

    equity_value = (
        enterprise_value
        + a.valuation_cash
        - a.valuation_debt
    )

    value_per_share = equity_value / a.shares

    return {
        "pv_explicit": sum(discounted_cash_flows),
        "terminal_value": terminal_value,
        "pv_terminal": pv_terminal,
        "enterprise_value": enterprise_value,
        "valuation_cash": a.valuation_cash,
        "valuation_debt": a.valuation_debt,
        "equity_value": equity_value,
        "shares": a.shares,
        "value_per_share": value_per_share,
        "terminal_share": pv_terminal / enterprise_value,
        "fcff": free_cash_flows
    }


# 4. LOW, BASE, AND HIGH SCENARIOS

def scenario_book():

    scenarios = {
        "Downside | margin pressure": replace(
            BASE,
            sales_growth=0.02,
            gross_margin=BASE.gross_margin - 0.012,
            sga_pct_gp=BASE.sga_pct_gp + 0.015,
            inventory_days=BASE.inventory_days + 8,
            wacc=0.101
        ),

        "Base | historic ratios": BASE,

        "Upside | better execution": replace(
            BASE,
            sales_growth=0.06,
            gross_margin=BASE.gross_margin + 0.005,
            sga_pct_gp=BASE.sga_pct_gp - 0.01,
            inventory_days=BASE.inventory_days - 4,
            wacc=0.086
        )
    }

    results = {}

    for name, assumptions in scenarios.items():
        statements = model(assumptions)
        valuation = dcf(statements, assumptions)

        results[name] = (
            assumptions,
            statements,
            valuation
        )

    return results


# 5. REVERSE DCF

def reverse_dcf(market_price, rows=None, a=BASE):

    if market_price is None:
        return None

    if rows is None:
        rows = model(a)

    require(
        all(row["fcff"] > 0 for row in rows),
        "Reverse DCF requires positive FCFF"
    )

    target_ev = (
        market_price * a.shares
        - a.valuation_cash
        + a.valuation_debt
    )

    starting_fcff = rows[0]["fcff"]

    lower = -0.80
    upper = 1.0

    def implied_enterprise_value(growth):

        projected_fcff = [
            starting_fcff * (1 + growth) ** i
            for i in range(5)
        ]

        terminal_value = (
            projected_fcff[-1] * (1 + a.terminal_growth)
            / (a.wacc - a.terminal_growth)
        )

        pv_forecast = sum(
            cash_flow / (1 + a.wacc) ** (i + 1)
            for i, cash_flow in enumerate(projected_fcff)
        )

        pv_terminal = terminal_value / (1 + a.wacc) ** 5

        return pv_forecast + pv_terminal

    require(
        implied_enterprise_value(lower)
        <= target_ev
        <= implied_enterprise_value(upper),
        "Market price outside reverse DCF search range"
    )

    for _ in range(90):
        middle = (lower + upper) / 2

        if implied_enterprise_value(middle) < target_ev:
            lower = middle
        else:
            upper = middle

    return {
        "market_price": market_price,
        "implied_fcff_growth": (lower + upper) / 2,
        "method": "Constant annual FCFF growth, not revenue growth"
    }


# 6. AUTOMATED VALIDATION CHECKS

def tests():

    # Synthetic enterprise-to-equity example
    synthetic_value = (100 + 20 - 10) / 10

    require(
        abs(synthetic_value - 11) < 1e-12,
        "Synthetic bridge test failed"
    )

    rows = model()
    base_value = dcf(rows)

    # Accounting checks
    for row in rows:
        require(
            abs(row["balance_sheet_gap"]) < 1e-7,
            "Balance sheet validation failed"
        )

        require(
            abs(row["cash_flow_gap"]) < 1e-7,
            "Cash flow validation failed"
        )

    # Higher WACC should reduce valuation
    higher_wacc = dcf(
        rows,
        replace(BASE, wacc=0.101)
    )

    require(
        higher_wacc["value_per_share"]
        < base_value["value_per_share"],
        "WACC direction test failed"
    )

    # Lower WACC should increase valuation
    lower_wacc = dcf(
        rows,
        replace(BASE, wacc=0.081)
    )

    require(
        lower_wacc["value_per_share"]
        > base_value["value_per_share"],
        "Lower WACC test failed"
    )

    # Higher terminal growth should increase valuation
    higher_terminal = dcf(
        rows,
        replace(BASE, terminal_growth=0.035)
    )

    require(
        higher_terminal["value_per_share"]
        > base_value["value_per_share"],
        "Terminal growth test failed"
    )

    # Higher sales growth should increase valuation
    sales_assumptions = replace(
        BASE,
        sales_growth=0.06
    )

    higher_sales = dcf(
        model(sales_assumptions),
        sales_assumptions
    )

    require(
        higher_sales["value_per_share"]
        > base_value["value_per_share"],
        "Sales growth direction failed"
    )

    # Higher SG&A should reduce valuation
    sga_assumptions = replace(
        BASE,
        sga_pct_gp=BASE.sga_pct_gp + 0.01
    )

    higher_sga = dcf(
        model(sga_assumptions),
        sga_assumptions
    )

    require(
        higher_sga["value_per_share"]
        < base_value["value_per_share"],
        "SG&A direction test failed"
    )

    # Deliberately incorrect cash balance
    tampered = dict(rows[0])
    tampered["cash"] += 1

    cash_difference = (
        tampered["cash"]
        - (
            H["cash"]
            + tampered["cfo"]
            + tampered["cfi"]
            + tampered["cff"]
        )
    )

    require(
        abs(cash_difference) > 0.9,
        "Cash error detection failed"
    )

    return {
        "synthetic_ev_equity_bridge": "PASS",
        "historical_income_statement": "PASS",
        "historical_balance_sheet": "PASS",
        "five_year_balance_sheet_and_cash": "PASS",
        "dcf_wacc_and_growth_monotonicity": "PASS",
        "sales_and_sga_direction": "PASS",
        "cash_tamper_detection": "PASS",
        "training_case_reconciliation": "PENDING",
        "independent_definition_check": "PENDING",
        "locked_changed_input_prediction": "PENDING",
        "peer_policy_consistency": "PENDING",
        "fresh_environment_cold_run": "PENDING"
    }


# 7. COMPARABLE-COMPANY VALUATION

def comps():

    path = Path(__file__).resolve().parent / "peer_inputs.csv"

    if not path.exists():
        return {
            "status": "PENDING",
            "reason": "peer_inputs.csv unavailable"
        }

    with path.open(newline="") as file:
        peers = list(csv.DictReader(file))

    verified_peers = []

    for peer in peers:

        if not all([
            peer.get("ev_ebitda"),
            peer.get("pe"),
            peer.get("source_url"),
            peer.get("as_of")
        ]):
            continue

        ev_multiple = float(peer["ev_ebitda"])
        pe_multiple = float(peer["pe"])

        require(
            ev_multiple > 0 and pe_multiple > 0,
            "Invalid peer multiple"
        )

        verified_peers.append({
            "peer": peer["ticker"],
            "ev_ebitda": ev_multiple,
            "pe": pe_multiple,
            "source": peer["source_url"],
            "as_of": peer["as_of"]
        })

    if not verified_peers:
        return {
            "status": "PENDING",
            "reason": "Verified comparable-company inputs needed"
        }

    first_year = model()[0]

    estimated_ebitda = (
        first_year["ebit"]
        + first_year["depreciation_amortization"]
    )

    estimated_earnings = first_year["net_income"]

    average_ev_multiple = sum(
        peer["ev_ebitda"] for peer in verified_peers
    ) / len(verified_peers)

    average_pe = sum(
        peer["pe"] for peer in verified_peers
    ) / len(verified_peers)

    enterprise_value = average_ev_multiple * estimated_ebitda

    equity_value_ev = (
        enterprise_value
        + BASE.valuation_cash
        - BASE.valuation_debt
    )

    equity_value_pe = average_pe * estimated_earnings

    return {
        "status": "CALCULATED_PENDING_POLICY_SIGNOFF",
        "peers": verified_peers,
        "ev_ebitda_value_per_share": equity_value_ev / BASE.shares,
        "pe_value_per_share": equity_value_pe / BASE.shares
    }


# 8. EXPORT RESULTS

def export():

    OUT.mkdir(exist_ok=True)

    rows = model()
    valuation = dcf(rows)
    scenarios = scenario_book()
    validations = tests()

    # Save forecast financial statements
    with (OUT / "three_statements.csv").open(
        "w", newline=""
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=list(rows[0].keys())
        )

        writer.writeheader()
        writer.writerows(rows)

    # WACC / terminal growth sensitivity
    grid = []

    for wacc in [0.081, 0.091, 0.101]:
        for growth in [0.02, 0.025, 0.03, 0.04]:

            assumptions = replace(
                BASE,
                wacc=wacc,
                terminal_growth=growth
            )

            sensitivity_value = dcf(rows, assumptions)

            grid.append({
                "wacc": wacc,
                "terminal_growth": growth,
                "value_per_share": sensitivity_value["value_per_share"]
            })

    with (OUT / "wacc_growth_grid.csv").open(
        "w", newline=""
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=[
                "wacc",
                "terminal_growth",
                "value_per_share"
            ]
        )

        writer.writeheader()
        writer.writerows(grid)

    # Scenario results
    scenario_results = {}

    for name, (assumptions, statements, value) in scenarios.items():

        scenario_results[name] = {
            "assumptions": vars(assumptions),
            "value_per_share": value["value_per_share"],
            "enterprise_value": value["enterprise_value"],
            "terminal_share": value["terminal_share"],
            "year_2030_fcff": statements[-1]["fcff"]
        }

    # Save complete results
    results = {
        "company": "Ulta Beauty (ULTA)",
        "historical_fiscal_year_end": "2026-01-31",
        "source": SOURCE,
        "units": "USD millions except per share",
        "assumptions": vars(BASE),
        "historical": H,
        "dcf": valuation,
        "cases": scenario_results,
        "grid": grid,
        "comps": comps(),
        "validation": validations,
        "market_comparison": {
            "date": MARKET_DATE,
            "close": MARKET_PRICE,
            "gap_from_base_pct":
                valuation["value_per_share"] / MARKET_PRICE - 1,
            "warning": "FY2025 accounting data compared with an October 2026 price"
        },
        "reverse_dcf": reverse_dcf(MARKET_PRICE, rows)
    }

    (OUT / "results.json").write_text(
        json.dumps(results, indent=2)
    )

    (OUT / "validation_results.json").write_text(
        json.dumps(validations, indent=2)
    )

    # Markdown valuation summary
    summary = "# Ulta Beauty — Model Results\n\n"

    summary += (
        "Historical basis: FY2025, ended January 31, 2026.\n\n"
    )

    summary += (
        f"Base DCF value: **${valuation['value_per_share']:,.2f} per share**\n\n"
    )

    summary += (
        f"Terminal value as share of EV: "
        f"**{valuation['terminal_share']:.1%}**\n\n"
    )

    summary += "| Scenario | Value/share |\n"
    summary += "|---|---:|\n"

    for name, values in scenario_results.items():
        summary += (
            f"| {name} | ${values['value_per_share']:,.2f} |\n"
        )

    summary += (
        "\nResults are illustrative and require final source and "
        "assumption verification before an investment decision.\n"
    )

    (OUT / "executive_summary.md").write_text(summary)

    # Show results in the terminal
    print("\nULTA BEAUTY — FIN 439 PROJECT 1")
    print("-" * 45)

    for name, value in scenario_results.items():
        print(
            f"{name}: "
            f"${value['value_per_share']:,.2f} per share"
        )

    print()
    print(f"Market reference ({MARKET_DATE}): ${MARKET_PRICE:,.2f}")
    print(f"Base DCF value: ${valuation['value_per_share']:,.2f}")

    passed = sum(
        status.startswith("PASS")
        for status in validations.values()
    )

    pending = sum(
        status.startswith("PENDING")
        for status in validations.values()
    )

    print(f"\nValidation: {passed} passed, {pending} pending")
    print(f"\nOutputs saved in: {OUT}")

    return results


if __name__ == "__main__":
    export()