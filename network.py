#!/bin/python3

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

    def send(self,souce_ip,target_ip,payload):
        #print(f"{payload}!! from {souce_ip}, to {target_ip}")
        target = self.ip_table[target_ip]
        target.recever.append([souce_ip,payload])
