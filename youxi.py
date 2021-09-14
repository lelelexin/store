import random
print("开始游戏请输入1.退出游戏请输入q")
star = int(input("请确定是否开始游戏"))
if star == 1:
    mon = 0
    a =int(input("请输入充值资金"))
    if a>=1000 and a<=2000:
            mon = (mon + a) * 1.1
            print(mon)
    elif a >= 2000:
            mon = (mon + a) * 1.2
            print(mon)
            i = 0
            xin = random.randint(0, 90)
            b = mon
            while i < 5:
                i = i + 1
                b = mon - 500
                num = int(input("请输入一个数字"))
                if num == xin:
                    print("OK")
                    break
                elif num>xin:
                    print("剩余资金:", b, "你猜大了", "剩余次数:", 5 - i)
                elif num<xin:
                    print("剩余资金:", b, "你猜小了", "剩余次数:", 5 - i)
                else:
                    exit ="q"




