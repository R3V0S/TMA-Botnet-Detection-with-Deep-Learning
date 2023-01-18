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

protocolMapping = {'arp': 1, 'icmp': 2, 'igmp': 3, 'ipv6': 4, 'ipv6-icmp': 5, 'ipx/spx': 6, 'pim': 7, 'rarp': 8, 'rtcp': 9, 'rtp': 10, 'tcp': 11, 'udp': 12, 'udt': 13}
labelsMapping = {'flow=Background': 1, 'flow=Background-google-analytics': 2, 'flow=From-Background': 3, 'flow=From-Botnet': 4, 'flow=From-Normal': 5, 'flow=Normal': 6, 'flow=To-Background': 7, 'flow=To-Normal': 8}

list_clients = {}
list_ddos_attackers = []

urlFirewall = 'http://localhost:8080/firewall/rules/0000000000000001'

def connectDB():
	# Connection to InfluxDB - Database RYU
	client = InfluxDBClient(host='localhost', port=8086, database="RYU")
	return client
	
	
def query(client, init, final):
	# Obtain 80 flows (step 40)
    query = 'SELECT * FROM "flows" ORDER BY DESC LIMIT %d SLIMIT %d' % (init, final)
	df = client.query_api().query_data_frame(query=query)
	# points = results.get_points()
	return df


# time               *Dur      *Proto *TotBytes *TotPkts datapath ipv4-dst   ipv4-src
# ----                ---       ----- --------   ------- -------- --------   --------
#								1 - ICMP
#								6 - TCP
	
# def checkBots(df):
	# Check if there is a DoS Attack to the network
	
    # pints.shape() = 80 x N   (resize (1, 80, N))
    # model.predict(points)
    # result
    # if botnet = true --> send request to RYU.

	# model.predict(df)    
    
    # DO ACTIONS TO BLOCK CLIENT
	# myobj = {'nw_src': ip_client+'/32', 'actions':'DENY', 'dl_type':'IPv4', 'priority':'10'}
	# x = requests.post(urlFirewall, json=myobj)
	# list_ddos_attackers.append(ip_client)


def detectBots():
	client = connectDB()
    segment = 0
    num_flows = 80
	while True:
		df = query(client, segment, segment + num_flows)
		if (df.row = 80):
        	segment+=40
		checkBots(df)
		sleep(2)

if __name__ == '__main__':
    detectBots()
		
