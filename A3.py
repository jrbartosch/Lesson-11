num = float(input('Please Enter a Number to Calculate if it is an Armstrong Number: '))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
if num == sum:
    print (num, 'is an Armstrong number.')
else:
    print (num, 'is not an Armstrong number.')