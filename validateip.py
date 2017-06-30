# Write a function to validate an IP address in IPv4

def validate_ip(ip_address):
    a = ip_address.split('.')
    if len(a) != 4:
        return False

    for x in a:
        if not x.isdigit():
            return False
        i = int(x)
        if i < 0 or i > 255:
            return False

    return True