# fizzbuzz function
def fizzbuzz(numbers):
    for number in numbers:
        if((number % 3 == 0) and (number % 5 == 0)):
            print(number, ': FizzBuzz')
        elif(number % 3 == 0):
            print(number, ': Fizz')
        elif(number % 5 == 0):
            print(number, ': Buzz')
        else:
            print(number, ':    ')


nums = [13, 14, 61, 87, 75, 22, 54, 86, 54, 75, 23, 87, 55, 11,
        545253, 6727257, 2345234, 72825, 4272576, 245445, 7828282850]

# This function will:
#       print "Fizz" if the number is divisible by 3
#       print "Buzz" if the number is divisible by 5
#       print "FizzBuzz" if the number is divisible by both 3 and 5

fizzbuzz(nums)
