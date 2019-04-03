import pandas as pd
import pymysql
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.externals import joblib


def process_hot_rate(arrlike):
    if arrlike['hot_rate'] < 0.2:
        arrlike['hot_rate'] = 1
    elif 0.4 > arrlike['hot_rate'] >= 0.2:
        arrlike['hot_rate'] = 2
    elif 0.6 > arrlike['hot_rate'] >= 0.4:
        arrlike['hot_rate'] = 3
    elif 0.8 > arrlike['hot_rate'] >= 0.6:
        arrlike['hot_rate'] = 4
    elif 1.0 >= arrlike['hot_rate'] >= 0.8:
        arrlike['hot_rate'] = 5
    return arrlike['hot_rate']


def process_price(arrlike):
    if arrlike['price'] < 100:
        arrlike['price'] = 1
    elif 200 > arrlike['price'] >= 100:
        arrlike['price'] = 2
    elif 300 > arrlike['price'] >= 200:
        arrlike['price'] = 3
    elif 400 > arrlike['price'] >= 300:
        arrlike['price'] = 4
    elif arrlike['price'] >= 400:
        arrlike['price'] = 5
    return arrlike['price']


def process_month_sold(arrlike):
    if arrlike['month_sold'] < 100:
        arrlike['month_sold'] = 1
    elif 200 > arrlike['month_sold'] >= 100:
        arrlike['month_sold'] = 2
    elif 300 > arrlike['month_sold'] >= 200:
        arrlike['month_sold'] = 3
    elif 400 > arrlike['month_sold'] >= 300:
        arrlike['month_sold'] = 4
    elif arrlike['month_sold'] >= 400:
        arrlike['month_sold'] = 5
    return arrlike['month_sold']


def process_diary_num(arrlike):
    if arrlike['month_sold'] < 100:
        arrlike['month_sold'] = 1
    elif 200 > arrlike['month_sold'] >= 100:
        arrlike['month_sold'] = 2
    elif 300 > arrlike['month_sold'] >= 200:
        arrlike['month_sold'] = 3
    elif 400 > arrlike['month_sold'] >= 300:
        arrlike['month_sold'] = 4
    elif arrlike['month_sold'] >= 400:
        arrlike['month_sold'] = 5
    return arrlike['month_sold']


def create_model():
    conn = pymysql.Connect(host='10.8.157.7', port=3306, user='root', password='root', db='CommandSysten',charset='utf8')
    # 读取数据库数据
    df = pd.read_sql('select * from spot', conn)
    conn.close()

    # 数据清洗
    df['hot_rate'] = df.apply(process_hot_rate, axis=1)
    df['price'] = df.apply(process_price, axis=1)
    df['month_sold'] = df.apply(process_month_sold, axis=1)
    df['diary_num'] = df.apply(process_diary_num, axis=1)

    df3 = df.loc[:, ['price', 'hot_rate', 'month_sold', 'diary_num']]
    df4 = df.loc[:, ['spot_type']]

    x_train, x_test, y_train, y_test = train_test_split(df3, df4)

    lr = KNeighborsClassifier()
    lr.fit(x_train, y_train)
    # save model
    joblib.dump(lr, './lr.pkl')
    return lr

