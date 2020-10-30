import re
import requests
import csv
lines = []
with open('01.csv', 'r') as csvFile:
    texts = csv.reader(csvFile)
    for text in texts:
        lines.append(text[0])
datas = []
datass = []
count = 0
# 提取阅读数,评论数，转发数，收藏数
for num in range(0,220):
    datas = []
    x = lines[num]
    w = x[-21:-13]
    q = x[-11:-5]
    start_urls1 = ['http://comet.blog.sina.com.cn/api?maintype=num&uid=' + w + '&aids=' + q]
    html = requests.get(start_urls1[0], timeout=500)
    pattern = re.compile(r"\d+")
    reads = re.findall(pattern, html.text)

    f = reads[-5]
    d = reads[-4]
    c = reads[-3]
    z = reads[-2]
    r = reads[-1]
    datas.append(f)
    datas.append(d)
    datas.append(c)
    datas.append(z)
    datas.append(r)
    print(f,d,c,z,r)
    count = count+1
    datass.append(datas)
print(count)
with open('03.csv', 'w', encoding='utf8',newline="") as file:
    write = csv.writer(file)
    write.writerows(datass)