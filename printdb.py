#usr/bin/env python
# -*- coding:utf-8 -*-

from pymongo import MongoClient
import json

class getmongo:
    con = MongoClient('172.16.4.83', 27017)
    db = con["sensordb"]
    col = db.sensors
    global dic
    dic = {}
    count = 0
    
    for data in col.find({'name':'Bad'}):
        del data['_id']
# BsonをJsonに変換
        json_list = json.dumps(data)
# Jsonをディクショナリに変換
        dic[count] = json.loads(json_list)
        count += 1
    print dic
