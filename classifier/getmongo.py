# usr/bin/env python
# -*- coding:utf-8 -*-

from pymongo import MongoClient
import json

class convertMongo:
    mongo_client = MongoClient('172.16.4.84', 27017)
    sensor_db = mongo_client['sensordb']
    sensors_collection = sensor_db.sensors
    global pre
    pre = sensor_db.predict
    global train_sensors_dic
    train_sensors_dic = {}
    count = 0

    for data in sensors_collection.find():
        del data['_id']
        json_list  = json.dumps(data)
        train_sensors_dic[count] = json.loads(json_list)
        count += 1

    def getTrainSensorsDic(self):
        return train_sensors_dic
    
    def postDB(self, result, value):
        pre.insert({'result':result, 'value':value})

    # count = 0
    # for count in dic:
    #     print dic[count]
