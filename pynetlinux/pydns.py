"""
set name server
"""

def set_nameserver(ip):
    with open("/etc/resolv.conf", 'w') as fd:
        fd.write("nameserver %s\n" % ip)
        fd.flush()

def get_nameserver():
    """
    get the nameserver
    """
    res = {"nameserver": ""}

    with open("/etc/resolv.conf", 'r') as fd:
        for line in fd:
            if "nameserver" in line:
                res["nameserver"] = line.strip("\n").split(" ")[-1]
        
    return res
