#Get 3 inputs from user
num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))
num3 = int(input("Enter third number"))
#initialize lowest_num to 0
lowest_num = 0
#compare user inputs to each other and determine smallest number
if num1 <= num2 and num1 <= num3:
    lowest_num = num1
elif num2 <= num1 and num2 <= num3:
    lowest_num = num2
elif num3 <= num1 and num3 <= num2:
    lowest_num = num3
#output lowest_num
print(lowest_num)
