list_of_ips = ["8.8.8.8", "77.8.8.8", "127.0.0.1"]

def convert_ranges_to_ip_list(ips):
    new_ips = []
    
    for ip in ips:
        splitted = ip.split("-")
        
        if len(splitted) == 2: 
            start = splitted[0]
            end = splitted[1]
            
            for i in range(int(start), int(end)+1):
                    new_ip = ip[:len(ip)-1] + str(i).zfill(3)
                    
                    if new_ip not in new_ips:
                        new_ips.append(new_ip)
        elif len(splitted) != 2:
            new_ips.append(ip)
             
    return new_ips
