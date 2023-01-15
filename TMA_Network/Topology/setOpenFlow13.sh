#!/bin/bash
sudo ovs-vsctl set Bridge s1 protocols=OpenFlow13
sudo ovs-vsctl set Bridge s2 protocols=OpenFlow13
sudo ovs-vsctl set Bridge s3 protocols=OpenFlow13