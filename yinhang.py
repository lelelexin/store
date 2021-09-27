print("==============================================")
print("|------------中国工商银行账户管理系统------------|")
print("|------------1、开户              ------------|")
print("|------------2、取钱              ------------|")
print("|------------3、存钱              ------------|")
print("|------------4、转账              ------------|")
print("|------------5、查询              ------------|")
print("|------------6、退出              ------------|")
print("==============================================")
import  random
from DBUtils import update
from DBUtils import select
bank={}
bank_name="中国工商银行"
def bank_adduser(username,account,password,country,province,street,door,money):
    sql = "select count(*) from person"
    param = []
    data = select(sql, param,mode='one')[0]
    if data>=100:
        return 3

    sql1 = "select * from person where username = %s"
    param1 = [username]
    data = select(sql1,param1)
    if len(data) > 0 :#如果一个变量在容器内就运行代码
        return 2

    sql2 = "insert into person values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    param2 = [account,username,password,country,province,street,door,money,bank_name]
    data = update(sql2,param2)
    return 1


def useradd():
    username=input("请输入您的用户名：")
    password = input("请输入密码：")
    print("请输入您的个人详细地址：")
    country = input("\t\t国籍:")
    province = input("\t\t省份:")
    street = input("\t\t街道:")
    door = input("\t\t门牌号:")
    account=random.randint(10000000,99999999)
    money=0
    a=bank_adduser(username,account,password,country,province,street,door,money)
    if a == 1:
        print("添加用户成功，以下是您的信息")
        info = '''
                    ------------个人信息------------
                    用户名:%s
                    账号：%s
                    密码：*****
                    国籍：%s
                    省份：%s
                    街道：%s
                    门牌号：%s
                    余额：%s
                    开户行名称：%s
                '''
        # 每个元素都可传入%
        sql = 'select money from person where account= %s'
        param = [account]
        data = select(sql, param, mode='one')[0]
        print(data)
        print(info % (username, account, country, province, street, door, data, bank_name))
    elif a ==2:
        print("用户已存在，请勿重复添加！")
    elif a == 3:
        print("数据库已满")

def usermoney():       #取款
    a = 4
    b = 0
    account = int(input("请输入你的账号："))
    sql = "select * from person where account = %s"
    param = [account]
    data = select(sql, param)
    if len(data) > 0:
        while True:
            password = int(input("请输入您的密码"))
            sal1 = 'select password from person where account = %s'
            param1 = [account]
            data1 = select(sal1, param1, mode='one')[0]
            if password == data1:
                withdraw_money = int(input("请输入你要取款的金额："))
                sql2 = 'select money from person where account=%s'
                param2 = [account]
                data2 = select(sql2, param2, mode='one')[0]
                if withdraw_money > data2:
                    print("您的账户余额不足！账户余额为：", data2)
                    break
                else:
                    sql3 = 'update person set money = money - %s  where  account = %s'
                    param3 = [withdraw_money,account]
                    update(sql3, param3)
                    sql4 = 'select money from person  where  account = %s'
                    param4 = [account]
                    data3 = select(sql4,param4,mode="one")[0]
                    print("取钱成功！您的账户余额为：", data3)
                    break
            else:
                print("密码不正确!您还有", a - 1, "次机会")
                b += 1
                a -= 1
                if b == 4:
                    print("您的账户已锁定，请明天再试。")
                    break
        else:
            print("您输入的账号不存在！")

def amunt():     #存款
    account_money =  input("请输入您存钱的账号：")
    sql = "select * from person where account = %s"
    param = [account_money]
    data = select(sql, param)
    if len(data) > 0:
        money = int(input("请输入你要存入的金额："))
        sql1 = 'update person set money = money + %s where  account = %s'
        param1 = [money,account_money]
        update(sql1, param1)
        sql2 = 'select money from person where account = %s'
        param2 = [account_money]
        data1 = select(sql2, param2,mode="one")[0]
        print("存款成功！当前可用余额：",data1)
    else:
        print("该用户不存在")

def transfer():      #转账
    account = int(input("请输入您的账号"))
    sql = "select * from person where account = %s"
    param = [account]
    data = select(sql, param)
    if len(data) > 0:
        account2 = int(input("请输入您要转账的账号："))
        sql1 = "select * from person where account = %s"
        param1 = [account2]
        data1 = select(sql1, param1)
        if len(data1) > 0:
            password = int(input("请输入您的密码"))
            sql2 = 'select password from person  where account = %s'
            param2 = [account]
            data2 = select(sql2, param2, mode='one')[0]
            while True:
                if password == data2:
                    money = int(input("请输入您要转账的金额："))
                    sql3 = 'select money from person where account = %s'
                    param3 = [account]
                    data3 = select(sql3, param3, mode='one')[0]
                    if money > data3:
                        print('您的余额不足，转账失败！')
                        break
                    else:
                        sql4 = 'update person set money = money - %s  where account  = %s'
                        param4 = [money, account]
                        update(sql4, param4)
                        sql5 = 'select money from person  where account = %s'
                        param5 = [account]
                        data4 = select(sql5, param5, mode='one')[0]
                        print("转账成功！您的余额为：", data4)
                        sql6 = "update person  set  money = money + %s  where account = %s"
                        param6 = [money, account2]
                        update(sql6, param6)
                        break
                else:
                        print("您输入的账号不正确")

def search(): #查询
    account = int(input("请输入您要查询的账号"))
    sql = "select * from person where account = %s"
    param = [account]
    data = select(sql, param)
    if len(data) > 0:
        password = int(input("请输入密码"))
        sql2 = 'select password from person where account = %s'
        param2 = [account]
        data2 = select(sql2, param2, mode='one')[0]
        print(data2)
        while True:
            if password == data2:
                sql3 = 'select * from person where account = %s'
                param3 = [account]
                data3 = select(sql3, param3)
                print(data3)
                break
    else:
        print('用户名密码错误')
#
while True:
    begin = input("请选择业务")
    if begin == "1":
        print("1、开户")
        useradd()
    elif begin == "2":
        print("2、取钱")
        usermoney()
    elif begin == "3":
        print("3、存钱")
        amunt()
    elif begin == "4":
        print("4、转账")
        transfer()
    elif begin == "5":
        print("5、查询 ")
        search()
    elif begin == "6":
        print("6、退出")
        break
