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

while tax_rate <= 0.2:
    tax_paid += (marginal_tax_increment) * tax_rate
    tax_rate += 0.1
    marginal_tax_increment += 10000
    print(tax_paid)
print(tax_paid)
