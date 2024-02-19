import random
s=0#
repeated_dates_dict = {}
def b_random_data():
  y = random.randint(1990,2024)#random.randint是为了随机生成规定里的数(random.randint is used to randomly generate specified numbers.)
  m = random.randint(1, 12)
  if m in [1, 3, 5, 7, 8, 10, 12]:
    d = random.randint(1, 31)
  elif m in[2]:
      d = random.randint(1, 29)
  else:
    d = random.randint(1, 30)
  return y, m, d
#建立一个方式(Create a function)
for _ in range(10000):
#嵌套循环 外面循环10000遍，里面随机生成一组23个人的生日(Nested loop: The outer loop is looped 10,000 times, and a group of 23 birthdays are randomly generated inside.)
  bp = {}

  for i in range(23):
      bp[f"date_{i+1}"] =b_random_data()#为随机数放入字典(Put into dictionary for random numbers)
  all_dates = set()

  is_yes = False
  for key in bp:#遍历(loop bp)
      value = bp[key]
      if value in all_dates:
          is_yes = True
          repeated_dates_dict.setdefault(value, 0)
          repeated_dates_dict[value] += 1#如果有相同的日期记录一次(If there is a record with the same date)
      else:
          all_dates.add(value)
          print('no')
  if is_yes:
      s +=1

print("Percentage of 'yes' results",s/10000)
print("Repeated dates：")
for date, count in repeated_dates_dict.items():
    if count > 1:
        print(date)
