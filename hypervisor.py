#!/bin/python3

from vm import VM

def _get_instance(vms,name):
    if name in vms:
        return vms[name]
    else:
        print(f"vm {name} is not exist")
        return None

class hypervisor:
    def __init__(self):
        self.vms = {}
    def show_vm_list(self):
        for i in self.vms:
            i.index
    def vm_create(self,vm_conf):
        instance = VM(vm_conf)
        self.vms[instance.name] = instance
        print(f"complete create {instance.name}")

    def vm_delete(self,vm_name):
        instance = _get_instance(self.vms, vm_name)
        instance.stop()
        del self.vms[vm_name]
        instance.delete()
        print(f"complete delete {vm_name}")

    def vm_start(self,vm_name):
        instance = _get_instance(self.vms, vm_name)
        instance.start()
        print(f"complete start {vm_name}")

    def vm_stop(self,vm_name):
        instance = _get_instance(self.vms, vm_name)
        instance.stop()
        print(f"complete stop {vm_name}")

    def vm_show_info(self,vm_name):
        instance = _get_instance(self.vms, vm_name)
        instance.show_info()

    def vm_add_nic(self,vm_name,name,ip):
        instance = _get_instance(self.vms, vm_name)
        instance.add_nic()
        instance.nic_linkup(name,ip)

