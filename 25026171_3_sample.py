# １．mathモジュール，randomモジュールをインポートしてください．
import math
import random

# ２．リスト「l（L小文字）」に好きな数字を5個入れて，出力してください．
l = [16, 25, 49, 64, 81]
print(l)

# ３．リストlの中身を全て足した変数「l_sum」を作り，「合計は(l_sum)です」と出力してください．
l_sum = sum(l)
print(f"合計は{l_sum}です")

# ４．リストlの中からランダムに1つ数字を選び，その平方根を出力してください．
# リストからランダムに選ぶ
selected_num = random.choice(l)

# 平方根を計算する
result = math.sqrt(selected_num)

print(f"選ばれた数字: {selected_num}")
print(f"平方根の結果: {result}")
