# _date_:2017/10/28 22:42

num1 = int(input("Num1:"))
num2 = int(input("Num2:"))
num3 = int(input("Num3:"))

if num1 > num2:
    if num1 > num3:
        print("max is :%d"%num1)
    else:
        print("max is %d"%num3)
else :
    if  num2 > num3:
        print("max is %d"%num2)
    else:
        print("max is %d"%num3)

#
# maxNum=num1
# list ={num1,num2,num3}
# for i in list:
#     if i > maxNum:
#         maxNum = i
# print("max is %d"%maxNum)