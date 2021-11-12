gross_income = int(input("Enter gross income: ")) #Input statement
if gross_income == 0:   
    tax = 0
    tax_paid = "0"

elif gross_income <= 20000:
    tax = 10
    tax_paid = "2000"

elif gross_income <= 50000: 
    tax = 20
    tax_paid = "10000"
else:
    tax = 100000
    tax_paid = "30000"

print("Income     Tax%    Taxpaid")
print("%5d%8d%11s" % (gross_income, tax, tax_paid))
print("The tax paid is $", str(tax_paid)) 



