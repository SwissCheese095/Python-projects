list = []
two_div_nums = []
print("Enter 5 numbers")
num1 = int(input())
list.append(num1)
num2 = int(input())
list.append(num2)
num3 = int(input())
list.append(num3)
num4 = int(input())
list.append(num4)
num5 = int(input())
list.append(num5)
print(list)
for i in list:
    if i % 2 == 0:
        two_div_nums.append(i)
        
print(two_div_nums)