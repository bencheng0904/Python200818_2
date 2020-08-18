import random
num=random.randint(1,10)

ans=input("請輸入數字:")

if num == type(str):
    print("請輸入數字")
if num == ans and num == type(int):
    print("恭喜答對")
elif num >= ans and num <= ans and num == type(int):
    print("哈哈你錯了")
    

