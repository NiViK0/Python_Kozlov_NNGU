--------------
---------------
----------
access_config = {"FastEthernet0/12": 10, "FastEthernet0/14": 11, "FastEthernet0/16": 17}

access_config_2 = {
"FastEthernet0/03": 100,
"FastEthernet0/07": 101,
"FastEthernet0/09": 107,
}
access_mode_template = [
"switchport mode access",
"switchport access vlan",
"switchport nonegotiate",
"spanning-tree portfast",
"spanning-tree bpduguard enable",
]
def generate_access_config(intf_vlan_mapping, access_template):
    for key in intf_vlan_mapping:
        print(key)
        #print(intf_vlan_mapping[key])
        for i in access_template:
            if i.endswith('access vlan'):
                print(i,intf_vlan_mapping[key] )
            else:
                print(i)
generate_access_config(access_config_2,access_mode_template)