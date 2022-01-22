# fizzbuzz function
def fizzbuzz(number):
    if((number % 3 == 0) and (number % 5 == 0)):
        print(number, ': FizzBuzz')
    elif(number % 3 == 0):
        print(number, ': Fizz')
    elif(number % 5 == 0):
        print(number, ': Buzz')
    else:
        print(number, ':    ')

# Write a function that takes in an array of numbers and returns the 2ND largest number


def second_largest(numbers):
    x = 0
    y = 0
    for number in numbers:
        if(number > x and number > y):
            x = number
        elif(number > y and number < x):
            y = number
    print(y)

# Write a function that takes in an array of numbers and returns the average of ONLY POSITIVE numbers


# Write a function that takes in an array of numbers and return True if the array is sorted largest to smallest and False otherwise


# Write a function that takes in a string and returns True if the string's length is greater than 10 and False otherwise


# nums are here
nums = [13, 14, 61, 87, 75, 22, 54, 86, 54, 75, 23, 87, 55, 11,
        545253, 6727257, 2345234, 72825, 4272576, 245445, 7828282850, -27451291, -4581, -5, -851, -93]

# This function will:
#       print "Fizz" if the number is divisible by 3
#       print "Buzz" if the number is divisible by 5
#       print "FizzBuzz" if the number is divisible by both 3 and 5

for num in nums:
    fizzbuzz(num)

second_largest(nums)
