import math as m
import datetime

# 1. こちらであらかじめ生年月日を入力すると年齢が出力されるプログラムを用意します．
# ですが，この入力時に数字以外を入れるとエラーで強制終了してしまいます．
# 数字以外が入力されたときに「正しい数字で入力してください．」と出力するように改善してください．

print('生年月日から年齢を計算します')

def age(year, month, day):
    today = datetime.date.today()
    birthday = datetime.date(year, month, day)
    return (int(today.strftime("%Y%m%d")) - int(birthday.strftime("%Y%m%d"))) // 10000

try:
    year = int(input('生まれた年を入力してください： '))
    month = int(input('生まれた月を入力してください： '))
    day = int(input('生まれた日を入力してください： '))
    print('あなたの年齢は', age(year, month, day), '歳です。')
except ValueError:
    print('正しい数字で入力してください．')


print('\n' + '='*30 + '\n') 


# 2. 辞書menuとリストorderをこちらで用意します．menuは料理の名前とその税抜きの価格が対応しています．
# orderは料理名と店内(eatin)か持ち帰り(takeout)かが書かれているタプルを要素として持ちます．
# こちらで用意する関数print_price，print_eatin，print_takeoutを用いた高階関数で，orderをもとにそれぞれ，
# 「（料理名）の価格は（店内 or お持ち帰り）で（税込の値段）円です．」と出力してください．

menu = {'ラーメン':900, 'オムライス':950, 'ハンバーグ':800, 'カレーライス':850}
order = [('ラーメン','eatin') , ('ハンバーグ','takeout'), ('カレーライス','eatin'), ('カレーライス','takeout')]

def print_price(dish, price, func):
    print(dish + 'の価格は' + func(price) + 'です。')

def price_eatin(price):
    return f'店内で{int(price * 1.1)}円'

def price_takeout(price):
    return f'お持ち帰りで{int(price * 1.08)}円'

print('--- 問題2の出力 ---')

for dish, type_str in order:
    price = menu[dish] 
    if type_str == 'eatin':
        print_price(dish, price, price_eatin)
    elif type_str == 'takeout':
        print_price(dish, price, price_takeout)


print('\n' + '='*30 + '\n') 


# 3. 問題2のprint_eatin，print_takeoutをラムダ式にして，orderをもとにそれぞれ，
# 「（料理名）の価格は（店内 or お持ち帰り）で（税込の値段）円です．」と出力してください．
# 補足：問題2のprint_priceはそのまま使用して良いです．

print('--- 問題3の出力 ---')

for dish, type_str in order:
    price = menu[dish]
    if type_str == 'eatin':
        print_price(dish, price, lambda p: f'店内で{int(p * 1.1)}円')
    elif type_str == 'takeout':
        print_price(dish, price, lambda p: f'お持ち帰りで{int(p * 1.08)}円')