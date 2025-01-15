num = float(input('Please enter a number up to which the sum should be calculated: '))
sum = 0
i = 1
while i <= num:
    sum += i
    i += 1
print('Sum =', sum)