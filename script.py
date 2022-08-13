import nmap


def port_scanner(ip):
    nmScan = nmap.PortScanner()
    return nmScan.scan(ip, '1-500')


for host in nmap.all_hosts():
    print('Host : %s (%s)' % (host, nmap[host].hostname()))
    print('State : %s' % nmap[host].state())
    for proto in nmap[host].all_protocols():
        print('----------')
        print('Protocol : %s' % proto)

        lport = nmap[host][proto].keys()
        lport.sort()
        for port in lport:
            print('port : %s\tstate : %s' %
                  (port, nmap[host][proto][port]['state']))
