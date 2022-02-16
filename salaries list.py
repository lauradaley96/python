salaries = [34, 27482, 284298, 241847, 58694, 2784, 28492, 593, 4592, 5883, 348522, 4956829, 48583, 4528, 4595852]
i = 0
while i <len(salaries):
    print(i+1, ")", salaries[i])
    i = i+1

print("-------")
#below you calcuclate the highest number in the list

i = 1
big = salaries[0]
while i<len(salaries):
    if salaries[i] >big:
        big = salaries[i]
    i = i+1
print("Highest number is:", big)