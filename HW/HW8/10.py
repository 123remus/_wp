def summary(data):
    for i in data:
        name = i['name']              # 學生姓名
        scores = i['scores']          # 分數列表
        total = sum(scores)                 # 總分
        average = total / len(scores)       # 平均分
        average = round(average, 1)         # 四捨五入到小數點一位
        print(name + " 的總分是", total, "，平均是", average)
students = [
    {'name': 'Alice', 'scores': [90, 80, 70]},
    {'name': 'Bob', 'scores': [100, 85, 95]}
]
print(summary(students))
