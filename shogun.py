#!/usr/bin/env python
# coding: utf-8

host = '127.0.0.1'
port = 9199
name = 'test'

import sys
import json
import random

import jubatus
from jubatus.common import Datum
from client import getmongo


getmongo = getmongo()
dic = getmongo.getDic()
value = 0
def train(client):
    # prepare training data
    # predict the last ones (that are commented out)
    for line in dic:
        value = dic[line]['value']
        datum = Datum()
        for (k, v) in [
                ('Good',value)
                ]:
            datum.add_number(k, v)
        for (k, v) in [
                ('bad',490)
                ]:
            datum.add_number(k, v)
        

    # training data must be shuffled on online learning!
    random.shuffle(datum)

    # run train
    client.train(datum)

def predict(client):
    # predict the last shogun
    data = [
        Datum({'value': 200}),
        Datum({'value': 190}),
        Datum({'value': 600}),
    ]
    for d in data:
        res = client.classify([d])
        # get the predicted shogun name
        sys.stdout.write(max(res[0], key=lambda x: x.score).label)
        sys.stdout.write(' ')
        sys.stdout.write(d.string_values[0][1].encode('utf-8'))
        sys.stdout.write('\n')

if __name__ == '__main__':
    # connect to the jubatus
    client = jubatus.Classifier(host, port, name)
    # run example
    train(client)
    predict(client)
