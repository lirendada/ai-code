import jieba

text = "小明毕业于北京大学计算系"

# 1. 精确模式
words_generator = jieba.cut(text)
for word in words_generator:
    print(word)

words_list = jieba.lcut(text)
print(words_list)

# 2. 全模式
all_words_list = jieba.lcut(text, cut_all=True)
print(all_words_list)

# 3. 搜索引擎模式
search_words_list = jieba.lcut_for_search(text)
print(search_words_list)

# 4. 自定义
jieba.load_userdict("./data/dict.txt")
longtext = "随着云计算技术的普及，越来越多企业开始采用云原生架构来部署服务，并借助大模型能力提升智能化水平，实现业务流程的自动化与智能决策。"
print(jieba.lcut(longtext))