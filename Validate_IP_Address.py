class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        def is_hex(s):
            for char in s:
                if not (char in string.hexdigits):
                    return False
            return True
        ary = IP.split('.')
        if len(ary) == 4:
            for i in ary:
                if not i.isdigit() or not 0 <= int(i) < 256 or (i[0] == '0' and len(i) > 1):
                    return "Neither"
            return "IPv4"
        ary = IP.split(':')
        if len(ary) == 8:
            for i in ary:
                if len(i) == 0 or not len(i) <= 4 or not is_hex(i):
                    return "Neither"
            return "IPv6"
        return "Neither"
