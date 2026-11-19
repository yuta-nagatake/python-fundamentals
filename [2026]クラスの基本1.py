# 1. こちらでクラスStudentを用意します．インスタンスを生成してintroduce関数を呼び出して「学籍番号〇〇の□□です．」と出力されるようにしてください．
class Student:
    def __init__(self, id ,name):
        self.id = id
        self.name = name
    
    def introduce(self):
        print(f'学籍番号{self.id}の{self.name}です。')

# --- 以下のコードを追加します ---
# インスタンスを生成する（引数として学籍番号と名前を渡す）
student1 = Student(25026171, "長竹悠汰")

# introduceメソッドを呼び出して出力する
student1.introduce()
# 2. 以下の仕様に則った座標を管理するクラスPointを作成してください．
# ・x , yを引数に持ち，インスタンス生成時に受け取る．
# ・今いる位置からdx , dy移動するメソッドmoveを持つ．
# ・現在位置を，「現在位置はx=○，y=□です．」と出力するメソッドshowを持つ．
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        
   
    def show(self):
        print(f'現在位置はx={self.x}，y={self.y}です。')        
# 3. 問題2で作ったクラスPointを，次の手順で操作し正しく動くことを確認してください．
# ①	x=0,y=0で初期化したインスタンスp1を生成する．
# ②	showメソッドを実行し，現在位置がx=0,y=0であることを確認する．
# ③	moveメソッドを使い，dx=5,dy=-3移動する．
# ④	showメソッドを実行し，現在位置がx=5,y=-3であることを確認する．

# ① x=0, y=0で初期化したインスタンスp1を生成する．
p1 = Point(0, 0)

# ② showメソッドを実行し，現在位置がx=0, y=0であることを確認する．
p1.show()

# ③ moveメソッドを使い，dx=5, dy=-3移動する．
p1.move(5, -3)

# ④ showメソッドを実行し，現在位置がx=5, y=-3であることを確認する．
p1.show()
