import csv
count = 0
k = 0
file = open('02.csv',encoding = 'utf8')
reader = csv.reader(file)
reader1 = list(reader)
file.close()
file3 = open('03.csv')
num = csv.reader(file3)
number = list(num)
for i in range(0,120):
    line = reader1[i]
    if line :
        for j in range(0,4):
            reader1[i].append(number[i][j])
        k = k + 1
print(count,k)
original = reader1
print(original)
file1 = open('02.csv', 'w',encoding='utf8', newline='')
content = csv.writer(file1)
for i in original:
    print(i)
    content.writerow(i)