# 產稱一個隨機整數1~100 (不要印出來)
# 讓使用者重複輸入數字去猜
# 猜對的話 印出 "終於猜對了!"
# 猜錯的話 要告訴他 比答案大/小

#==============
# Fish version
#==============
# import random
# guess = 0
# number = random.randint(1, 100)
# print(number)
# while guess != number:
    # guess = input('請猜一個1~100的數字: ')
    # guess = int(guess)
    # if guess == number:
        # print('終於猜對了!')
        # break
    # elif guess > number:
        # print('比答案 "大"，再猜一次吧','\n')
    # else:
        # print('比答案 "小"，再猜一次吧','\n')
        
#============
# 老師解法：
#============
import random 
start = input('請決定隨機數字範圍開始值:')
end = input('請決定隨機數字範圍結束值:')
start = int(start)
end = int(end)

r = random.randint(start, end)
count = 0
while True:
    count += 1 #count = count +1 
    num = input('請猜數字: ')
    num = int(num)
    if num == r:
        print('你猜中了!')
        print('這是你猜的第', count, '次')
        break
    elif num > r:
        print('比答案大')
    elif num < r:
        print('比答案小')
    print('這是你猜的第', count, '次')


