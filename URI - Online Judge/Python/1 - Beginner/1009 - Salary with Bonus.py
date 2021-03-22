name = input()
gross_salary = float(input())
sales_price_total = float(input())

net_salary = gross_salary + (sales_price_total * 0.15)

print('TOTAL = R$ {:.2f}'.format(net_salary))
