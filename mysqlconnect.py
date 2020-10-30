import pymongo
import csv
import time
client = pymongo.MongoClient(host = '127.0.0.1',
                       port = 27017)
print('连接上了!')
db = client.blogs
collection = db.blogs
# 创建连接MongoDB数据库函数
def insertToMongoDB(collection):

    with open('02.csv','r',encoding='utf-8')as csvfile:
        # 调用csv中的DictReader函数直接获取数据为字典形式
        reader=csv.DictReader(csvfile)
        # 创建一个counts计数一下 看自己一共添加了了多少条数据
        counts=0
        for each in reader:
            # 将数据中需要转换类型的数据转换类型。原本全是字符串（string）。
            each['titles'] = str(each['titles'])
            each['tags']=str(each['tags'])
            each['time']=str(each['time'])
            each['contents'] = str(each['contents'])
            each['collect'] = str(each['collect'])
            each['loves'] = str(each['loves'])
            each['reads'] = str(each['reads'])
            each['reprints'] = str(each['reprints'])
            each['comments'] = str(each['comments'])
            each['urls'] = str(each['urls'])
            collection.insert(each)
            counts+=1
            print('成功添加了'+str(counts)+'条数据 ')
#转换数据格式
def change():
    start_time = time.time()
    handler = pymongo.MongoClient().blogs.blogs
    handler.update_many({}, [
        {'$set':
             {'loves':
                  {'$convert':
                       {'input': '$loves', 'to': 'int'}
                   }
              }
         }
    ])
    handler.update_many({}, [
        {'$set':
             {'reads':
                  {'$convert':
                       {'input': '$reads', 'to': 'int'}
                   }
              }
         }
    ])
    handler.update_many({}, [
        {'$set':
             {'collect':
                  {'$convert':
                       {'input': '$collect', 'to': 'int'}
                   }
              }
         }
    ])
    handler.update_many({}, [
        {'$set':
             {'reprints':
                  {'$convert':
                       {'input': '$reprints', 'to': 'int'}
                   }
              }
         }
    ])
    handler.update_many({}, [
        {'$set':
             {'comments':
                  {'$convert':
                       {'input': '$comments', 'to': 'int'}
                   }
              }
         }
    ])

# 创建主函数
def main():
    #insertToMongoDB(collection)
    change()
# 判断是不是调用的main函数。这样以后调用的时候就可以防止不会多次调用 或者函数调用错误
if __name__=='__main__':
    main()




