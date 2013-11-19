__author__ = 'Parthan'

"""Find IP addresses in the given string.

You are given some text that can contain different IP-addresses. You should find all correct IPv4 addresses written in
dot-decimal notation; (Read about IP-addresses here). We don't know about the subnet mask, so addresses ending with 0
and 255 are considered to be correct for our purposes. All "words" in the text must be separated by whitespaces.

Your function should return a list of strings in the order of how these IPs appears in the text.

Reg Exp: \b(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.
            (25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b

"""

import re

def checkio(text):
    cx = re.compile('\b[0-9.]{1,3}\.[0-9.]{1,3}\.[0-9.]{1,3}\.[0-9.]{1,3}\b')
    res = []
    words = text.split()
    for word in words:
        ips = cx.findall(word)
        print "ips", ips
        for ip in ips:
            nos = [num for num in ip.split('.') if num < 256]
            if len(nos) == 4:
                print 'ip', ip
                res.append(ip)
            else:
                continue
    return res

if __name__ == "__main__":
    assert checkio("192.168.1.1 and 10.0.0.1 or 127.0.0.1") == ["192.168.1.1", "10.0.0.1", "127.0.0.1"], "Sample 1"
    assert checkio(u"10.0.0.1.1 but 127.0.0.256 1.1.1.1") == ["1.1.1.1"], "Sample 2"
    assert checkio("167.11.0.0 1.2.3.255 192,168,1,1") == ["167.11.0.0", "1.2.3.255"], "Sample 3"
    assert checkio("00250.00001.0000002.1 251.1.2.1") == ["251.1.2.1"], "Sample 4"