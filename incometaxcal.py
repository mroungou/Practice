# Exercise 12: Calculate income tax for the given income by adhering to the below rules
# Taxable Income	Rate (in %)
# First $10,000	0
# Next $10,000	10
# The remaining	20
# Expected Output:

# For example, suppose the taxable income is 45000 the income tax payable is

# 10000*0% + 10000*10%  + 25000*20% = $6000.

income = 45000
tax_rate = 0.0
tax_paid = 0
marginal_tax_increment = 0

# while tax_rate <= 0.2:
#     tax_paid += marginal_tax_increment * tax_rate
#     tax_rate += 0.1
#     marginal_tax_increment += 10000

# print(tax_paid)

# the implemention above does not yield the correct answwer
print(f'Given income ${income}')

if income <= 10000:
    tax_paid = 0
elif income <= 20000:
    # no tax on the first $10k
    x = income - 10000
    # 10% tax
    tax_paid = x*0.1
else:
    # no tax on first $10k
    tax_paid = 0
    # 10% tax on the nexxt $10k
    tax_paid = 10000 * 0.1
    # remaining 20% tax
    tax_paid += (income - 20000)*0.2

print(f'Total tax paid is ${tax_paid}')
