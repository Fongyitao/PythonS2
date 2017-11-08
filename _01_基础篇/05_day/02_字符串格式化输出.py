#__author: Fong
#date_: 2017/11/8 23:37 

name = input("name:")
age = int(input("age:"))
salary = input("salary:")

if salary.isdigit(): # 判断是不是正整数
    print("is digit")
    int(salary)
else:
    exit("must digit") # 输入的不是digit程序就结束

msg = """
--------info of %s--------
Name:%s
Age:%s
Salary；%s
You will be retired in %s years
----------end-------
"""%(name,name,age,salary,65 - age)


print(msg)
