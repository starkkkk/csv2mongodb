import pymongo
import pandas as pd
import os


# read the csv file
def read_csv(cpath):
    # cdata = pd.read_csv(cpath, encoding='gbk', names=col_names, header=None, skiprows=1)
    # cdata = pd.read_csv(cpath, encoding='gbk')
    cdata = pd.read_csv(cpath, encoding='ansi')
    return cdata


# output csv list
def recursive_listdir(path):
    filelist = []
    if path.endswith(".csv"):
        filelist = [path]
    else:
        files = os.listdir(path)
        for file in files:
            file_path = os.path.join(path, file)
            if file.endswith(".csv"):
                filelist.append(file_path)
            # elif os.path.isdir(file_path):
            #     recursive_listdir(file_path)
    return filelist


if __name__ == '__main__':

    # get file path: ['fpath','fpath','fpath']
    # path = r"D:\Study\data\关键个体发现\code & data\俄乌战争_v.csv"
    # path = r"D:\Study\data\关键个体发现\code & data\俄乌战争.csv"
    path = r"D:\Study\data\关键个体发现\code & data\基于综合评估指标体系的影响力计算模型\node importance\data1"
    filepath = recursive_listdir(path)

    # connect mongodb database
    # client = pymongo.MongoClient(host='localhost', port=27017, username='root', password='root')
    client = pymongo.MongoClient(host='localhost', port=27017)
    # db = client["war"]
    # col = db["person"]
    # db = client["war"]
    # col = db["content"]
    db = client["Hk"]
    col = db["content"]


    # 关键词,标题,简要,内容,发布来源,站点,作者id,作者昵称,作者头像地址,作者所在地区,
    # 作者性别,评论数,点赞数,转发数,收藏数,详情地址,发布时间,粉丝数,发文数,微博认证,
    # 省,市

    # col_names = ['keyword',
    #              'title',
    #              'abstract',
    #              'content',
    #              'publish_source',
    #              'site',
    #              'id',
    #              'nickname',
    #              'avatar_address',
    #              'region',
    #              'gender',
    #              'comments',
    #              'stars',
    #              'retweets',
    #              'favorites',
    #              'detail_address',
    #              'time',
    #              'fans',
    #              'posts',
    #              'certification',
    #              'province',
    #              'city']

    # import data to database
    for fp in filepath:
        data = read_csv(fp).to_dict('index')
        for value in data.values():
            col.insert_one(value)
