#!/bin/python3

class Packet:
    def __init__(
        self,
        src_ip,
        dst_ip,
        payload
    ):
        self.src_ip = src_ip
        self.dst_ip = dst_ip
        self.payload = payload

class Network:
    def __init__(self,name,subnet):
        self.name = ""
        self.subnet = ""
        self.ip_table = {}

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
