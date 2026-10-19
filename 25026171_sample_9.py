# 1. こちらで用意する関数averageは引数として与えられたリストの平均値を求める関数です．しかし，用意した内容ではこちらで用意するリストl1,l2のうちl1の平均値を求められても，l2の平均値は求められません．averageの中身を正しく修正してください．

def average(a):
    return sum(a) / len(a)

l1 = [1,2,3,4,5]
l2 = [6,7,8,9,10,11]

print(average(l1))
print(average(l2))

# 2. 与えられた引数nに対して，n!（nの階乗）を戻り値とするfactorial関数を作ってください．また，factorial(10)の値を出力しなさい．
# 補足：関数の中で出力はせず，戻り値としてください．

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result  

print(factorial(10))