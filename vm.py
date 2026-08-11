#!/bin/python3
import uuid
import state_manager as sm
from dataclasses import dataclass
import network as nt
class NIC:
    def __init__(self, number):
        self.name = "eno"+str(number)
        self.state = "down"
        self.mtu = "1500"
        self.ether = "aa:aa:aa:aa:aa:aa"
        self.ip = ""
        self.recever = []
        self.network = None

    def linkUp(self,ip,network):
        self.ip = ip
        self.state = "up"
        network.add_to_net(self.ip, self)
        self.network = network
        print(f"{self.name} is linkupped !!")

    def linkDown(self):
        self.ip = ""
        self.state = "down"
        network.delete_from_net(self.ip)
        self.network = None
        print(f"{self.name} is linkdown")

    def show_info(self):
        print(f"nic: {self.name}")
        print(f"state: {self.state}")
        print(f"mtu: {self.mtu}")
        print(f"link/ether: {self.ether}")
        print(f"ip: {self.ip}")

    def send(self,target_ip,message):
        #create packet
        packet = nt.Packet(self.ip, target_ip,message)
        self.network.send(packet)

    def check_reachable(self,target_ip):
        ip_table = self.network.show_ip_table()
        if target_ip in ip_table:
            return True
        else:
            return False


class Disk:
    def __init__(self,size,number):
        self.size = size
        self.ftype = "ext4"
        self.name = ""
        if number == 1:
            self.status = "mount"
        else:
            self.status = "umount"
        self.id = str(uuid.uuid4())
        self.name = "sd"+chr(96+int(number))

    def format(self,ftype):
        if ftype in ["ext3","ext4","zfs","fat64"]:
            self.ftype = ftype
        else:
            print(f"{ftype} is unknown file system")
    def mount(self):
        self.status = "mount"
    def umount(self):
        self.status = "umount"


@dataclass
class vm_config:
    name: int = "",
    cpu: int = -1,
    memory: int = -1,
    disk_size: int = -1,
    nic_num: int = -1

class VM:
    def __init__(self, config: vm_config):
        self.name = config.name
        self.cpu = config.cpu
        self.memory = config.memory
        self.status = sm.stopped()
        self.disk = Disk(config.disk_size,1)
        self.nics = {}
        for _ in range(int(config.nic_num)):
            self.add_nic()

    def start(self):
        self.status = self.status.start()
    
    def stop(self):
        self.status = self.status.stop()
    def delete(self):
        del self

    def show_info(self):
        print(f"VM: {self.name}")
        print(f"CPU: {self.cpu}")
        print(f"Memory: {self.memory}GB")
        print(f"Status: {self.status.status()}")
        print(f"disk {self.disk.name}: {self.disk.size} GB")
        print(f"nic info:")
        print([i for i in self.nics])
        print()

    def add_nic(self)->None:
        nic_nums = len(self.nics)
        new_nic = NIC(nic_nums+1)
        self.nics[new_nic.name] = new_nic
        return new_nic.name

    def nic_linkup(self,name,ip,network)->None:
        nic = self.nics[name]
        nic.linkUp(ip,network)

    def mount(self):
        self.disk.mount()

    def umount(self):
        self.disk.umount()

    def send_message(self,target_ip,message):
        for this in self.nics:
            if self.nics[this].check_reachable(target_ip):
                break
            this = None
        if this == None:
            print(f"cant send message to {target_ip}")
        self.nics[this].send(target_ip,message)

    def receve_message(self):
        for this in self.nics:
            data = self.nics[this].recever
            if data != None:
                while True:
                    d = data.pop()
                    print(f"{d[1]} from {d[0]}")
                    if len(data)==0:
                        break
