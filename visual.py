import datetime


import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
db = client.meteo
messages = db['messages']

def getInfo(start, end):
    x = []
    t1 = []
    t2 = []

    for message in messages.find({"time": {"$gte": start, "$lte": end}}):
        print(message)

        # message.t1 = float(message["t1"])
        # if message.t1 > -127:

        air = float(message['t1'])
        land = float(message['t2'])
        time = message['time']
        x.append(time)
        t1.append(air)
        t2.append(land)


        # if air > -127:
            # pprint.pprint(air)
            # difrent = float(message['l'])/air
            # pprint.pprint(difrent)
            # pprint.pprint(message['l'])
            # time = message['time']
            # x.append(time)
            # y.append(air)
    fig, ax = plt.subplots(figsize=[10, 10])
    ax.plot(x, t1)
    ax.plot(x, t2)
        # s.plot.bar()
    fig.savefig('my_plot.png')
    print(start, end)
    return (start, end)
def getInfoById(start, end, id):
    x = []
    t1 = []
    t2 = []

    for message in messages.find({"id": id, "time": {"$gte": start, "$lte": end}}):
        print(message)

        # message.t1 = float(message["t1"])
        # if message.t1 > -127:

        air = float(message['t1'])
        land = float(message['t2'])
        time = message['time']
        x.append(time)
        t1.append(air)
        t2.append(land)

    fig, ax = plt.subplots(figsize=[30, 10])
    ax.plot(x, t1)
    ax.plot(x, t2)
    fig.savefig('my_plot.png')
    print(start, end)
    return (start, end)

when = None
