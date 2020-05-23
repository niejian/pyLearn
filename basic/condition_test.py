# 条件判断
age = input('age:')
# 接收到的字符串转数字
age = int(age)
if age >= 18:
  print('your age is %d' % age)
  print('adult')
elif age >= 6:
  print('your age is %d' % age)
  print('teenager')  
else :
  print('your age is %d' % age)
  print('children')  

# 小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：

# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖

height = input('身高（m）：')
weight = input('体重（kg）：')
float_height = float(height)
float_weight = float(weight)
bmi = float_weight / (float_height * float_height)
if bmi >= 32:
  print('bmi: %f, 严重肥胖！' % bmi)
elif bmi >= 28:
  print('bmi: %f, 肥胖！' % bmi)
elif bmi >= 25:
  print('bmi: %f, 过重！' % bmi)
elif bmi >= 18.5:
  print('bmi: %f, 正常！' % bmi)
elif bmi < 18.5:
  print('bmi: %f, 过轻！' % bmi)
