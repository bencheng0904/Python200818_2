import random
num=random.randint(1,20)

i=1
while i<6:
    ans=int(input("請輸入數字(1~20):"))
    if ans > num:
        print("答案太大")
        i=i+1
    elif ans < num:
        print("答案太小")
        i=i+1
    elif ans == num:
        print("恭喜答對")
        print("你猜了"+str(i)+"次")
        break

    
        
        
        
        
        