# 使用input()函数输入，输入的内容都是字符串类型，所以需要强转
name = input("请输入你的名字：")
age = int(input("请输入你的年龄："))
print("你好，" + name + "，你今年" + str(age) + "岁了！")