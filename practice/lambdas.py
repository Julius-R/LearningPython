item_total = 45.72
tax_rate = 7.25
sales_tax_amount = lambda item_total, tax_rate: round(item_total * (tax_rate/100), 2)

def calculate_total(item_total, tax_rate):
    total_price = item_total + sales_tax_amount(item_total, tax_rate)
    return total_price

print('Your total is: $' + str(calculate_total(item_total, tax_rate)))
print('Tax was : $' + str(sales_tax_amount(item_total, tax_rate)))
