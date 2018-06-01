import re

result1 = re.search(r'FishC','I love FishC.com!')
print("result1:" + str(result1))
# 匹配字符串的开始位置,必须以FishC开头才能匹配
result2 = re.search(r'^FishC','I love FishC.com!')
print("result2:" + str(result2))
result3 = re.search(r'FishC','FishC.com!')
print("result3:" + str(result3))
# | 表示选择匹配，匹配前面的或者后面的这个只能匹配FishC或者FishD
result4 = re.search(r'Fish(C|D)','I love FishC.com!')
print("result4:" + str(result4))
# $ 表示已什么结尾的匹配
result5 = re.search(r'FishC$','I love FishC.com!')
print("result5:" + str(result5))
result6 = re.search(r'FishC$','I love FishC')
print("result6:" + str(result6))