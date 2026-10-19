import random as r
# 1. リストaを用意してください．要素はランダムな数字（0~100までの整数）20個とし，出力してください．この生成には内包表記を使用してください．

a = [r.randint(0, 100) for _ in range(20)] #randint=ランダムな整数を一つ生成する機能
print("リストa:", a)

# 2. リストbを用意してください．bの要素はリストaの要素のうち，50以上の整数とし，出力してください．
b = [x for x in a if x >= 50]
print("リストb:", b)

# 3. リストbの中で重複する要素を見つけてください．見つけた場合には「重複があります．」と出力し，見つけられなかった場合には「重複はありません．」と出力してください．

if len(b) != len(set(b)):  #setは重複を許さないもの
    print("重複があります。")
else:
    print("重複はありません。")

# 4. こちらで用意するリストcを，型ごとに分けたリストを含むリストdataを作成してください．ただし，リストcに含まれる型はint型
c = [10, True, 'こんにちは', 'Hello', 0.12, False, False, '16', 133, 'True', 123.456]

ints = []
floats = []
bools = []
strs = []

for item in c:
    
    if isinstance(item, bool):
        bools.append(item)

    elif isinstance(item, int):
        ints.append(item)

    elif isinstance(item, float):
        floats.append(item)
        
    elif isinstance(item, str):
        strs.append(item)

data = [ints, floats, bools, strs]
print("data:", data)











