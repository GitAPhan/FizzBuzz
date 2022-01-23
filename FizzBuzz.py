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


# def second_largest(numbers):
#     largest = 'a'
#     second_largest = 'a'
#     for number in numbers:
# #     #     if(second_largest == 'a' and number != max(numbers)):
# #     #         second_largest = number
# #     #     elif(number > second_largest and number != max(numbers)):
# #     #         second_largest = number
#         if(largest = 'a'):
#             largest = number
#     print(second_largest)

# Write a function that takes in an array of numbers and returns the average of ONLY POSITIVE numbers


def avg_of_positive(numbers):
    sum = 0
    count = 0
    for number in numbers:
        if(number > 0):
            sum = sum + number
            count = count + 1
    return(sum/count)

# Write a function that takes in an array of numbers and return True if the array is sorted largest to smallest and False otherwise


def validate_big_to_small(numbers):
    x = 'a'
    for number in numbers:
        if(x == 'a'):
            x = number
        elif(x < number):
            return False
        else:
            x = number        
    return True

# Write a function that takes in a string and returns True if the string's length is greater than 10 and False otherwise


def string_over_ten(numbers):
    if(len(numbers) > 10):
        print(True)
    else:
        print(False)


# nums are here
zeros = [0, 0, 0, 0]
nums = [13, 14, 61, 87, 75, 22, 54, 86, 54, 75, 23, 87, 55, 11,
        545253, 6727257, 2345234, 72825, 4272576, 245445, 7828282850, -27451291, -4581, -5, -851, -93]

big_to_small = [451451451, 34134, 3432, 342, 64, 45, 23, 12, 9, 5, 2]

less_than_ten = [21412, -3525, 35623, -675, 326, 5, -4]

string = 'this is a string'
short_string = 'string'
# This function will:
#       print "Fizz" if the number is divisible by 3
#       print "Buzz" if the number is divisible by 5
#       print "FizzBuzz" if the number is divisible by both 3 and 5

# for num in nums:
#     fizzbuzz(num)

# second_largest(big_to_small)

# print(avg_of_positive(nums))

print(validate_big_to_small([4,1,2]))
# validate_big_to_small(big_to_small)

# string_over_ten(nums)
# string_over_ten(big_to_small)
# string_over_ten(string)
# string_over_ten(short_string)
