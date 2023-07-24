# Step 1: Input values
wages = int(input("Enter wages: "))
taxable_interest = int(input("Enter taxable interest: "))
unemployment_compensation = int(input("Enter unemployment compensation: "))
status = int(input("Enter status (1=single and 2=married): "))
taxes_withheld = int(input("Enter taxes withheld: "))

# Step 2: Identify deduction amount based on status
if status == 1:
    deduction = 12000
elif status == 2:
    deduction = 24000
else:
    status = 1  # Set status to 1 if not input as 1 or 2
    deduction = 12000

# Step 3: Calculate AGI (Adjusted Gross Income)
agi = wages + taxable_interest + unemployment_compensation

# Step 4: Calculate taxable income
taxable_income = agi - deduction
if taxable_income < 0:
    taxable_income = 0

# Step 5: Calculate tax amount
if status == 1:
    if taxable_income <= 10000:
        tax_amount = round(taxable_income * 0.10)
    elif taxable_income <= 40000:
        tax_amount = round(1000 + (taxable_income - 10000) * 0.12)
    elif taxable_income <= 85000:
        tax_amount = round(4600 + (taxable_income - 40000) * 0.22)
    else:
        tax_amount = round(14500 + (taxable_income - 85000) * 0.24)
else:
    if taxable_income <= 20000:
        tax_amount = round(taxable_income * 0.10)
    elif taxable_income <= 80000:
        tax_amount = round(2000 + (taxable_income - 20000) * 0.12)
    else:
        tax_amount = round(9200 + (taxable_income - 80000) * 0.22)

# Step 6: Calculate amount due or refund
amount_due_or_refund = tax_amount - taxes_withheld

# Step 7: Output AGI, deduction, taxable income, tax amount, and amount due or refund
print("AGI: $" + str(agi))
print("Deduction: $" + str(deduction))
print("Taxable income: $" + str(taxable_income))
print("Federal Tax: $" + str(tax_amount))

if amount_due_or_refund >= 0:
    print("Tax due: $" + str(amount_due_or_refund))
else:
    print("Tax refund: $" + str(abs(amount_due_or_refund)))
