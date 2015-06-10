#!/usr/bin/env python
# coding: utf-8

host = '127.0.0.1'
port = 9199
name = 'test2'

import sys
import json
import random

import jubatus
from jubatus.common import Datum
from client import getmongo


getmongo = getmongo()

def train(client):
    # prepare training data
    # predict the last ones (that are commented out)
    dic = getmongo.getDic()
    train_data = []
    value = 0
    for line in dic:
        value = dic[line]['value']
        train_data.append(('Good', Datum({'value': value})))

    # training data must be shuffled on online learning!
    random.shuffle(train_data)

    # run train
    client.train(train_data)

# def predict(client):
#     # predict the last shogun
#     data = [
#         Datum({'value': 200}),
#         Datum({'value': 190}),
#         Datum({'value': 600}),
#     ]
#     for d in data:
#         res = client.classify([d])
#         # get the predicted shogun name
#         sys.stdout.write(max(res[0], key=lambda x: x.score).label)
#         sys.stdout.write(' ')
#         sys.stdout.write(d.string_values[0][1].encode('utf-8'))
#         sys.stdout.write('\n')

if __name__ == '__main__':
    # connect to the jubatus
    client = jubatus.Classifier(host, port, name)
    # run example
    train(client)
    # predict(client)
