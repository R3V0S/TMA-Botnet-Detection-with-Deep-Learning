# Topology Information
## Start topology
Command:
```
sudo mn --custom Topology/myTopo.py --topo mytopo --switch ovsk --controller remote
```
## Start xterm terminals for each server
This section provides specific information for opening the servers created above.
So, after starting the Topology using the above command, run the following command within the Mininet CLI for each server:
```
xterm <server_name>
```
Example for the server 1:
```
xterm server1
```
## Running the servers
Here is the necessary command that has to be executed in each xterm terminal in order to start each of the servers:
```
python3 -m http.server 80
```

## Showing the new flow rules for each switch
The next command allows us to see the new flow rules added on each switch during the process:
```
sh Topology/switchFlowRules.sh
```
