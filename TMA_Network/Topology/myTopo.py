from mininet.topo import Topo

class MyTopo(Topo):
    def __init__(self):
        # Initialize topology
        Topo.__init__(self)

        # Add hosts 
        h1 = self.addHost('h1', ip='10.0.0.10/24', mac='00:00:00:00:00:10')
        h2 = self.addHost('h2', ip='10.0.0.11/24', mac='00:00:00:00:00:11')
        a1 = self.addHost('a1', ip='10.0.0.12/24', mac='00:00:00:00:00:12')
        a2 = self.addHost('a2', ip='10.0.0.13/24', mac='00:00:00:00:00:13')

        # Add servers 
        server1 = self.addHost('server1', ip='10.0.0.100/24', mac='00:00:00:00:01:00')
        server2 = self.addHost('server2', ip='10.0.0.101/24', mac='00:00:00:00:01:01')
        server3 = self.addHost('server3', ip='10.0.0.102/24', mac='00:00:00:00:01:02')

        # Add switches
        s1 = self.addSwitch('s1', dpid="0000000000000001")
        s2 = self.addSwitch('s2', dpid="0000000000000002")
        s3 = self.addSwitch('s3', dpid="0000000000000003")

        # Add links hosts
        self.addLink(s3, h1, port1=2)
        self.addLink(s3, h2, port1=3)
        self.addLink(s3, a1, port1=4)
        self.addLink(s3, a2, port1=5)

        # Add links servers
        self.addLink(s2, server1, port1=4)
        self.addLink(s2, server2, port1=5)
        self.addLink(s2, server3, port1=6)

        # Add links switches                       
        self.addLink(s1, s2, port1=1, port2=1)
        self.addLink(s1, s3, port1=2, port2=1)


# Adding the 'topos' dict 
topos = {'mytopo': (lambda: MyTopo())}
