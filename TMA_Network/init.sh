sudo ovs-vsctl set Bridge r1 protocols=OpenFlow13
sudo ovs-vsctl set Bridge s1 protocols=OpenFlow13
sudo ovs-vsctl set Bridge s2 protocols=OpenFlow13
curl -X PUT http://localhost:8080/firewall/module/enable/0000000000000001
curl -X POST -d '{"nw_dst":"10.0.0.100/32", "actions":"ALLOW", "dl_type":"IPv4"}' http://localhost:8080/firewall/rules/0000000000000001
curl -X POST -d '{"nw_dst":"10.0.0.101/32", "actions":"ALLOW", "dl_type":"IPv4"}' http://localhost:8080/firewall/rules/0000000000000001
curl -X POST -d '{"nw_dst":"10.0.0.102/32", "actions":"ALLOW", "dl_type":"IPv4"}' http://localhost:8080/firewall/rules/0000000000000001
curl -X POST -d '{"nw_src":"10.0.0.100/32", "actions":"ALLOW", "dl_type":"IPv4"}' http://localhost:8080/firewall/rules/0000000000000001
curl -X POST -d '{"nw_src":"10.0.0.101/32", "actions":"ALLOW", "dl_type":"IPv4"}' http://localhost:8080/firewall/rules/0000000000000001
curl -X POST -d '{"nw_src":"10.0.0.102/32", "actions":"ALLOW", "dl_type":"IPv4"}' http://localhost:8080/firewall/rules/0000000000000001

