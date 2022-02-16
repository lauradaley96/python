salary = int(input("Enter your salary:"))

if salary>=2000:
    tax=salary*20/100
    net=salary-tax
if salary<2000:
    tax=salary*10/100
    net=salary-tax

print("Tax:", tax)
print("Net Salary:", net)