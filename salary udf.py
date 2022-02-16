def salaryslip(name, salary):
    if salary>=2000:
        tax=salary*20/100
    else:
        tax=salary*15/100
    net_salary=salary-tax
    print("Name of Employee: ", name)
    print("Salary: ", salary)
    print("Tax: ", tax)
    print("Net Salary: ", net_salary)
    print("---------")

salaryslip("Laura", 5000)
salaryslip("Joe", 1200)
salaryslip("Rihanoon", 3500)
salaryslip("Frank", 4800)