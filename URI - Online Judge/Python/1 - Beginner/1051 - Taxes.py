salary = float(input())
taxes = 0
if salary > 4500:
    taxes = (salary - 4500) * 0.28
    salary -= (salary - 4500)
if salary > 3000:
    taxes += (salary - 3000) * 0.18
    salary -= (salary - 3000)
if salary > 2000:
    taxes += (salary - 2000) * 0.08

print('R$ %.2f' % taxes) if taxes > 0 else print('Isento')
