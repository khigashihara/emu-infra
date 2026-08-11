#!/bin/python3

class Packet:
    def __init__(
        self,
        src_ip,
        dst_ip,
        src_mac,
        dst_mac,
        payload
    ):
        self.src_ip = src_ip
        self.dst_ip = dst_ip
        self.src_mac = src_mac
        self.dst_mac = dst_mac
        self.payload = payload

class ARPTable:
    def __init__(self):
        self.table = {}

class ARP:
    def __init__(self,table,nic):
        self.table = table
        self.nic = nic
    def request(self,ip):
        return self.nic.send(self.nic.ip,ip,f"who is {ip} ?")

    def register(self,ip,mac):
        self.table[ip] = mac
    def lookup(self,ip):
        return self.table.get(ip)

class switch:
    def __init__(self, network):
        self.network = network
        self.ports = {}

    def forward(self,packet):
        if "who is" in packet.payload:
            data = packet.payload.split()
            for i in self.ports:
                ip,mac = self.ports[i].arp_reply()
                if ip == data[2]:
                    return mac
            return None
                
        target = self.ports[packet.dst_mac]
        target.recever.append([packet.src_ip,packet.payload])


class router:
    def __init__(self):
        self.tables = {}
    def add_table(self,net,dst):
        self.tables[net] = dst

class Network:
    def __init__(self,name,subnet):
        self.name = ""
        self.subnet = ""
        #self.ip_table = {}

    def add_to_net(self,ip,nic_object):
        self.ip_table[ip] = nic_object

    def delete_from_net(self,ip):
        del self.ip_table[ip]

    def show_ip_table(self):
        return self.ip_table

    def send(self,packet: Packet):
        #print(f"{payload}!! from {souce_ip}, to {target_ip}")
        target = self.ip_table[packet.dst_ip]
        target.recever.append([packet.src_ip,packet.payload])
