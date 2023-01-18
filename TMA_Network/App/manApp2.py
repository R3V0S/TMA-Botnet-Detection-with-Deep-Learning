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
# from influxdb import InfluxDBClient
# from influxdb import DataFrameClient
from time import sleep
import requests

from influxdb_client import InfluxDBClient
import pandas as pd
from keras.models import load_model

protocolMapping = {'arp': 1, 'icmp': 2, 'igmp': 3, 'ipv6': 4, 'ipv6-icmp': 5, 'ipx/spx': 6, 'pim': 7, 'rarp': 8,
                   'rtcp': 9, 'rtp': 10, 'tcp': 11, 'udp': 12, 'udt': 13}
labelsMapping = {'flow=Background': 1, 'flow=Background-google-analytics': 2, 'flow=From-Background': 3,
                 'flow=From-Botnet': 4, 'flow=From-Normal': 5, 'flow=Normal': 6, 'flow=To-Background': 7,
                 'flow=To-Normal': 8}

list_clients = {}
list_ddos_attackers = []

urlFirewall = 'http://localhost:8080/firewall/rules/0000000000000001'


def connectDB():
    # Connection to InfluxDB - Database RYU
    print('CONNECTING TO DB...')
    client = InfluxDBClient(url='http://localhost:8086')
    return client


def query(client, init, final):
    query= '''
    from(bucket: "RYU")
    |> range(start:-10h, stop: now())
    |> filter(fn: (r) => r._measurement == "flows")
    |> filter(fn: (r) => r._field == "*")
    |> limit(n: %d, offset: %d)'''

    # Obtain 80 flows (step 40)
    queryDB = query % (final, init)
    df = client.query_api().query_data_frame(query=queryDB)
    # df = client.query(queryDB)
    # points = results.get_points()
    return df


def cleanDf(df):
    pmap = {'1': 2, '6': 11}  # Are 1 or 6 strings or ints?
    df['Proto'] = df['Proto'].map(pmap)


def checkBots(df):
    model = load_model('path')
    predictions = model.predict(df)
    print(predictions)
#     # if(predictions == ???):
#     # ips = df['ipv4-src'].unique()
#     # for ip in ips:
#         # myobj = {'nw_src': ip + '/32', 'actions': 'DENY', 'dl_type': 'IPv4', 'priority': '10'}
#         # x = requests.post(urlFirewall, json=myobj)
#         # list_ddos_attackers.append(ip)

#     # print('Attackers Banned')

def printCosas(df):
    print(df.head())

def detectBots():
    client = connectDB()
    segment = 0
    num_flows = 80
    while True:
        df = query(client, segment, segment + num_flows)
        printCosas(df)
        cleanDf(df)
        # checkBots(df)
        if df.row == 80:
            segment += 40
        sleep(2)


if __name__ == '__main__':
    detectBots()
