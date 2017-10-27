# _date_:2017/10/28 0:42

x = 3

y = x * x

z = x ** 2  # x的2次方

print(y)
print(z)

a = 3 ** x
print(a)  # 3的x次方

'''
多行注释
'''

name = input("your name:")
age = input("your age：")  # input接收的都是字符串

# int integer  整数  把字符串转成int，用int(被转的数据)
# str string   字符串 把数据转成字符串用str(被转的数据)

age = int(age)
print("You name is %s,you can still live for %s" % (name, 100 - age),"years")
