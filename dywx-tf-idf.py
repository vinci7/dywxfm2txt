import jieba.analyse

project = "dywx"
index = 0
mdDir = "{}-md".format(project)
fileName = "{}/{}{}.md".format(mdDir, project, index)

# 读取文件
def read(fileName):
    text = open(fileName).read()
    return text


# jieba分词器通过词频获取关键词
def jieba_keywords(text):
    print(jieba.analyse.extract_tags(text, topK=10, withWeight=False, allowPOS=()))
    #print(keywords)




text = read(fileName)
jieba_keywords(text)