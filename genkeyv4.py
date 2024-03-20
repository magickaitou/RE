import math

# tìm khoảng của octet trong khoảng 0xaca22c5 0xaca22cb là có thể pass serial1
array = [65535.998, 65536.00199999999]
for i in array:
    tmp = math.sqrt(i* pow(10,12)/2)
    tmp = round(tmp)
    print(hex(tmp))
array_2 = [65536.00199999999, 65535.998]
for i in array_2:
    tmp = math.sqrt(i* pow(10,12)/2)
    tmp = round(tmp)
    print(hex(tmp))
