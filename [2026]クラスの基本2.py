import datetime

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def introduce(self):
        print(f'{self.name}です。')
        
    def year_of_birth(self):
        now_year = datetime.date.today().year
        print(f'{now_year - self.age}年生まれです。')
    
# 1. こちらでクラスPersonを用意します．クラスPersonを継承して，追加で変数company_nameを持つクラスCompanyを作ってください．
# introduceメソッドは，「{company_name}の{name}です．」と出力されるようにオーバーライドしてください．
# ただし，メソッドyear_of_birthはクラスCompanyには書かないようにしてください．
class Company(Person):
    def __init__(self, name, age, company_name):
        
        super().__init__(name, age)
      
        self.company_name = company_name
        
    def introduce(self):
       
        print(f'{self.company_name}の{self.name}です．')

# 2. クラスPersonを継承して，追加で変数school_name, idを持つクラスUniversityを作ってください．
# introduceメソッドは，2行で「{name}です．」「{school_name}所属，学籍番号は{id}です．」と出力されるようにオーバーライドしてください．
# 1行目「{name}です．」に関しては，クラスPersonから持ってくるようにして，クラスUniversity自体には直接の文章を書かないようにしてください．
class University(Person):
    def __init__(self, name, age, school_name, id):
        super().__init__(name, age)
        self.school_name = school_name
        self.id = id
        
    def introduce(self):
        
        super().introduce()
        print(f'{self.school_name}所属，学籍番号は{self.id}です．')
    

print("--- Personの動作確認 ---")
a = Person('長竹悠汰', 20)
a.introduce()
a.year_of_birth()

# 3. ① クラスCompanyでインスタンスを生成し，introduceメソッドとyear_of_birthメソッドが正しく使えるか確認してください．
print("\n--- Companyの動作確認 ---")
c = Company('長竹悠汰', 20, '株式会社Python')
c.introduce()

c.year_of_birth()

# 3. ② クラスUniversityでインスタンスを生成し，introduceメソッドが正しく使えるか確認してください．
print("\n--- Universityの動作確認 ---")
u = University('長竹悠汰', 20, '室蘭工業大学', '25026171')
u.introduce()
