# -*- coding: utf-8 -*-

import sys, json
from jubatus.classifier import client
from jubatus.common import Datum
from pymongo import MongoClient
from client import getmongo

NAME = "lux";

if __name__ == '__main__':

    # 1.Jubatus Serverへの接続設定
    classi = client.Classifier("127.0.0.1",9199,NAME)

    # 2.学習用データの準備
    getmongo =  getmongo()
    good = getmongo.getValue(good)
    bad = getmongo.getValue(bad)

    value = 0
    for line in good:
        good_value = good[line]['value']
        bad_value = bad[line]['value']
        datum = Datum()

        for (k, v) in [
                u'good',
                ['value', good_value],
                ]:
            datum.add_number(k, v)
        
        for (k, v) in [
                u'bad',
                ['value', bad_value],
                ]:
            datum.add_number(k, v)

        random.shuffle(datum)
        # 3.データの学習（学習モデルの更新）
        classi.train(datum)
        # 4.結果の出力
        data = [
                Datum({'value', 400})
                ]
        for d in data:
            res = client.classify([d])
            sys.stdout.write(max(res[0], key=lambda x: x.score).label)
            sys.stdout.write(' ')
            sys.stdout.write(d.string_values[0][1].encode('utf-8'))
            sys.stdout.write('\n')
