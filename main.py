import vm
from vm import VM
from vm import NIC
import hypervisor as HP
import network


def main()-> None:
    network1 = network.Network("net1","192.168.10.0/24")
    conf = vm.vm_config(
            name = "hoge",
            cpu = 4,
            memory = 64,
            disk_size = 256,
            nic_num = 0,
        )

    hp = HP.hypervisor()
    hp.vm_create(conf)
    # hp.show_vm_list()

    # hp.vm_show_info("hoge")
    hp.vm_start("hoge")
    # hp.vm_start("hoge")
    # hp.vm_show_info("hoge")
    hp.vm_add_nic("hoge","eno1",network1,"192.168.10.12")
    conf2 = conf
    conf2.name = "huga"
    hp.vm_create(conf2)
    hp.vm_add_nic("huga","eno1",network1,"192.168.10.13")
    # hp.vm_stop("hoge")
    hp.vm_show_info("hoge")
    # hp.vm_delete("hoge")
    # hp.vm_show_info("hoge")

    hp.show_vm_list()
    vm1 = hp.vm_get("hoge")

    vm1.send_message("192.168.10.13","hello world")

    vm2 = hp.vm_get("huga")
    vm2.receve_message()

if __name__ == "__main__":
    main()
