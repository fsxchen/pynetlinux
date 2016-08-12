def test(v):
    test.result = v
    return v

def get_default_if():
    """ Returns the default interface """
    f = open ('/proc/net/route', 'r')
    for line in f:
        words = line.split()
        dest = words[1]
        print dest
        try:
            if (int (dest) == 0):
                interf = words[0]
                break
        except ValueError, e:
            print e
            pass
    return interf

def get_default_gw():
    """ Returns the default gateway """
    octet_list = []
    gw_from_route = None
    f = open ('/proc/net/route', 'r')
    for line in f:
        words = line.split()
        dest = words[1]
        try:
            if (int (dest) == 0):
                gw_from_route = words[2]
                break
        except ValueError:
            pass
        
    if not gw_from_route:
        return None 
    
    for i in range(8, 1, -2):
        octet = gw_from_route[i-2:i]
        octet = int(octet, 16)
        octet_list.append(str(octet)) 
    
    gw_ip = ".".join(octet_list)
            
    return gw_ip

def set_default_gw(gw):
    import subprocess

    while get_default_gw():
        subprocess.check_call("route del default",
                          shell=True
                          )

    subprocess.check_call("route add default gw %s" % gw,
                          shell=True
                          )

def get_default_route():
    """

    """
    import os, re
    default_route = None

    for line in os.popen('ip route show'):
        if test(re.match('^\s*default\s+via\s+(\S+)\s+dev\s+(\S+)\s*\n$', line)):
            m = test.result
            default_route = {
                'gateway': m.group(1),
                'interface_name': m.group(2)
            }
            break

    return default_route