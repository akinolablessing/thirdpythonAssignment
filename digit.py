integer = int(input("Enter an integer between 0 and 1000: ")) 
firstinteger =int (integer / 100)
secondinteger =int (integer/10)%10
thirdinteger = integer%10
sum = firstinteger + secondinteger + thirdinteger
print(f"The sum of the digits is {sum}")
 