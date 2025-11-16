### If we list all the natural numbers below 
#  that are multiples of 
#  or 
# , we get 
#  and 
# . The sum of these multiples is 
# .

# Find the sum of all the multiples of 
#  or 
#  below 
# .

def multiple_3_and_5(num):
    total = 0
    for number in range(1, num):
        if number % 3 == 0 or number % 5 == 0:
            total += number 
    return total
print(multiple_3_and_5(100))