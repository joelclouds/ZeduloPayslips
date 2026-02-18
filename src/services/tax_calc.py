def ghana_tax_calculator(gross_income_pesewas: int, untaxed_bonus_pesewas: int, calc_tier_2=True, rounding="nearest"):
    """
    Calculates Ghana income tax (PAYE), employee_ssf, and net income on a monthly basis.
    
    ⚠️  ALL VALUES ARE IN PESEWAS (integers) to avoid floating point errors.
        1 Ghana Cedi (GHS) = 100 pesewas

    Args:
        gross_income_pesewas (int): Last month's gross salary in pesewas
        untaxed_bonus_pesewas (int): Last month's bonus in pesewas
        calc_tier_2 (bool): Whether to calculate Tier 2 pension contribution
        rounding (str): Rounding mode for fractional pesewas
            - "nearest" (default): Round to nearest pesewa (0.5 → 1)
            - "truncate": Always round down (floor)
            - "ceil": Always round up

    Returns:
        dict: All monetary values in pesewas (integers)
    """

    # Validate rounding mode
    if rounding not in ("nearest", "truncate", "ceil"):
        raise ValueError(f"rounding must be 'nearest', 'truncate', or 'ceil', got '{rounding}'")

    # Handle negative values
    gross_income_pesewas = max(0, gross_income_pesewas)
    untaxed_bonus_pesewas = max(0, untaxed_bonus_pesewas)

    # ---- Helper: Apply rounding based on mode ----
    def apply_rounding(value: int, divisor: int) -> int:
        """Apply rounding mode to (value / divisor)."""
        if rounding == "nearest":
            return (value + divisor // 2) // divisor
        elif rounding == "truncate":
            return value // divisor
        elif rounding == "ceil":
            return (value + divisor - 1) // divisor
        return value // divisor

    # ---- Employee SSF (5.5%) ----
    employee_ssf = apply_rounding(gross_income_pesewas * 55, 1000)

    # Taxable income after employee_ssf deduction
    taxable_income = gross_income_pesewas - employee_ssf

    # ---- PAYE Tax Bands (Monthly - Ghana 2024) ----
    income_tax = 0
    remaining = taxable_income

    tax_bands = [
        (49000, 0),       # 490.00 GHS   → 0%
        (11000, 50),      # 110.00 GHS   → 5%
        (13000, 100),     # 130.00 GHS   → 10%
        (316667, 175),    # 3166.67 GHS  → 17.5%
        (1600000, 250),   # 16000.00 GHS → 25%
        (3052000, 300),   # 30520.00 GHS → 30%
        (None, 350),      # Above        → 35%
    ]

    for band_limit, rate in tax_bands:
        if remaining <= 0:
            break

        taxable_amount = remaining if band_limit is None else min(remaining, band_limit)
        band_tax = apply_rounding(taxable_amount * rate, 1000)
        income_tax += band_tax
        remaining -= taxable_amount

    # Tier 2 pension (5%)
    tier_2 = apply_rounding(gross_income_pesewas * 5, 100) if calc_tier_2 else 0

    # Employer SSF (13%)
    employer_ssf = apply_rounding(gross_income_pesewas * 13, 100)

    # Bonus tax (5%)
    bonus_tax = apply_rounding(untaxed_bonus_pesewas * 5, 100)
    bonus = untaxed_bonus_pesewas - bonus_tax

    # Totals
    total_deduct = employee_ssf + income_tax
    total_contrib = tier_2 + employer_ssf
    net_income = gross_income_pesewas - total_deduct + bonus
    total_income = gross_income_pesewas + untaxed_bonus_pesewas

    return {
        "gross_income": gross_income_pesewas,
        "employee_ssf": employee_ssf,
        "income_tax": income_tax,
        "tier_2": tier_2,
        "employer_ssf": employer_ssf,
        "untaxed_bonus": untaxed_bonus_pesewas,
        "bonus_tax": bonus_tax,
        "total_deductions": total_deduct,
        "total_contributions": total_contrib,
        "total_income": total_income,
        "net_income": net_income,
    }


# --------------------------
# Helper Functions for Conversion
# --------------------------

def ghs_to_pesewas(ghs_amount: float) -> int:
    """Convert Ghana Cedis to pesewas (integer)."""
    return int(round(ghs_amount * 100))


def pesewas_to_ghs(pesewas_amount: int) -> float:
    """Convert pesewas to Ghana Cedis (float for display only)."""
    return pesewas_amount / 100


def format_ghs(pesewas_amount: int) -> str:
    """Format pesewas as Ghana Cedi string (e.g., 'GHS 5,000.00')."""
    return f"GHS {pesewas_amount / 100:,.2f}"


# --------------------------
# Example Usage & Comparison
# --------------------------
if __name__ == "__main__":
    print("=" * 80)
    print("GHANA TAX CALCULATOR - ROUNDING MODE COMPARISON")
    print("=" * 80)

    gross = 500000  # GHS 5,000.00
    bonus = 50000   # GHS 500.00

    print(f"\nInput: Gross = {format_ghs(gross)}, Bonus = {format_ghs(bonus)}\n")

    for mode in ("nearest", "truncate", "ceil"):
        result = ghana_tax_calculator(gross, bonus, rounding=mode)
        print(f"📌 Rounding Mode: '{mode}'")
        print(f"   Employee SSF:  {format_ghs(result['employee_ssf'])}")
        print(f"   Income Tax:    {format_ghs(result['income_tax'])}")
        print(f"   Net Income:    {format_ghs(result['net_income'])}")
        print()

    print("=" * 80)
