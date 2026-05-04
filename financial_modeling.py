# SimpleInterest:Principal of R4500 at 7% p.a for 5 years.
# Model: I=P*r*t

simple_interest = 4500 * 0.07 * 5
print(simple_interest)


# Compound Interest: Principal of R12,000 at 6.5% for 8 years.
# Model: A = P(1 + i)^n

compound_interest = 12000(1 + 0.065/8)**8*8
print(compound_interest)

# Hire Purchase: Cost R22,000, 15% deposit, 11% SI, 3 years.
# Model: A = [Pbal(1 + rt)] ÷ 36

hire_purchase =  [22000 * 1.]
print(hire_purchase)
# Inflation Analysis: Present cost R1,550, 5.5% rate, 12 years.
# Model: A = P(1 + i)^n

inflation_analysis = 1550(1 + 0.055)**12
print(inflation_analysis)


# Reducing Depreciation: R480,000 at 18% for 6 years.
# Model: A = P(1 − i)^n

reduction_depreciation = 480000(1 - 0.18)**6
print(reduction_depreciation)

# Quarterly Compounding: R95,000 at 9% for 4 years.
# Model: A = P(1 + r4)4t

quarterly_coumpounding = 95000(1 + 0.09/4)**4*4
print(quarterly_coumpounding)

#Loan Accrual: R30,000 at 14% for 1 year.
# Model: I = [P(1 + r12 )12] − P

loan_accural = 30000 * (1 + 12 * 0.12)**12 -30000
print(loan_accural)

# Capital Doubling Time: R15,000 at 12.5% Simple Interest.
# Model: t = I/(P × r)

capital_doubling_time = 0.125 / (15000 * 0.125)
print(capital_doubling_time)

# Effective Annual Rate: 13.2% Nominal monthly to EAR.
# Model: ief f = (1 + inom/m)^(m) − 1

effective_annual_rate = (1 + )
print(effective_annual_rate)

# Fund Growth: R2,500,000 at 15% semi-annually for 10y.
# Model: A = P(1 + r2)^2t

fund_growth = 2500000(1 + 0.15*2)**2*10
print(fund_growth)
