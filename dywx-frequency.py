# import matplotlib.pyplot as plt     #数学绘图库
# import jieba               #分词库
# from wordcloud import WordCloud   #词云库
import os, codecs
import jieba
from collections import Counter

project = "dywx"
index = 0
mdDir = "{}-md".format(project)
fileName = "{}/{}{}.md".format(mdDir, project, index)



 
#1、读入txt文本数据
text = open(fileName, 'r').read()

#2、结巴分词，默认精确模式。可以添加自定义词典userdict.txt,然后jieba.load_userdict(file_name) ,file_name为文件类对象或自定义词典的路径
# 自定义词典格式和默认词库dict.txt一样，一个词占一行：每一行分三部分：词语、词频（可省略）、词性（可省略），用空格隔开，顺序不可颠倒
 
cut_text= jieba.cut(text)
result= "/".join(cut_text)#必须给个符号分隔开分词结果来形成字符串,否则不能绘制词云
#print(result)


 
def get_words(txt):
    seg_list = jieba.cut(txt)
    c = Counter()
    for x in seg_list:
        if len(x)>1 and x != '\r\n':
            c[x] += 1
    print('常用词频度统计结果')
    for (k,v) in c.most_common(100):
        print('%s%s %s  %d' % ('  '*(5-len(k)), k, '*'*int(v/3), v))
 
if __name__ == '__main__':
    with codecs.open(fileName, 'r', 'utf8') as f:
        txt = f.read()
    get_words(txt)


# #3、生成词云图，这里需要注意的是WordCloud默认不支持中文，所以这里需已下载好的中文字库
# #无自定义背景图：需要指定生成词云图的像素大小，默认背景颜色为黑色,统一文字颜色：mode='RGBA'和colormap='pink'
# wc = WordCloud(font_path=r"PingFang.ttc",background_color='white',width=800,height=600,max_font_size=50,
#                max_words=1000)
# #,min_font_size=10)#,mode='RGBA',colormap='pink')
# wc.generate(result)
# wc.to_file(r"D:\Python\test\wordcloud\output\wordcloud.png") #按照设置的像素宽高度保存绘制好的词云图，比下面程序显示更清晰
 
# # 4、显示图片
# plt.figure("词云图") #指定所绘图名称
# plt.imshow(wc)       # 以图片的形式显示词云
# plt.axis("off")      #关闭图像坐标系
# plt.show()