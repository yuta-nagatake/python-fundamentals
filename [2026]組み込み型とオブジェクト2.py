import random as r

# 1. こちらで用意するリストlの1つ1つの要素に対して，それぞれインスタンスのIDを出力してください．
# 補足：インスタンスIDはid()関数で調べられます。
l = [r.randint(1,5) for _ in range(10)]

print(" 1の出力結果は")
for item in l:
    print(f"値: {item} -> インスタンスIDは{id(item)}")

# 2. こちらで用意するタプルtには1番目の要素に室蘭工業大学の緯度（北緯），2番目の要素に経度（東経）が入っています．これらを任意の変数にアンパックし，formatメソッドを使い．「室蘭工業大学は北緯○度，東経□度に位置しています．」という文章を作成し，出力してください．
t = (42.378125, 141.031317)


latitude, toukei = t


message = "室蘭工業大学は北緯{}度，東経{}度に位置する．".format(latitude, toukei)

print("2の出力結果は")
print(message)
