def tax(salary):
    T=salary*20/100
    return T

salary=int(input("Input here"))
netsalary=salary-tax(salary)
print("Tax:", tax(salary))
print("Net:", netsalary)

