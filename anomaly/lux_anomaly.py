# -*- coding: utf-8 -*-

import sys, json
from jubatus.anomaly import client
from jubatus.common import Datum
from pymongo import MongoClient
from getmongo import convertMongo 

NAME = "lux";

if __name__ == '__main__':

    # 1.Jubatus Serverへの接続設定
    anom = client.Anomaly("127.0.0.1",9199,NAME)

    # 2.学習用データの準備
    mongo_dic =  convertMongo()
    dic = mongo_dic.getDic()
    name = '' 
    value = 0
    for line in dic:
        name = dic[line]['name']
        value = dic[line]['value']
        datum = Datum()

        for (k, v) in [
                ['name', name],
                ]:
            datum.add_string(k, v)
        
        for (k, v) in [
                ['value', value],
                ]:
            datum.add_number(k, v)
        
        # 3.データの学習（学習モデルの更新）
        ret = anom.add(datum)
        
        # 4.結果の出力
        if (ret.score != float('Inf')) and (ret.score!= 1.0):
            # print ret, label
            print ret
