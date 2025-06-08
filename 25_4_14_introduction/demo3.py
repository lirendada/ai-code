message = "It's a beautiful day."
print(message)

message2 = 'It\'s a beautiful day.'
print(message2)

# 格式化字符串 + 精度控制
print("今天%10.2f°C, %s和%s一起去游玩。" % (25.5, "小明", "小红"))

# 快速字符串格式化
man = "小明"
woman = "小红"
temp = 25.5
print(f"今天{temp}°C, {man}和{woman}一起去游玩。")