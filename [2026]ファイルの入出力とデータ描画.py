import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# 1. CSVデータの読み込み
data_dict = {}
total_sales = 0
total_employees = 0

with open('H28keisen-oroshikouri.csv', 'r', encoding='UTF-8') as f:
    for line in f:
      
        items = line.split(',')
        city = items[0]
        employees = int(items[2])  
        sales = int(items[3])     
        
        
        data_dict[city] = sales / employees
        
        # 全体平均を出すための合計
        total_sales += sales
        total_employees += employees

# 2. 全体における従業者1人当たりの年間商品販売額を算出（合計販売額 ÷ 合計従業者数）
overall_average = total_sales / total_employees

# 3. グラフ用データに「全体」の計算結果を追加
data_dict['全体'] = overall_average

# 4. データを降順に並べ替え

sorted_data = sorted(data_dict.items(), key=lambda x: x[1], reverse=True)

# グラフ
labels = []
values = []
for item in sorted_data:
    labels.append(item[0])  
    values.append(item[1])  

# 5. 棒グラフの描画と画像保存

plt.rcParams['font.family'] = 'Yu Gothic'

plt.xticks(rotation=270)

plt.bar(range(0, len(sorted_data)), values, tick_label=labels)

plt.tight_layout()

plt.savefig('graph.png')

