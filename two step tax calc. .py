annual_income = float(input("Enter the annual income: "))
tax_paid = 0.0
if annual_income <= 90000:
    tax_paid = annual_income*0.18 - 556.02
    if tax_paid<0: tax_paid=0
else:
    tax_paid=(annual_income-85528)*.32 + 14839.02
tax_paid = round (tax_paid,0) 

print("The tax is: $", str(tax_paid))





