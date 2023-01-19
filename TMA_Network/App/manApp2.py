#! /usr/bin/env python3
import os
import socket
import array
from ryu.lib import snortlib
from ryu.lib import alert
from ryu.lib.packet import packet
from ryu.lib.packet import ethernet
from ryu.lib.packet import ipv4
from ryu.lib.packet import icmp
from time import sleep
import requests
from keras.layers import Dense, Dropout, Flatten, Reshape, GlobalAveragePooling1D, Conv2D, MaxPooling2D, Conv1D, MaxPooling1D
from tensorflow.keras.optimizers import RMSprop, Adam
from influxdb import InfluxDBClient
import pandas as pd
import numpy as np
from keras.models import load_model
# from sklearn.preprocessing import MinMaxScaler, StandardScaler, MaxAbsScaler

protocolMapping = {'arp': 1, 'icmp': 2, 'igmp': 3, 'ipv6': 4, 'ipv6-icmp': 5, 'ipx/spx': 6, 'pim': 7, 'rarp': 8,
                   'rtcp': 9, 'rtp': 10, 'tcp': 11, 'udp': 12, 'udt': 13}
labelsMapping = {'flow=Background': 1, 'flow=Background-google-analytics': 2, 'flow=From-Background': 3,
                 'flow=From-Botnet': 4, 'flow=From-Normal': 5, 'flow=Normal': 6, 'flow=To-Background': 7,
                 'flow=To-Normal': 8}

list_clients = {}
list_ddos_attackers = []

urlFirewall = 'http://localhost:8080/firewall/rules/0000000000000001'

def create_segments_and_labels(df):
    segments = []
    seg = []
    for column in df:
        fs = df[column].values
        seg.append(fs)
    segments.append(seg)
    reshaped_segment = np.asarray(segments, dtype= np.float32).reshape(-1, 60, 4)
    return reshaped_segment

def connectDB():
    print('CONNECTING TO DB...')
    client = InfluxDBClient(host = 'localhost', port=8086)
    return client


def query(client, rows, ofset):
    client.switch_database('RYU')
    rs = client.query('SELECT * FROM "flows" ORDER BY DESC LIMIT %d SLIMIT %d' % (rows, ofset))
    return rs

def GetDataframe(rs):
    df = pd.DataFrame(rs.get_points())
    return df

def formatDataFrame(df):
    pmap = {'1': 'icmp', '6': 'tcp'}  # Are 1 or 6 strings or ints?
    df['Proto'] = df['Proto'].map(pmap)
    PROTO = "Proto_mapped"
    df[PROTO] = df['Proto'].map(protocolMapping)
    df.drop(['time','datapath' ,'ipv4-dst','ipv4-src', 'Proto'], axis=1, inplace= True)
    df['Dur'] = df['Dur'].astype(float)
    # print(df.head())    
    # print(df.dtypes)
    reshapedDF = create_segments_and_labels(df)
    # print(reshapedDF.shape)
    reshapedDF = reshapedDF.reshape(reshapedDF.shape[0], 60 * 4)
    reshapedDF = reshapedDF.astype("float32")
    # print(reshapedDF.shape)
    # scaler = MinMaxScaler()
    # reshapedDF = scaler.fit_transform(reshapedDF)
    return reshapedDF

def checkBots(df):
    model = load_model(os.getcwd() + '/modelo2/modelo2test.h5')
    # print(model.summary())
    predictions = model.predict(df)
    # print(predictions)
    if (predictions[0][0] == 1.0):
        print('BACKGROUND')
    if (predictions[0][1] == 1.0):
        print('BOTNET')
        myobj = {'nw_dst': '10.0.0.100/32', 'actions': 'DENY', 'dl_type': 'IPv4', 'priority': '10'}
        x = requests.post(urlFirewall, json=myobj)
        myobj = {'nw_dst': '10.0.0.101/32', 'actions': 'DENY', 'dl_type': 'IPv4', 'priority': '10'}
        x = requests.post(urlFirewall, json=myobj)
        myobj = {'nw_dst': '10.0.0.102/32', 'actions': 'DENY', 'dl_type': 'IPv4', 'priority': '10'}
        x = requests.post(urlFirewall, json=myobj)
        print('ACCESS BLOQUED')


def detectBots():
    client = connectDB()
    segment = 0
    num_flows = 60
    while True:
        rs = query(client, num_flows, segment)
        df = GetDataframe(rs)
        if df.shape[0] == 60:
            reshapedDF = formatDataFrame(df)
            checkBots(reshapedDF)
            segment += 55
        sleep(2)


if __name__ == '__main__':
    detectBots()
