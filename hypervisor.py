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
            print(i)

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

    def vm_add_nic(self,vm_name,switch,ip):
        instance = _get_instance(self.vms, vm_name)
        name = instance.add_nic()
        instance.nic_linkup(name,switch)
        instance.nic_get_ip(name,switch,ip)

    def vm_get(self,vm_name) -> VM:
        return _get_instance(self.vms, vm_name)

#    def vm_send_message(self,vm_name,target_ip, message):
#        instance = _get_instance(self.vms, vm_name)
#        instance.send_message(target_ip, message)

