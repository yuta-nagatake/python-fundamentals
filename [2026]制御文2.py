# 1.変数aに1,2,3……のように順番に連続した数字を足していき，100を超えたら停止し，最終的なaの値を出力するコードをwhile文で書きなさい．
a=0
i = 1  

while a <= 100:
    a += i
    i += 1

print(f"最終的なaの値: {a}")
 
# 2.変数bに1~20の間で奇数の場合は足す，偶数の場合は引くを行い，最終的な結果を出力するコードをfor文で書きなさい．
b=0

for i in range(1, 21):
    if i % 2 == 1:  
        b += i
    else:  
        b -= i

print(f"最終的なbの値: {b}")

# 3.変数cに「Muroran Institute of Technology」の中にあるa,i,u,e,oの数を入れ、最終的なcの値を出力するコードを書きなさい．
c=0
S="Muroran Institute of Technology"

for i in S:
    if i in "aiueo":
        c += 1

print(f"最終的なcの値: {c}")

# 4.変数answer,dxを用意し，繰り返し文で∫_(-10)^10 x^2  dx を解き最終的なanswerを出力するコードを書きなさい．dxは任意の数字（0~1までの小数が望ましい）とする．
# 補足：積分の定義のような細長い長方形を足し合わせていくことを想定しています．dxを小さくすればするほどより精確な答えに近づいていきます．
answer=0
dx=0.01

x = -10.0
while x < 10.0:
    answer += (x**2) * dx
    x += dx

print(f"最終的なanswerの値: {answer}")
