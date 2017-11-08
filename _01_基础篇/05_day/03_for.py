#__author: Fong
#date_: 2017/11/9 0:06 

for i in range(3):
    userName = input("input your name>>>")
    pwd = input("input your password>>>")
    if userName == "admin" and pwd == "888":
        print("Welcome %s login..."%userName)
        break
    else:
        print("Invalid userName or password")




