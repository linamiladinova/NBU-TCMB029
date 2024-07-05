from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info
import random

class CustomTopo(Topo):
    def build(self):
        # Add 812 switches
        switches = []
        for i in range(812):
            switch = self.addSwitch(f's{i+1}')
            switches.append(switch)

        # Add 18 hosts and connect them to random switches
        for i in range(18):
            host = self.addHost(f'h{i+1}')
            switch = random.choice(switches)
            self.addLink(host, switch)

        # Connect all switches in a linear topology for simplicity
        for i in range(811):
            self.addLink(switches[i], switches[i+1])

topos = { 'mytopo': ( lambda: CustomTopo() ) }

def run():
    setLogLevel('info')
    topo = CustomTopo()
    controller = RemoteController('c0', ip='127.0.0.1', port=6653)
    net = Mininet(topo=topo, controller=controller)
    net.start()
    CLI(net)
    net.stop()

if __name__ == '__main__':
    run()
