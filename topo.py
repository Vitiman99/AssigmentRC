from mininet.topo import Topo
from mininet.net import Mininet

class MyTopo(Topo):
    def build(self):
        # Agregar hosts y switches
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')
        h5 = self.addHost('h5')
        s1 = self.addSwitch('s1')

        # Agregar enlaces
        self.addLink(h1, s1)
        self.addLink(h2, s1)
        self.addLink(h3, s1)
        self.addLink(h4, s1)
        self.addLink(h5, s1)

topos = {
    'RC-Topo': ( lambda: MyTopo() )
}

