import vm
from vm import VM
from vm import NIC
import hypervisor as HP



def main()-> None:
    conf = vm.vm_config(
            name = "hoge",
            cpu = 4,
            memory = 64,
            disk_size = 256,
            nic_num = 2,
        )
    hp =HP.hypervisor()
    hp.vm_create(conf)
    hp.show_vm_list()

    hp.vm_show_info("hoge")
    hp.vm_start("hoge")
    hp.vm_start("hoge")
    hp.vm_show_info("hoge")
    hp.vm_add_nic("hoge","eno1","192.168.10.12")

    hp.vm_stop("hoge")
    hp.vm_show_info("hoge")
    hp.vm_delete("hoge")
    #hp.vm_show_info("hoge")

if __name__ == "__main__":
    main()
