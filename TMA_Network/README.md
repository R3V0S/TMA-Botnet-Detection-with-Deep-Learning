# 5GSFN-Final-Project
5GSFN-Final-Project

## GENERAL STEPS
1. Run the Ryu Firewall
```
~/5GSFN-Final-Project$ sudo ryu-manager rest_controller.py
```
2.  Run the Mininet Topology
```
~/5GSFN-Final-Project$ sudo mn --custom Topology/myTopo.py --topo mytopo --switch ovsk --controller remote
```
3. Set the Initial Configuration
```
~/5GSFN-Final-Project$ sh initialConfig.sh
```
4. Command to show the flow tables in each switch
```
~/5GSFN-Final-Project$ sh Topology/switchFlowRules.sh
```
5. Run the App
```
~/5GSFN-Final-Project$ sudo python3 App/ManagerAPP.py
```

## ATTACKS
1. Copy the custom rules into the snort directory
```
~$ sudo cp 5GSFN-Final-Project/Snort/Myrules.rules /etc/snort/rules/
```
2. Run the Snort configuration script
```
~/5GSFN-Final-Project$ sudo sh Snort/snort-config.sh
```
3. Run the Mininet servers
```
mininet> xterm server1 server2 server3 honeypot1
```
4. Run the server command for each xterm terminal
```
python3 -m http.server 80
```
5. Run the attackers' terminals
```
mininet> xterm a1 a2
```

## LOAD BALANCER
1. To test the Load Balancer, run the following command on Mininet for each host that you want to connect to the DMZ servers, using the Virtual IP address 10.0.0.150

-> Exampe for the host 1:
```
mininet> h1 curl 10.0.0.150
```
