
"""
FIN 439 Project 1 - Ulta Beauty
Independent Model Validation

Run: python3 verify_project.py
"""

import csv
from pathlib import Path
from dataclasses import replace

from project1_ulta import BASE, H, model, dcf


# Locate the Project 1 folder
FOLDER = Path(__file__).resolve().parent


# TEST 1: KNOWN-ANSWER DCF

def test_dcf():

    example = [{"fcff": 100.0} for i in range(5)]

    assumptions = replace(
        BASE,
        wacc=0.10,
        terminal_growth=0.0,
        valuation_cash=0.0,
        valuation_debt=0.0,
        shares=10.0
    )

    result = dcf(example, assumptions)

    assert abs(result["enterprise_value"] - 1000) < 0.001
    assert abs(result["value_per_share"] - 100) < 0.001

    print("PASS: Synthetic known-answer DCF")


# TEST 2: HISTORICAL DATA

def test_historical():

    assert abs(
        H["revenue"] - H["cogs"] - H["gross_profit"]
    ) < 0.001

    assert abs(
        H["gross_profit"]
        - H["sga"]
        - H["preopening"]
        - H["operating_income"]
    ) < 0.001

    assert abs(
        H["total_assets"]
        - H["total_liabilities"]
        - H["equity"]
    ) < 0.001

    print("PASS: Historical financial reconciliation")


# TEST 3: FINANCIAL STATEMENTS

def test_statements():

    statements = model()

    assert len(statements) == 5

    for year in statements:

        assert abs(year["balance_sheet_gap"]) < 0.001
        assert abs(year["cash_flow_gap"]) < 0.001

    print("PASS: Five-year balance sheet checks")
    print("PASS: Cash flow reconciliation")


# TEST 4: WACC SENSITIVITY

def test_wacc():

    statements = model()

    base_value = dcf(
        statements, BASE
    )["value_per_share"]

    higher_wacc = replace(BASE, wacc=0.101)

    new_value = dcf(
        statements, higher_wacc
    )["value_per_share"]

    assert new_value < base_value

    print("PASS: WACC directional test")


# TEST 5: REVENUE GROWTH SENSITIVITY

def test_revenue():

    base_value = dcf(
        model(BASE), BASE
    )["value_per_share"]

    higher_growth = replace(
        BASE,
        sales_growth=0.06
    )

    new_value = dcf(
        model(higher_growth),
        higher_growth
    )["value_per_share"]

    assert new_value > base_value

    print("PASS: Revenue growth sensitivity")


# TEST 6: DELIBERATE CASH ERROR

def test_cash_error():

    statement = model()[0].copy()

    statement["cash"] += 1.0

    correct_cash = (
        H["cash"]
        + statement["cfo"]
        + statement["cfi"]
        + statement["cff"]
    )

    assert abs(statement["cash"] - correct_cash) > 0.9

    print("PASS: Deliberate cash error detected")


# TEST 7: COMPARABLE-COMPANY INPUTS

def test_peers():

    peer_file = FOLDER / "peer_inputs.csv"

    if not peer_file.is_file():

        print("PENDING: peer_inputs.csv not found")
        print("Expected location:", peer_file)
        return

    with peer_file.open(
        "r",
        newline="",
        encoding="utf-8-sig"
    ) as file:

        reader = csv.DictReader(file)
        peers = list(reader)
        columns = reader.fieldnames or []

    required = [
        "ticker",
        "ev_ebitda",
        "pe",
        "source_url",
        "as_of"
    ]

    if any(column not in columns for column in required):
        print("PENDING: Peer file has missing columns")
        return

    complete_peers = []

    for peer in peers:

        if all(
            (peer.get(column) or "").strip()
            for column in required
        ):
            complete_peers.append(peer)

    if len(complete_peers) < 2:
        print("PENDING: Two complete peer records needed")
        return

    try:
        for peer in complete_peers:

            ev_multiple = float(peer["ev_ebitda"])
            pe_multiple = float(peer["pe"])

            assert ev_multiple > 0
            assert pe_multiple > 0

    except (ValueError, AssertionError):
        print("FAIL: Invalid peer valuation multiple")
        return

    dates = {peer["as_of"] for peer in complete_peers}

    if len(dates) != 1:
        print("FAIL: Peer valuation dates do not match")
        return

    print("PASS: Comparable-company input format")
    print("NOTE: Independent source and definition review needed")


# TEST 8: PROFESSOR'S TRAINING CASE

def test_training_case():

    print("PENDING: Professor's published training-case answers")
    print("This is separate from the synthetic DCF test")


# RUN ALL TESTS

def main():

    print()
    print("ULTA BEAUTY - PROJECT 1 VALIDATION")
    print("----------------------------------------")

    test_dcf()
    test_historical()
    test_statements()
    test_wacc()
    test_revenue()
    test_cash_error()
    test_peers()
    test_training_case()

    print("----------------------------------------")
    print("Validation script finished")


if __name__ == "__main__":
    main()