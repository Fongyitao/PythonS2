# _date_:2017/10/28 23:52

sumOuShu = 0
sumJiShu = 0

i = 0

'''
while i <= 100:
    sumOuShu += i
    i += 2
print(sum)
'''

while i <= 100:
    if i % 2 == 0:
        sumOuShu += i
    elif i % 2 == 1:
        sumJiShu += i
    i += 1

print("1-100以内偶数和：%d", sumOuShu)
print("1-100以内奇数和：%d", sumJiShu)
