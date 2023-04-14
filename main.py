import pymongo
import pandas as pd


# read the csv file
def read_csv(cpath):
    # cdata = pd.read_csv(cpath, encoding='gbk', names=col_names, header=None, skiprows=1)
    cdata = pd.read_csv(cpath, encoding='gbk')
    return cdata


if __name__ == '__main__':
    # filepath = "D:\Study\data\关键个体发现\code & data\俄乌战争_v.csv"
    filepath = "D:\Study\data\关键个体发现\code & data\俄乌战争.csv"

    client = pymongo.MongoClient('localhost', 27017)
    # db = client["Hk"]
    # col = db["content"]

    db = client["war"]
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

    data = read_csv(filepath).to_dict('index')
    for value in data.values():
        col.insert_one(value)
