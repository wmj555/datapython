#-*- coding: utf-8 -*-
import  pandas as  pd
import numpy as np
import sklearn
import scipy
import sklearn.preprocessing as pre
import csv
import re

data_set = pd.read_csv('05.csv')
data_set.info()
# 读取数据
data = pd.read_csv("05.csv",sep=",",header=None)
data.columns = ["titles","tags","time","contents","urls","collect","loves","reads","reprints","comments"]
data.head()
#找出缺失值，查看缺失值数量
null_all = data.isnull().sum()
print(null_all)

#发现缺失值，且在contents列，定位到缺失值
contents_null = data[pd.isnull(data["contents"])]
print(contents_null)
data = data[data['contents'].notna()]


#填补，将空的tags标签转化为杂谈
dd = data
print(dd)
dd['tags']=dd['tags'].fillna('杂谈')

#填补，将空的时间标记
data = dd
data['time'] = data['time'].fillna("时间未知")


#将标签转化为int

def convert_currency(var):
    for i in data['reads']:
        pattern = re.compile(r"\d+")
        num = re.findall(pattern, i)
        if num:
            a= (int(num[0]))
            return int(a)
data["reads"].apply(convert_currency)
print(data.dtypes)