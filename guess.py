# 產生一個隨機整數1~100
# 讓使用者重複輸入數字去猜
# 猜對的話，印出“猜對囉！” 和 “這是你猜的第幾次！”
# 猜錯的話，印出“比答案大／小！”

import random
start = input('請隨機數字範圍開始值： ')
end = input('請隨機數字範圍結束值： ')
start = int(start)
end = int(end)

r = random.randint(start, end)
count = 0
while True:
    count += 1 # count = count + 1
    num = input('請猜數字： ')
    num = int(num)
    if num == r:
        print('猜對囉！')
        print('至這是你猜的第', count, '次！')
        break
    elif num > r:
        print('比答案大！')
    elif num < r:
        print('比答案小！')